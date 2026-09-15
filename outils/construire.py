#!/usr/bin/env python3
"""
explorai-marque — générateur du dépôt.

Source de vérité unique : data/explorai-marque.json
Ce script produit tous les fichiers dérivés : regles/*.md, pages HTML, llms.txt,
llms-full.txt, README.md, SKILL.md, data/explorai-actifs.json,
data/explorai-jetons.json, data/explorai-index.json,
assets/css/explorai-jetons.css, sitemap.xml, robots.txt.

Usage :
    python3 outils/construire.py            # régénère les fichiers dérivés
    python3 outils/construire.py --verifier # vérifie que le dépôt est à jour et cohérent

Aucune dépendance hors de la bibliothèque standard Python 3.8+.
"""
import hashlib
import html
import json
import os
import re
import struct
import sys
import tempfile
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SOURCE = "data/explorai-marque.json"
AVERTISSEMENT = "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."


# ---------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------
def charger():
    return json.loads((RACINE / SOURCE).read_text(encoding="utf-8"))


def slugifier(texte):
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t


def fmt_nombre(x):
    """Nombre à la française : virgule décimale, sans zéros inutiles."""
    if isinstance(x, float):
        s = ("%.2f" % x).rstrip("0").rstrip(".")
    else:
        s = str(x)
    return s.replace(".", ",")


def compact(texte):
    """Retire toute espace, y compris insécable (valeurs CSS)."""
    return re.sub(r"\s", "", texte)


def liste_fr(items):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " et " + items[-1]


# ---------------------------------------------------------------------------
# Modèle de blocs : un même contenu, rendu en Markdown et en HTML
# ---------------------------------------------------------------------------
class H:
    def __init__(self, niveau, texte, ancre=None):
        self.niveau, self.texte = niveau, texte
        self.ancre = ancre or slugifier(texte)


class P:
    def __init__(self, texte, classe=None):
        self.texte, self.classe = texte, classe


class UL:
    def __init__(self, items):
        self.items = items


class OL:
    def __init__(self, items):
        self.items = items


class TABLE:
    def __init__(self, entetes, lignes, alignement=None, legende=None, total=None, accent=None):
        self.entetes, self.lignes, self.accent = entetes, lignes, accent
        self.alignement = alignement or ["gauche"] * len(entetes)
        self.legende, self.total = legende, total


class CODE:
    def __init__(self, langage, texte, titre=None):
        self.langage, self.texte, self.titre = langage, texte, titre


class NOTE:
    def __init__(self, titre, texte, genre="note"):
        self.titre, self.texte, self.genre = titre, texte, genre


class IMAGES:
    """Liste de (chemin, alt, légende, fond)."""
    def __init__(self, items):
        self.items = items


class Rendu:
    """Résout les liens selon la cible (Markdown dans regles/, Markdown à la racine, HTML, texte intégral)."""

    def __init__(self, cible, sections, site):
        self.cible = cible  # 'md-regles' | 'md-racine' | 'html' | 'absolu'
        self.sections = {s["id"]: s for s in sections}
        self.site = site

    def lien(self, ref):
        if re.match(r"^https?://|^mailto:", ref):
            return ref
        m = re.match(r"^(c\d\d)(#.*)?$", ref)
        if m:
            s = self.sections[m.group(1)]
            frag = m.group(2) or ""
            base = f"{s['id']}-{s['slug']}"
            if self.cible == "md-regles":
                return f"{base}.md{frag}"
            if self.cible == "md-racine":
                return f"regles/{base}.md{frag}"
            if self.cible == "html":
                return f"{base}.html{frag}"
            return f"{self.site}regles/{base}.md{frag}"
        # chemin de fichier du dépôt
        if self.cible == "md-regles":
            return "../" + ref
        if self.cible == "absolu":
            return self.site + ref
        return ref

    def image(self, chemin):
        if self.cible == "md-regles":
            return "../" + chemin
        if self.cible == "absolu":
            return self.site + chemin
        return chemin

    # -- en ligne --------------------------------------------------------
    def auto_liens(self, texte):
        return re.sub(r"(?<!\[)\b[Ss]ection (c\d\d)\b(?![^\[]*\])", lambda m: f"[{m.group(0)}]({m.group(1)})", texte)

    def en_ligne_md(self, texte):
        texte = self.auto_liens(str(texte))
        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f"[{m.group(1)}]({self.lien(m.group(2))})", texte)

    def en_ligne_html(self, texte):
        texte = self.auto_liens(str(texte))
        morceaux = re.split(r"(`[^`]+`)", texte)
        out = []
        for mo in morceaux:
            if mo.startswith("`") and mo.endswith("`") and len(mo) > 1:
                out.append("<code>" + html.escape(mo[1:-1]) + "</code>")
                continue
            liens = []

            def garder(m):
                liens.append((m.group(1), m.group(2)))
                return f"\x00{len(liens) - 1}\x00"

            mo = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", garder, mo)
            mo = html.escape(mo, quote=False)
            mo = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", mo)
            mo = re.sub(r"(?<![\w&])#([0-9A-Fa-f]{6})\b",
                        lambda m: f'<span class="hex"><i style="background:#{m.group(1)}"></i>#{m.group(1)}</span>', mo)

            def remettre(m):
                lib, ref = liens[int(m.group(1))]
                return f'<a href="{html.escape(self.lien(ref))}">{html.escape(lib, quote=False)}</a>'

            mo = re.sub(r"\x00(\d+)\x00", remettre, mo)
            out.append(mo)
        return "".join(out)

    # -- Markdown ---------------------------------------------------------
    def md(self, blocs):
        L = []
        for b in blocs:
            if isinstance(b, H):
                L.append("#" * b.niveau + " " + self.en_ligne_md(b.texte))
            elif isinstance(b, P):
                L.append(self.en_ligne_md(b.texte))
            elif isinstance(b, UL):
                L.append("\n".join("- " + self.en_ligne_md(i) for i in b.items))
            elif isinstance(b, OL):
                L.append("\n".join(f"{n}. " + self.en_ligne_md(i) for n, i in enumerate(b.items, 1)))
            elif isinstance(b, TABLE):
                def cel(x):
                    return self.en_ligne_md("" if x is None else x).replace("|", "\\|").replace("\n", " ")
                sep = {"gauche": ":---", "droite": "---:", "centre": ":---:"}
                t = ["| " + " | ".join(cel(e) for e in b.entetes) + " |",
                     "| " + " | ".join(sep[a] for a in b.alignement) + " |"]
                for r in b.lignes:
                    t.append("| " + " | ".join(cel(x) for x in r) + " |")
                if b.total:
                    t.append("| " + " | ".join(f"**{cel(x)}**" if cel(x) else "" for x in b.total) + " |")
                if b.legende:
                    L.append(f"Tableau — {self.en_ligne_md(b.legende)}")
                L.append("\n".join(t))
            elif isinstance(b, CODE):
                if b.titre:
                    L.append(self.en_ligne_md(b.titre) + " :")
                L.append(f"```{b.langage}\n{b.texte}\n```")
            elif isinstance(b, NOTE):
                L.append("> **" + b.titre + ".** " + self.en_ligne_md(b.texte))
            elif isinstance(b, IMAGES):
                L.append("\n".join(f"- ![{alt}]({self.image(c)}) `{c}` — {self.en_ligne_md(leg)}" for c, alt, leg, _ in b.items))
        return "\n\n".join(L) + "\n"

    # -- HTML -------------------------------------------------------------
    def html(self, blocs, rotation):
        out, ouvert, n = [], False, 0
        for b in blocs:
            if isinstance(b, H) and b.niveau == 2:
                if ouvert:
                    out.append("</section>")
                acc = rotation[n % len(rotation)]
                n += 1
                out.append(f'<section id="{b.ancre}" data-accent="{acc}">')
                out.append(f'<h2><a class="ancre" href="#{b.ancre}">{self.en_ligne_html(b.texte)}</a></h2>')
                ouvert = True
            elif isinstance(b, H):
                out.append(f'<h{b.niveau} id="{b.ancre}">{self.en_ligne_html(b.texte)}</h{b.niveau}>')
            elif isinstance(b, P):
                c = f' class="{b.classe}"' if b.classe else ""
                out.append(f"<p{c}>{self.en_ligne_html(b.texte)}</p>")
            elif isinstance(b, UL):
                out.append("<ul>" + "".join(f"<li>{self.en_ligne_html(i)}</li>" for i in b.items) + "</ul>")
            elif isinstance(b, OL):
                out.append("<ol>" + "".join(f"<li>{self.en_ligne_html(i)}</li>" for i in b.items) + "</ol>")
            elif isinstance(b, TABLE):
                al = {"gauche": "", "droite": ' class="num"', "centre": ' class="centre"'}
                da = f' data-accent="{b.accent}"' if b.accent else ""
                t = [f'<div class="tableau"{da}><table>']
                if b.legende:
                    t.append(f"<caption>{self.en_ligne_html(b.legende)}</caption>")
                t.append("<thead><tr>" + "".join(f'<th scope="col"{al[a]}>{self.en_ligne_html(e)}</th>' for e, a in zip(b.entetes, b.alignement)) + "</tr></thead><tbody>")
                for r in b.lignes:
                    t.append("<tr>" + "".join(f"<td{al[a]}>{self.en_ligne_html('' if x is None else x)}</td>" for x, a in zip(r, b.alignement)) + "</tr>")
                if b.total:
                    t.append('<tr class="total">' + "".join(f"<td{al[a]}>{self.en_ligne_html(x)}</td>" for x, a in zip(b.total, b.alignement)) + "</tr>")
                t.append("</tbody></table></div>")
                out.append("".join(t))
            elif isinstance(b, CODE):
                tit = f'<figcaption>{self.en_ligne_html(b.titre)}</figcaption>' if b.titre else ""
                out.append(f'<figure class="code">{tit}<pre><code class="language-{b.langage}">{html.escape(b.texte)}</code></pre></figure>')
            elif isinstance(b, NOTE):
                out.append(f'<aside class="encadre {b.genre}"><p><strong>{html.escape(b.titre)}.</strong> {self.en_ligne_html(b.texte)}</p></aside>')
            elif isinstance(b, IMAGES):
                f = ['<ul class="galerie">']
                for c, alt, leg, fond in b.items:
                    f.append(f'<li><figure><div class="apercu fond-{fond}"><img src="{html.escape(self.image(c))}" alt="{html.escape(alt)}" loading="lazy"></div>'
                             f'<figcaption>{self.en_ligne_html(leg)}<br><code>{html.escape(c)}</code></figcaption></figure></li>')
                f.append("</ul>")
                out.append("".join(f))
        if ouvert:
            out.append("</section>")
        return "\n".join(out)


# ---------------------------------------------------------------------------
# Contenu des sections
# ---------------------------------------------------------------------------
def s_identite(m):
    mq, ent, gv = m["identite"]["marque"], m["identite"]["entreprise"], m["identite"]["gouvernance"]
    B = [H(2, "Nom et signature"),
         TABLE(["Élément", "Règle"], [
             ["Nom en texte courant", f"**{mq['nom_texte_courant']}**, en un seul mot."],
             ["Graphies interdites", ", ".join(f"`{g}`" for g in mq["graphie_interdite"])],
             ["Mot-symbole du logo", f"`{mq['mot_symbole_du_logo']}` — {mq['note_graphie']}"],
             ["Signature", f"«\u00a0{mq['signature']}\u00a0»"],
             ["Règle de signature", mq["regle_signature"]],
         ]),
         H(2, "Organisation"),
         TABLE(["Champ", "Valeur"], [
             ["Description", mq["organisation"]["description"]],
             ["Ville", mq["organisation"]["ville"]],
             ["Courriel", mq["organisation"]["courriel"]],
             ["Site public", mq["organisation"]["site_public"]],
         ]),
         H(2, "Entreprise"),
         NOTE("Statut", ent["statut_des_informations"], "attention"),
         P(ent["description"]),
         P("Domaines d'intervention : " + liste_fr(ent["domaines_d_intervention"]) + "."),
         TABLE(["Phase", "Contenu"], [[d["phase"], d["contenu"]] for d in ent["demarche"]], legende="Démarche type"),
         TABLE(["Client", "Objet"], [[x["client"], x["objet"]] for x in ent["mandats_cites_publiquement"]], legende="Mandats cités publiquement — non vérifiés"),
         H(2, "Gouvernance"),
         TABLE(["Élément", "Règle"], [
             ["Arbitre", gv["arbitre"]],
             ["Responsable nommé", gv["responsable_nomme"] or "Non nommé — à compléter."],
             ["Cycle de révision", gv["cycle_de_revision"]],
             ["Journal des versions", gv["journal_des_versions"] + " Voir `CHANGELOG.md`."],
         ]),
         NOTE("Règle", gv["regle"], "attention")]
    return B


def s_logo(m):
    lg = m["logo"]
    B = [P(lg["principe"]), H(2, "Variantes")]
    B.append(TABLE(["Variante", "Fichier", "Fonds admis", "Note"],
                   [[v["nom"], f"`{v['fichier']}`", ", ".join(v["fonds"]) or "Aucun", v["note"]] for v in lg["variantes"]]))
    B.append(IMAGES([(v["fichier"], f"Logo Explorai, variante {v['cle']}", v["nom"], {"bleu": "clair", "blanc": "bleu", "vert": "bleu"}[v["cle"]]) for v in lg["variantes"]]))
    B += [H(2, "Zone de protection"), P(lg["zone_de_protection"]),
          H(2, "Mesures"),
          TABLE(["Contexte", "Valeur", "Remarque"], [[x["contexte"], x["valeur"], x["remarque"]] for x in lg["mesures"]]),
          H(2, "Interdits"), UL(lg["interdits"]),
          H(2, "Favicon"),
          P(f"{lg['favicon']['dessin']}. {lg['favicon']['regle']} Fichiers : " + ", ".join(f"`{f}`" for f in lg["favicon"]["fichiers"]) + "."),
          P("Choix de fichier et URL de téléchargement : section c11.")]
    return B


def s_typo(m):
    t = m["typographie"]
    B = [H(2, "Familles"),
         TABLE(["Rôle", "Police", "Usage", "Précision"], [
             ["Principale", t["principale"]["nom"], t["principale"]["usage"], "Graisses " + ", ".join(map(str, t["principale"]["graisses"])) + ". " + t["principale"]["interlettrage"]],
             ["Secondaire", t["secondaire"]["nom"], t["secondaire"]["usage"], t["secondaire"]["interdit"]],
         ]),
         H(2, "Niveaux de repli"),
         P("Un fichier emploie un seul niveau, du début à la fin."),
         TABLE(["Niveau", "Nom", "Sans empattement", "Monospace", "Quand"],
               [[str(n["niveau"]), n["nom"], n["sans"], n["mono"], n["quand"]] for n in t["niveaux_de_repli"]]),
         H(2, "Interdits"), UL(t["interdits"]),
         H(2, "Déclarations CSS"),
         CODE("css", "/* Déclaration normative */\n" + t["declaration_normative"]["sans"] + "\n" + t["declaration_normative"]["mono"], "Pile normative (charte v3)"),
         CODE("css", t["declaration_web_etendue"]["sans"] + "\n" + t["declaration_web_etendue"]["mono"], "Pile web étendue"),
         NOTE("Statut de la pile web étendue", t["declaration_web_etendue"]["statut"], "attention"),
         H(2, "Échelle web"),
         TABLE(["Rôle", "Police", "Corps", "Interlettrage"], [[e["role"], e["police"], e["corps"], e["interlettrage"]] for e in t["echelle_web"]]),
         P("Échelle des documents : section c12."),
         H(2, "Fichiers de police"),
         P(t["fichiers"]["provenance"]), P(t["fichiers"]["usage"]),
         TABLE(["Famille", "Graisse", "WOFF2", "TTF"], [[f["famille"], str(f["graisse"]), f"`{f['woff2']}`", f"`{f['ttf']}`"] for f in t["fichiers"]["liste"]]),
         P("Licences : " + ", ".join(f"`{x}`" for x in t["fichiers"]["licences"]) + ".")]
    return B


def s_palette(m):
    c = m["couleurs"]
    B = [P(c["principe"]), H(2, "Couleurs de marque"),
         TABLE(["Nom", "Hex", "Variable CSS", "Accent", "Rôle"],
               [[x["nom"], x["hex"], f"`{x['variable_css']}`", "oui" if x["accent"] else "non", x["role"]] for x in c["marque"]]),
         H(2, "Palette étendue"),
         TABLE(["Nom", "Hex", "Variable CSS", "Rôle"], [[x["nom"], x["hex"], f"`{x['variable_css']}`", x["role"]] for x in c["etendue"]]),
         H(2, "Teintes dérivées"), P(c["teintes_derivees"]["principe"])]
    rows = []
    for k in ("10", "22"):
        td = c["teintes_derivees"][k]
        rows.append([f"{k} %", td["usage"], td["turquoise"], td["vert"], td["lavande"], td["rose"]])
    B.append(TABLE(["Teinte", "Usage", "Turquoise", "Vert", "Lavande", "Rose"], rows))
    B.append(P("Variables CSS : `--cyan-10`, `--cyan-22`, `--green-10`, `--green-22`, `--lav-10`, `--lav-22`, `--pink-10`, `--pink-22`."))
    B += [H(2, "Associations autorisées"),
          TABLE(["Paire", "Intention"], [[a["paire"], a["intention"]] for a in c["associations_autorisees"]]),
          NOTE("Décision v3", c["decision_v3"]),
          P("Fichiers de jetons : `assets/css/explorai-jetons.css` et `data/explorai-jetons.json`.")]
    return B


def s_couleur_usage(m):
    c = m["couleur_en_usage"]
    iw = c["implementation_web"]
    return [H(2, "Règles"),
            TABLE(["Id", "Règle"], [[r["id"], r["enonce"]] for r in c["regles"]]),
            H(2, "À faire, à éviter"),
            TABLE(["", "Énoncé"], [["À faire", x] for x in c["a_faire"]] + [["À éviter", x] for x in c["a_eviter"]]),
            H(2, "Implémentation web"),
            P(f"Attribut `{iw['attribut']}`, valeurs " + ", ".join(f"`{v}`" for v in iw["valeurs"]) + ". " + iw["effet"]),
            CODE("html", iw["exemple"])]


def s_icono(m):
    ic = m["iconographie"]
    B = [P(ic["principe"]), H(2, "Règles"), TABLE(["Id", "Règle"], [[r["id"], r["enonce"]] for r in ic["regles"]]),
         H(2, "Les neuf formes")]
    B.append(TABLE(["Forme", "Sens", "Ouvre", "N'ouvre pas", "Exemple"],
                   [[f"**{f['nom']}** (`{f['cle']}`)", f["sens"], ", ".join(f["ouvre"]), ", ".join(f["n_ouvre_pas"]), f["exemple"]] for f in ic["formes"]]))
    B.append(IMAGES([(f"assets/img/icones/explorai-icone-{f['cle']}-bleu.svg", f"Forme {f['nom']}", f"{f['nom']} — {f['geometrie']}", "clair") for f in ic["formes"]]))
    B += [H(2, "Correspondance par livrable"),
          TABLE(["Livrable", "Section", "Forme"], [[a["livrable"], a["section"], f"`{a['forme']}`"] for a in ic["application_livrables"]]),
          H(2, "Fichiers"),
          P("Variantes : " + ", ".join(ic["variantes_de_couleur"]) + ". Motif de chemin : `assets/img/icones/explorai-icone-{forme}-{bleu|vert|blanc}.{svg|png}`; couleur héritée : `assets/img/icones/explorai-icone-{forme}.svg`. Choix de variante : section c11.")]
    return B


def s_motif(m):
    mo = m["motif"]
    return [P(mo["principe"]), P(f"Forme employée : `{mo['forme']}`."),
            H(2, "Règles"), UL(mo["regles"]),
            H(2, "Interdit"), UL(mo["interdits"]),
            IMAGES([("assets/img/icones/explorai-icone-exploration-vert.svg", "Forme Exploration verte", "Motif sur fond bleu : variante verte", "bleu"),
                    ("assets/img/icones/explorai-icone-exploration-bleu.svg", "Forme Exploration bleue", "Motif sur fond clair : variante bleue", "clair")])]


def s_tableaux(m):
    t = m["tableaux"]
    return [H(2, "Traitement"),
            TABLE(["Élément", "Traitement", "Valeur"], [[r["element"], r["traitement"], r["valeur"] or "—"] for r in t["regles"]]),
            H(2, "Web"), P(t["regle_web"]),
            H(2, "Exemple"),
            P("Exemple fictif conforme : section c12, « Exemple de tableau ».")]


def s_graphiques(m):
    g = m["graphiques"]
    return [H(2, "Paramètres"), TABLE(["Paramètre", "Valeur"], [[p["parametre"], p["valeur"]] for p in g["parametres"]]),
            H(2, "Types admis"), TABLE(["Type", "Usage"], [[x["type"], x["usage"]] for x in g["types"]]),
            H(2, "Règle de livraison"), NOTE("Obligatoire", g["regle_de_livraison"], "attention")]


def s_ecriture(m):
    e = m["ecriture"]
    return [H(2, "Conventions"), TABLE(["Cas", "Règle", "Exemple"], [[c["cas"], c["regle"], c["exemple"]] for c in e["conventions"]]),
            H(2, "Caractères"),
            P("Les exemples ci-dessus contiennent les caractères réels : les recopier tels quels."),
            TABLE(["Caractère", "Unicode", "Emploi"], [[c["caractere"], f"`{c['unicode']}`", c["emploi"]] for c in e["caracteres"]]),
            H(2, "Ton de voix"), UL(e["ton_de_voix"]),
            P("Nom de la marque et signature : section c00.")]


def s_supports(m):
    s = m["supports"]
    w = s["web"]
    return [NOTE("Règle commune", s["regle_commune"]),
            H(2, "Document"),
            P(f"Formats : {', '.join(s['document']['formats'])}. {s['document']['resume']} Règles complètes : section c12."),
            H(2, "Web et interface"),
            TABLE(["Élément", "Règle"], [
                ["Fond de page", w["fond_de_page"]],
                ["Rayons", f"{w['rayons']['petits_elements']} petits éléments · {w['rayons']['cartes']} cartes · {w['rayons']['blocs_pleine_largeur']} blocs pleine largeur · {w['rayons']['boutons_et_etiquettes']} boutons et étiquettes"],
                ["Focus", w["focus"]],
                ["Survol", w["survol"]],
                ["Mouvement", w["mouvement"]],
                ["Densité — site", w["densite"]["site"]],
                ["Densité — application", w["densite"]["application"]],
            ]),
            P("Formes de contenu web : section c13. Interface d'application : section c14.")]


def s_actifs(m, manifeste):
    a = m["actifs"]
    doc = m["document"]
    B = [P(a["principe"]),
         H(2, "Variante selon le fond"),
         TABLE(["Fond", "Logo", "Icône"], [[x["fond"], f"`{x['logo']}`" if x["logo"] != "—" else "—", f"`{x['icone']}`"] for x in a["variante_selon_le_fond"]]),
         H(2, "Format selon le support"),
         TABLE(["Support", "Format", "Raison"], [[x["support"], x["format"], x["raison"]] for x in a["format_selon_le_support"]]),
         H(2, "À faire, à éviter"),
         TABLE(["", "Énoncé"], [["À faire", x] for x in a["a_faire"]] + [["À éviter", x] for x in a["a_eviter"]]),
         H(2, "Télécharger"),
         P(f"Préfixe GitHub Pages : `{doc['url_site']}`. Préfixe brut : `{doc['url_brute']}`. Adresse d'un actif = préfixe + chemin."),
         TABLE(["Motif", "Chemin"], [[k, f"`{v}`"] for k, v in a["motifs_de_chemin"].items()]),
         P("Formes : " + ", ".join(f"`{f['cle']}`" for f in m["iconographie"]["formes"]) + ".")]
    B.append(H(2, "Inventaire"))
    tot = manifeste["document"]["totaux"]
    B.append(P("Totaux : " + ", ".join(f"{v} {k}" for k, v in tot.items()) + ". Inventaire complet, avec URL, dimensions, poids et empreinte SHA-256 : `data/explorai-actifs.json`."))
    B.append(TABLE(["Chemin", "Type", "Forme", "Variante", "Dimensions"],
                   [[f"`{x['chemin']}`", x["type"], x.get("forme", "—"), x.get("variante", "—"), x["dimensions"]] for x in manifeste["actifs"]]))
    B.append(H(2, "Usage par variante"))
    rows = [["logo", k, v] for k, v in a["usage_par_variante"]["logo"].items()] + [["icône", k, v] for k, v in a["usage_par_variante"]["icone"].items()] + [["favicon", "—", a["usage_par_variante"]["favicon"]]]
    B.append(TABLE(["Type", "Variante", "Usage"], rows))
    B.append(H(2, "Insertion"))
    for x in a["insertion"]:
        B.append(CODE(x["langage"], x["code"], x["contexte"]))
    B.append(H(2, "Provenance"))
    B.append(TABLE(["Lot", "Provenance"], [[k.replace("_", " "), v] for k, v in a["provenance"].items()]))
    B.append(H(2, "Nomenclature"))
    n = a["nomenclature"]
    B.append(TABLE(["Catégorie", "Règle", "Exemples", "Raison"], [
        ["Fichier du dépôt", n["fichier_du_depot"]["regle"], ", ".join(f"`{e}`" for e in n["fichier_du_depot"]["exemples"]), n["fichier_du_depot"]["raison"]],
        ["Actif de marque", n["actif_de_marque"]["regle"], ", ".join(f"`{e}`" for e in n["actif_de_marque"]["exemples"]), n["actif_de_marque"]["raison"]],
        ["Section de règles", n["section_de_regles"]["regle"], ", ".join(f"`{e}`" for e in n["section_de_regles"]["exemples"]), n["section_de_regles"]["raison"]],
        ["Archive", n["archive"], "`explorai-marque.zip`", "—"],
    ]))
    return B


def s_document(m):
    d = m["document_gabarit"]
    B = [P(d["principe"]), NOTE("Modèle", d["modele"]),
         H(2, "Page"), TABLE(["Paramètre", "Valeur"], [[x["parametre"], x["valeur"]] for x in d["page"]]),
         H(2, "Rythme et découpage"), TABLE(["Règle", "Énoncé"], [[x["regle"], x["enonce"]] for x in d["rythme"]]),
         H(2, "Styles nommés"),
         TABLE(["Style", "Police", "Graisse", "Corps (pt)", "Interligne", "Couleur", "Emploi"],
               [[s["style"], s["police"], str(s["graisse"]), fmt_nombre(s["corps_pt"]), ("%.2f" % s["interligne"]).replace(".", ","), s["couleur"], s["emploi"]] for s in d["styles"]],
               ["gauche", "gauche", "droite", "droite", "droite", "gauche", "gauche"]),
         P("Aucun style n'emploie l'italique."),
         H(2, "Types de page"),
         TABLE(["Type", "Forme d'icône", "Règle"], [[t["type"], f"`{t['forme']}`" if " " not in t["forme"] else t["forme"], t["regle"]] for t in d["types_de_page"]]),
         H(2, "Cohérence des chiffres"), NOTE("Règle", d["regle_de_coherence"], "attention"),
         H(2, "Polices dans un document"), P(d["polices"]["comportement"]),
         TABLE(["", "Énoncé"], [["À faire", x] for x in d["polices"]["a_faire"]] + [["À éviter", x] for x in d["polices"]["a_eviter"]]),
         P(d["polices"]["note_web"])]
    ex = d["exemple_tableau"]
    B += [H(2, "Exemple de tableau", "exemple-de-tableau"),
          TABLE(ex["colonnes"], ex["lignes"], ex["alignement"], legende=f"{ex['titre']} — accent {ex['accent']} ({ex['statut']})", total=ex["total"],
                accent={"turquoise": "cyan", "vert": "green", "lavande": "lavender", "rose": "pink"}[ex["accent"]]),
          P(ex["note"], "note"),
          P("Vérification avant diffusion : section c15.")]
    return B


def s_contenu_web(m):
    c = m["contenu_web"]
    return [P(c["principe"]),
            H(2, "Hiérarchie des titres"), P(c["hierarchie"]["regle"]),
            TABLE(["Niveau", "Règle"], [[n["niveau"], n["regle"]] for n in c["hierarchie"]["niveaux"]]),
            H(2, "Texte"), TABLE(["Élément", "Règle"], [[t["element"], t["regle"]] for t in c["texte"]]),
            H(3, "Disposition à deux colonnes"), UL(c["deux_colonnes"]),
            H(2, "Mises en valeur"), TABLE(["Forme", "Règle"], [[x["forme"], x["regle"]] for x in c["mises_en_valeur"]]),
            H(2, "Tableaux et graphiques"), UL(c["tableaux_web"]),
            H(2, "Contenus interactifs"), P(c["interactif"]["principe"]),
            TABLE(["Composant", "Emploi"], [[x["composant"], x["emploi"]] for x in c["interactif"]["composants"]]),
            H(2, "Listes et séquences"), UL(c["listes"]),
            H(2, "Médias"), UL(c["medias"]),
            H(2, "Contenu technique"), UL(c["technique"])]


def s_interface(m):
    i = m["interface"]
    return [P(i["principe"]),
            H(2, "Principes"), TABLE(["Id", "Principe"], [[p["id"], p["enonce"]] for p in i["principes"]]),
            NOTE("Validation humaine", i["validation_humaine"]),
            H(2, "Composants"), TABLE(["Composant", "Règle"], [[c["composant"], c["regle"]] for c in i["composants"]]),
            H(2, "Plancher de qualité"), TABLE(["Critère", "Énoncé"], [[p["critere"], p["enonce"]] for p in i["plancher_de_qualite"]])]


def s_verification(m):
    v = m["verification"]
    return [H(2, "Tout livrable"), OL(["☐ " + x for x in v["tout_livrable"]]),
            H(2, "Document"), TABLE(["Point", "Vérification"], [[x["point"], x["enonce"]] for x in v["document"]]),
            H(2, "Application"), P(v["application"])]


def s_limites(m):
    l = m["limites"]
    return [H(2, "Absent du dépôt"), UL(l["absent_du_depot"]),
            H(2, "Polices"), UL(l["polices"]),
            H(2, "Contenu non vérifié"), UL(l["contenu_non_verifie"]),
            H(2, "Hypothèses de publication"), UL(l["hypotheses_de_publication"]),
            H(2, "Note de production"), P(l["note_de_production"]),
            H(2, "À compléter"), UL(l["a_completer"])]


CONSTRUCTEURS = {
    "c00": s_identite, "c01": s_logo, "c02": s_typo, "c03": s_palette, "c04": s_couleur_usage,
    "c05": s_icono, "c06": s_motif, "c07": s_tableaux, "c08": s_graphiques, "c09": s_ecriture,
    "c10": s_supports, "c11": None, "c12": s_document, "c13": s_contenu_web, "c14": s_interface,
    "c15": s_verification, "c16": s_limites,
}


def blocs_section(m, s, manifeste):
    if s["id"] == "c11":
        return s_actifs(m, manifeste)
    return CONSTRUCTEURS[s["id"]](m)


# ---------------------------------------------------------------------------
# Manifeste des actifs
# ---------------------------------------------------------------------------
def dimensions(chemin):
    p = RACINE / chemin
    if p.suffix == ".svg":
        vb = re.search(r'viewBox="([^"]+)"', p.read_text(encoding="utf-8"))
        return (vb.group(1) if vb else "?"), "viewBox"
    if p.suffix == ".png":
        with open(p, "rb") as f:
            f.read(16)
            w, h = struct.unpack(">II", f.read(8))
        return f"{w}×{h}", "pixels"
    if p.suffix == ".ico":
        with open(p, "rb") as f:
            _, _, n = struct.unpack("<HHH", f.read(6))
            tailles = []
            for _ in range(n):
                w, h = struct.unpack("<BB", f.read(2))
                f.read(14)
                tailles.append(f"{w or 256}×{h or 256}")
        return ", ".join(tailles), "pixels"
    return "—", "—"


def manifeste_actifs(m):
    doc, a = m["document"], m["actifs"]
    formes = {f["cle"]: f for f in m["iconographie"]["formes"]}
    fichiers = []
    for c in sorted((RACINE / "assets/img/logo").glob("*")):
        v = re.search(r"explorai-logo-(\w+)\.", c.name).group(1)
        fichiers.append(dict(type="logo", variante=v, usage=a["usage_par_variante"]["logo"][v], regles="c01", preferer=(c.suffix == ".svg" and v != "vert")))
        fichiers[-1]["_c"] = c
    for cle in formes:
        for v in ("bleu", "vert", "blanc"):
            for ext in ("svg", "png"):
                c = RACINE / f"assets/img/icones/explorai-icone-{cle}-{v}.{ext}"
                fichiers.append(dict(type="icone", forme=cle, sens=formes[cle]["sens"], variante=v, usage=a["usage_par_variante"]["icone"][v], regles="c05", preferer=(ext == "svg"), _c=c))
        c = RACINE / f"assets/img/icones/explorai-icone-{cle}.svg"
        fichiers.append(dict(type="icone", forme=cle, sens=formes[cle]["sens"], variante="heritee", usage=a["usage_par_variante"]["icone"]["heritee"], regles="c05", preferer=True, _c=c))
    for c in (RACINE / "assets/img/explorai-favicon.png", RACINE / "favicon.ico"):
        fichiers.append(dict(type="favicon", variante="bleu-vert", usage=a["usage_par_variante"]["favicon"], regles="c01", preferer=c.suffix == ".png", _c=c))
    for f in m["typographie"]["fichiers"]["liste"]:
        for fmt in ("woff2", "ttf"):
            c = RACINE / f[fmt]
            fichiers.append(dict(type="police", famille=f["famille"], graisse=f["graisse"], variante=str(f["graisse"]),
                                 usage="Web (@font-face)." if fmt == "woff2" else "Installation sur poste, intégration bureautique.", regles="c02", preferer=fmt == "woff2", _c=c))
    actifs = []
    for f in fichiers:
        c = f.pop("_c")
        rel = c.relative_to(RACINE).as_posix()
        if not c.exists():
            raise SystemExit(f"Actif manquant : {rel}")
        dim, unite = dimensions(rel)
        e = {"id": slugifier(c.stem.replace("explorai-", "") + "-" + c.suffix[1:]), "type": f["type"]}
        for k in ("forme", "sens", "famille", "graisse"):
            if k in f:
                e[k] = f[k]
        e.update({"variante": f["variante"], "format": c.suffix[1:].upper(), "chemin": rel,
                  "url": doc["url_site"] + rel, "url_brute": doc["url_brute"] + rel,
                  "octets": c.stat().st_size, "sha256": hashlib.sha256(c.read_bytes()).hexdigest(),
                  "dimensions": dim, "unite_dimensions": unite, "usage": f["usage"],
                  "preferer": f["preferer"], "regles": f["regles"]})
        actifs.append(e)
    totaux = {}
    for e in actifs:
        totaux[e["type"]] = totaux.get(e["type"], 0) + 1
    totaux["total"] = len(actifs)
    return {
        "document": {
            "titre": "Manifeste des actifs de marque Explorai",
            "avertissement": AVERTISSEMENT,
            "version": doc["version"], "date_version": doc["date_version"], "langue": doc["langue"],
            "regles": SOURCE,
            "base_url": doc["url_site"], "base_url_brute": doc["url_brute"],
            "choix_de_variante": {x["fond"]: {"logo": x["logo"], "icone": x["icone"]} for x in a["variante_selon_le_fond"]},
            "motifs_de_chemin": a["motifs_de_chemin"],
            "totaux": totaux,
        },
        "actifs": actifs,
    }


# ---------------------------------------------------------------------------
# Jetons
# ---------------------------------------------------------------------------
def jetons_json(m):
    c, t, w = m["couleurs"], m["typographie"], m["supports"]["web"]
    col = {}
    for x in c["marque"] + c["etendue"]:
        col[x["variable_css"][2:]] = {"$type": "color", "$value": x["hex"], "$description": f"{x['nom']} — {x['role']}"}
    for k, nom in (("10", "10"), ("22", "22")):
        td = c["teintes_derivees"][k]
        for coul, var in (("turquoise", "cyan"), ("vert", "green"), ("lavande", "lav"), ("rose", "pink")):
            col[f"{var}-{nom}"] = {"$type": "color", "$value": td[coul], "$description": f"{coul} à {k} % — {td['usage']}"}
    pile_n = t["declaration_normative"]
    def pile(decl):
        return [p.strip().strip("'") for p in decl.split(":", 1)[1].rstrip(";").split(",")]
    return {
        "$description": f"Jetons de design Explorai, version {m['document']['version']} ({m['document']['date_version']}). Format DTCG (Design Tokens Community Group). {AVERTISSEMENT}",
        "couleur": col,
        "police": {
            "sans": {"$type": "fontFamily", "$value": pile(pile_n["sans"]), "$description": "Pile normative, charte v3"},
            "mono": {"$type": "fontFamily", "$value": pile(pile_n["mono"]), "$description": "Pile normative, charte v3"},
            "sans-web": {"$type": "fontFamily", "$value": pile(t["declaration_web_etendue"]["sans"]), "$description": t["declaration_web_etendue"]["statut"]},
            "mono-web": {"$type": "fontFamily", "$value": pile(t["declaration_web_etendue"]["mono"]), "$description": t["declaration_web_etendue"]["statut"]},
        },
        "graisse": {str(g): {"$type": "fontWeight", "$value": g} for g in t["principale"]["graisses"]},
        "rayon": {k.replace("_", "-"): {"$type": "dimension", "$value": compact(v)} for k, v in w["rayons"].items()},
        "focus": {"$type": "border", "$value": {"color": "{couleur.cyan}", "width": "3px", "style": "solid"}, "$description": w["focus"]},
        "accent-rotation": {"$description": "Ordre de rotation des accents (section c04)", "$type": "color",
                            "$value": ["{couleur.cyan}", "{couleur.green}", "{couleur.lavender}", "{couleur.pink}"]},
    }


def jetons_css(m):
    c, t, w = m["couleurs"], m["typographie"], m["supports"]["web"]
    doc = m["document"]
    L = ["/* =====================================================================",
         "   Explorai — jetons de design",
         f"   Version  : v{doc['version']} — {doc['date_version']}",
         f"   Norme    : {doc['norme']} ({doc['date_norme']})",
         f"   {AVERTISSEMENT}",
         f"   URL      : {doc['url_site']}assets/css/explorai-jetons.css",
         "   ===================================================================== */", ""]
    noms = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold"}
    for f in t["fichiers"]["liste"]:
        fam = f["famille"]
        fichier = f["woff2"].split("/")[-1]
        L.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{f['graisse']};font-display:swap;src:url('../fonts/{fichier}') format('woff2');}}")
    L += ["", ":root{", "  /* couleurs */"]
    for x in c["marque"] + c["etendue"]:
        L.append(f"  {x['variable_css']}:{x['hex']};  /* {x['nom']} */")
    L.append("  /* teintes dérivées 10 % / 22 % */")
    for coul, var in (("turquoise", "cyan"), ("vert", "green"), ("lavande", "lav"), ("rose", "pink")):
        L.append(f"  --{var}-10:{c['teintes_derivees']['10'][coul]};  --{var}-22:{c['teintes_derivees']['22'][coul]};")
    L += ["  /* accent courant, redéfini par [data-accent] */",
          "  --accent:var(--cyan); --accent-10:var(--cyan-10); --accent-22:var(--cyan-22);",
          "  /* polices : pile web étendue (voir section c02) */",
          "  --font-sans:" + t["declaration_web_etendue"]["sans"].split(":", 1)[1].strip(),
          "  --font-mono:" + t["declaration_web_etendue"]["mono"].split(":", 1)[1].strip(),
          "  /* rayons */"]
    for k, v in w["rayons"].items():
        L.append(f"  --radius-{k.replace('_', '-')}:{compact(v)};")
    L += ["}", "",
          "[data-accent=\"cyan\"]{--accent:var(--cyan);--accent-10:var(--cyan-10);--accent-22:var(--cyan-22);}",
          "[data-accent=\"green\"]{--accent:var(--green);--accent-10:var(--green-10);--accent-22:var(--green-22);}",
          "[data-accent=\"lavender\"]{--accent:var(--lavender);--accent-10:var(--lav-10);--accent-22:var(--lav-22);}",
          "[data-accent=\"pink\"]{--accent:var(--pink);--accent-10:var(--pink-10);--accent-22:var(--pink-22);}",
          "",
          "/* focus normé : turquoise 3 px, décalé de 3 px, jamais supprimé */",
          ":focus-visible{outline:3px solid var(--cyan);outline-offset:3px;}", ""]
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def entete_md(m, s, url_md, url_html):
    doc = m["document"]
    return "\n".join([
        "---",
        f"id: {s['id']}",
        f"titre: \"{s['titre']}\"",
        f"resume: \"{s['resume']}\"",
        f"version: \"{doc['version']}\"",
        f"date: {doc['date_version']}",
        f"norme: \"{doc['norme']}\"",
        f"langue: {doc['langue']}",
        f"source: \"{SOURCE}#/{s['cle']}\"",
        f"url: {url_md}",
        f"html: {url_html}",
        f"genere: \"{AVERTISSEMENT}\"",
        "---", ""])


def blocs_accueil(m):
    doc = m["document"]
    B = [P(f"Référence de la marque Explorai, pensée d'abord pour les agents (LLM) et lisible par les personnes. "
           f"Version **{doc['version']}** du {doc['date_version']}, conforme aux {doc['norme']} ({doc['date_norme']}). Langue : {doc['langue']}."),
         H(2, "Pour un agent : ordre de lecture", "pour-un-agent"),
         OL([f"`llms.txt` — orientation et liste des ressources ({doc['url_site']}llms.txt).",
             f"`{SOURCE}` — **toutes les règles**, structurées. C'est la source de vérité.",
             "`data/explorai-actifs.json` — chaque fichier d'image et de police, avec son URL, ses dimensions, son empreinte et son usage admis.",
             "`regles/cNN-*.md` — les mêmes règles en prose Markdown, une section par fichier. `llms-full.txt` les réunit en un seul fichier.",
             "`assets/css/explorai-jetons.css` ou `data/explorai-jetons.json` — jetons prêts à importer.",
             "Avant de livrer : liste de contrôle de la section c15."]),
         H(2, "Hiérarchie des sources", "hierarchie-des-sources"),
         TABLE(["Rang", "Fichier", "Statut"], [
             ["1", f"`{SOURCE}`", "Source de vérité unique. Seul fichier de règles modifié à la main."],
             ["2", "`regles/*.md`, `*.html`, `llms.txt`, `llms-full.txt`, `README.md`, `SKILL.md`", "Dérivés générés. En cas d'écart, la source s'applique."],
             ["2", "`data/explorai-actifs.json`, `data/explorai-jetons.json`, `data/explorai-index.json`, `assets/css/explorai-jetons.css`", "Dérivés générés. Les chemins et empreintes du manifeste sont calculés sur les fichiers réels."],
             ["3", "`CHANGELOG.md`", "Journal des versions, rédigé à la main."],
         ]),
         NOTE("Arbitrage", doc["arbitrage"]),
         H(2, "Sections", "sections"),
         TABLE(["Id", "Section", "Contenu", "JSON"],
               [[s["id"], f"[{s['titre']}]({s['id']})", s["resume"], f"`#/{s['cle']}`"] for s in m["sections"]]),
         H(2, "Questions fréquentes", "questions-frequentes"),
         TABLE(["Question", "Réponse courte", "Section"],
               [[q["question"], q["reponse"], f"[{q['section']}]({q['section']})"] for q in m["questions_frequentes"]]),
         H(2, "Fichiers lisibles par machine", "fichiers-machine"),
         TABLE(["Fichier", "Contenu"], [
             ["[llms.txt](llms.txt)", "Orientation pour agents (format llmstxt.org)."],
             ["[llms-full.txt](llms-full.txt)", "Toutes les sections en Markdown, en un fichier."],
             [f"[{SOURCE}]({SOURCE})", "Règles structurées — source de vérité."],
             ["[data/explorai-actifs.json](data/explorai-actifs.json)", "Manifeste des actifs : chemin, URL, URL brute, format, dimensions, octets, SHA-256, usage."],
             ["[data/explorai-jetons.json](data/explorai-jetons.json)", "Jetons au format DTCG."],
             ["[data/explorai-index.json](data/explorai-index.json)", "Index du dépôt : sections, fichiers, URL."],
             ["[assets/css/explorai-jetons.css](assets/css/explorai-jetons.css)", "Variables CSS, @font-face, accents `data-accent`, focus."],
             ["[SKILL.md](SKILL.md)", "Le dépôt employé comme skill d'agent."],
         ]),
         H(2, "Arborescence", "arborescence"),
         CODE("text", ARBORESCENCE),
         H(2, "Publication et régénération", "publication"),
         OL(["Pousser la branche `main` sur " + doc["depot"] + ".",
             "Dans GitHub : Settings > Pages > Deploy from a branch > `main` / `(root)`. Le fichier `.nojekyll` sert les `.md` et `.json` tels quels.",
             f"Le site répond alors à {doc['url_site']}.",
             "Pour modifier une règle : éditer `" + SOURCE + "`, lancer `python3 outils/construire.py`, puis `python3 outils/construire.py --verifier`, consigner dans `CHANGELOG.md`, mettre à jour `VERSION`, étiqueter le commit (`git tag vX.Y`)."]),
         P("Limites et contenu non vérifié : section c16.")]
    return B


ARBORESCENCE = """explorai-marque/
├── README.md              accueil GitHub (généré)
├── index.html             accueil GitHub Pages (généré)
├── c00-…html … c16-…html  une page HTML par section (générées)
├── llms.txt               orientation pour agents (généré)
├── llms-full.txt          toutes les règles en Markdown (généré)
├── SKILL.md               dépôt employé comme skill (généré)
├── CHANGELOG.md           journal des versions
├── VERSION                numéro de version
├── robots.txt · sitemap.xml · favicon.ico · .nojekyll
├── data/
│   ├── explorai-marque.json   SOURCE DE VÉRITÉ
│   ├── explorai-actifs.json   manifeste des actifs (généré)
│   ├── explorai-jetons.json   jetons DTCG (généré)
│   └── explorai-index.json    index du dépôt (généré)
├── regles/
│   └── c00-…md … c16-…md      une section par fichier (générées)
├── assets/
│   ├── css/explorai-jetons.css  jetons CSS (généré)
│   ├── css/explorai-site.css    mise en page du site
│   ├── fonts/                   DM Sans, IBM Plex Mono (WOFF2, TTF, OFL)
│   └── img/
│       ├── explorai-favicon.png
│       ├── logo/     explorai-logo-{bleu|blanc|vert}.{svg|png}
│       └── icones/   explorai-icone-{forme}[-{bleu|vert|blanc}].{svg|png}
└── outils/
    └── construire.py           générateur et vérificateur"""


def page_html(m, titre, resume, corps, courant, alt_md, pointeur, surtitre):
    doc = m["document"]
    v = doc["version"]
    nav = []
    for s in m["sections"]:
        cur = ' aria-current="page"' if s["id"] == courant else ""
        nav.append(f'<li><a href="{s["id"]}-{s["slug"]}.html"{cur}><span class="mono">{s["id"]}</span> {html.escape(s["titre"])}</a></li>')
    fichier = "index.html" if courant == "accueil" else next(f"{s['id']}-{s['slug']}.html" for s in m["sections"] if s["id"] == courant)
    canon = doc["url_site"] + ("" if fichier == "index.html" else fichier)
    ld = {"@context": "https://schema.org", "@type": "TechArticle", "headline": titre, "description": resume,
          "inLanguage": doc["langue"], "version": v, "dateModified": doc["date_version"], "url": canon,
          "isPartOf": {"@type": "WebSite", "name": "Explorai — normes graphiques", "url": doc["url_site"]},
          "publisher": {"@type": "Organization", "name": "Explorai", "url": "https://www.explor.ai"},
          "encoding": [{"@type": "MediaObject", "encodingFormat": "text/markdown", "contentUrl": doc["url_site"] + alt_md},
                       {"@type": "MediaObject", "encodingFormat": "application/json", "contentUrl": doc["url_site"] + SOURCE}]}
    return f"""<!doctype html>
<html lang="fr-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)} — Explorai, normes graphiques</title>
<meta name="description" content="{html.escape(resume)}">
<meta name="generator" content="outils/construire.py — v{v}">
<link rel="canonical" href="{canon}">
<link rel="alternate" type="text/markdown" href="{alt_md}" title="Version Markdown">
<link rel="alternate" type="application/json" href="{SOURCE}{pointeur}" title="Règles JSON">
<link rel="help" href="llms.txt" type="text/plain" title="Orientation pour agents">
<link rel="icon" href="assets/img/explorai-favicon.png" type="image/png">
<link rel="stylesheet" href="assets/css/explorai-jetons.css?v={v}">
<link rel="stylesheet" href="assets/css/explorai-site.css?v={v}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<!-- {AVERTISSEMENT} -->
<a class="saut" href="#contenu">Aller au contenu</a>
<header class="entete">
  <a href="index.html" class="logo"><img src="assets/img/logo/explorai-logo-bleu.svg" alt="Explorai — accueil des normes graphiques" width="132"></a>
  <p class="mono">{html.escape(doc['norme'])} · dépôt v{v} · {doc['date_version']}</p>
</header>
<div class="cadre">
<nav class="sommaire" aria-label="Sections">
  <p class="surtitre"><a href="index.html">Accueil</a></p>
  <ol>
  {chr(10).join(nav)}
  </ol>
</nav>
<main id="contenu">
<article>
<header class="titre">
  <img class="repere" src="assets/img/icones/explorai-icone-exploration-bleu.svg" alt="" width="56">
  <p class="surtitre">{html.escape(surtitre)}</p>
  <h1>{html.escape(titre)}</h1>
  <p class="intro">{html.escape(resume)}</p>
  <p class="sources">Mêmes règles : <a href="{alt_md}">Markdown</a> · <a href="{SOURCE}">JSON</a> · <a href="llms-full.txt">texte intégral</a></p>
</header>
{corps}
</article>
</main>
</div>
<footer class="pied">
  <img src="assets/img/logo/explorai-logo-blanc.svg" alt="Explorai" width="150">
  <p>« {html.escape(m['identite']['marque']['signature'])} »</p>
  <p class="mono">v{v} · {doc['date_version']} · <a href="{doc['depot']}">dépôt GitHub</a> · <a href="llms.txt">llms.txt</a> · <a href="CHANGELOG.md">journal</a></p>
</footer>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Fichiers d'orientation
# ---------------------------------------------------------------------------
def llms_txt(m):
    doc = m["document"]
    S = doc["url_site"]
    c = {x["cle"]: x["hex"] for x in m["couleurs"]["marque"]}
    L = [f"# Explorai — normes graphiques (dépôt explorai-marque v{doc['version']})", "",
         f"> Référence de la marque Explorai, firme montréalaise en intelligence artificielle et en développement logiciel. "
         f"Règles applicables (identité, logo, typographie, palette, accents, icônes, motif, tableaux, graphiques, écriture, supports, "
         f"actifs, document, contenu web, interface, vérification) et fichiers d'actifs téléchargeables. "
         f"Norme : {doc['norme']} ({doc['date_norme']}). Langue : {doc['langue']}. Version {doc['version']}, {doc['date_version']}.", "",
         f"Source de vérité unique : {S}{SOURCE}. Tous les autres fichiers en sont générés. "
         f"Pour appliquer la marque : charger ce JSON, puis {S}data/explorai-actifs.json pour les URL des images et des polices. "
         f"Les URL brutes ({doc['url_brute']}…) fonctionnent aussi sans GitHub Pages.", "",
         "## Règles essentielles", "",
         f"- Nom en texte courant : Explorai, en un seul mot. Le logo épelle « explor.ai »; cet écart ne passe jamais au texte.",
         f"- Signature : « {m['identite']['marque']['signature']} », jamais verrouillée avec le logo.",
         f"- Couleurs : bleu foncé {c['bleu']}, vert {c['vert']}, turquoise {c['turquoise']}, lavande {c['lavande']}, rose vibrant {c['rose']}, White Smoke {c['white_smoke']} (fond web seulement).",
         "- Un seul accent par unité de lecture, rotation turquoise, vert, lavande, rose. Le vert marque les totaux et les synthèses. Le rose n'est jamais un texte.",
         "- Polices : DM Sans + IBM Plex Mono; repli Calibri + Consolas, puis Arial + Courier New; jamais de mélange; aucun italique.",
         "- Logo : bleu sur fond clair, blanc sur fond bleu ou saturé; zone de protection d'une hauteur de logo; jamais recoloré ni déformé.",
         "- Icônes : neuf formes, une intention par forme; bleu sur fond clair, vert sur fond bleu; Exploration seule admise en motif.",
         "- Écriture : " + ", ".join(x["exemple"] for x in m["ecriture"]["conventions"] if x["cas"] in ("Symbole monétaire", "Pourcentage", "Guillemets")) + ", majuscules accentuées; espace insécable U+00A0, espace fine insécable U+202F pour les milliers.",
         "- Tout graphique porte une note de lecture; toute barre part de zéro.", "",
         "## Données", "",
         f"- [explorai-marque.json]({S}{SOURCE}): toutes les règles, structurées — source de vérité",
         f"- [explorai-actifs.json]({S}data/explorai-actifs.json): manifeste des logos, icônes, favicons et polices — url, url_brute, format, dimensions, octets, sha256, usage",
         f"- [explorai-jetons.json]({S}data/explorai-jetons.json): jetons de design au format DTCG",
         f"- [explorai-jetons.css]({S}assets/css/explorai-jetons.css): variables CSS, @font-face, attribut data-accent, focus",
         f"- [explorai-index.json]({S}data/explorai-index.json): index du dépôt, sections et URL",
         "", "## Règles par section (Markdown)", ""]
    for s in m["sections"]:
        L.append(f"- [{s['id']} — {s['titre']}]({S}regles/{s['id']}-{s['slug']}.md): {s['resume']}")
    L += ["", "## Optional", "",
          f"- [llms-full.txt]({S}llms-full.txt): toutes les sections réunies en un seul fichier Markdown",
          f"- [SKILL.md]({S}SKILL.md): mode d'emploi du dépôt comme skill d'agent",
          f"- [Site HTML]({S}index.html): les mêmes règles, mises en page pour les personnes",
          f"- [CHANGELOG.md]({S}CHANGELOG.md): journal des versions",
          f"- [Dépôt GitHub]({doc['depot']}): sources et historique", ""]
    return "\n".join(L)


def skill_md(m):
    doc = m["document"]
    L = ["---", "name: explorai-marque",
         "description: Applique les normes graphiques Explorai (couleurs, polices, logo, icônes, tableaux, graphiques, écriture française, documents Word et PDF, pages web, interfaces) à tout livrable Explorai, et vérifie sa conformité avant diffusion.",
         "---", "",
         f"# Explorai — normes graphiques (v{doc['version']})", "",
         f"<!-- {AVERTISSEMENT} -->", "",
         "## Quand utiliser ce skill", "",
         "- Produire un document, un rapport, une offre, une page web, une interface ou un graphique aux couleurs d'Explorai.",
         "- Vérifier qu'un livrable respecte la marque avant diffusion.", "",
         "## Méthode", "",
         f"1. Lire `{SOURCE}` : toutes les règles, structurées. Il fait foi.",
         "2. Identifier le support (document, web, interface) et lire la section correspondante dans `regles/` : c12, c13 ou c14.",
         "3. Choisir les actifs dans `data/explorai-actifs.json` selon le fond (champ `document.choix_de_variante`). Référencer le fichier par son chemin ou son `url_brute`; ne jamais recolorer ni recopier un tracé.",
         "4. Pour le web, importer `assets/css/explorai-jetons.css`; ailleurs, lire les valeurs dans `data/explorai-jetons.json`.",
         "5. Pour un fichier bureautique, employer les polices de `assets/fonts/` ou le niveau de repli 2, sans mélange.",
         "6. Avant de livrer, cocher la liste de `regles/c15-verification.md`.",
         "7. Règle absente ou contradictoire : ne pas inventer; signaler l'écart au responsable de la marque.", "",
         "## Rappels", ""]
    for r in m["couleur_en_usage"]["regles"]:
        L.append(f"- {r['id']} — {r['enonce']}")
    L += ["", "## Fichiers", ""]
    for s in m["sections"]:
        L.append(f"- `regles/{s['id']}-{s['slug']}.md` — {s['titre']} : {s['resume']}")
    L.append("")
    return "\n".join(L)


def index_json(m, manifeste):
    doc = m["document"]
    S = doc["url_site"]
    return {
        "avertissement": AVERTISSEMENT,
        "identifiant": doc["identifiant"], "version": doc["version"], "date_version": doc["date_version"],
        "norme": {"nom": doc["norme"], "date": doc["date_norme"]}, "langue": doc["langue"],
        "depot": doc["depot"], "url_site": S, "url_brute": doc["url_brute"],
        "source_de_verite": {"chemin": SOURCE, "url": S + SOURCE, "url_brute": doc["url_brute"] + SOURCE},
        "ordre_de_lecture": ["llms.txt", SOURCE, "data/explorai-actifs.json", "regles/", "regles/c15-verification.md"],
        "fichiers": [
            {"chemin": "llms.txt", "role": "orientation", "genere": True},
            {"chemin": "llms-full.txt", "role": "texte intégral Markdown", "genere": True},
            {"chemin": SOURCE, "role": "règles — source de vérité", "genere": False},
            {"chemin": "data/explorai-actifs.json", "role": "manifeste des actifs", "genere": True},
            {"chemin": "data/explorai-jetons.json", "role": "jetons DTCG", "genere": True},
            {"chemin": "data/explorai-index.json", "role": "index", "genere": True},
            {"chemin": "assets/css/explorai-jetons.css", "role": "jetons CSS", "genere": True},
            {"chemin": "assets/css/explorai-site.css", "role": "mise en page du site", "genere": False},
            {"chemin": "SKILL.md", "role": "skill d'agent", "genere": True},
            {"chemin": "README.md", "role": "accueil GitHub", "genere": True},
            {"chemin": "CHANGELOG.md", "role": "journal des versions", "genere": False},
            {"chemin": "VERSION", "role": "numéro de version", "genere": True},
            {"chemin": "outils/construire.py", "role": "générateur", "genere": False},
        ],
        "sections": [{"id": s["id"], "titre": s["titre"], "resume": s["resume"], "pointeur_json": f"#/{s['cle']}",
                      "markdown": f"{S}regles/{s['id']}-{s['slug']}.md", "html": f"{S}{s['id']}-{s['slug']}.html"} for s in m["sections"]],
        "actifs": {"total": manifeste["document"]["totaux"]["total"], "manifeste": S + "data/explorai-actifs.json",
                   "motifs_de_chemin": m["actifs"]["motifs_de_chemin"]},
    }


# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------
def construire(dest):
    m = charger()
    doc = m["document"]
    S = doc["url_site"]
    rotation = ["cyan", "green", "lavender", "pink"]
    sorties = {}

    manifeste = manifeste_actifs(m)
    sorties["data/explorai-actifs.json"] = json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n"
    sorties["data/explorai-jetons.json"] = json.dumps(jetons_json(m), ensure_ascii=False, indent=2) + "\n"
    sorties["data/explorai-index.json"] = json.dumps(index_json(m, manifeste), ensure_ascii=False, indent=2) + "\n"
    sorties["assets/css/explorai-jetons.css"] = jetons_css(m)

    complet = [f"# Explorai — normes graphiques, texte intégral (v{doc['version']}, {doc['date_version']})", "",
               f"> {AVERTISSEMENT} Norme : {doc['norme']}. Source : {S}{SOURCE}. {doc['arbitrage']}", ""]
    for s in m["sections"]:
        base = f"{s['id']}-{s['slug']}"
        blocs = blocs_section(m, s, manifeste)
        md = Rendu("md-regles", m["sections"], S)
        corps_md = md.md(blocs)
        sorties[f"regles/{base}.md"] = entete_md(m, s, f"{S}regles/{base}.md", f"{S}{base}.html") + f"# {s['id']} — {s['titre']}\n\n{s['resume']}\n\n" + corps_md
        ab = Rendu("absolu", m["sections"], S)
        corps_ab = ab.md([H(x.niveau + 1, x.texte, x.ancre) if isinstance(x, H) else x for x in blocs])
        complet += [f"## {s['id']} — {s['titre']}", "", f"Source : {S}regles/{base}.md · JSON : `{SOURCE}#/{s['cle']}`", "", s["resume"], "", corps_ab, "---", ""]
        hr = Rendu("html", m["sections"], S)
        sorties[f"{base}.html"] = page_html(m, s["titre"], s["resume"], hr.html(blocs, rotation), s["id"], f"regles/{base}.md", f"#/{s['cle']}", f"{s['id'].upper()} / RÈGLES")
    sorties["llms-full.txt"] = "\n".join(complet)

    acc = blocs_accueil(m)
    sorties["README.md"] = (f"# Explorai — normes graphiques\n\n<!-- {AVERTISSEMENT} -->\n\n"
                            + Rendu("md-racine", m["sections"], S).md(acc))
    sorties["index.html"] = page_html(m, "Explorai — normes graphiques",
                                      f"Référence de la marque Explorai pour agents et personnes. Version {doc['version']}, {doc['norme']}.",
                                      Rendu("html", m["sections"], S).html(acc, rotation), "accueil", "README.md", "", "RÉFÉRENCE DE MARQUE")
    sorties["llms.txt"] = llms_txt(m)
    sorties["SKILL.md"] = skill_md(m)
    sorties["VERSION"] = doc["version"] + "\n"

    urls = [S] + [f"{S}{s['id']}-{s['slug']}.html" for s in m["sections"]]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', f"<!-- {AVERTISSEMENT} -->", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{doc['date_version']}</lastmod></url>")
    sm.append("</urlset>")
    sorties["sitemap.xml"] = "\n".join(sm) + "\n"
    sorties["robots.txt"] = "\n".join([
        f"# Explorai — normes graphiques v{doc['version']}. {AVERTISSEMENT}",
        "# Contenu public, destiné à être lu et appliqué par des personnes et des agents.",
        f"# Point d'entrée pour un agent : {S}llms.txt puis {S}{SOURCE}",
        "User-agent: *", "Allow: /", "",
        f"Sitemap: {S}sitemap.xml", ""])

    for chemin, contenu in sorties.items():
        p = Path(dest) / chemin
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenu, encoding="utf-8")
    return sorties


# ---------------------------------------------------------------------------
# Vérification
# ---------------------------------------------------------------------------
def verifier():
    erreurs = []
    m = charger()
    with tempfile.TemporaryDirectory() as tmp:
        sorties = construire(tmp)
        for chemin, contenu in sorties.items():
            reel = RACINE / chemin
            if not reel.exists():
                erreurs.append(f"absent : {chemin}")
            elif reel.read_text(encoding="utf-8") != contenu:
                erreurs.append(f"périmé (relancer construire.py) : {chemin}")

    # couleurs : toute valeur hex de la source appartient à la palette
    c = m["couleurs"]
    admis = {x["hex"].upper() for x in c["marque"] + c["etendue"]}
    for k in ("10", "22"):
        admis |= {v.upper() for kk, v in c["teintes_derivees"][k].items() if kk != "usage"}
    texte = (RACINE / SOURCE).read_text(encoding="utf-8")
    for h in set(re.findall(r"#[0-9A-Fa-f]{6}\b", texte)):
        if h.upper() not in admis:
            erreurs.append(f"couleur hors palette dans la source : {h}")

    # liens et images des pages générées
    for p in list(RACINE.glob("*.html")) + list(RACINE.glob("regles/*.md")) + [RACINE / "README.md"]:
        contenu = p.read_text(encoding="utf-8")
        refs = re.findall(r'(?:href|src)="([^"]+)"', contenu) + re.findall(r"\]\(([^)]+)\)", contenu)
        for r in refs:
            if re.match(r"^(https?:|mailto:|#)", r):
                continue
            cible = r.split("#")[0].split("?")[0]
            if cible and not (p.parent / cible).resolve().exists():
                erreurs.append(f"lien brisé dans {p.relative_to(RACINE)} : {r}")

    # URL absolues vers le site : le chemin doit exister dans le dépôt
    base = m["document"]["url_site"]
    for p in [RACINE / "llms.txt", RACINE / "llms-full.txt", RACINE / "data/explorai-actifs.json", RACINE / "data/explorai-index.json"]:
        for u in set(re.findall(re.escape(base) + r"[^\s\"')>\]`]*", p.read_text(encoding="utf-8"))):
            rel = u[len(base):].split("#")[0].rstrip(".,;:")
            if rel and not (RACINE / rel).exists():
                erreurs.append(f"URL sans fichier dans {p.name} : {u}")

    # termes retirés du périmètre
    for p in RACINE.rglob("*"):
        if p.is_file() and p.suffix in (".md", ".html", ".json", ".txt", ".css") and p.name not in ("CHANGELOG.md",) and "fonts" not in p.parts:
            t = p.read_text(encoding="utf-8")
            for motif in (r"exemple\.ca", r"-v6\b", r"presentation\.html", r"\bPOTX\b", r"PowerPoint", r"diapositive"):
                if re.search(motif, t, re.I):
                    erreurs.append(f"terme obsolète « {motif} » dans {p.relative_to(RACINE)}")

    # valeurs CSS : aucune espace insécable
    for p in (RACINE / "assets/css").glob("*.css"):
        if re.search("[\u00a0\u202f]", p.read_text(encoding="utf-8")):
            erreurs.append(f"espace insécable dans {p.relative_to(RACINE)}")

    # version
    if (RACINE / "VERSION").read_text().strip() != m["document"]["version"]:
        erreurs.append("VERSION ne correspond pas à document.version")
    if f"## v{m['document']['version']}" not in (RACINE / "CHANGELOG.md").read_text(encoding="utf-8"):
        erreurs.append("CHANGELOG.md ne documente pas la version courante")

    if erreurs:
        print("ÉCHEC")
        for e in erreurs:
            print(" -", e)
        return 1
    print(f"OK — dépôt cohérent, version {m['document']['version']}")
    return 0


if __name__ == "__main__":
    if "--verifier" in sys.argv:
        sys.exit(verifier())
    s = construire(RACINE)
    print(f"{len(s)} fichiers générés.")
