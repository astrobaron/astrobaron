---
layout: default
title: 3.1 Les systèmes de coordonnées
parent: Module 3
nav_order: 1\n
---

# {{ page.title }}
{: .no_toc }

{: .text-delta }
- TOC
{:toc}
---
Les astronomes utilisent plusieurs systèmes de coordonnées pour repérer les objets sur la voûte céleste et suivre leurs déplacements apparents et réels. Parmi ceux-ci, deux vont particulièrement retenir notre attention. En tenant compte des mouvements de la Terre, nous serons en mesure de comprendre les mouvements des étoiles et du Soleil dans le ciel. Avant de procéder, cependant, il est bon de se remémorer la façon avec laquelle on se repère à la surface de la Terre, c'est-à-dire de revoir le système de coordonnées terrestres.

## 3.1.1 Les systèmes de coordonnées : se repérer
### 3.1.1.A. Système de coordonnées sur la Terre

La latitude et la longitude sont utilisées comme système de coordonnées pour se repérer sur la Terre. Les longitudes sont parallèles à la ligne qui joint les Pôles Nord et Sud. Les latitudes sont parallèles à l'équateur de la Terre.  

![img](/assets/images/Module3/lat_long/lat_long.002.jpeg)
{%capture caption %} Longitue et latitude.  {% endcapture %}
{% include figcaption.html caption=caption %}

La figure ci-dessous vous montre la sphère terrestre. On y repère l'équateur terrestre, perpendiculaire à l'axe de rotation de la Terre et partageant la Terre en deux hémisphères, les deux pôles, les points par lesquels passe cet axe, ainsi que les grands cercles qui passent par les pôles et qui sont perpendiculaires à l'équateur. Ce sont les méridiens.


![img](/assets/images/Module3/lat_long/lat_long.001.jpeg)
{%capture caption %} Le méridien de Greenwich et l'équateur sur la sphère terrestre. {% endcapture %}
{% include figcaption.html caption=caption %}

Il suffit de deux angles pour repérer n'importe quel point, par exemple la ville de Montréal, à la surface de la Terre. On choisit d'habitude la longitude, qui est l'angle, mesuré le long de l'équateur terrestre, entre le méridien du lieu (c'est-à-dire le grand cercle qui passe par les pôles et Montréal), et le méridien d'un lieu de référence qui est, pour des raisons historiques, la ville de Greenwich, en Angleterre. Les longitudes sont mesurées en degrés Est ou Ouest. La longitude de Montréal est de 73,5 $^{\circ}$ Ouest. La latitude d'un lieu représente, quant à elle, l'angle, mesuré le long du méridien du lieu, entre l'équateur et le lieu. Elle est mesurée en degrés, et peut être positive, si le point est dans l'hémisphère nord, ou négative s'il est dans l'hémisphère sud. Montréal se trouve à une latitude de +45,5 $^{\circ}$, ou 45,5$^{\circ}$ Nord.

### 3.1.1.B. Système horizontal

Maintenant que nous savons repérer un point quelconque à la surface de la Terre, voyons comment les astronomes repèrent un objet quelconque sur la sphère céleste. Le premier système astronomique que nous allons introduire est le système d'**horizon**, ou horizontal (voir la figure suivante). Dans ce système, on imagine l'observateur à l'intérieur d'une gigantesque sphère, la **sphère céleste**, sur laquelle sont épinglées les étoiles (notez que, dans cette représentation, la notion de profondeur, ou de distance à une étoile, est complètement mise de côté).

![img](/assets/images/Module3/lat_long/lat_long.003.jpeg)
{%capture caption %} Le système d'horizon. Adaptée d'une figure de L'Astorina.  {% endcapture %}
{% include figcaption.html caption=caption %}

L'observateur est au centre de cette sphère. Le point de la sphère céleste directement au-dessus de sa tête s'appelle le **zénith**. Le point opposé de la sphère céleste, directement au-dessous de ses pieds, s'appelle le **nadir**. Le plan à mi-chemin entre le zénith et le nadir est l'horizon de l'observateur. Dans ce système, la position d'une étoile donnée est mesurée, encore une fois, par deux angles : l'**altitude**, qui est la hauteur angulaire de l'étoile au-dessus de l'horizon, c'est-à-dire le nombre de degrés, mesurés le long d'un grand cercle passant par le zénith et l'étoile, entre l'étoile et l'horizon; et l'**azimut**, qui est l'angle, mesuré (vers l'est) le long de l'horizon, entre la direction nord et le grand cercle passant par l'étoile. Ce système est un système purement local : deux observateurs à différents endroits sur Terre vont avoir des zéniths et des horizons différents, et vont mesurer, pour une étoile donnée, une altitude et un azimut différents. Ce système reste néanmoins très utile pour décrire l'aspect du ciel à un endroit donné à la surface de la Terre. La vidéo suivante, faite avec le logiciel [Stellarium](https://stellarium.org/fr/), permetait de voir le mouvement apparent des étoiles.

<p align="center">
  <video width="700" controls>
    <source src="/assets/images/Module3/mouvement_ciel.mp4" type="video/mp4">
  </video>
</p>

Ces définitions nous permettent de comprendre un résultat important pour la suite. Considérons un observateur à une latitude géographique $\phi$ à la surface de la Terre. Dessinons maintenant le système horizontal particulier de cet observateur, en particulier son horizon, lors de l'observation de l'étoile polaire.

![img](/assets/images/Module3/lat_long/lat_long.004.jpeg)
{%capture caption %} L'altitude de l'étoile polaire dans le système horizontal.  {% endcapture %}
{% include figcaption.html caption=caption %}

Cet observateur verra l'étoile polaire, qui indique approximativement la direction nord, à un certain angle au-dessus de son horizon. Cet angle est défini comme l'altitude du pôle Nord, et sera, comme la figure ci-dessus le montre, égal à $\phi$. Ainsi donc, très généralement, **la hauteur du pôle Nord au-dessus de l'horizon d'un observateur (ou l'altitude de l'étoile polaire) est égale à la latitude géographique de l'observateur**. Ce résultat nous permettra, par la suite, de comprendre l'aspect du ciel à n'importe quel point à la surface de la Terre.

<p align="center">
  <video width="700" controls>
    <source src="/assets/images/Module3/mouvement_ciel_polaire.mp4" type="video/mp4">
  </video>
</p>

Dans cette animation, réalisée avec le logiciel [Stellarium](https://stellarium.org/fr/), remarquez que l'étoile polaire (située approximativement dans le prolongement de l'axe de rotation) demeure toujours à la même hauteur au-dessus de l'horizon.

Avant de passer à la description du second système de coordonnées astronomiques, il convient ici d'ouvrir une parenthèse. Le mouvement annuel de la Terre autour du Soleil se fait sur une orbite que l'on appelle l'**écliptique**. Cependant, il est souvent plus pratique de décrire ce mouvement tel qu'il est perçu par un observateur situé à la surface de la Terre. Les astronomes ont donc tendance à parler du mouvement apparent annuel du Soleil dans le ciel (un mouvement dû, encore une fois, au mouvement de révolution de la Terre autour du Soleil). Dans le même esprit, ils vont dire que ce mouvement apparent du Soleil se fait sur un cercle, l'écliptique, et que le Soleil met un an pour revenir au même point dans le ciel. La figure ci-dessous vous montre le mouvement réel, en haut, ainsi que le mouvement apparent, vu par un observateur terrestre, en bas.

![img](/assets/images/Module3/lat_long/lat_long.005.jpeg)
{%capture caption %} Le mouvement réel et apparent de la Terre et du Soleil.  {% endcapture %}
{% include figcaption.html caption=caption %}

Sachez distinguer ces deux mouvements, et ne soyez pas trompés : nous ne sommes pas revenus à une conception géocentrique de l'Univers. Notez également que l'axe de rotation de la Terre n'est pas perpendiculaire à l'écliptique. En d'autres mots, l'équateur terrestre n'est pas dans le même plan que l'écliptique. L'angle entre ces deux plans est de 23,5$^{\circ}$.


### 3.1.1.C. Système équatorial
Ce système de coordonnées est indépendant de l'observateur, et décrit la position d'un astre quelconque à la surface de la sphère céleste. La Terre est au centre de ce système de coordonnées (voir la figure suivante). Si l'on projette l'équateur terrestre sur la sphère céleste, on obtient l'**équateur céleste**. De la même façon, le prolongement de l'axe de rotation terrestre coupe la sphère céleste en deux points, qui sont les **pôles Nord et Sud célestes**. On peut également considérer l'ensemble des grands cercles qui passent par les pôles célestes, que l'on appelle les **cercles horaires**. Remarquez comme ces concepts sont similaires à ceux revus lors de la description du système de coordonnées géographiques. Ici, la sphère **céleste** remplace la sphère **terrestre**.

![img](/assets/images/Module3/603px-Coordonnees_equatoriales.svg.png)
{%capture caption %} Le système de coordonnées 'équatoriales'. Crédit : [Autiwa](https://commons.wikimedia.org/wiki/File:Coordonnees_equatoriales.svg). {% endcapture %}
{% include figcaption.html caption=caption %}

On peut, pour décrire la position d'un objet quelconque à la surface de la sphère céleste, utiliser des angles similaires à la longitude et la latitude décrits plus tôt. Par analogie complète, on appelle la **déclinaison** d'une étoile, symbolisée $\delta$, l'angle, mesuré le long du cercle horaire de cet objet, entre l'équateur céleste et l'objet. Les déclinaisons, sont mesurées en degrés, et vont de -90$^{\circ}$ à +90$^{\circ}$, en passant par 0$^{\circ}$. Pour l'autre angle, équivalent à la longitude terrestre, il nous faut avoir un cercle horaire qui serve d'origine, analogue au méridien de Greenwich. On utilise comme cercle horaire d'origine, celui qui passe par un point particulier situé sur l'équateur céleste, que l'on appelle le **point vernal**. Le point vernal, et sa contrepartie, le **point automnal**, représentent les deux points d'intersection, sur la sphère céleste, de l'équateur céleste et de l'écliptique. Le point vernal indique la position apparente du Soleil le 21 mars, à l'équinoxe du printemps; le point automnal indique sa position six mois plus tard, au début de l'automne. L'**ascension droite** est donc mesurée le long de l'équateur céleste, vers l'est, à partir du point vernal. Plutôt que d'être mesurées en degrés, comme les longitudes terrestres, les ascensions droites, symbolisées , sont mesurées en unités de temps, c'est-à-dire en heures, minutes, et secondes de temps. Les ascensions droites vont de 0 h à 24 h.


<div class="attention">
  <b>Attention!</b>
  <ul>
  Les unités d'angle et de temps sont interchangeables dans les systèmes de coordonnées astronomiques. Cette équivalence est basée sur le fait que la Terre fait une rotation complète, c'est-à-dire couvre 360$^{\circ}$, en 24 heures. 360$^{\circ}$ correspondent donc à 24 heures, une heure équivaut à 15$^{\circ}$, une minute de temps équivaut à 15 minutes d'arc, et une seconde de temps correspond à 15 secondes d'arc. Ne confondez pas unités de temps et unités d'angle.
  </ul>
</div>

**Note sur les distances angulaires**

Les mesures angulaires s'expriment habituellement dans le système sexagésimal. Ce système est basé sur le nombre 60 plutôt que le nombre 10 de notre système décimal. La notation sexagésimale fut développée par les Babyloniens, et on la retrouve encore de nos jours dans l'expression du temps (1 heure vaut 60 minutes, 1 minute vaut 60 secondes). Dans le cas des mesures angulaires, un cercle correspond à 360 degrés. Chaque degré est subdivisé en 60 minutes, et chaque minute est elle-même subdivisée en 60 secondes. Le symbole adopté pour un degré est ($^{\circ}$), pour une minute ('), et pour une seconde (''). On parle alors de minute d'arc et de seconde d'arc afin de les distinguer de leur homonyme de temps. À titre d'exemple, mentionnons que la pleine Lune ou le Soleil font un angle de 0,5$^{\circ}$ sur le ciel. On dit que leur diamètre angulaire est de 0.5 $^{\circ}$ ou 30'.

La figure suivante illustre comment on peut obtenir une mesure de distance angulaire approximative sur le ciel, en utilisant ses doigts et sa main.

<p align="center">
  <img src="/assets/images/Module3/measuring-sky-with-hand.png" />
</p>
{%capture caption %} Mesurer des distances angulaires avec sa main. Crédit : [Time and Date](https://www.timeanddate.com/astronomy/measuring-the-sky-by-hand.html).  {% endcapture %}
{% include figcaption.html caption=caption %}


## 3.1.2 Comment se repérer dans le ciel?
Les étapes décrites ci-dessous vous permettront d'observer le ciel, en repérant et en vous orientant grâce aux coordonnées du système équatorial.

* **1) Trouvez la casserole**, un astérisme qui permet de voir la constellation de  la Grande Ourse.


![img](/assets/images/Module3/lat_long/lat_long.006.jpeg)
{%capture caption %} La casserole est seulement une partie de la constellation de la Grande Ourse. Image tirée de Stellarium.  {% endcapture %}
{% include figcaption.html caption=caption %}



* **2) Trouvez l'étoile polaire** : Prolongez le segment entre les deux étoiles de l'extrémité du carré de la Grande Ourse (segment A-B sur la figure ci-dessus) de 5 fois sa longueur, pour arriver à l'étoile polaire, qui est au bout de la queue de la Petite Ourse.

* **3) Trouvez le méridien du lieu** : Le méridien du lieu où l'on observe est l'arc de cercle qui part de l'étoile polaire, passe par le zénith, et se prolonge vers le sud.

* **4) Trouvez l'équateur céleste et son intersection avec le méridien** : L'équateur céleste est le cercle perpendiculaire à la direction de l'étoile polaire. Le point d'intersection du méridien et de l'équateur est le point qui fait un angle de 90o avec l'étoile polaire le long du méridien.

  Durant un jour donné, le mouvement des étoiles, du Soleil, des planètes, et (de façon un peu plus approximative) de la Lune est dominé par la rotation de la Terre. Ces objets se déplacent donc de l'est à l'ouest le long de cercles parallèles à l'équateur, plus ou moins au nord ou au sud de celui-ci.

  Cependant, de jour en jour, le Soleil se déplace de l'ouest à l'est dans son mouvement apparent autour de la Terre le long du cercle de l'écliptique. Les planètes et la Lune suivent aussi, approximativement, le cercle de l'écliptique, de l'ouest à l'est (sauf durant le mouvement rétrograde des planètes).

* **5) Déterminez l'heure sidérale ** : L'heure sidérale (voir la section 1.1.3.A. Le jour solaire et le jour sidéral du module 1) est synchronisée avec l'heure solaire au moment de l'équinoxe d'automne (21 septembre). Le temps sidéral prend deux heures d'avance par mois (une demi-heure par semaine) sur le temps solaire. Selon la date de l'année, trouvez le décalage de l'heure sidérale par rapport à l'heure solaire (par exemple le 28 octobre : h.sid. = h.sol. + 2,5 heures). Sachant l'heure solaire au moment de l'observation (n'oubliez pas de soustraire une heure de l'heure avancée), déterminez l'heure sidérale. L'heure sidérale donne la coordonnée (ascension droite) des points (étoiles) qui passent au méridien.

* **6) Repérez le point automnal (jan. juin) ou le point vernal (juil. déc.)** : Les points vernal et automnal sont situés sur l'équateur à des coordonnées de 0 h (point vernal) et 12 h (point automnal). Un décalage d'une heure correspond à un déplacement de 15o le long du cercle de l'équateur. Si l'heure sidérale est 21 h, alors le point vernal est situé 3 h (ou 45o) à l'est du méridien, et le point automnal est 9 h (ou 135o) à l'ouest du méridien (et donc sous l'horizon).

* **7) Déterminez l'orientation de l'écliptique par rapport à l'équateur** : L'écliptique et l'équateur sont deux cercles qui se croisent à un angle de 23,5$^{\circ}$ aux points vernal et automnal. Le Soleil suit l'écliptique tout au long de l'année, de l'ouest vers l'est. À l'équinoxe de printemps (le 21 mars), le Soleil passe par le point vernal en croisant l'équateur du sud (où il a passé l'hiver) au nord (où il passera l'été). Donc au point vernal, l'écliptique va du sud-ouest au nord-est, faisant un angle de 23,5$^{\circ}$ avec l'équateur. Au point automnal, l'écliptique va du nord-ouest au sud-est.

* **8) Trouvez les planètes le long de l'écliptique** : Vénus, Jupiter, Mars et Saturne sont les objets les plus brillants situés à moins de quelques degrés de l'écliptique (mise à part la Lune). Vénus est la plus brillante, visible le soir à l'ouest ou le matin à l'est. Jupiter et Mars peuvent être de brillance comparable; Mars est rougeâtre et Jupiter blanchâtre. Saturne est plus faible et se compare aux étoiles les plus brillantes dans le ciel.

## 3.1.3 Les mouvements de la Terre

La Terre effectue, simultanément, plusieurs mouvements. Le mouvement résultant est donc très complexe. Nous distinguons deux mouvements principaux :

* Un mouvement de rotation :

  La Terre tourne sur elle-même une fois par 23 h 56 m. La vitesse de rotation à l'équateur est de 1700 km/h, ou de 0,47 km/s. Parce que l'intérieur de notre planète n'est pas complètement solidifié, la rotation déforme notre planète. Le diamètre de la Terre mesuré à l'équateur est légèrement supérieur à celui mesuré d'un pôle à l'autre. La valeur du diamètre polaire est 12 714 km, tandis que celle du diamètre équatorial est plus grande de 43 km, soit 12 757 km. Ce renflement est à l'origine de deux autres mouvements de notre planète, la précession et la nutation.

* Un mouvement de révolution :

  La Terre tourne autour du Soleil une fois par an (365,25 jours). La vitesse de révolution de la Terre sur son orbite est de 108 000 km/h, ou de 30 km/s.

### 3.1.3.A. Un mouvement de précession
La direction de l'axe de rotation de la Terre n'est pas fixe dans l'espace, mais trace plutôt un cercle à un angle de 23,5$^{\circ}$ du pôle de l'écliptique avec une période de 26 000 ans (voir les deux figures ci-dessous). Ceci équivaut à un déplacement de la direction de l'axe de rotation de la Terre de 50 secondes d'arc par année. Ce mouvement est dû à l'attraction de la Lune et du Soleil sur le bourrelet, ou renflement, équatorial de la Terre.

![img](/assets/images/Module3/lat_long/lat_long.007.jpeg)
{%capture caption %} La précession de la Terre.  {% endcapture %}
{% include figcaption.html caption=caption %}

<p align="center">
  <video width="700" controls>
    <source src="/assets/images/Module3/149_axial_precession.mp4" type="video/mp4">
  </video>
</p>
{%capture caption %} La précession de la Terre. Crédits : NASA/JPL-Caltech  {% endcapture %}
{% include figcaption.html caption=caption %}

À cause de la précession, l'étoile polaire ne sera pas toujours l'étoile qui nous permettra de retrouver le Nord.

<p align="center">
  <img src="/assets/images/Module3/precession-changing-pole-star.png" />
</p>
{%capture caption %} La trajectoire de l'axe du pôle Nord sur la voûte céleste. Crédit : [Explaining Science](https://explainingscience.org/2020/09/25/the-changing-pole-star/).  {% endcapture %}
{% include figcaption.html caption=caption %}

### 3.1.3.B. Un mouvement de nutation  

Ce mouvement correspond à une petite oscillation supplémentaire de l'axe de rotation terrestre par rapport au mouvement général de précession décrit plus haut. Ce mouvement est dû, encore une fois, à l'attraction de la Lune sur le renflement terrestre, et au fait que l'orbite de la Lune soit inclinée de 5$^{\circ}$ par rapport à l'écliptique. Ce mouvement, de nature oscillatoire, a une amplitude de 9 secondes d'arc, et une période de 19 ans (voir la figure ci-dessous).


<p align="center">
  <img src="/assets/images/Module3/500px-Praezession.svg.png" />
</p>
{%capture caption %} La nutation, en rouge, de l'axe de rotation de la Terre. Le mouvement de précession est dessiné en bleu et l'axe de rotation est en vert. Crédit : [Dr. H. Sulzer](https://fr.wikipedia.org/wiki/Nutation#/media/Fichier:Praezession.svg).  {% endcapture %}
{% include figcaption.html caption=caption %}

## 3.1.4 La rotation de la Terre et le mouvement apparent des étoiles
Vous avez peut-être remarqué que les étoiles ont un mouvement apparent sur la sphère céleste. Repérez, à un moment donné de la nuit, la position d'une constellation. Revenez quelques heures plus tard, et cette constellation se sera déplacée dans le ciel. Elle sera peut-être même disparue en dessous de l'horizon. Ce mouvement apparent est dû à la rotation de la Terre. On peut schématiser le mouvement apparent des astres en utilisant le système horizontal décrit précédemment. Plaçons-nous donc à un endroit typique à la surface de la Terre, disons à une latitude géographique de +34$^{\circ}$N.

Comme nous l'avons vu plus haut, la hauteur du pôle Nord céleste sera aussi de +34$^{\circ}$; cette direction est indiquée sur la figure ci-dessous. Puisque la Terre est en rotation autour de l'axe polaire, les étoiles semblent se déplacer, en un jour, sur des grands cercles parallèles à l'équateur céleste, tel qu'indiqué sur la figure. Notez également la position de l'horizon, qui détermine la portion de la trajectoire apparente quotidienne de chaque étoile qui est visible à l'observateur : seule la portion de la trajectoire apparente sur la sphère céleste au-dessus de l'horizon sera visible. La majorité des étoiles se lèvent (à l'est), et se couchent (à l'ouest).

![img](/assets/images/Module3/lat_long/lat_long.008.jpeg)
{%capture caption %} Le mouvement apparent des étoiles sur la voûte céleste.  {% endcapture %}
{% include figcaption.html caption=caption %}

## 3.1.5 La rotation de la Terre et le mouvement apparent du Soleil

La course apparente quotidienne du Soleil, sur la sphère céleste, également due au mouvement de rotation de la Terre, peut aussi être représentée de cette façon, mais avec un détail additionnel important : en raison du mouvement orbital de la Terre autour du Soleil au cours de l'année, la morphologie de la trajectoire apparente quotidienne du Soleil, sur la sphère céleste, dépend de la période de l'année. Nous l'illustrons ci-dessous (figure suivante) pour le premier jour des quatre saisons, pour un observateur situé à une latitude géographique de +30$^{\circ}$ N. Notez deux détails importants : en été, le Soleil monte beaucoup plus haut dans le ciel, et il passe une plus grande fraction de sa trajectoire apparente au-dessus de l'horizon.

Maintenant, plaçons-nous encore une fois à quelques endroits particuliers sur Terre, afin de voir à quoi ressemblent les trajectoires apparentes du Soleil à ces endroits. Nous choisissons, pour ce faire, un point de latitude 66,5$^{\circ}$ N, ainsi que le pôle Nord. Les trajectoires apparentes du Soleil, à une latitude de 66,5$^{\circ}$ N au début de l'été et au début de l'hiver, sont indiquées sur la figure suivante :

C'est le phénomène du Soleil de minuit. Les trajectoires correspondantes du début de l'hiver au cercle polaire et au pôle Nord sont aussi montrées aux figures précédentes. Dans ce cas, à 66,5$^{\circ}$ N, le Soleil ne se lève pas cette journée-là. Au pôle, le Soleil ne se lèvera pas pendant six mois; c'est la nuit polaire. 

## 3.1.6 Le mouvement de révolution et les saisons
## 3.1.7 L'aspect changeant du ciel
