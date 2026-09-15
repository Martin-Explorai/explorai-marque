---
id: c13
titre: "Contenu web"
resume: "Hiérarchie des titres, texte long, mises en valeur, interactif, listes, médias, code."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/contenu_web"
url: https://martin-explorai.github.io/explorai-marque/regles/c13-contenu-web.md
html: https://martin-explorai.github.io/explorai-marque/c13-contenu-web.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c13 — Contenu web

Hiérarchie des titres, texte long, mises en valeur, interactif, listes, médias, code.

Chaque bloc suit la rotation d'accent de la [section c04](c04-couleur-en-usage.md) : turquoise, vert, lavande, rose, puis retour au turquoise.

## Hiérarchie des titres

Six niveaux de titre, et rien de plus. Au-delà, le lecteur perçoit du bruit typographique plutôt qu'une structure.

| Niveau | Règle |
| :--- | :--- |
| Affichage | DM Sans 500, interlettrage −0,055 em. Réservé au premier écran d'une page. |
| H1 | Un seul par page. Il nomme le sujet, pas la section. |
| H2 | Ouvre une section. Toujours accompagné d'une icône de section et d'un sur-titre. |
| H3 | Sous-section, ou titre de carte. |
| H4 | Regroupe quelques paragraphes à l'intérieur d'une sous-section. |
| H5 | Rare. Employé surtout dans la documentation technique. |
| H6 — sur-titre | IBM Plex Mono, capitales, interlettrage ouvert. C'est l'étiquette, pas le titre. |

## Texte

| Élément | Règle |
| :--- | :--- |
| Introduction | Se distingue par sa taille, pas par sa couleur. |
| Texte courant | Corps de 17 px, interligne 1,65, longueur de ligne inférieure à 68 caractères. Réglage par défaut de toute page. |
| Note de lecture | Encre pâle #71658D, 12,5 px. Précisions de source, notes de graphique, mentions légales. |

### Disposition à deux colonnes

- Réservée aux textes de référence parcourus plutôt que lus en continu : notes de méthode, historiques, annexes.
- Jamais pour le corps principal d'un article web.
- Repasse sur une seule colonne sous 900 px de largeur.
- Les paragraphes ne se coupent pas entre deux colonnes. Aucun titre de niveau 2 ne commence à l'intérieur de la disposition.
- L'accent de la section reste unique dans la disposition.

## Mises en valeur

| Forme | Règle |
| :--- | :--- |
| Citation détachée | Sort un passage du flux. Attribution nommée sous la citation. |
| Encadré d'attention | Encadrement dans l'accent de la section. Signale un point sur lequel une décision est attendue. Jamais combiné avec un fond coloré. |
| Encadré de recommandation | Filet supérieur dans l'accent de la section, fond neutre. Un fond coloré sous un texte courant fatigue la lecture. |
| Surlignage | Dans l'accent de la section, au maximum une fois par page. Remplace le gras coloré, qui n'existe pas dans le système. |
| Filet latéral | Marque une note de l'auteur : une précision utile hors du fil du texte. |

## Tableaux et graphiques

- Mêmes règles que la [section c07](c07-tableaux.md).
- En-têtes triables : la mise en forme ne bouge pas quand l'ordre change; l'indicateur d'ordre est en vert.
- Le tableau défile horizontalement dans son cadre plutôt que de réduire le corps du texte.
- Au-delà de quatre segments, un anneau cède la place à un tableau.

## Contenus interactifs

L'interaction sert à cacher ce qui n'est pas encore utile.

| Composant | Emploi |
| :--- | :--- |
| Onglets | Contenus parallèles de même nature, dont le lecteur n'en consulte qu'un. |
| Accordéon | Questions dont le lecteur ne consulte qu'une ou deux réponses. |
| Filtres de liste | Un seul filtre actif à la fois. L'option « Tout » reste toujours disponible. |

## Listes et séquences

- Numéroter seulement ce qui est un ordre : étapes, phases, échéanciers. Une liste de caractéristiques n'est pas une séquence.
- Une puce par idée, jamais deux phrases collées.
- Pas de point final si l'élément n'est pas une phrase.
- Parallélisme grammatical entre tous les éléments.
- Liste de définitions pour un glossaire : terme, puis définition en une phrase.

## Médias

- Une image porte une légende, ou elle ne sert à rien.
- La légende dit ce que l'image montre, pas ce qu'elle est.
- Légende placée sous l'image, séparée par un filet, encre pâle, 13 px, jamais en italique.
- Une image décorative porte un texte de remplacement vide (alt="").
- Le motif ferme une section, il n'en ouvre jamais une.

## Contenu technique

- Une valeur citée dans une phrase prend la police IBM Plex Mono : la variable `--accent` vaut `#2DDCF9`.
- Aucun paragraphe entier n'est composé en monospace.
- Les blocs de code sont en IBM Plex Mono, sur fond neutre #F2F1F5.
- Un badge d'état porte toujours un mot : la couleur seule ne transmet aucune information.
