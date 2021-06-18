---
layout: default
title: 1.1 Les étalons d'espace et de temps
parent: Module 1
nav_order: 1\n
figno:0
---

# {{ page.title }}
{: .no_toc }

{: .text-delta }
- TOC
{:toc}
---
## Introduction
Notre univers est très vaste et il existe depuis très longtemps. À l'échelle humaine, il est difficile d'imaginer la taille et l'âge de l'Univers. Les nombres deviennent si grands qu'ils défient notre compréhension. C'est pourquoi il est commode d'en faire un modèle spatial et temporel à l'échelle en utilisant des étalons plus appropriés. L'objectif des prochaines sections est d'établir ces étalons que nous utiliserons tout au long du cours.

## 1.1.1 Distances, dimensions et masses
Pour se donner une idée grossière des distances et des dimensions, commençons par citer quelques *nombres astronomiques*! Le tableau 1 présente la taille et la masse de la Terre et du Soleil ainsi que la distance moyenne qui les sépare.

| Nom                           |      Symbole  |  Valeur |
|----------                     |:-------------:|------:|
| Rayon de la Terre             |  $R_{\oplus}$ | 6 400 km |
| Rayon du Soleil               |  $R_{\odot}$  | 696 000 km |
| Masse de la Terre             |  $M_{\oplus}$ | $6 \times 10^{24}$ kg |
| Masse du Soleil               |  $M_{\odot}$  | $2 \times 10^{30}$ kg |
| Distance moyenne Terre-Soleil | UA            | 49 600 000 km |
{%capture caption %} Quelques nombres astronomiques (Note : on utilise souvent la notation exponentielle pour simplifier l'écriture des grands nombres. Voir la section <a href="/pages/rappel"> Avant de commencer. </a> pour plus d'informations.)  {% endcapture) %}
{% include table_caption.html no=1 caption=caption %}


Il s'agit vraiment de très grands nombres et, comme toujours en physique, on définit plutôt des unités ou des étalons plus appropriés pour simplifier la notation. Ainsi, à l'échelle du système solaire, nous utiliserons :

* le rayon terrestre, $R_{\oplus}$, comme étalon de la taille,

* la masse terrestre, $M_{\oplus}$,  comme étalon de la masse,

* la distance moyenne Terre-Soleil = 1 Unité Astronomique (UA) comme étalon de la distance.

Avec ces étalons, on constate que :

* $1 R_{\odot} \approx 100 R_{\oplus} $
* $1 M_{\odot} \approx 3.3 \times 10^5 M_{\oplus} $
* 1 UA $\approx 200 R_{\oplus} $

Ces étalons nous permettent de créer un modèle à l'échelle du système solaire comme celui des figues [Figure 1](#fig:1) et [Figure 2](#fig:2).


{% include image.html src='/assets/images/Module1/image_1_1_1_a.jpg' alt='alt and id' class='max-400px-wide' caption='An informative caption.' %}


{% include figanchor.html no=1 %}
![img](/assets/images/Module1/image_1_1_1_a.jpg)
{%capture caption %}Crédit : NASA. {% endcapture %}
{% include figcaption.html no=1 caption=caption %}

{% include figanchor.html no=2 %}
![img](/assets/images/Module1/image_1_1_1_b.png)
{%capture caption %}Crédit de l'image : NASA. {% endcapture %}
{% include figcaption.html no=2 caption=caption %}

Grâce à ce modèle, on se rend compte que le volume de l'orbite de la planète naine Pluton ne contient essentiellement que du vide. En fait, les planètes sont à des distances énormes par rapport à leur dimension.

Bien que ces étalons dépassent déjà l'imagination, ils ne sont plus appropriés dans le domaine stellaire (étoiles, galaxies, etc.). Par exemple, la distance entre le Soleil et l'étoile la plus proche de nous, Alpha du Centaure, est de $4 \times 10^{13}$ km ou 260 000 UA.

Nous définissons donc de nouvelles unités telles le rayon et la masse du Soleil, $R_\odot$ et $M_\odot$, pour décrire les caractéristiques physiques des autres étoiles.

Pour les mesures de distance, nous utiliserons un nouvel étalon astronomique, l'**année-lumière**. Ce dernier est défini de la façon suivante – une année-lumière (AL) est la distance parcourue par la lumière dans le vide en une année (la vitesse de la lumière vaut environ 300 000 km/s). En termes de nos étalons précédents, le kilomètre et l'unité astronomique, l'année-lumière vaut : **1 AL = 300 000 km/s x 3 x $10^7$ s = $ 9 \times 10^{12}$ km = 60 000 UA**

L'année-lumière n'est donc pas une mesure de temps, mais bien une mesure de distance. Si on utilise cet étalon à l'échelle du système solaire on trouve que :

* la distance Terre-Lune est de 1,3 secondes-lumière.

* la distance Terre-Soleil est de 8 minutes-lumière.

* la distance Terre-Jupiter varie entre 35 et 52 minutes-lumière.

* la distance Terre-Pluton varie entre 5,3 et 5,6 heures-lumière.

C'est-à-dire qu'en voyageant à la vitesse de la lumière il faudrait 1,3 secondes pour atteindre la Lune, 8 minutes pour atteindre le Soleil, etc. Si on revient aux distances stellaires, on constate que cet étalon est plus adéquat. Ainsi, la distance entre le Soleil et Alpha du Centaure est de 4,3 AL. Vu de cette étoile, le Soleil n'est plus qu'une étoile parmi les $2.5 \times 10^{11}$ (deux cent cinquante milliards) autres étoiles de notre galaxie, la Voie Lactée. Il en va de même pour les $10^{11}$ (cent milliards) galaxies que nos télescopes nous révèlent. On se rend compte encore une fois que l'espace est pratiquement vide. Le tableau ci-dessous présente quelques autres distances typiques du domaine interstellaire et intergalactique.



Finalement, il faut remarquer que, puisque la lumière voyage à une vitesse finie, on observe donc les astres tels qu'ils étaient au moment où ils ont émis cette lumière. Donc, à tout instant, on voit la Lune telle qu'elle était il y a 1,3 secondes, le Soleil tel qu'il était il y a 8 minutes, le centre de notre galaxie tel qu'il était il y a 30 000 ans, etc. Plus on observe des objets éloignés, plus on regarde dans le passé !

| Tables   |      Are      |  Cool |
|----------|:-------------:|------:|
| col 1 is |  left-aligned | $1600 |
| col 2 is |    centered   |   $12 |
| col 3 is | right-aligned |    $1 |

{% include table_caption.html no=2 caption=caption %}



## 1.1.2 Le calendrier cosmique

## 1.1.3 La mesure du temps en astronomie
Notre vie de tous les jours est ponctuée par le passage du temps à plusieurs échelles : une période de cours, une semaine de congé, une saison de ski, etc. Pour s'y retrouver, nous mesurons le passage du temps en termes de secondes, de minutes, d'heures, de jours, de mois et d'années. D'où vient cette façon de mesurer le temps ?

À l'origine, nos ancêtres ont utilisé divers mouvements des objets de la voûte céleste pour mesurer l'écoulement du temps. Pour bien comprendre, il faut se ramener à une époque où on croyait que la Terre était immobile et au centre de l'Univers. Bien sûr, ce n'est pas le cas et plusieurs des mouvements observés sur la voûte céleste résultent des mouvements de notre planète comme la rotation sur elle-même et sa révolution autour du Soleil.

### 1.1.3.A. Le jour solaire et le jour sidéral

### 1.1.3.B. Le calendrier
