---
id: c04
titre: "Couleur en usage"
resume: "Un accent par unité de lecture, rotation, exceptions, implémentation web."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/couleur_en_usage"
url: https://martin-explorai.github.io/explorai-marque/regles/c04-couleur-en-usage.md
html: https://martin-explorai.github.io/explorai-marque/c04-couleur-en-usage.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c04 — Couleur en usage

Un accent par unité de lecture, rotation, exceptions, implémentation web.

## Règles

| Id | Règle |
| :--- | :--- |
| R1 | Un accent par unité de lecture : une section, un tableau, un graphique. Le bleu foncé et les neutres ne comptent pas comme accents. |
| R2 | Rotation dans l'ordre : turquoise, puis vert, puis lavande, puis rose. La rotation suit l'ordre des sections. |
| R3 | Le vert marque les totaux et les synthèses. Dans un document chiffré, il est réservé aux lignes de total, aux sommaires et aux pages de synthèse. C'est l'exception à la rotation. |
| R4 | Le rose reste un signal : encadrement, surlignage, option non retenue, point d'attention. Jamais un texte, jamais un aplat de fond étendu. |
| R5 | Le fond bleu foncé inverse les rôles : l'accent devient le vert, le texte secondaire passe au voile, les encadrements passent au vert ou au turquoise. |

## À faire, à éviter

|  | Énoncé |
| :--- | :--- |
| À faire | Un seul accent par section, appliqué à l'encadré, au tableau et au graphique de cette section. |
| À faire | Le rose en encadrement d'un point d'attention, une fois par document. |
| À éviter | Un encadré turquoise à côté d'un tableau vert dans la même section : deux codes couleur pour une seule unité de lecture. |
| À éviter | Le rose en aplat de fond sous un paragraphe, ou en couleur de texte. |

## Implémentation web

Attribut `data-accent`, valeurs `cyan`, `green`, `lavender`, `pink`. Redéfinit `--accent`, `--accent-10` et `--accent-22` pour la section : encadré, filet, alternance de tableau, ligne de total, surlignage et badges suivent. Règles fournies dans `assets/css/explorai-jetons.css`.

```html
<section data-accent="green"> … </section>
```
