---
id: c03
titre: "Palette"
resume: "Valeurs hexadécimales, rôle exclusif de chaque couleur, teintes dérivées, associations."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/couleurs"
url: https://martin-explorai.github.io/explorai-marque/regles/c03-palette.md
html: https://martin-explorai.github.io/explorai-marque/c03-palette.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c03 — Palette

Valeurs hexadécimales, rôle exclusif de chaque couleur, teintes dérivées, associations.

Chaque couleur a un rôle exclusif. Le rôle décide de l'emploi, pas la préférence.

## Couleurs de marque

| Nom | Hex | Variable CSS | Accent | Rôle |
| :--- | :--- | :--- | :--- | :--- |
| Bleu foncé | #231651 | `--blue` | non | Fond dominant, titres, texte de structure. Couleur de référence de la marque. |
| Vert | #ACF127 | `--green` | oui | Accent d'énergie sur fond bleu : sur-titres, mot final d'un titre, icônes inversées. Marque les totaux et les synthèses. |
| Turquoise | #2DDCF9 | `--cyan` | oui | Accent de clarté : encadrements, séries de graphiques, texte secondaire sur bleu, contour de focus. |
| Lavande | #DA9FEC | `--lavender` | oui | Accent de nuance : encadrements, seconde série de graphiques. |
| Rose vibrant | #F127AC | `--pink` | oui | Signal ponctuel. Encadrement et surlignage seulement — jamais en couleur de texte. |
| White Smoke | #F6F6F6 | `--paper` | non | Fond de page web et d'interface. Retiré des documents. |

## Palette étendue

| Nom | Hex | Variable CSS | Rôle |
| :--- | :--- | :--- | :--- |
| Encre | #3B3550 | `--ink` | Texte courant sur fond clair. Moins dur que le bleu foncé sur de longs paragraphes. |
| Encre pâle | #71658D | `--ink-pale` | Texte secondaire, sur-titres, légendes, notes de lecture, pieds de page. |
| Voile | #D9D4E4 | `--veil` | Texte secondaire et filets sur fond bleu foncé. |
| Neutre | #F2F1F5 | `--neutral` | Fond de bloc et de carte. Bleu de marque à 6 % sur blanc. |
| Filet | #DEDBE6 | `--rule` | Bordures, séparateurs, cadres de carte sur fond clair. |
| Grille | #EFEDF3 | `--grid` | Lignes de grille des graphiques, 0,8 pt, sur un seul axe. |
| Noir | #231F20 | `--black` | Impression technique et supports en noir seul. Pas en usage courant. |
| Blanc | #FFFFFF | `--white` | Fond de carte, de tableau et de graphique. |

## Teintes dérivées

Deux teintes seulement par accent, calculées sur blanc. Elles servent les tableaux, les mises en évidence et les fonds de carte.

| Teinte | Usage | Turquoise | Vert | Lavande | Rose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 10 % | Alternance de lignes, fond de carte | #EAFCFE | #F7FEE9 | #FBF5FD | #FEE9F7 |
| 22 % | Ligne de total, mise en évidence | #D1F7FE | #EDFCD0 | #F7EAFB | #FCD0ED |

Variables CSS : `--cyan-10`, `--cyan-22`, `--green-10`, `--green-22`, `--lav-10`, `--lav-22`, `--pink-10`, `--pink-22`.

## Associations autorisées

| Paire | Intention |
| :--- | :--- |
| bleu + vert | L'association principale. Énergie et affirmation. |
| bleu + turquoise | Clarté, technique, données. |
| bleu + lavande | Nuance, second plan, séquence. |

> **Décision v3.** Le gris neutre #F6F6F6 est retiré des documents : tout fond neutre y est une déclinaison pâle du bleu de marque. Il reste en usage comme fond de page web et d'interface.

Fichiers de jetons : `assets/css/explorai-jetons.css` et `data/explorai-jetons.json`.
