---
id: c16
titre: "Limites"
resume: "Ce que le dépôt ne contient pas, contenu non vérifié, points à compléter."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/limites"
url: https://martin-explorai.github.io/explorai-marque/regles/c16-limites.md
html: https://martin-explorai.github.io/explorai-marque/c16-limites.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c16 — Limites

Ce que le dépôt ne contient pas, contenu non vérifié, points à compléter.

## Absent du dépôt

- Fichiers EPS en quadrichromie pour l'imprimerie. Le SVG couvre l'écran et l'impression numérique, il ne remplace pas un EPS.
- Modèle bureautique DOTX. La [section c12](c12-document.md) en donne la spécification complète.
- Fichiers de dessin d'origine des logos (voir provenance, [section c11](c11-actifs.md)).
- Aucune norme de présentation (PPTX) : ce type de support est hors du périmètre du dépôt depuis la version 8.0.

## Polices

- Les polices fournies sont des sous-ensembles latins (Fontsource). Elles couvrent le français, sauf l'espace fine insécable U+202F, que le logiciel rend avec une police de repli.
- Pour une installation bureautique complète, les familles officielles DM Sans et IBM Plex Mono sont disponibles sur Google Fonts.
- La pile web étendue (Segoe UI, Helvetica Neue, SF Mono, Menlo) est une addition propre au web, hors charte v3, à faire valider.

## Contenu non vérifié

- Les mandats et les informations d'entreprise de la [section c00](c00-identite-gouvernance.md) sont repris du site public explor.ai et ne sont pas vérifiés par ce dépôt.
- Tout exemple marqué « fictif » ([section c12](c12-document.md) notamment) est une donnée de démonstration.

## Hypothèses de publication

- GitHub Pages publie la branche main depuis la racine du dépôt, à l'adresse https://martin-explorai.github.io/explorai-marque/.
- Les URL brutes supposent la branche main.

## Note de production

Logos : SVG obtenus par vectorisation des PNG fournis, puis recolorés selon les trois variantes. Écart de silhouette mesuré inférieur à 0,15 % des pixels — des reproductions fidèles, pas les fichiers de dessin d'origine. Icônes, variantes bleu, vert et blanc : fichiers vectoriels d'origine reçus directement pour les neuf formes — la référence la plus fidèle. Les PNG correspondants ont été rendus depuis ces mêmes vecteurs, aux mêmes dimensions que les fichiers remplacés. Seule la variante en couleur héritée (currentColor) des icônes reste vectorisée.

## À compléter

- Nom, fonction et adresse du responsable de la marque.
- Journal des versions publié.
- Validation des polices web ajoutées entre les niveaux 2 et 3.
