---
id: c11
titre: "Actifs"
resume: "Choisir une variante et un format, URL de téléchargement, insertion, nomenclature."
version: "8.0"
date: 2026-09-15
norme: "Normes graphiques Explorai v3"
langue: fr-CA
source: "data/explorai-marque.json#/actifs"
url: https://martin-explorai.github.io/explorai-marque/regles/c11-actifs.md
html: https://martin-explorai.github.io/explorai-marque/c11-actifs.html
genere: "Fichier généré par outils/construire.py à partir de data/explorai-marque.json — ne pas modifier à la main."
---
# c11 — Actifs

Choisir une variante et un format, URL de téléchargement, insertion, nomenclature.

Le fond décide de la variante, le support décide du format. Aucune recoloration hors des variantes fournies, dans aucun cas.

## Variante selon le fond

| Fond | Logo | Icône |
| :--- | :--- | :--- |
| Blanc, White Smoke #F6F6F6, neutre #F2F1F5 | `bleu` | `bleu` |
| Bleu foncé #231651 | `blanc` | `vert` |
| Aplat vert #ACF127 | `bleu` | `bleu` |
| Aplat rose #F127AC, aplat saturé | `blanc` | `blanc` |
| Photographie sombre | `blanc` | `blanc` |
| Composant dont la couleur change selon l'état (SVG en ligne) | — | `heritee` |

## Format selon le support

| Support | Format | Raison |
| :--- | :--- | :--- |
| Site web, application | SVG | Net à toute densité d'écran. |
| Document Word | SVG | Pris en charge depuis Office 2016; PNG en repli. |
| Gabarit de courriel, plateforme sociale | PNG | Le vectoriel y est refusé ou mal rendu. |
| Impression en quadrichromie | EPS | Non fourni — à produire. |
| Icône de site | PNG + ICO | Forme Exploration verte sur carré bleu. |

## À faire, à éviter

|  | Énoncé |
| :--- | :--- |
| À faire | Employer le fichier tel quel, redimensionné proportionnellement. |
| À faire | Respecter la zone de protection du logo : une fois sa hauteur, sur les quatre côtés. |
| À faire | Télécharger depuis l'URL brute du manifeste (data/explorai-actifs.json, champ url_brute) : elle ne dépend pas de GitHub Pages. |
| À éviter | Recolorer un SVG en modifiant son attribut fill, sauf les neuf fichiers en couleur héritée. |
| À éviter | Étirer, pivoter, ajouter un contour, une ombre ou un effet. |
| À éviter | Recopier le tracé d'un SVG dans un autre fichier au lieu de référencer l'actif. |

## Télécharger

Préfixe GitHub Pages : `https://martin-explorai.github.io/explorai-marque/`. Préfixe brut : `https://raw.githubusercontent.com/Martin-Explorai/explorai-marque/main/`. Adresse d'un actif = préfixe + chemin.

| Motif | Chemin |
| :--- | :--- |
| logo | `assets/img/logo/explorai-logo-{bleu\|blanc\|vert}.{svg\|png}` |
| icone | `assets/img/icones/explorai-icone-{forme}-{bleu\|vert\|blanc}.{svg\|png}` |
| icone_couleur_heritee | `assets/img/icones/explorai-icone-{forme}.svg` |
| favicon | `assets/img/explorai-favicon.png` |
| police | `assets/fonts/{Famille}-{Graisse}.{woff2\|ttf}` |

Formes : `apprentissage`, `consultation`, `accompagnement`, `deploiement`, `exploration`, `innovation`, `plus`, `financement`, `transformation`.

## Inventaire

Totaux : 6 logo, 63 icone, 2 favicon, 12 police, 83 total. Inventaire complet, avec URL, dimensions, poids et empreinte SHA-256 : `data/explorai-actifs.json`.

| Chemin | Type | Forme | Variante | Dimensions |
| :--- | :--- | :--- | :--- | :--- |
| `assets/img/logo/explorai-logo-blanc.png` | logo | — | blanc | 1251×205 |
| `assets/img/logo/explorai-logo-blanc.svg` | logo | — | blanc | 0 0 1251 205 |
| `assets/img/logo/explorai-logo-bleu.png` | logo | — | bleu | 1251×204 |
| `assets/img/logo/explorai-logo-bleu.svg` | logo | — | bleu | 0 0 1251 204 |
| `assets/img/logo/explorai-logo-vert.png` | logo | — | vert | 1252×205 |
| `assets/img/logo/explorai-logo-vert.svg` | logo | — | vert | 0 0 1252 205 |
| `assets/img/icones/explorai-icone-apprentissage-bleu.svg` | icone | apprentissage | bleu | 0 0 157.94 109.18 |
| `assets/img/icones/explorai-icone-apprentissage-bleu.png` | icone | apprentissage | bleu | 633×438 |
| `assets/img/icones/explorai-icone-apprentissage-vert.svg` | icone | apprentissage | vert | 0 0 157.94 109.18 |
| `assets/img/icones/explorai-icone-apprentissage-vert.png` | icone | apprentissage | vert | 633×438 |
| `assets/img/icones/explorai-icone-apprentissage-blanc.svg` | icone | apprentissage | blanc | 0 0 157.94 109.18 |
| `assets/img/icones/explorai-icone-apprentissage-blanc.png` | icone | apprentissage | blanc | 633×438 |
| `assets/img/icones/explorai-icone-apprentissage.svg` | icone | apprentissage | heritee | 0 0 633 438 |
| `assets/img/icones/explorai-icone-consultation-bleu.svg` | icone | consultation | bleu | 0 0 151.48 96.79 |
| `assets/img/icones/explorai-icone-consultation-bleu.png` | icone | consultation | bleu | 607×388 |
| `assets/img/icones/explorai-icone-consultation-vert.svg` | icone | consultation | vert | 0 0 151.48 96.79 |
| `assets/img/icones/explorai-icone-consultation-vert.png` | icone | consultation | vert | 607×388 |
| `assets/img/icones/explorai-icone-consultation-blanc.svg` | icone | consultation | blanc | 0 0 151.48 96.79 |
| `assets/img/icones/explorai-icone-consultation-blanc.png` | icone | consultation | blanc | 607×388 |
| `assets/img/icones/explorai-icone-consultation.svg` | icone | consultation | heritee | 0 0 607 388 |
| `assets/img/icones/explorai-icone-accompagnement-bleu.svg` | icone | accompagnement | bleu | 0 0 148.12 100.72 |
| `assets/img/icones/explorai-icone-accompagnement-bleu.png` | icone | accompagnement | bleu | 593×403 |
| `assets/img/icones/explorai-icone-accompagnement-vert.svg` | icone | accompagnement | vert | 0 0 148.12 100.72 |
| `assets/img/icones/explorai-icone-accompagnement-vert.png` | icone | accompagnement | vert | 593×403 |
| `assets/img/icones/explorai-icone-accompagnement-blanc.svg` | icone | accompagnement | blanc | 0 0 148.12 100.72 |
| `assets/img/icones/explorai-icone-accompagnement-blanc.png` | icone | accompagnement | blanc | 593×403 |
| `assets/img/icones/explorai-icone-accompagnement.svg` | icone | accompagnement | heritee | 0 0 593 403 |
| `assets/img/icones/explorai-icone-deploiement-bleu.svg` | icone | deploiement | bleu | 0 0 92.13 92.1 |
| `assets/img/icones/explorai-icone-deploiement-bleu.png` | icone | deploiement | bleu | 370×369 |
| `assets/img/icones/explorai-icone-deploiement-vert.svg` | icone | deploiement | vert | 0 0 92.13 92.1 |
| `assets/img/icones/explorai-icone-deploiement-vert.png` | icone | deploiement | vert | 370×369 |
| `assets/img/icones/explorai-icone-deploiement-blanc.svg` | icone | deploiement | blanc | 0 0 92.13 92.1 |
| `assets/img/icones/explorai-icone-deploiement-blanc.png` | icone | deploiement | blanc | 370×369 |
| `assets/img/icones/explorai-icone-deploiement.svg` | icone | deploiement | heritee | 0 0 370 369 |
| `assets/img/icones/explorai-icone-exploration-bleu.svg` | icone | exploration | bleu | 0 0 134.51 114.72 |
| `assets/img/icones/explorai-icone-exploration-bleu.png` | icone | exploration | bleu | 539×460 |
| `assets/img/icones/explorai-icone-exploration-vert.svg` | icone | exploration | vert | 0 0 134.51 114.72 |
| `assets/img/icones/explorai-icone-exploration-vert.png` | icone | exploration | vert | 539×460 |
| `assets/img/icones/explorai-icone-exploration-blanc.svg` | icone | exploration | blanc | 0 0 134.51 114.72 |
| `assets/img/icones/explorai-icone-exploration-blanc.png` | icone | exploration | blanc | 539×460 |
| `assets/img/icones/explorai-icone-exploration.svg` | icone | exploration | heritee | 0 0 539 460 |
| `assets/img/icones/explorai-icone-innovation-bleu.svg` | icone | innovation | bleu | 0 0 118.7 121.09 |
| `assets/img/icones/explorai-icone-innovation-bleu.png` | icone | innovation | bleu | 476×485 |
| `assets/img/icones/explorai-icone-innovation-vert.svg` | icone | innovation | vert | 0 0 118.7 121.09 |
| `assets/img/icones/explorai-icone-innovation-vert.png` | icone | innovation | vert | 476×485 |
| `assets/img/icones/explorai-icone-innovation-blanc.svg` | icone | innovation | blanc | 0 0 118.7 121.09 |
| `assets/img/icones/explorai-icone-innovation-blanc.png` | icone | innovation | blanc | 476×485 |
| `assets/img/icones/explorai-icone-innovation.svg` | icone | innovation | heritee | 0 0 476 485 |
| `assets/img/icones/explorai-icone-plus-bleu.svg` | icone | plus | bleu | 0 0 100 100 |
| `assets/img/icones/explorai-icone-plus-bleu.png` | icone | plus | bleu | 401×401 |
| `assets/img/icones/explorai-icone-plus-vert.svg` | icone | plus | vert | 0 0 100 100 |
| `assets/img/icones/explorai-icone-plus-vert.png` | icone | plus | vert | 401×401 |
| `assets/img/icones/explorai-icone-plus-blanc.svg` | icone | plus | blanc | 0 0 100 100 |
| `assets/img/icones/explorai-icone-plus-blanc.png` | icone | plus | blanc | 401×401 |
| `assets/img/icones/explorai-icone-plus.svg` | icone | plus | heritee | 0 0 401 401 |
| `assets/img/icones/explorai-icone-financement-bleu.svg` | icone | financement | bleu | 0 0 105.55 128.13 |
| `assets/img/icones/explorai-icone-financement-bleu.png` | icone | financement | bleu | 424×514 |
| `assets/img/icones/explorai-icone-financement-vert.svg` | icone | financement | vert | 0 0 105.55 128.13 |
| `assets/img/icones/explorai-icone-financement-vert.png` | icone | financement | vert | 424×514 |
| `assets/img/icones/explorai-icone-financement-blanc.svg` | icone | financement | blanc | 0 0 105.55 128.13 |
| `assets/img/icones/explorai-icone-financement-blanc.png` | icone | financement | blanc | 424×514 |
| `assets/img/icones/explorai-icone-financement.svg` | icone | financement | heritee | 0 0 424 514 |
| `assets/img/icones/explorai-icone-transformation-bleu.svg` | icone | transformation | bleu | 0 0 125.19 114.01 |
| `assets/img/icones/explorai-icone-transformation-bleu.png` | icone | transformation | bleu | 501×457 |
| `assets/img/icones/explorai-icone-transformation-vert.svg` | icone | transformation | vert | 0 0 125.19 114.01 |
| `assets/img/icones/explorai-icone-transformation-vert.png` | icone | transformation | vert | 501×457 |
| `assets/img/icones/explorai-icone-transformation-blanc.svg` | icone | transformation | blanc | 0 0 125.19 114.01 |
| `assets/img/icones/explorai-icone-transformation-blanc.png` | icone | transformation | blanc | 501×457 |
| `assets/img/icones/explorai-icone-transformation.svg` | icone | transformation | heritee | 0 0 501 457 |
| `assets/img/explorai-favicon.png` | favicon | — | bleu-vert | 512×512 |
| `favicon.ico` | favicon | — | bleu-vert | 16×16, 24×24, 32×32, 48×48, 64×64 |
| `assets/fonts/DMSans-Regular.woff2` | police | — | 400 | — |
| `assets/fonts/DMSans-Regular.ttf` | police | — | 400 | — |
| `assets/fonts/DMSans-Medium.woff2` | police | — | 500 | — |
| `assets/fonts/DMSans-Medium.ttf` | police | — | 500 | — |
| `assets/fonts/DMSans-SemiBold.woff2` | police | — | 600 | — |
| `assets/fonts/DMSans-SemiBold.ttf` | police | — | 600 | — |
| `assets/fonts/DMSans-Bold.woff2` | police | — | 700 | — |
| `assets/fonts/DMSans-Bold.ttf` | police | — | 700 | — |
| `assets/fonts/IBMPlexMono-Regular.woff2` | police | — | 400 | — |
| `assets/fonts/IBMPlexMono-Regular.ttf` | police | — | 400 | — |
| `assets/fonts/IBMPlexMono-Medium.woff2` | police | — | 500 | — |
| `assets/fonts/IBMPlexMono-Medium.ttf` | police | — | 500 | — |

## Usage par variante

| Type | Variante | Usage |
| :--- | :--- | :--- |
| logo | bleu | Variante principale. Sur blanc, sur White Smoke et sur toute teinte pâle, y compris l'aplat vert. Variante par défaut de tout document. |
| logo | blanc | Variante inversée. Sur bleu foncé, photographie sombre et aplat de couleur saturée, y compris le rose. |
| logo | vert | Hors emploi courant. Fourni, mais sans usage admis : sur aplat vert, employer la variante bleu foncé. |
| icône | bleu | Fond clair : blanc, White Smoke, neutre, aplat vert. |
| icône | vert | Fond bleu foncé #231651. Seule variante admise sur ce fond. |
| icône | blanc | Aplat de couleur saturée, ou photographie sombre. |
| icône | heritee | Usage en ligne dans le HTML : le fichier porte fill="currentColor" et prend la couleur du texte environnant. Seule recoloration admise. |
| favicon | — | Icône de site. Forme Exploration verte sur carré bleu foncé. |

## Insertion

Page web — logo d'en-tête, 132 px :

```html
<img src="https://martin-explorai.github.io/explorai-marque/assets/img/logo/explorai-logo-bleu.svg"
     alt="Explorai" width="132">
```

Page web — icône de section sur fond clair :

```html
<img src="https://martin-explorai.github.io/explorai-marque/assets/img/icones/explorai-icone-accompagnement-bleu.svg"
     alt="" width="62">
```

Couleur héritée — SVG collé en ligne :

```html
<span style="color:#2DDCF9">
  <!-- contenu de explorai-icone-plus.svg, fill="currentColor" -->
  <svg viewBox="0 0 401 401">…</svg>
</span>
```

Motif de couverture en CSS, fond bleu :

```css
.couverture {
  background: #231651
    url("https://martin-explorai.github.io/explorai-marque/assets/img/icones/explorai-icone-exploration-vert.svg")
    no-repeat right -80px bottom -60px / 38%;
}
```

Jetons et polices dans une page web :

```html
<link rel="stylesheet"
      href="https://martin-explorai.github.io/explorai-marque/assets/css/explorai-jetons.css">
```

Téléchargement en ligne de commande :

```bash
curl -LO https://raw.githubusercontent.com/Martin-Explorai/explorai-marque/main/assets/img/logo/explorai-logo-bleu.svg
```

Document Word :

```texte
Insertion > Images > le fichier SVG. Le PNG du même dossier sert de repli si le logiciel refuse le vectoriel.
```

## Provenance

| Lot | Provenance |
| :--- | :--- |
| logos | Vectorisation des PNG fournis (potrace), recolorés selon la variante. Écart de silhouette mesuré < 0,15 % des pixels. Aucun original reçu à ce jour. |
| icones bleu vert blanc | Fichiers vectoriels d'origine reçus directement pour les neuf formes, dans les trois couleurs. Non vectorisés : référence la plus fidèle. Les PNG correspondants sont rendus depuis ces mêmes vecteurs, aux mêmes dimensions que les fichiers qu'ils remplacent. |
| icones couleur heritee | Les neuf fichiers currentColor restent issus de la vectorisation initiale; aucun original n'a été reçu pour cette variante. |

## Nomenclature

| Catégorie | Règle | Exemples | Raison |
| :--- | :--- | :--- | :--- |
| Fichier du dépôt | Nom stable, sans numéro de version. La version se lit dans data/explorai-marque.json (document.version), dans le fichier VERSION, dans l'en-tête de chaque fichier généré et dans les étiquettes Git (v8.0). | `data/explorai-marque.json`, `assets/css/explorai-jetons.css`, `regles/c03-palette.md` | Une URL stable reste valide d'une version à l'autre pour les agents et les skills qui la référencent. Le cache navigateur est contourné par un paramètre ?v= dans les pages HTML. |
| Actif de marque | nom-type-variante, sans version | `explorai-logo-bleu.svg`, `explorai-icone-exploration-vert.svg`, `explorai-favicon.png` | Un actif change de dessin, pas de millésime. |
| Section de règles | cNN-sujet, identifiant cNN stable | `c04-couleur-en-usage.md`, `c04-couleur-en-usage.html` | L'identifiant cNN sert de référence courte et ne change pas si le titre change. |
| Archive | explorai-marque.zip, contenant le dossier racine explorai-marque/. | `explorai-marque.zip` | — |
