# Explorai — normes graphiques

<!-- Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main. -->

Référence de la marque Explorai, pensée d'abord pour les agents (LLM) et lisible par les personnes. Version **8.0** du 2026-09-15, conforme aux Normes graphiques Explorai v3 (2026-09). Langue : fr-CA.

## Pour un agent : ordre de lecture

1. `llms.txt` — orientation et liste des ressources (https://martin-explorai.github.io/explorai-marque/llms.txt).
2. `data/explorai-marque.json` — **toutes les règles**, structurées. C'est la source de vérité.
3. `data/explorai-actifs.json` — chaque fichier d'image et de police, avec son URL, ses dimensions, son empreinte et son usage admis.
4. `regles/cNN-*.md` — les mêmes règles en prose Markdown, une section par fichier. `llms-full.txt` les réunit en un seul fichier.
5. `assets/css/explorai-jetons.css` ou `data/explorai-jetons.json` — jetons prêts à importer.
6. Avant de livrer : liste de contrôle de la [section c15](regles/c15-verification.md).

## Hiérarchie des sources

| Rang | Fichier | Statut |
| :--- | :--- | :--- |
| 1 | `data/explorai-marque.json` | Source de vérité unique. Seul fichier de règles modifié à la main. |
| 2 | `regles/*.md`, `*.html`, `llms.txt`, `llms-full.txt`, `README.md`, `SKILL.md` | Dérivés générés. En cas d'écart, la source s'applique. |
| 2 | `data/explorai-actifs.json`, `data/explorai-jetons.json`, `data/explorai-index.json`, `assets/css/explorai-jetons.css` | Dérivés générés. Les chemins et empreintes du manifeste sont calculés sur les fichiers réels. |
| 3 | `CHANGELOG.md` | Journal des versions, rédigé à la main. |

> **Arbitrage.** En cas de contradiction entre un fichier généré et data/explorai-marque.json, ce dernier s'applique et le fichier généré doit être reconstruit. En cas de contradiction entre data/explorai-marque.json et le document source des Normes graphiques v3, l'écart remonte au responsable de la marque avant toute production.

## Sections

| Id | Section | Contenu | JSON |
| :--- | :--- | :--- | :--- |
| c00 | [Identité et gouvernance](regles/c00-identite-gouvernance.md) | Nom, signature, organisation, qui arbitre un écart, cycle de révision. | `#/identite` |
| c01 | [Logo](regles/c01-logo.md) | Deux variantes d'emploi, zone de protection, mesures minimales, interdits, favicon. | `#/logo` |
| c02 | [Typographie](regles/c02-typographie.md) | DM Sans et IBM Plex Mono, trois niveaux de repli, échelle web, fichiers de police. | `#/typographie` |
| c03 | [Palette](regles/c03-palette.md) | Valeurs hexadécimales, rôle exclusif de chaque couleur, teintes dérivées, associations. | `#/couleurs` |
| c04 | [Couleur en usage](regles/c04-couleur-en-usage.md) | Un accent par unité de lecture, rotation, exceptions, implémentation web. | `#/couleur_en_usage` |
| c05 | [Iconographie](regles/c05-iconographie.md) | Neuf formes, leur sens, ce qu'elles ouvrent et n'ouvrent pas, correspondance par livrable. | `#/iconographie` |
| c06 | [Motif](regles/c06-motif.md) | Emploi de la forme Exploration en fond : taille, position, couleur. | `#/motif` |
| c07 | [Tableaux](regles/c07-tableaux.md) | En-tête bleu, alternance dans l'accent, aucun quadrillage, ligne de total. | `#/tableaux` |
| c08 | [Graphiques](regles/c08-graphiques.md) | Ordre des séries, grille, axes, base à zéro, types admis, note de lecture. | `#/graphiques` |
| c09 | [Écriture](regles/c09-ecriture.md) | Conventions typographiques du français, ton de voix. | `#/ecriture` |
| c10 | [Supports](regles/c10-supports.md) | Règle commune, document, web : rayons, focus, survol, mouvement, densité. | `#/supports` |
| c11 | [Actifs](regles/c11-actifs.md) | Choisir une variante et un format, URL de téléchargement, insertion, nomenclature. | `#/actifs` |
| c12 | [Gabarit de document](regles/c12-document.md) | DOCX et PDF : page, rythme, onze styles nommés, types de page, polices, exemple de tableau. | `#/document_gabarit` |
| c13 | [Contenu web](regles/c13-contenu-web.md) | Hiérarchie des titres, texte long, mises en valeur, interactif, listes, médias, code. | `#/contenu_web` |
| c14 | [Interface d'application](regles/c14-interface.md) | Principes d'interface produit, composants, états, plancher de qualité. | `#/interface` |
| c15 | [Vérification avant diffusion](regles/c15-verification.md) | Listes de contrôle : tout livrable, document, application. | `#/verification` |
| c16 | [Limites](regles/c16-limites.md) | Ce que le dépôt ne contient pas, contenu non vérifié, points à compléter. | `#/limites` |

## Questions fréquentes

| Question | Réponse courte | Section |
| :--- | :--- | :--- |
| Quelles sont les couleurs de la marque ? | Bleu foncé #231651, vert #ACF127, turquoise #2DDCF9, lavande #DA9FEC, rose vibrant #F127AC; White Smoke #F6F6F6 pour le fond web. | [c03](regles/c03-palette.md) |
| Combien d'accents dans une section ? | Un seul, selon la rotation turquoise, vert, lavande, rose. | [c04](regles/c04-couleur-en-usage.md) |
| Quelle couleur pour les totaux et les synthèses ? | Le vert, par exception à la rotation. | [c04](regles/c04-couleur-en-usage.md) |
| Comment employer le rose ? | En signal : encadrement et surlignage. Jamais en texte, jamais en aplat de fond étendu. | [c04](regles/c04-couleur-en-usage.md) |
| Quelles polices ? | DM Sans pour les titres et le texte, IBM Plex Mono pour les sur-titres, étiquettes et chiffres de référence. Repli : Calibri + Consolas, puis Arial + Courier New, sans mélange. | [c02](regles/c02-typographie.md) |
| Quel fichier de logo ? | Fond clair : explorai-logo-bleu.svg. Fond bleu ou saturé : explorai-logo-blanc.svg. Le logo vert n'a pas d'emploi courant. | [c01](regles/c01-logo.md) |
| Taille minimale et zone de protection du logo ? | 90 px à l'écran, 25 mm en impression; zone égale à une fois la hauteur du logo sur les quatre côtés. | [c01](regles/c01-logo.md) |
| Quelle icône pour quelle section ? | Selon la table de correspondance : chaque forme ouvre certaines sections et en exclut d'autres. | [c05](regles/c05-iconographie.md) |
| Comment employer le motif ? | Forme Exploration recadrée en bord de page, 20 à 45 % de la largeur, un seul par page, jamais sur une page de contenu. | [c06](regles/c06-motif.md) |
| Comment mettre en forme un tableau ? | En-tête bleu foncé, alternance blanc / accent 10 %, aucun quadrillage, ligne de total à 22 % encadrée dans l'accent. | [c07](regles/c07-tableaux.md) |
| Comment mettre en forme un graphique ? | Fond blanc, base à zéro, grille sur un seul axe, séries turquoise, lavande, vert, rose, note de lecture obligatoire. | [c08](regles/c08-graphiques.md) |
| Comment écrire les montants et les pourcentages ? | 166 250 $, 47 %, avec espaces insécables; guillemets « français ». | [c09](regles/c09-ecriture.md) |
| Comment écrire le nom de la marque ? | « Explorai » en un seul mot dans le texte courant; le logo épelle « explor.ai ». | [c00](regles/c00-identite-gouvernance.md) |
| Quels styles pour un document Word ? | Onze styles nommés, de Titre de couverture (DM Sans 700, 32 pt) à Pied de page (IBM Plex Mono 400, 7,5 pt). | [c12](regles/c12-document.md) |
| Quelles règles pour une interface ? | Bleu pour la navigation, un seul élément vert par écran, turquoise pour les chiffres, rose pour les blocages, corps de 14 à 15 px. | [c14](regles/c14-interface.md) |
| Où télécharger un actif ? | data/explorai-actifs.json donne, pour chaque fichier, son URL GitHub Pages (url) et son URL brute (url_brute). | [c11](regles/c11-actifs.md) |
| Qui tranche un écart à la charte ? | Le responsable de la marque, avant la production. | [c00](regles/c00-identite-gouvernance.md) |

## Fichiers lisibles par machine

| Fichier | Contenu |
| :--- | :--- |
| [llms.txt](llms.txt) | Orientation pour agents (format llmstxt.org). |
| [llms-full.txt](llms-full.txt) | Toutes les sections en Markdown, en un fichier. |
| [data/explorai-marque.json](data/explorai-marque.json) | Règles structurées — source de vérité. |
| [data/explorai-actifs.json](data/explorai-actifs.json) | Manifeste des actifs : chemin, URL, URL brute, format, dimensions, octets, SHA-256, usage. |
| [data/explorai-jetons.json](data/explorai-jetons.json) | Jetons au format DTCG. |
| [data/explorai-index.json](data/explorai-index.json) | Index du dépôt : sections, fichiers, URL. |
| [assets/css/explorai-jetons.css](assets/css/explorai-jetons.css) | Variables CSS, @font-face, accents `data-accent`, focus. |
| [SKILL.md](SKILL.md) | Le dépôt employé comme skill d'agent. |

## Arborescence

```text
explorai-marque/
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
    └── construire.py           générateur et vérificateur
```

## Publication et régénération

1. Pousser la branche `main` sur https://github.com/Martin-Explorai/explorai-marque.
2. Dans GitHub : Settings > Pages > Deploy from a branch > `main` / `(root)`. Le fichier `.nojekyll` sert les `.md` et `.json` tels quels.
3. Le site répond alors à https://martin-explorai.github.io/explorai-marque/.
4. Pour modifier une règle : éditer `data/explorai-marque.json`, lancer `python3 outils/construire.py`, puis `python3 outils/construire.py --verifier`, consigner dans `CHANGELOG.md`, mettre à jour `VERSION`, étiqueter le commit (`git tag vX.Y`).

Limites et contenu non vérifié : [section c16](regles/c16-limites.md).
