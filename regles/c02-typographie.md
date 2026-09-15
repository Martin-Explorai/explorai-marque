---
id: c02
titre: "Typographie"
resume: "DM Sans et IBM Plex Mono, trois niveaux de repli, échelle web, fichiers de police."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/typographie"
url: https://martin-explorai.github.io/explorai-marque/regles/c02-typographie.md
html: https://martin-explorai.github.io/explorai-marque/c02-typographie.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c02 — Typographie

DM Sans et IBM Plex Mono, trois niveaux de repli, échelle web, fichiers de police.

## Familles

| Rôle | Police | Usage | Précision |
| :--- | :--- | :--- | :--- |
| Principale | DM Sans | Titres, sous-titres, texte courant. | Graisses 400, 500, 600, 700. Négatif sur les grands corps uniquement. |
| Secondaire | IBM Plex Mono | Sur-titres, étiquettes, numérotation, chiffres de référence, légendes techniques. | Jamais de paragraphe entier en monospace. |

## Niveaux de repli

Un fichier emploie un seul niveau, du début à la fin.

| Niveau | Nom | Sans empattement | Monospace | Quand |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Marque | DM Sans | IBM Plex Mono | Web, PDF, et tout fichier produit sur un poste équipé des deux polices. |
| 2 | Remplacement | Calibri | Consolas | Fichier bureautique modifiable diffusé hors de l'organisation. |
| 3 | Universel | Arial | Courier New | Destinataire dont l'environnement est inconnu, ou contrainte technique explicite. |

## Interdits

- Mélanger deux niveaux : DM Sans avec Consolas, ou Calibri avec IBM Plex Mono.
- Diffuser un fichier bureautique en polices de niveau 1 sans les intégrer au fichier ni passer au PDF.
- Substituer par une police à empattements — comportement par défaut de Word, qui déforme la mise en page.
- Employer l'italique : la charte ne le prévoit pas, ni pour les citations ni pour les légendes.

## Déclarations CSS

Pile normative (charte v3) :

```css
/* Déclaration normative */
font-family: 'DM Sans', Calibri, Arial, sans-serif;
font-family: 'IBM Plex Mono', Consolas, 'Courier New', monospace;
```

Pile web étendue :

```css
font-family: 'DM Sans', 'Calibri', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
font-family: 'IBM Plex Mono', 'Consolas', 'SF Mono', Menlo, 'Courier New', monospace;
```

> **Statut de la pile web étendue.** Addition propre au web, hors charte v3. À faire valider par le responsable de la marque.

## Échelle web

| Rôle | Police | Corps | Interlettrage |
| :--- | :--- | :--- | :--- |
| Affichage | DM Sans 500 | 44 à 92 px | -0,055 em |
| Niveau 1 | DM Sans 500 | 38 à 68 px | -0,045 em |
| Niveau 2 | DM Sans 500 | 29 à 46 px | -0,038 em |
| Niveau 3 | DM Sans 500 | 21 à 28 px | -0,025 em |
| Introduction | DM Sans 400 | 18 à 22 px | 0 |
| Texte courant | DM Sans 400 | 17 px | 0 |
| Sur-titre | IBM Plex Mono 500 | 11,5 px | +0,11 em |

Échelle des documents : [section c12](c12-document.md).

## Fichiers de police

Sous-ensembles latins publiés par Fontsource (paquets npm @fontsource/dm-sans 5.3.0 et @fontsource/ibm-plex-mono 5.3.0). WOFF2 d'origine; TTF convertis depuis ces WOFF2. Licence SIL Open Font License 1.1, jointe.

WOFF2 pour le web (@font-face dans assets/css/explorai-jetons.css). TTF pour une installation sur poste ou une intégration dans un fichier bureautique.

| Famille | Graisse | WOFF2 | TTF |
| :--- | :--- | :--- | :--- |
| DM Sans | 400 | `assets/fonts/DMSans-Regular.woff2` | `assets/fonts/DMSans-Regular.ttf` |
| DM Sans | 500 | `assets/fonts/DMSans-Medium.woff2` | `assets/fonts/DMSans-Medium.ttf` |
| DM Sans | 600 | `assets/fonts/DMSans-SemiBold.woff2` | `assets/fonts/DMSans-SemiBold.ttf` |
| DM Sans | 700 | `assets/fonts/DMSans-Bold.woff2` | `assets/fonts/DMSans-Bold.ttf` |
| IBM Plex Mono | 400 | `assets/fonts/IBMPlexMono-Regular.woff2` | `assets/fonts/IBMPlexMono-Regular.ttf` |
| IBM Plex Mono | 500 | `assets/fonts/IBMPlexMono-Medium.woff2` | `assets/fonts/IBMPlexMono-Medium.ttf` |

Licences : `assets/fonts/OFL-DMSans.txt`, `assets/fonts/OFL-IBMPlexMono.txt`.
