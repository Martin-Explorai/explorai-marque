---
id: c14
titre: "Interface d'application"
resume: "Principes d'interface produit, composants, états, plancher de qualité."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/interface"
url: https://martin-explorai.github.io/explorai-marque/regles/c14-interface.md
html: https://martin-explorai.github.io/explorai-marque/c14-interface.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c14 — Interface d'application

Principes d'interface produit, composants, états, plancher de qualité.

L'interface est calme, dense et lisible du premier coup d'œil : la marque s'y exprime par la structure, pas par la décoration.

## Principes

| Id | Principe |
| :--- | :--- |
| STRUCTURE | Le bleu foncé porte la navigation, jamais le contenu. Barre d'application et élément actif du menu en bleu; la zone de travail reste blanche. |
| COULEUR | Le vert signale l'état actif et la réussite. Un seul élément vert par écran. |
| DONNEE | Le turquoise appartient aux chiffres : séries de graphiques, étiquettes de mesure, encadrement d'un panneau d'analyse. |
| ALERTE | Le rose est réservé aux conflits et aux blocages. Il ne décore jamais une carte et ne signale jamais une simple nouveauté. |
| DENSITE | Priorité à la densité sur le blanc : corps de 14 à 15 px. Les marges généreuses restent au site web. |

> **Validation humaine.** Dans un écran de validation, la machine propose et l'humain confirme. L'interface rend le désaccord facile à exprimer.

## Composants

| Composant | Règle |
| :--- | :--- |
| Bouton principal | Un seul par écran. Il porte le verbe exact de ce qui va se produire : « Valider les 34 lignes », pas « Soumettre ». |
| Boutons secondaire et discret | Pour les actions de second rang. Ils ne concurrencent pas le bouton principal. |
| Sélecteur segmenté | Deux à quatre options qui changent la lecture de la même donnée. Au-delà, une liste déroulante. |
| Champ de saisie | Étiquette au-dessus du champ, jamais à l'intérieur. Le texte d'aide explique le format attendu avant l'erreur. Le message d'erreur dit quoi corriger. On marque les champs facultatifs plutôt que d'employer un astérisque seul. |
| Message d'état | Réussite en vert, blocage en rose. Chaque message nomme l'objet et la suite : « Deux ordres réclament le poste 4 à la même heure. » |
| État vide | Dit pourquoi la zone est vide et quand du contenu y apparaîtra, puis propose une action. |
| Vignette de mesure | La mesure principale est en bleu foncé, une seule par écran. Les mesures d'appui sont sur fond blanc, cadre filet #DEDBE6. |
| Tableau de données | En-têtes triables, valeurs numériques alignées à droite en chiffres tabulaires, ligne de total selon la [section c07](c07-tableaux.md). |
| Barre d'application | Fond bleu foncé, logo blanc de 104 px. |

## Plancher de qualité

| Critère | Énoncé |
| :--- | :--- |
| Contraste et couleur | Le vert et le turquoise ne portent jamais de texte sur fond blanc : leur contraste est insuffisant. Aucune information n'est transmise par la couleur seule — un état est toujours doublé d'un mot. |
| Clavier | Chaque action est atteignable au clavier, dans l'ordre de lecture. Le contour de focus est visible, turquoise, jamais supprimé. |
| Densité et zoom | L'interface reste utilisable à 200 % de zoom, sans défilement horizontal de la page. Les tableaux défilent dans leur cadre plutôt que de réduire la police. |
| Mouvement | Aucune animation décorative. Les transitions montrent seulement ce qui vient de changer et se désactivent si le système le demande. |
