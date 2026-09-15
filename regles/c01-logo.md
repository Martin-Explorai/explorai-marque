---
id: c01
titre: "Logo"
resume: "Deux variantes d'emploi, zone de protection, mesures minimales, interdits, favicon."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/logo"
url: https://martin-explorai.github.io/explorai-marque/regles/c01-logo.md
html: https://martin-explorai.github.io/explorai-marque/c01-logo.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c01 — Logo

Deux variantes d'emploi, zone de protection, mesures minimales, interdits, favicon.

Le logo ne se redessine pas, ne se recompose pas et ne se recolore pas. Deux variantes d'emploi, pas trois.

## Variantes

| Variante | Fichier | Fonds admis | Note |
| :--- | :--- | :--- | :--- |
| Principale — bleu foncé | `assets/img/logo/explorai-logo-bleu.svg` | blanc, White Smoke #F6F6F6, toute teinte pâle, aplat vert #ACF127 | Variante par défaut de tout document. |
| Inversée — blanc | `assets/img/logo/explorai-logo-blanc.svg` | bleu foncé #231651, photographie sombre, aplat de couleur saturée, aplat rose #F127AC | Le rose reste un signal, pas un fond de signature. |
| Vert — hors emploi courant | `assets/img/logo/explorai-logo-vert.svg` | Aucun | Fourni dans les actifs, mais le logo vert n'existe pas comme variante d'emploi courant. Sur aplat vert, employer la variante bleu foncé. |

- ![Logo Explorai, variante bleu](../assets/img/logo/explorai-logo-bleu.svg) `assets/img/logo/explorai-logo-bleu.svg` — Principale — bleu foncé
- ![Logo Explorai, variante blanc](../assets/img/logo/explorai-logo-blanc.svg) `assets/img/logo/explorai-logo-blanc.svg` — Inversée — blanc
- ![Logo Explorai, variante vert](../assets/img/logo/explorai-logo-vert.svg) `assets/img/logo/explorai-logo-vert.svg` — Vert — hors emploi courant

## Zone de protection

Une fois la hauteur du logo, sur les quatre côtés, depuis le rectangle englobant. Aucun texte, aucun filet, aucune image dans cette zone. Elle prime sur la mise en page : si elle ne tient pas, le logo est trop grand.

## Mesures

| Contexte | Valeur | Remarque |
| :--- | :--- | :--- |
| Largeur minimale à l'écran | 90 px | Sous ce seuil, le point du « .ai » se ferme. |
| Largeur minimale en impression | 25 mm | Vérifier sur épreuve papier, pas à l'écran. |
| Couverture de document | 60 mm (2,5 po) | Aligné à droite en pied de couverture. |
| Pied de page courant | 32 mm | Facultatif : le pied de page textuel suffit. |
| En-tête du site web | 132 px, variante bleue | Aligné sur la marge gauche. |
| Pied de page web | 150 px, variante blanche | Sur fond bleu foncé. |
| Barre d'application | 104 px, variante blanche | Exception au seuil de 90 px : contexte fixe vérifié à l'écran. |

## Interdits

- Déformation
- Rotation
- Effet ou ombre
- Contour ajouté
- Recoloration hors des variantes fournies
- Redimensionnement non proportionnel

## Favicon

Forme Exploration verte sur carré bleu foncé. Le mot-symbole n'est jamais réduit à 16 px. Fichiers : `assets/img/explorai-favicon.png`, `favicon.ico`.

Choix de fichier et URL de téléchargement : [section c11](c11-actifs.md).
