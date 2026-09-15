---
id: c07
titre: "Tableaux"
resume: "En-tête bleu, alternance dans l'accent, aucun quadrillage, ligne de total."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/tableaux"
url: https://martin-explorai.github.io/explorai-marque/regles/c07-tableaux.md
html: https://martin-explorai.github.io/explorai-marque/c07-tableaux.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c07 — Tableaux

En-tête bleu, alternance dans l'accent, aucun quadrillage, ligne de total.

## Traitement

| Élément | Traitement | Valeur |
| :--- | :--- | :--- |
| En-tête | Aplat bleu foncé, texte blanc en demi-gras, sans bordure | #231651 |
| Lignes | Alternance blanc / teinte de l'accent à 10 % | #FFFFFF + teinte 10 % |
| Filets internes | Aucun : l'alternance remplace le quadrillage | — |
| Ligne de total | Teinte de l'accent à 22 %, encadrement complet dans l'accent | 1,25 pt |
| Alignement | Libellés à gauche, valeurs numériques à droite | — |
| Accent | Un seul par tableau, selon la rotation | — |

## Web

Le tableau défile horizontalement dans son cadre plutôt que de réduire le corps du texte. Les en-têtes triables portent un indicateur d'ordre en vert.

## Exemple

Exemple fictif conforme : [section c12](c12-document.md), « Exemple de tableau ».
