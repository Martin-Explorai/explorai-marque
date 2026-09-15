---
id: c12
titre: "Gabarit de document"
resume: "DOCX et PDF : page, rythme, onze styles nommés, types de page, polices, exemple de tableau."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/document_gabarit"
url: https://martin-explorai.github.io/explorai-marque/regles/c12-document.md
html: https://martin-explorai.github.io/explorai-marque/c12-document.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c12 — Gabarit de document

DOCX et PDF : page, rythme, onze styles nommés, types de page, polices, exemple de tableau.

Un modèle Word avec styles nommés réduit les écarts de conformité plus efficacement que l'ajout de règles. Le rédacteur applique un style; il n'a pas à retenir une valeur d'interligne.

> **Modèle.** Aucun fichier DOTX n'est fourni. Les onze styles ci-dessous sont la spécification du modèle à produire; un générateur de DOCX les applique tels quels.

## Page

| Paramètre | Valeur |
| :--- | :--- |
| Format | Lettre US, 8,5 × 11 po. A4 accepté à l'export européen. |
| Orientation | Portrait. Le paysage est réservé aux annexes de tableaux larges. |
| Marges | 2,5 cm sur les quatre côtés. |
| Colonnes | Une seule. Aucun texte courant sur deux colonnes. |
| Fond de page | Blanc. Les pages bleues sont des pages entières, pas des fonds. |
| En-tête | Logo bleu à gauche, titre du document à droite, filet #DEDBE6. |
| Pied de page | Nom du client · numéro de page · date, en IBM Plex Mono. |

## Rythme et découpage

| Règle | Énoncé |
| :--- | :--- |
| Rythme | Interligne du corps : 1,5. Espace avant un titre : deux interlignes. Espace après : un demi. Aucun retrait de première ligne. |
| Saut de page | Chaque titre de niveau 1 ouvre une page. Un titre ne reste jamais seul en bas de page; un tableau ne se coupe jamais après sa ligne d'en-tête; une ligne de total n'est jamais séparée de son tableau. |
| Numérotation | La couverture et les intercalaires ne portent pas de numéro. La numérotation commence à la première page de contenu. |
| Icône | Une forme par section, en haut de la première page de la section, 7 mm de haut, selon la correspondance de la [section c05](c05-iconographie.md). |
| Accent | Un accent par section, en rotation. Le récapitulatif financier fait exception : il est toujours en vert. |
| Longueur de ligne | Inférieure à 80 caractères, obtenue par les marges de 2,5 cm. |

## Styles nommés

| Style | Police | Graisse | Corps (pt) | Interligne | Couleur | Emploi |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| Titre de couverture | DM Sans | 700 | 32 | 1,02 | #FFFFFF | Couverture seulement |
| Titre 1 | DM Sans | 600 | 22 | 1,10 | #231651 | Ouvre une section et une page |
| Titre 2 | DM Sans | 600 | 16 | 1,20 | #231651 | Sous-section |
| Titre 3 | DM Sans | 600 | 12,5 | 1,25 | #231651 | Regroupe des paragraphes |
| Introduction | DM Sans | 400 | 12 | 1,45 | #3B3550 | Premier paragraphe d'une section |
| Corps | DM Sans | 400 | 10,5 | 1,50 | #3B3550 | Texte courant |
| Liste à puces | DM Sans | 400 | 10,5 | 1,45 | #3B3550 | Puce dans l'accent de la section |
| Tableau | DM Sans | 400 | 9,5 | 1,35 | #3B3550 | Cellules; l'en-tête passe en 600 blanc |
| Légende | DM Sans | 400 | 8,5 | 1,45 | #71658D | Sous une image ou un graphique |
| Sur-titre | IBM Plex Mono | 500 | 8 | 1,50 | #71658D | Capitales, interlettrage +0,11 em |
| Pied de page | IBM Plex Mono | 400 | 7,5 | 1,40 | #71658D | Client · page · date |

Aucun style n'emploie l'italique.

## Types de page

| Type | Forme d'icône | Règle |
| :--- | :--- | :--- |
| Couverture | `exploration` | Fond bleu foncé pleine page, sur-titre vert, titre blanc en 32 pt, logo blanc de 60 mm aligné à droite en pied. Motif Exploration recadré dans l'angle. Aucun numéro de page. |
| Sommaire | `exploration` | Numéros de section en IBM Plex Mono, titres en 11 pt demi-gras, filet de séparation #DEDBE6. |
| Intercalaire de section | selon la section | Page bleue pleine, icône verte de la section, numéro en IBM Plex Mono vert. Pas de logo, pas de numéro de page. |
| Texte courant | selon la section | Titre 1, paragraphe d'introduction en 12 pt, corps en 10,5 pt, titres de niveau 3, encadré de mesure dans l'accent. |
| Section de constat | `transformation` | Les titres de niveau 3 remplacent une liste à puces : un enjeu qui demande deux phrases n'est pas une puce. |
| Listes à puces | selon la section | Puce dans l'accent de la section. Une idée par puce. Pas de point final quand l'élément n'est pas une phrase complète. |
| Démarche en cartes | `accompagnement` | Grille de deux cartes par deux, filet de carte #DEDBE6. Chaque phase porte sa durée en IBM Plex Mono. |
| Tableau de phase | `financement` | En-tête bleu, alternance dans la teinte 10 % de l'accent, ligne de total encadrée à 22 %. Libellés à gauche, valeurs à droite en chiffres tabulaires. Aucun filet interne. |
| Synthèse chiffrée | `financement` | Toujours en vert, quelle que soit la position dans la rotation. |
| Page de clôture | `consultation` | Seconde et dernière page bleue du document. Un seul motif par page, recadré dans l'angle. |

## Cohérence des chiffres

> **Règle.** Un total de phase se vérifie toujours à la main : heures × tarif. Un tableau dont la somme ne tombe pas juste coûte plus cher en crédibilité que l'écart lui-même.

## Polices dans un document

Les corps, les interlignes et les marges ne changent pas d'un niveau de police à l'autre. Seules les polices changent; la mise en page absorbe l'écart de chasse.

|  | Énoncé |
| :--- | :--- |
| À faire | Diffuser en PDF dès que le destinataire n'a pas à modifier le document : le niveau 1 est alors garanti. |
| À faire | Si le DOCX doit rester modifiable : intégrer les polices au fichier, ou produire le document au niveau 2 dès le départ. |
| À éviter | Mélanger les niveaux : DM Sans avec Consolas, ou Calibri avec IBM Plex Mono. |
| À éviter | Laisser Word substituer seul : sans repli déclaré, il choisit une police à empattements et déforme la mise en page. |

Dans un fichier bureautique, une seule police est nommée par style : la pile web étendue de la [section c02](c02-typographie.md) ne s'y applique pas.

## Exemple de tableau

Tableau — Phase 2a — Preuve de valeur — accent rose (fictif)

| Activités | Tarif A | Tarif B | Sous-total |
| :--- | ---: | ---: | ---: |
| Connecteur ERP et extraction des ordres | 60 H | 8 H | 11 700 $ |
| Moteur d'ordonnancement, première version | 90 H | 12 H | 17 550 $ |
| Interface de séquence et de validation | 50 H | 6 H | 9 600 $ |
| Ateliers de calibrage des contraintes | — | 24 H | 5 400 $ |
| **Total de la phase** | **200 H** | **50 H** | **44 250 $** |

Fictif. Tarif A 165 $/h, tarif B 225 $/h, valeurs de démonstration seulement. Chaque sous-total vérifie heures × tarif.

Vérification avant diffusion : [section c15](c15-verification.md).
