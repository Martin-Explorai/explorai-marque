---
id: c15
titre: "Vérification avant diffusion"
resume: "Listes de contrôle : tout livrable, document, application."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/verification"
url: https://martin-explorai.github.io/explorai-marque/regles/c15-verification.md
html: https://martin-explorai.github.io/explorai-marque/c15-verification.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c15 — Vérification avant diffusion

Listes de contrôle : tout livrable, document, application.

## Tout livrable

1. ☐ Aucune couleur hors de la palette normée ([section c03](c03-palette.md)).
2. ☐ Un seul accent par unité de lecture ([section c04](c04-couleur-en-usage.md)).
3. ☐ Titres et texte courant en DM Sans, étiquettes en IBM Plex Mono, niveau de repli unique ([section c02](c02-typographie.md)).
4. ☐ Logo présent, bonne variante selon le fond, non déformé ([section c01](c01-logo.md)).
5. ☐ Zone de protection du logo respectée ([section c01](c01-logo.md)).
6. ☐ Une seule forme d'icône par section, conforme à la correspondance ([section c05](c05-iconographie.md)).
7. ☐ Chaque graphique porte un titre en deux niveaux et une note de lecture ([section c08](c08-graphiques.md)).
8. ☐ Conventions d'écriture du français appliquées aux chiffres ([section c09](c09-ecriture.md)).
9. ☐ Nom de la marque écrit « Explorai » dans le texte courant ([section c00](c00-identite-gouvernance.md)).

## Document

| Point | Vérification |
| :--- | :--- |
| Format de sortie | PDF par défaut, polices intégrées, hyperliens actifs. Le DOCX ne part que si le client doit annoter ou remplir. |
| Cohérence des chiffres | Chaque total de phase est recalculé à la main et confronté au récapitulatif. Les heures du récapitulatif égalent la somme des phases. |
| Conventions d'écriture | Espaces insécables devant %, $ et H. Séparateur de milliers en espace fine. Virgule décimale. Guillemets français. |
| Accents de section | Un accent par section, en rotation. Le récapitulatif financier reste vert. |
| Ruptures de page | Aucun titre seul en bas de page, aucun tableau coupé après sa ligne d'en-tête, aucune ligne de total séparée de son tableau. |
| Anonymisation | Avant tout usage d'une offre comme exemple interne, le nom du client, les montants et les coordonnées sont remplacés — pas masqués. |

## Application

Plancher de qualité de la [section c14](c14-interface.md), vérifié avant la mise en production au même titre que les tests fonctionnels.
