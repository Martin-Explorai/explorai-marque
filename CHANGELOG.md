# Journal des versions — explorai-marque

Toute modification est consignée avec sa date et son motif (règle de gouvernance, section c00).
La version du dépôt ne renumérote pas la charte : la norme appliquée reste **Normes graphiques Explorai v3 (2026-09)**.

## v8.0 — 2026-09-15

Refonte structurelle : le livrable `explorai-site-v6` devient le dépôt `explorai-marque`, pensé d'abord pour la consultation par des agents (LLM).

### Source de vérité
- `data/explorai-marque.json` devient la **seule** source de vérité. En v6, `marque.html` faisait foi et quatre copies des règles (HTML, JSON, texte, lisez-moi) étaient tenues à la main.
- Tous les autres fichiers de règles sont générés par `outils/construire.py`. `--verifier` contrôle que les dérivés sont à jour, que les liens et chemins existent, que toute couleur appartient à la palette et qu'aucun terme obsolète ne subsiste.
- Les règles qui n'existaient que dans les pages de démonstration sont intégrées à la source : gabarit de document (c12), contenu web (c13), interface d'application (c14), listes de vérification (c15).

### Retrait
- Section **présentations** retirée : page `presentation.html`, normes PPTX, gabarit POTX, mentions « diapositive » dans les règles d'accent, ligne « Présentation client » de la correspondance des icônes.
- L'exemple de la forme Déploiement, qui citait une présentation, est remplacé par « Section « Mise en service » d'une offre de service ou d'un rapport de livraison ».
- Retirés comme redondants : `explorai-apercu-v6.html`, `explorai-lisezmoi-v6.md` (remplacé par `README.md`), `explorai-script-v6.js` (le site n'emploie plus de script), `explorai-style-v6.css` (remplacé par `explorai-jetons.css` et `explorai-site.css`).
- Retirés des pages : l'offre fictive « Groupe Vallée » page par page, les maquettes d'application, les témoignages nominatifs et les chiffres sectoriels non vérifiés. Un seul exemple de tableau, marqué « fictif », est conservé (c12).

### Publication
- Adresses réelles : dépôt `https://github.com/Martin-Explorai/explorai-marque`, site `https://martin-explorai.github.io/explorai-marque/`. Le domaine fictif `exemple.ca` disparaît.
- Le manifeste des actifs donne pour chaque fichier une URL GitHub Pages, une URL brute (`raw.githubusercontent.com`), les dimensions, le poids et une empreinte SHA-256.
- Ajout de `.nojekyll`, `SKILL.md`, `VERSION`, `data/explorai-jetons.json` (DTCG), `data/explorai-index.json`, `llms-full.txt` en Markdown.

### Nomenclature
- Les fichiers du dépôt portent désormais des **noms stables, sans version** (`explorai-marque.json` au lieu de `explorai-marque-v6.json`) : une URL citée par un agent reste valide d'une version à l'autre. La version se lit dans `VERSION`, dans l'en-tête des fichiers et dans les étiquettes Git. **Décision à faire valider par le responsable de la marque**, car elle modifie la convention v6.
- Les actifs de marque gardent la règle `nom-type-variante`, sans version.
- Les sections de règles portent un identifiant stable `c00` à `c16`.

### Polices
- Ajout de DM Sans (400, 500, 600, 700) et IBM Plex Mono (400, 500) en WOFF2 et TTF, sous-ensembles latins Fontsource 5.3.0, licence OFL 1.1 jointe. Le site ne dépend plus de Google Fonts.

### Corrections
- Écriture : toutes les valeurs chiffrées de la source (exemples, mesures, montants) et les guillemets contiennent désormais les espaces insécables réelles (U+00A0, U+202F) au lieu d’espaces ordinaires.
- Actifs : le chemin du favicon (`assets/img/explorai-favicon.png`) est corrigé; la note de production contradictoire de l'ancienne section Actifs (tous les SVG dits vectorisés) est alignée sur la provenance réelle (icônes d'origine, logos vectorisés).
- Document : la référence à un modèle `explorai-modele-document-v6.dotx` inexistant est remplacée par une spécification explicite des onze styles.
- Typographie : l'interdiction de l'italique, énoncée seulement dans une page de démonstration, rejoint les interdits typographiques.

## v6 — 2026-09

Site statique de sept pages, `marque.html` normatif, fichiers machine `llms.txt`, `llms-full.txt`, `explorai-marque-v6.json`, `explorai-actifs-v6.json`.
