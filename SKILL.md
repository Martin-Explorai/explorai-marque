---
name: explorai-marque
description: Applique les normes graphiques Explorai (couleurs, polices, logo, icônes, tableaux, graphiques, écriture française, documents Word et PDF, pages web, interfaces) à tout livrable Explorai, et vérifie sa conformité avant diffusion.
---

# Explorai — normes graphiques (v8.0)

<!-- Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main. -->

## Quand utiliser ce skill

- Produire un document, un rapport, une offre, une page web, une interface ou un graphique aux couleurs d'Explorai.
- Vérifier qu'un livrable respecte la marque avant diffusion.

## Méthode

1. Lire `data/explorai-marque.json` : toutes les règles, structurées. Il fait foi.
2. Identifier le support (document, web, interface) et lire la section correspondante dans `regles/` : c12, c13 ou c14.
3. Choisir les actifs dans `data/explorai-actifs.json` selon le fond (champ `document.choix_de_variante`). Référencer le fichier par son chemin ou son `url_brute`; ne jamais recolorer ni recopier un tracé.
4. Pour le web, importer `assets/css/explorai-jetons.css`; ailleurs, lire les valeurs dans `data/explorai-jetons.json`.
5. Pour un fichier bureautique, employer les polices de `assets/fonts/` ou le niveau de repli 2, sans mélange.
6. Avant de livrer, cocher la liste de `regles/c15-verification.md`.
7. Règle absente ou contradictoire : ne pas inventer; signaler l'écart au responsable de la marque.

## Rappels

- R1 — Un accent par unité de lecture : une section, un tableau, un graphique. Le bleu foncé et les neutres ne comptent pas comme accents.
- R2 — Rotation dans l'ordre : turquoise, puis vert, puis lavande, puis rose. La rotation suit l'ordre des sections.
- R3 — Le vert marque les totaux et les synthèses. Dans un document chiffré, il est réservé aux lignes de total, aux sommaires et aux pages de synthèse. C'est l'exception à la rotation.
- R4 — Le rose reste un signal : encadrement, surlignage, option non retenue, point d'attention. Jamais un texte, jamais un aplat de fond étendu.
- R5 — Le fond bleu foncé inverse les rôles : l'accent devient le vert, le texte secondaire passe au voile, les encadrements passent au vert ou au turquoise.

## Fichiers

- `regles/c00-identite-gouvernance.md` — Identité et gouvernance : Nom, signature, organisation, qui arbitre un écart, cycle de révision.
- `regles/c01-logo.md` — Logo : Deux variantes d'emploi, zone de protection, mesures minimales, interdits, favicon.
- `regles/c02-typographie.md` — Typographie : DM Sans et IBM Plex Mono, trois niveaux de repli, échelle web, fichiers de police.
- `regles/c03-palette.md` — Palette : Valeurs hexadécimales, rôle exclusif de chaque couleur, teintes dérivées, associations.
- `regles/c04-couleur-en-usage.md` — Couleur en usage : Un accent par unité de lecture, rotation, exceptions, implémentation web.
- `regles/c05-iconographie.md` — Iconographie : Neuf formes, leur sens, ce qu'elles ouvrent et n'ouvrent pas, correspondance par livrable.
- `regles/c06-motif.md` — Motif : Emploi de la forme Exploration en fond : taille, position, couleur.
- `regles/c07-tableaux.md` — Tableaux : En-tête bleu, alternance dans l'accent, aucun quadrillage, ligne de total.
- `regles/c08-graphiques.md` — Graphiques : Ordre des séries, grille, axes, base à zéro, types admis, note de lecture.
- `regles/c09-ecriture.md` — Écriture : Conventions typographiques du français, ton de voix.
- `regles/c10-supports.md` — Supports : Règle commune, document, web : rayons, focus, survol, mouvement, densité.
- `regles/c11-actifs.md` — Actifs : Choisir une variante et un format, URL de téléchargement, insertion, nomenclature.
- `regles/c12-document.md` — Gabarit de document : DOCX et PDF : page, rythme, onze styles nommés, types de page, polices, exemple de tableau.
- `regles/c13-contenu-web.md` — Contenu web : Hiérarchie des titres, texte long, mises en valeur, interactif, listes, médias, code.
- `regles/c14-interface.md` — Interface d'application : Principes d'interface produit, composants, états, plancher de qualité.
- `regles/c15-verification.md` — Vérification avant diffusion : Listes de contrôle : tout livrable, document, application.
- `regles/c16-limites.md` — Limites : Ce que le dépôt ne contient pas, contenu non vérifié, points à compléter.
