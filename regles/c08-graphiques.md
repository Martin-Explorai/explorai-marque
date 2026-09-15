---
id: c08
titre: "Graphiques"
resume: "Ordre des séries, grille, axes, base à zéro, types admis, note de lecture."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/graphiques"
url: https://martin-explorai.github.io/explorai-marque/regles/c08-graphiques.md
html: https://martin-explorai.github.io/explorai-marque/c08-graphiques.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c08 — Graphiques

Ordre des séries, grille, axes, base à zéro, types admis, note de lecture.

## Paramètres

| Paramètre | Valeur |
| :--- | :--- |
| Ordre des séries | Turquoise #2DDCF9, lavande #DA9FEC, vert #ACF127, rose #F127AC |
| Composition d'un total | Bleu foncé pour la part principale, vert pour la part secondaire |
| Fond | Blanc plein. Jamais transparent, jamais coloré |
| Grille | #EFEDF3, 0,8 pt, sur un seul axe |
| Axes | #DEDBE6. Cadre supérieur et droit supprimés |
| Texte d'axe et de légende | DM Sans 9 pt #71658D |
| Étiquettes de valeur | DM Sans 8,5 pt demi-gras #231651 |
| Base des barres | Zéro obligatoire. Aucune échelle tronquée |
| Anneau | Épaisseur 42 % du rayon, séparation blanche 2 pt, total au centre |
| Résolution d'export | 200 ppp minimum pour l'impression |

## Types admis

| Type | Usage |
| :--- | :--- |
| Barres horizontales | Comparer des grandeurs entre catégories nommées. Accueille les libellés longs. |
| Barres empilées | Montrer une composition à l'intérieur d'un total. |
| Anneau | Répartir un total en parts. Quatre segments au maximum. |
| Barres groupées | Comparer deux séries sur les mêmes catégories. |
| Courbe cumulative | Suivre une progression le long d'une séquence. |
| Nuage de points | Vérifier la relation entre deux variables. |

## Règle de livraison

> **Obligatoire.** Tout graphique porte un titre en deux niveaux — l'étiquette du type en monospace, puis en clair ce que le graphique montre — et une note de lecture. Un graphique sans note de lecture ne part pas chez un client.
