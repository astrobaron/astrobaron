---
layout: default
title: 3.3 La distance et la vitesse des étoiles et des galaxies
parent: Module 3
nav_order: 1\n
---

# {{ page.title }}
{: .no_toc }

{: .text-delta }
- TOC
{:toc}
---
Nous venons de voir comment, à l'aide de la 3e loi de Kepler, nous pouvons mesurer la distance relative des planètes dans le système solaire. Il existe évidemment d'autres techniques, comme l'utilisation du radar, pour obtenir cette information. L'échelle des distances dans le système solaire est un ingrédient essentiel pour interpréter correctement les paramètres physiques intrinsèques (masse, rayon, température, etc.) des planètes, des lunes ou de tout autre objet de notre système, ainsi que leur évolution.

Il en va de même avec les étoiles et les galaxies. Afin de comprendre les propriétés physiques intrinsèques et l'évolution de ces objets, il faut avant tout connaître leur distance et leur mouvement par rapport à la Terre et au Soleil. Les prochaines sections décrivent quelques-unes des méthodes utilisées pour estimer la distance et la vitesse des étoiles et des galaxies par rapport à nous.

## 3.3.1 Parallaxe géocentrique et stellaire
Il est évident que nous ne pouvons pas mesurer les distances astronomiques en déplaçant un étalon de longueur fixe (par exemple 1 mètre) entre la Terre (ou le Soleil) et les astres, comme on le ferait pour mesurer la distance entre les murs de notre salon. Par contre, pour les objets astronomiques les plus rapprochés (la Lune, les planètes, le Soleil et les étoiles de notre voisinage), nous pouvons mesurer directement les distances à l'aide d'une méthode trigonométrique basée sur la technique de l'arpentage, la **méthode de la parallaxe**. Cette méthode combine l'information obtenue de deux points de vue différents pour déduire la distance d'un objet.

Prenons un exemple simple, le fonctionnement de notre cerveau (!). Celui-ci utilise les deux images différentes captées par chacun de nos yeux pour évaluer la distance nous séparant de ce qui nous entoure. La figure suivante montre que :

* l'angle $\theta$ entre les images perçues par l'œil droit et l'œil gauche diminue si la distance entre les yeux et l'objet augmente.

* pour une distance fixe, $\theta$ augmente si la ligne de base (l'écart entre les deux yeux) augmente.

![img](/assets/images/Module3/3.3/3.3.001.jpeg)
{%capture caption %} La mesure des distance nécessite deux yeux. {% endcapture %}
{% include figcaption.html caption=caption %}

On appelle l'angle $\theta$, la **parallaxe**. L'expérience illustrée à la figure ci-dessus nous montre qu'il est plus facile de mesurer la parallaxe si la ligne de base (la distance entre les deux yeux) est plus grande. Si nous appliquons cette méthode à l'astronomie, on constate qu'il existe deux lignes de base naturelles :
* Le diamètre de la Terre ($R_{\oplus}$) – qui permet de mesurer la **parallaxe géocentrique** – fut utilisé initialement pour mesurer les distances d'objets se trouvant à l'intérieur du système solaire. De nos jours, l'utilisation du radar permet d'obtenir les distances des planètes de façon plus précise.

* Le diamètre de l'orbite de la Terre autour du Soleil, c'est-à-dire l'unité astronomique (UA) qui permet de mesurer la **parallaxe héliocentrique** et donc les distances aux étoiles les plus proches.

La figure suivante montre que deux images obtenues simultanément par deux observateurs diamétralement opposés à la surface de la Terre, permet de mesurer la parallaxe géocentrique d'une planète de notre système solaire.

![img](/assets/images/Module3/3.3/3.3.002.jpeg)
{%capture caption %}  La mesure d'une distance par la parallaxe géocentrique. {% endcapture %}
{% include figcaption.html caption=caption %}

Le triangle rectangle formé du rayon terrestre ($R_{\oplus}$), de la distance inconnue (D) et de la parallaxe géocentrique ($P_g$) implique que $tan(P_g) =\frac{R_{\oplus}}{D}$.

On en déduit la distance, puisque $R_{\oplus}$ est connu et que la **parallaxe géocentrique** correspond à la moitié du déplacement angulaire apparent (tel que mesuré des deux points d'observation) de la planète par rapport aux étoiles éloignées.

Lorsque nous désirons évaluer les distances aux étoiles, même celles qui sont les plus proches, le diamètre terrestre ne constitue plus une ligne de base suffisamment grande pour que le déplacement angulaire apparent soit mesurable. Par contre, nous pouvons utiliser le rayon de l'orbite de la Terre autour du Soleil à titre de remplacement. La figure ci-dessous présente la méthode de la parallaxe héliocentrique.

![img](/assets/images/Module3/3.3/3.3.003.jpeg)
{%capture caption %}  La mesure d'une distance par la parallaxe héliocentrique. Adaptée de  [Pline](https://fr.wikipedia.org/wiki/Parallaxe#/media/Fichier:Sch%C3%A9ma-Parallaxe-fr.png) {% endcapture %}
{% include figcaption.html caption=caption %}


La géométrie de cette situation est similaire à celle de la parallaxe géocentrique. Ainsi, on obtient $tan(P)=\frac{d}{D}$, où d est la distance Terre-Soleil.

La parallaxe héliocentrique, notée P ou $P_h$, d'une étoile correspond, cette fois-ci, à la moitié du déplacement angulaire apparent mesuré sur deux clichés, de la même région du ciel, obtenus à six mois d'intervalle. Les distances aux étoiles, même les plus rapprochées de nous, sont tellement grandes que les parallaxes mesurées sont toujours inférieures à une seconde d'arc (1''), ou 1/3600 de degré. On peut donc simplifier la relation ci-dessus, car $tan (P_h) \approx P_h$.

De plus, si on exprime en seconde d'arc, on obtient alors $D(U.A.)=\frac{206265U.A.}{P_h}$, avec $P_h$ exprimé en seconde d'arc.

Donc si la moitié du déplacement angulaire apparent est de 1'', la distance de l'objet est 206 265 unités astronomiques. Cette distance correspond à 3,26 années-lumière. On peut utiliser cette distance comme un autre étalon de distance que nous appellerons le **parsec** (pc). Donc, par définition :

* à une distance de 1 parsec, une étoile aurait une parallaxe de 1'', ou bien, de cette distance, le rayon de l'orbite terrestre soutiendrait un angle de 1''.

* et la distance en parsec s'exprime sous la forme simple $D(pc)=\frac{1}{P_h}$, avec $P_h$ exprimé en seconde d'arc.

Le tableau suivant présente la parallaxe héliocentrique et la distance de quelques étoiles. On connaît aujourd'hui, de cette façon, la distance de plus de 10 000 étoiles à l'intérieur d'un volume de 20 pc de rayon autour du Soleil.

| Nom  |  $P_h$ ('') |  D (pc) | D(A.L.)  |
|:-:|:-:|:-:|:-:|
|  $\alpha$ Cen |  0,753 | 1,33 | 4,3
| Barnard | 0,548 | 1,82 | 6,0
| Wolf 359 | 0,419 | 2,39|7,8|
| BD +36${\circ}$2147 | 0,400 | 2,50 |8,2
| L 726-8 | 	0,385 | 2,60 |8,5|
|Sirius A+B | 0,377 | 2,65 | 8,6 |   

{%capture caption %} La parallaxe et la distance de certaines étoiles proches.  {% endcapture) %}
{% include table_caption.html caption=caption %}

La méthode trigonométrique directe d'évaluation des distances cesse cependant d'être utile lorsque la précision de la mesure devient comparable à l'angle mesuré. Sur Terre, l'erreur minimale de mesure des déplacements angulaires est de ±0,005". On fait cependant mieux avec un satellite en orbite terrestre. Le satellite Hipparcos (soit High Precision Parallax Collecting Satellite) a contribué considérablement à l'amélioration de cette technique : le produit final de cet ambitieux projet astrométrique est un premier catalogue contenant 118 000 étoiles avec des mesures astrométriques précises à 0",001, et un second catalogue, baptisé Tycho, qui contient environ 120 000 étoiles ayant des mesures astrométriques précises à 0,0025''. Plus récemment, le satellite Gaia vient d’effectuer un pas de géant dans ce domaine, en calculant la parallaxe de 1,3 milliards d’objets astronomiques, avec une précision inégalée de l’ordre de 0,000010 ‘’. Malgré cette amélioration, les distances échantillonnées à l'aide de cette technique, soit environ 3200 A.L. (1000 pc), restent minuscules à l'échelle de l'Univers.

<div class="savoir">
  <b>Pour en savoir plus</b>
  <ul>
    <li> La position en 3d de l'amas ouvert des Hyades par <a href="https://sci.esa.int/web/gaia/-/60226-the-hyades-cluster">  Gaia</a></li>.
  </ul>
</div>

## 3.3.2 La bougie standard

La méthode de la parallaxe, que nous venons de décrire, est remarquable de simplicité et de précision. En effet, cette méthode est purement géométrique et ne fait donc pas appel aux propriétés intrinsèques des objets étudiés. La seule contrainte est de pouvoir observer et mesurer un déplacement angulaire apparent. Par contre, comme nous l'avons également vu, à l'heure actuelle, cette contrainte limite la distance maximale de mesure directe à 3200 AL (1000 pc). Pour mesurer des distances plus grandes, nous devons utiliser une méthode indirecte, basée sur une caractéristique propre à l'objet visé.

Une de ces méthodes consiste à comparer la brillance intrinsèque d'une étoile avec sa brillance apparente. Comme on le sait, la brillance (ou l'intensité lumineuse) est inversement proportionnelle au carré de la distance. En d'autres termes, si on double la distance entre nous et une source lumineuse, la brillance apparente de la source diminuera d'un facteur 4. On peut donc relier la distance, $d$ , à laquelle se trouve une étoile de la Terre ou du Soleil à sa brillance observée (apparente), $I$ , et sa brillance réelle (intrinsèque), $I_0$, de la façon suivante : $d=\sqrt(\frac{I_0}{I})$

Évidemment, le problème consiste à connaître la brillance intrinsèque, ou luminosité, d'une étoile avec suffisamment de précision. Il nous faut donc un critère indépendant pour estimer cette luminosité. Certains types d'étoiles nous facilitent la tâche, car elles sont faciles à identifier et leur luminosité est bien standardisée. On les appelle alors des **bougies standards**.

C'est le cas, par exemple, des étoiles pulsantes de type céphéide (voir module 5), dont la période de variation est reliée à la luminosité. Une mesure de la période de pulsation permet donc d'estimer et d'utiliser la relation donnée précédemment pour déterminer $I_0$. Les étoiles de type céphéide permettent d'estimer des distances jusqu'à environ 10-30 millions d'AL, soit jusqu'aux galaxies proches de la Voie Lactée.

Lors des phases évolutives finales, certaines étoiles peuvent aussi servir de bougie standard. Ainsi, comme nous le verrons au module 5, les étoiles qui passent par une phase explosive, appelée supernova de type Ia (SNIa), deviennent soudainement très brillantes pendant quelques semaines. La brillance maximale que ces étoiles atteignent est toujours la même. On peut donc s'en servir pour calibrer leur distance et celle de la galaxie à laquelle elles sont liées. Ce type de bougies standard, très brillantes, nous permet de mesurer des distances allant jusqu'à plusieurs milliards d'AL, c'est-à-dire presque aux confins de l'Univers observable.

## 3.3.3 Mouvements stellaires
Vues de la surface terrestre, les étoiles (comme tous les objets de la voûte céleste) se déplacent régulièrement d'est en ouest. Il s'agit, bien entendu, d'un déplacement apparent causé par la rotation de la Terre (voir plus haut). Si nous faisons abstraction de cet effet, les étoiles semblent toujours être à la même position les unes par rapport aux autres. D'ailleurs, nos ancêtres les appelaient les étoiles fixes. Pourtant, chaque étoile est animée d'une vitesse, souvent rapide, dans une direction particulière. Ce mouvement est imperceptible à l'œil nu, car les distances aux étoiles sont très grandes. Cependant, en comparant des photographies des mêmes régions du ciel, obtenues à plusieurs années d'intervalle, on peut distinguer un petit changement dans les positions relatives des étoiles entre elles.

La figure suivante illustre la géométrie du déplacement d'une étoile par rapport à un observateur. Ce mouvement est représenté par un vecteur (vitesse globale), c'est-à-dire un certain déplacement par unité de temps dans une direction donnée. Il peut être divisé en deux composantes : la vitesse radiale, mesurée le long de la ligne de visée à l'étoile; et la vitesse tangentielle, mesurée perpendiculairement à cette ligne de visée.

![img](/assets/images/Module3/3.3/3.3.004.jpeg)
{%capture caption %}  Le mouvement global d'une étoile et ses deux composantes. {% endcapture %}
{% include figcaption.html caption=caption %}

### 3.3.3.A. Le mouvement propre et la vitesse tangentielle
Le **mouvement propre** ($\mu$) est le déplacement angulaire tangentiel d'une étoile sur la voûte céleste. Il nous apparaît sous la forme d'un changement graduel de la position apparente d'une étoile. Parfois, dans le cas des étoiles proches, il se superpose au mouvement apparent, causé par la parallaxe. Le mouvement propre est obtenu en comparant les positions des étoiles sur des photographies espacées de plusieurs années, et il s'exprime en seconde d'arc par année (''/année). Pour obtenir la vitesse tangentielle d'une étoile à partir du mouvement propre, il faut en plus connaître sa distance. Le tableau ci-dessous présente le mouvement propre, la distance et la vitesse tangentielle correspondante de quelques étoiles proches.

<p align="center">
  <img src="https://web.archive.org/web/20080721013827im_/http://my.hwy.com.au/~sjquirk/images/film/barnard2005.gif" />
</p>
{%capture caption %} Le déplacement de l'étoile de Barnard. Crédit : [Steve Quirk](https://web.archive.org/web/20080721013827/http://my.hwy.com.au/~sjquirk/images/film/barnard.htmll).  {% endcapture %}
{% include figcaption.html caption=caption %}


| Nom  | ("/année) |  D (A.L.) | Vitesse tangentielle (km/sec)  |   
|:-:|:-:|:-:|:-:|
| Barnard  | 10,35  | 5,93  |  90 |
| Kapteyn  |8,89   | 12,75  | 164  |   
| CD-36${\circ}$15693  |  6,90 | 11,67  |  117 |   
|  CD-37${\circ}$15492 |  6,08 | 14,47  | 128  |   
|  61 Cygni |  5,22 | 11,15  |  85 |   
|  BD+36${\circ}$2147 | 4,78  |  8,15 |  57 |   

Remarquez que même si ces vitesses sont grandes, les déplacements associés sont impossibles à déceler à l'œil nu au cours d'une vie humaine. Par contre, sur de grandes périodes de temps, il serait possible de voir un changement. Ainsi, la figure suivante illustre l'aspect de la constellation de la Grande Ourse, il y a 50 000 ans, aujourd'hui et dans 50 000 ans.


![img](/assets/images/Module3/3.3/3.3.005.jpeg)
{%capture caption %}  L'aspect de la constellation de la Grande Ourse au cours du temps. Image réalisée à l'aide de Stellarium. {% endcapture %}
{% include figcaption.html caption=caption %}



### 3.3.3.B. L'effet Doppler et la vitesse radiale

L'autre composante du mouvement d'une étoile, décrit à la figure 32, est la **vitesse radiale** (Vr). Il s'agit de la vitesse à laquelle une étoile se déplace par rapport à un observateur le long de sa ligne de visée. Quoiqu'en apparence plus difficile à mesurer, la vitesse radiale s'obtient très aisément grâce à l'**effet Doppler**.

Cet effet se produit dès qu'une source émettant des ondes se déplace par rapport à un observateur. L'effet Doppler est le changement apparent de la longueur d'onde (ou de la fréquence) d'un signal lorsque la source est en mouvement par rapport au récepteur (l'observateur). La figure suivante présente les trois situations possibles entre une source et un observateur.

![img](/assets/images/Module3/3.3/3.3.006.jpeg)
{%capture caption %}  Le changement apparent de la longueur d'onde en fonction de la direction de déplacement par rapport à un observateur. {% endcapture %}
{% include figcaption.html caption=caption %}
<p align="center">
  <img src="/assets/images/Module3/Doppler_Effect.gif" />
</p>
{%capture caption %} Le changement apparent de longueur d'onde d'une source en mouvement. Crédit : [Doleron](https://commons.wikimedia.org/wiki/File:Doppler_Effect.gif?uselang=fr).  {% endcapture %}
{% include figcaption.html caption=caption %}

L'effet Doppler s'applique aussi bien aux ondes sonores qu'aux ondes électromagnétiques (radio, visible, ultraviolet, etc.). Ainsi, la longueur d'onde d'une onde lumineuse sera plus courte (et sera donc décalée vers le bleu) si la source est en mouvement vers l'observateur, et plus longue (et décalée vers le rouge) si la source s'éloigne. Dans le cas des ondes sonores, on dira plutôt qu'un son est plus aigu ou plus grave dans les deux mêmes circonstances. La différence sera d'autant plus grande que la vitesse, dans un sens ou dans l'autre, est élevée. Nous pouvons exprimer cet effet, de façon analytique, sous la forme $Vr=\frac{c(\lambda-\lambda_0)}{\lambda_0}$.

Dans cette expression, c est la vitesse de la lumière (ou du son dans le cas des ondes sonores), $\lambda_0$ est la longueur d'onde du signal émis, et $\lambda$ est la longueur d'onde du signal reçu et mesuré par l'observateur. Si la source est au repos par rapport à l'observateur, alors $\lambda=\lambda_0$ ; si la source s'approche de l'observateur, alors $\lambda<\lambda_0$ et la vitesse radiale est négative, tandis que si la source s'éloigne de l'observateur $\lambda>\lambda_0$, et la vitesse radiale est positive.

Il peut sembler curieux de parler de longueurs d'onde individuelle et de les comparer entre elles, puisque nous savons très bien que les étoiles émettent leur radiation à un ensemble de longueurs d'onde. Mais comme nous l'avons déjà vu au module 2, il est possible de décomposer et d'isoler de la radiation de n'importe quelle longueur d'onde en provenance d'une source lumineuse, au moyen d'un prisme et de filtres appropriés. Il s'agit alors tout simplement de comparer la longueur d'onde mesurée avec celle que l'on obtient d'une source *comparable et immobile*, située dans un laboratoire, pour obtenir la vitesse radiale de la source en mouvement. L'extrait sonore ci-bas présente l'effet Doppler pour le son.
<p align="center">
  <audio controls="controls">
    <source type="audio/mp3" src="/assets/images/Module3/doppler.mp3"></source>
  </audio>
</p>
{%capture caption %}  L'effet Doppler pour le son. {% endcapture %}
{% include figcaption.html caption=caption %}

## 3.3.4 L'échelle des distances – du système solaire aux galaxies
Comme nous venons de le voir, on utilise le parsec (1 pc = 3,2 années-lumière) pour mesurer la distance des étoiles. Dans le cas de notre galaxie, la Voie Lactée, et des galaxies proches on utilise le kiloparsec (kpc), soit 1000 pc. Dans le cas des objets les plus lointains, les distances sont si grandes que l'on devra maintenant utiliser le **mégaparsec (Mpc)**, soit un million de parsecs ou 1000 kpc. Un mégaparsec est environ 3 x 1019 km ou 30 000 000 000 000 000 000 km !

### 3.3.4.A. La découverte du décalage vers le rouge, le « redshift », des galaxies

Nous avons vu que l'effet Doppler permet de mesurer la vitesse d'approche ou de récession d'un objet par rapport à un observateur immobile. Si une source lumineuse s'approche de l'observateur, le flux de cette source sera perçu à des longueurs d'onde plus courtes. Dans la situation inverse, si la source s'éloigne, le flux semblera décalé vers les longueurs d'onde plus grandes; on parle alors d'un décalage vers le rouge ou d'un  **« redshift »**.

Vers 1914, l'astronome Vesto Slipher (1875-1969) publie les décalages Doppler de 13 des galaxies les plus brillantes. Étrangement, la majorité consiste en des décalages vers le rouge plutôt qu'un mélange à peu près égal de décalages vers le bleu et de décalages vers le rouge. Ce phénomène du **redshift** des galaxies nous indique que la majorité des galaxies s'éloigne de nous. Vers 1920, Edwin **Hubble** (1889-1953) et Milton Humason (1891-1972) obtiennent des observations avec le nouveau télescope réflecteur de 2,5m du Mont Wilson. Ils mesurent les décalages doppler de 45 galaxies. Encore une fois, la majorité de ces objets montre des décalages vers le rouge, confirmant les résultats antérieurs.

En 1928, le physicien H.P. Robertson découvre un autre fait curieux : plus une galaxie est distante (donc plus elle semble petite sur le ciel), plus son décalage vers le rouge est grand. Ce résultat est illustré à la figure ci-dessous. De plus, la relation est linéaire : **le décalage vers le rouge est directement proportionnel à la distance**. Puisque la majorité des galaxies montre des décalages vers le rouge et donc s'éloigne de nous et que, de plus, plus le décalage vers le rouge est grand, plus la galaxie est loin, on en conclut que l'**Univers est en expansion**.

<p align="center">
  <img src="/assets/images/Module3/redshift.jpeg" />
</p>
{%capture caption %} La relation entre le « redshift » et la distance (dimension) des galaxies. Crédit :  Palomar Observatory, California Institute of Technology).  {% endcapture %}
{% include figcaption.html caption=caption %}

### 3.3.4.B. Un Univers en expansion
C'est en 1931, qu'Hubble et Humason publient leur relation entre la vitesse de récession et la distance d'un objet. Cette relation, appelée la loi de Hubble, s'exprime simplement comme $V=H_0 \times d$.

où $H_0$ est la constante de Hubble en km/sec/Mpc, V est la vitesse de récession en km/sec, et d est la distance en Mpc. La détermination la plus récente à partir d'observations d'étoiles céphéïdes (voir le module 5) à l'aide du télescope spatial Hubble indique que vaut environ 72 km/sec/Mpc. Cela signifie qu'une galaxie ayant une vitesse de récession de 720 km/sec est à une distance d'environ ~10 Mpc.

<p align="center">
  <img src="/assets/images/Module3/hubble_law.gif" />
</p>
{%capture caption %} La représentation graphique de la loi de Hubble. Crédit : NASA.  {% endcapture %}
{% include figcaption.html caption=caption %}

Si toutes les galaxies s'éloignent de nous, est-ce que cela signifie que nous sommes au centre de l'Univers? Ce concept signifierait que nous avons bouclé la boucle depuis la révolution copernicienne, qui nous avait déplacés du centre du système solaire pour nous ramener maintenant au centre de l'Univers! La réponse est que nous n'avons pas à être au centre pour voir toutes les galaxies s'éloigner de nous. Un observateur dans une autre galaxie verrait également toutes les galaxies s'éloigner de lui puisque toutes les galaxies s'éloignent de toutes les autres. Nous reviendrons sur ce concept au module 5. À l'aide de la loi de Hubble, on peut désormais mesurer la distance d'objets aux confins de l'Univers.

Afin de bien percevoir la dimension de l'Univers observable, les distances d'objets caractéristiques vous sont données au tableau ci–dessous :

| Objet  | Km  |  A.L. |  Pc |   
|:-:|:-:|:-:|:-:|
| Terre-Lune  | 384 000  | 1,3 sec.-lum.  |   |   
| Soleil-Terre  | 150 000 000  | 8,3 min.-lum.  |   |   
|  Soleil-Jupiter | 800 000 000  |  45 min.-lum. |   |   
| Soleil-Pluton  |  6 000 000 000 | 5,5 heu.-lum.  |   |   
| Centaurus  |   |  4,3 ann.-lum. |  1,3 pc |   
| Centre de la Galaxie  |   | 27 000 ann.-lum.  |  8,5 kpc |   
|  Nuages de Magellan |   |  200 000 ann.-lum. | 60 kpc  |   
|  Andromède |   |  2 200 000 ann.-lum. | 660 kpc  |   
|  Centaurus A |   |  14 000 000 ann.-lum.| 4,4 Mpc  |   
|  Amas de la Vierge |   |  48 000 000 ann.-lum.| 15 Mpc  |   
|  Amas de la Coma |   |  300 000 000 ann.-lum.| 90 Mpc  |   
|  Amas de l'Hydre |   |  2 500 000 000 ann.-lum.| 800 Mpc  |   
|  Quasar |   |  12 000 000 000 ann.-lum.| 4 000 Mpc  |   
{%capture caption %}  Quelques distances de l'Univers observable.  {% endcapture %}
{% include table_caption.html caption=caption %}
