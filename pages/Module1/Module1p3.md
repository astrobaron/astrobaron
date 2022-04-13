---
layout: default
title: 1.3 Les lois de la physique
parent: Module 1
nav_order: 1\n
---

# {{ page.title }}
{: .no_toc }

{: .text-delta }
- TOC
{:toc}
---

Comme nous l'avons vu au tout début de ce module, l'objectif de l'astronomie et de l'astrophysique est de comprendre l'ensemble des phénomènes du cosmos et d'en donner une interprétation cohérente à l'aide des lois de la physique. La prochaine section propose donc une description de la nature de la matière et de la lumière ainsi que des grands principes physiques utiles à notre compréhension de l'Univers. Certains aspects spécifiques au monde des étoiles et des galaxies, telles les mesures de brillance, de couleur et de composition chimique sont aussi abordés.

## 1.3.1 Atome et spectre électromagnétique

La matière qui nous entoure, sur Terre et dans l'espace, est formée d'un ensemble relativement restreint de structures simples, les atomes. Les atomes sont donc les blocs de construction élémentaires de toute la matière dans l'Univers. Ils sont eux-mêmes formés de trois particules plus simples, les électrons, les protons et les neutrons, dont les caractéristiques sont présentées au tableau ci-dessous. Par souci de complétude, il faut noter que les protons et les neutrons ne sont plus véritablement considérés comme des particules élémentaires. Chacune de ces deux particules est formée, à son tour, de trois quarks plus élémentaires.


| Particule |   Massse (kg)      |  Charge électrique |
|---------- |:----------:|------:|
| Électron  | $9.109 \times 10^{-31}$ | négative |
| Proton    | $1.673 \times 10^{-27}$ | positive |
| neutron   | $1.675 \times 10^{-27}$  | aucune |
{%capture caption %} Propriétés des particules élémentaires.  {% endcapture) %}
{% include table_caption.html caption=caption %}

La figure suivante présente le modèle de Niels Bohr (1885-1962) de la structure d'un atome. Cette représentation, très simplifiée, nous permet de bien comprendre la structure de base d'un atome. Le noyau renferme les protons et les neutrons, et sa taille est de l'ordre de 10-15 m. Les électrons se retrouvent sur des orbitales de formes variées (pas nécessairement circulaires ou sphériques) autour du noyau.


![img](/assets/images/Module1/bohr/bohr.001.jpeg)
{%capture caption %} Le modèle atomique de Bohr. {% endcapture %}
{% include figcaption.html caption=caption %}

Les différentes sortes d'atomes, appelées éléments, sont constituées d'un nombre plus ou moins grand de protons, de neutrons et d'électrons. Le plus simple des éléments est l'hydrogène, dont le noyau est constitué d'un seul proton autour duquel circule un seul électron. Le deuxième élément, l'hélium, est composé de deux protons, deux neutrons et deux électrons. Chaque nouvel élément possède un proton de plus que le précédent. Dans des conditions physiques normales, un atome possède autant d'électrons que de protons, de telle sorte qu'il est électriquement neutre. Dans le noyau, le rôle des neutrons est d'assurer la stabilité mécanique du noyau atomique. Leur nombre dans le noyau varie d'un élément à l'autre et n'est pas nécessairement égal au nombre de protons. Il peut même être différent pour deux noyaux d'un même élément, comme c'est le cas pour l'uranium avec 92 protons et 141, 142, 143 ou 146 neutrons. Ces différents noyaux sont appelés les isotopes d'un élément, l'uranium dans ce cas-ci.

Les propriétés physiques et chimiques des éléments varient d'un élément à l'autre. Néanmoins, il existe des similitudes entre certains éléments, ce qui permet de les regrouper en familles dans ce qu'on appelle le Tableau périodique des éléments, illustré à la figure ci-dessous. Dans ce tableau, les 92 premiers éléments (de l'hydrogène jusqu'à l'uranium) sont appelés les éléments naturels. On dit que ce sont des éléments naturels car leur noyau est suffisamment stable pour que leur durée de vie soit très longue (généralement supérieure à 109 années). Les autres, au-delà de l'uranium, possèdent des noyaux très massifs et instables qui ont tendance à se briser (fissionner) facilement. Ces éléments, dont la durée de vie est généralement courte (souvent à peine quelques secondes), sont créés artificiellement, généralement en laboratoire, et n'existent pas dans la nature. Les structures que l'on observe dans l'Univers sont donc le fruit de combinaisons des 92 éléments naturels que l'on connaît.

![img](/assets/images/Module1/1280px-Mendeleev_Table_5th_II.jpg)
{%capture caption %} Une des première version du tableau périodique de Mendeleïev. {% endcapture %}
{% include figcaption.html caption=caption %}


![img](/assets/images/Module1/20161202092013-tableauperiodiquedeselementsversionsimplifiegif.gif)
{%capture caption %} Le tableau périodique. Crédit : Québec Science.  {% endcapture %}
{% include figcaption.html caption=caption %}

<div class="savoir">
  <b>Pour en savoir plus</b>
  <ul>
    <li><a href="https://periodictable.com/">Le tableau périodique en photo</a></li>
    <li><a href="https://ptable.com/?lang=fr#Propriétés/">Version dynamique du tableau périodique</a></li>
  </ul>
</div>



### 1.3.1.A. La structure de l'atome
L'organisation de la matière, en structures plus ou moins complexes, est rendue possible grâce à l'existence de quatre forces, aussi appelées interactions, fondamentales. L'intensité relative et le comportement de ces quatre interactions sont différents pour chacune d'entre elles. De plus, elles agissent à différentes échelles dans l'Univers, du niveau microscopique au niveau macroscopique.




### 1.3.1.B. Les interactions

**A. L'interaction gravitationnelle**

La plus familière de toutes est l'interaction gravitationnelle. Comme nous l'avons vu, c'est au cours de la deuxième moitié du 17e siècle qu'Isaac Newton énonça ce qui allait devenir la Loi de la gravitation universelle. Pour y arriver, il a inventé à lui seul une branche des mathématiques qui porte aujourd'hui le nom de calcul différentiel et intégral. Son génie fut d'unifier les lois du mouvement planétaire décrites par Kepler avec la loi de la chute des corps sur Terre énoncée par Galilée. Cette loi, nommée **loi de la gravitation universelle**, s'énonce comme suit. Chaque particule de matière dans l'Univers attire toute autre particule avec une force proportionnelle au produit de leurs masses et inversement proportionnelle au carré de la distance qui les sépare.

Cette loi prend la forme analytique suivante : $F_{grav} = - G \frac{m_1 \times m_2}{d^2}$.


où $F_{grav}$ est la grandeur de la force, $m_1$ et $m_2$ sont les masses des deux particules (objets), $d$ est la distance qui les sépare, et $G$ est une constante. Le signe négatif indique qu'il s'agit d'une force attractive.

La force gravitationnelle est donc une force attractive dont l'intensité décroît avec le carré de la distance. Cette interaction, dont l'intensité relative est faible, est responsable des grandes structures comme les planètes, les étoiles, et les galaxies. C'est aussi la force gravitationnelle qui décidera, comme nous le verrons plus tard, du destin ultime de l'Univers.

<div class="attention">
  <b>Attention!</b>
  <ul>
  Il importe ici de faire une brève mise au point concernant le concept de masse et de poids. La masse d'un corps est une mesure de la quantité de matière qu'il contient (un astronaute par exemple). Il s'agit d'une propriété intrinsèque et invariable de ce corps. Le poids, par contre, est une mesure de la force gravitationnelle s'exerçant entre un corps et une planète (la Terre par exemple). C'est une quantité variable. Pour mieux comprendre, imaginez un astronaute faisant un voyage de la Terre à la Lune. Sa masse ne change pas d'un endroit à l'autre, mais son poids sur la Lune est environ six fois moindre que sur la Terre!
  </ul>
</div>


**B. L'interaction électromagnétique**

À une échelle plus réduite on retrouve la signature de l'interaction électromagnétique. La théorie décrivant les interactions électromagnétiques est un autre exemple de simplification dans le domaine de la physique. Elle regroupe dans une description uniforme les phénomènes faisant intervenir les charges électriques, leurs déplacements (les courants), ainsi que le rayonnement électromagnétique (la lumière) et les champs magnétiques qui sont souvent engendrés par ces déplacements. Cette théorie a été élaborée en grande partie par James Clerk Maxwell (au 19e siècle).

Certains aspects de la théorie de l'électromagnétisme s'apparentent un peu à ceux de la théorie de l'interaction gravitationnelle. Ainsi, la force électrique qui s'exerce entre deux charges électriques porte le nom de Loi électrostatique de Coulomb et s'énonce comme suit :

Loi électrostatique de Coulomb : Chaque particule chargée attire toute autre particule chargée avec une force proportionnelle au produit de leurs charges électriques et inversement proportionnelle au carré de la distance qui les sépare.

Sa forme analytique est la suivante : $F_{élec} = K \frac{Q_1 \times Q_2}{d^2}$


où $F_{élec}$ est la grandeur de la force, $Q_1$ et $Q_2$ sont les charges électriques des deux particules, $d$ est la distance qui les sépare, et $K$ est une constante.

Cette force est de nature attractive ou répulsive, dépendant des charges électriques en cause (attractive si les charges sont de signes opposés et répulsive si les charges sont de même signe), et son intensité (relativement plus grande que celle de la force gravitationnelle) décroît elle aussi avec le carré de la distance. Cette interaction gouverne le mouvement des électrons autour du noyau atomique. Elle assure aussi la cohésion des liens entre les atomes à l'intérieur des molécules, des cristaux, des cellules, etc. C'est grâce à la force électromagnétique que la lumière, sous tous ses aspects (radio, visible, rayon-X, etc.) existe. Nous y reviendrons d'ailleurs bientôt.

**C. Les interactions nucléaires**

Finalement, il existe deux autres interactions appelées interaction nucléaire forte et interaction nucléaire faible. Bien que les intensités relatives de ces deux forces soient très grandes si on les compare à celle de la force gravitationnelle, leur existence n'est connue que depuis peu de temps car ces interactions n'agissent qu'à l'intérieur des noyaux atomiques, sur des distances très petites. Ces forces sont responsables de la stabilité des noyaux ainsi que celle des protons et des neutrons. Elles permettent de comprendre les phénomènes de fusion et de fission des noyaux de même que la radioactivité qui en découle. Ces interactions ont joué un rôle primordial dans les premiers instants qui ont suivi la création de l'Univers par le Big Bang. Elles sont aussi importantes pour comprendre correctement les phénomènes de fusion au cœur des étoiles ainsi que les phases évolutives finales de ces dernières.


| Interaction       |  Intensité relative | Messager                    | Masse du messager  | Distance de l'interaction  |
|-------------------|---------------------|-----------------------------|--------------------|---|
| Forte             | $10{38}$            | Gluon (g) entre les quarks  | Non nulle          | Courte ($<10^{-15}$ m)  |
| Électromagnétique | $10{36}$            | Photon (g)                  | Nulle              | Infinie   |
| Faible            | $10{33}$            | Boson (Z, W)                | Non nulle          | Courte ($<10^{-15}$ m)  |
| Gravitation       | $10{0}=1$           | Graviton (?)                | Non nulle          | Infinie  |
{%capture caption %} Récapitulatif des différences entre interactions du point de vue de l'électrodynamique quantique
Interaction.  {% endcapture) %}
{% include table_caption.html caption=caption %}






### 1.3.1.C. Le spectre électromagnétique
Presque toute l'information utilisée pour comprendre la nature et le fonctionnement de l'Univers est recueillie sous forme de rayonnement. C'est la raison pour laquelle les astronomes ont développé toute une panoplie de techniques pour extraire le maximum des signaux (souvent très faibles) qui arrivent aux télescopes. Avant de décrire ces diverses techniques et les instruments associés, il est nécessaire de comprendre ce qu'est la lumière, quelles sont ses propriétés, et comment elle interagit avec la matière.

#### Propriétés

Nous venons de voir que la matière est formée d'atomes qui sont eux-mêmes composés de particules chargées électriquement. Or, le mouvement des charges électriques (en fait l'accélération) engendre ce que l'on appelle de la radiation (ou onde) électromagnétique. Ce que nos yeux perçoivent, et que nous appelons **lumière visible** est constitué d'ondes électromagnétiques et ne représente qu'une petite partie de l'ensemble du rayonnement électromagnétique possible.

Une **onde électromagnétique** est un phénomène ondulatoire dans lequel un champ électrique et un champ magnétique oscillent. Pour créer un champ électrique, il suffit de placer une charge électrique (un électron par exemple) dans l'espace. Si cette charge se déplace, un champ magnétique est aussi créé. Le champ électromagnétique résultant sert alors de « milieu » de propagation aux ondes électromagnétiques.

Comme le montre la figure affichée ci-dessous, les deux champs oscillent à angle droit l'un de l'autre, et la combinaison des deux forme une onde qui se déplace dans une direction perpendiculaire aux deux champs.

![img](/assets/images/Module1/onde_em/onde_em.001.jpeg)
{%capture caption %} Onde électromagnétique. Figure adaptée de ploufandsplash. {% endcapture %}
{% include figcaption.html caption=caption %}

Cette onde peut être caractérisée par la quantité d'énergie qu'elle transporte. L'énergie associée à l'onde est directement proportionnelle à sa fréquence (\nu) ou, de façon équivalente, inversement proportionnelle à sa longueur d'onde ($\lambda$), comme on peut le voir dans l'équation suivante : $E_{photon}=h \nu$= \frac{hc}{\lambda}

où E est l'énergie du photon associé à l'onde, et h et c sont des constantes (la constante de Planck et la vitesse de la lumière respectivement).

Plus la longueur d'onde est grande, plus la quantité d'énergie est faible et vice-versa. On associe généralement des noms aux différents domaines de longueurs d'onde (et donc d'énergie) du spectre électromagnétique.

| Nom de la région   |       Domaine de longueur d'onde       |
|:------------------:|:-------------:|
| Ondes radio     |  10 cm – 100 m   |
| Micro-ondes     |  1 mm – 10 cm    |   
| Infrarouge      |  1 $\mu$m – 1 mm |  
| Visible         |  350 nm - 1 $\mu$m |
| Ultraviolet     |  10 nm – 350 nm|
| Rayons X        | 0,1 nm – 10 nm|
| Rayons $\gamma$ | 0,001 nm – 0,1 nm |
{%capture caption %}Le spectre électromagnétique. {% endcapture) %}
{% include table_caption.html caption=caption %}

![img](/assets/images/Module1/light-spectrum-fr.jpg)
{%capture caption %} Le spectre électromagnétique. Crédit : Scientific Committee on Emerging and Newly Identified Health Risks, Light Sensitivity (2008). {% endcapture %}
{% include figcaption.html caption=caption %}

![img](/assets/images/Module1/Les-differents-domaines-du-spectre-electromagnetique_W640.jpg)
{%capture caption %} Le spectre électromagnétique. Crédit : D. Pellion. {% endcapture %}
{% include figcaption.html caption=caption %}


Notons qu'il ne faut pas confondre le son qui est le résultat de la propagation d'ondes mécaniques (variations de pression de l'air) et les ondes radio qui sont des ondes électromagnétiques.

À l'exception de leur énergie, toutes les ondes électromagnétiques, quel que soit le domaine du spectre, ont les mêmes propriétés :

* Les ondes électromagnétiques ne nécessitent aucun support matériel pour se propager. Elles peuvent donc voyager dans le vide. Ce n'est pas le cas pour les ondes sonores ou les ondes à la surface de l'eau.

* La vitesse de déplacement est constante et la même (la vitesse de la lumière : 299 800 km/s) pour toutes les ondes électromagnétiques.

En général, les astres émettent ou réfléchissent des ondes dans plusieurs domaines du spectre électromagnétique. L'aspect d'un objet peut-être très différent d'un domaine de longueur d'onde à un autre dépendant des phénomènes physiques (et donc des énergies) qui sont à l'œuvre. À titre d'exemple, la figure ci-dessous illustre plusieurs visages différents de notre galaxie - la Voie Lactée - tels qu'ils peuvent être observés dans plusieurs domaines du spectre électromagnétique. Les différences morphologiques peuvent être associées à des structures ou des phénomènes physiques différents de notre galaxie.

![img](/assets/images/Module1/mwmw_8x10.jpg)
{%capture caption %} La Voie Lactée observée à diverses longueurs d'onde. Crédit : NASA Goddard Space Flight Center. {% endcapture %}
{% include figcaption.html caption=caption %}

#### Température et Chaleur

Pour comprendre comment la lumière est produite, il est aussi nécessaire de posséder des outils sur le mouvement et l'énergie des atomes. Une des notions de base est celle de la température.

La **température** est une mesure de **l'énergie cinétique** moyenne du gaz, c'est-à-dire une mesure de l'énergie qui met en mouvement les atomes qui constituent le gaz. Un gaz dont les molécules ou atomes bougent rapidement aura une température plus haute que celle du même gaz dont les particules sont moins rapides.

À ce stade, il convient de ne pas confondre chaleur et température. La **chaleur** mesure l'énergie contenue dans un corps, alors que la température mesure l'intensité des vitesses de mouvements des particules qui forment le corps.

### 1.3.1.D. Les sources d'information autres que la lumière.

* Les rayons cosmiques sont des particules chargées (surtout des noyaux d'atomes d'hydrogène et d'hélium) voyageant presque à la vitesse de la lumière. Lorsqu'ils arrivent au voisinage de la Terre, ils frappent les molécules de la partie supérieure de l'atmosphère et les brisent en un grand nombre de particules subatomiques secondaires, produisant par collisions successives une douche de millions de particules à la surface de la Terre.

  Ils nous renseignent sur les phénomènes énergétiques du cosmos (étoiles à neutrons, supernova, etc.).

<p align="center">
  <img src="/assets/images/Module1/cosmicrays.jpg" />
</p>
{%capture caption %}Représentation artistique de rayons cosmiques. Crédit : A. Chantelauze, S. Staffi, L. Bret. {% endcapture %}
{% include figcaption.html caption=caption %}

* Le vent solaire est un flux constant de noyaux d'atomes (surtout ceux d'hydrogène) et d'électrons en provenance du Soleil. Ces particules possèdent des énergies très inférieures à celles des rayons cosmiques et mettent quelques jours à franchir la distance Terre-Soleil. Au contact de la haute atmosphère terrestre, le vent solaire ionise et excite les molécules, qui par la suite reviennent à leur état initial en émettant de la lumière, causant ainsi le phénomène des aurores boréales.

<p align="center">
  <img src="/assets/images/Module1/solar-wind.jpg" />
</p>
{%capture caption %} Le vent solaire pousse sur le champ magnétique de la Terre. Crédit : NASA. {% endcapture %}
{% include figcaption.html caption=caption %}

* Les neutrinos sont des particules sans charge produites par les réactions nucléaires au centre des étoiles. Ils ont une masse très faible et voyagent presque à la vitesse de la lumière. Ils interagissent très peu avec la matière, ce qui rend leur détection particulièrement ardue. Ils nous informent sur l'activité interne des étoiles, surtout notre Soleil.

<p align="center">
  <img src="/assets/images/Module1/1024px-Sudbury_Neutrino_Observatory.detector_outside.jpg" alt="drawing" width="500"/>
</p>
{%capture caption %} L'Observatoire de neutrinos de Sudbury, détecteur de neutrinos solaires construit sous deux kilomètres de roche dans une mine de nickel active située à 25 kilomètres du centre-ville de Grand Sudbury, en Ontario, au Canada. Crédit : SNOLab. {% endcapture %}
{% include figcaption.html caption=caption %}


* Les ondes gravitationnelles (ou la radiation gravitationnelle) sont une prédiction de la théorie de la relativité générale d'Einstein. D'après cette théorie, toute masse accélérée devrait émettre des ondes gravitationnelles, tout comme une charge électrique accélérée émet des ondes électromagnétiques. Certains phénomènes astronomiques spectaculaires, comme la collision de deux trous noirs, peuvent produire une grande quantité d'ondes gravitationnelles. L’intensité du flux des ondes reçues à la Terre est extrêmement faible et il est nécessaire d’utiliser un détecteur très sophistiqué afin de pouvoir les détecter. C’est en septembre 2015 que les ondes gravitationnelles ont été détectées pour la première fois grâce à LIGO (Laser Interferometer Gravitational-Wave Observatory).

<p align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zLAmF0H-FTM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>


* Les météoroïdes et micrométéoroïdes sont des petites particules de matière (dont la dimension peut aller de quelques mètres jusqu'aux grains de sable) en orbite autour du Soleil. Elles entrent parfois en collision avec les planètes et leurs satellites et tombent, à l'occasion, à leur surface. On peut aussi inclure dans cette rubrique les échantillons de sols lunaire et martien qui ont été rapportés ou retrouvés au sol et analysés. Ces particules donnent un aperçu de la composition chimique initiale du système solaire.

<p align="center">
  <img src="/assets/images/Module1/Namibie_Hoba_Meteorite_05.JPG" />
</p>
{%capture caption %} Lorsqu'un météoroïde tombe sur le sol, on parle alors de météorite. On voit ici la météorite Hoba trouvé en Namibie, qui est la météorite intacte la plus grande découverte à ce jour. Crédit : Patrick Giraud. {% endcapture %}
{% include figcaption.html caption=caption %}

## 1.3.2 La lumière des étoiles

### 1.3.2.A. La loi de Planck
Comme nous venons de le voir, la matière est constituée d'atomes, eux-mêmes formés de particules électriques. Lorsque les atomes sont en mouvement, ils émettent des ondes électromagnétiques (de la lumière visible, des ondes radio, des rayons X, etc.). Les atomes d'un objet sont toujours en mouvement dès que celui-ci est chaud; en fait, c'est seulement à la température du zéro absolu (0 K ou -273 °C) que les atomes n'émettent pas de rayonnement.

L'intensité du rayonnement émis par un objet (chaud) n'est pas la même à toutes les longueurs d'onde. Par exemple, la lumière blanche du Soleil se décompose dans les différentes couleurs de l'arc-en-ciel lorsqu'elle traverse des gouttes de pluie, et l'intensité n'est pas la même pour toutes les couleurs. Il y a des informations cachées dans la lumière émise par un objet, qui peuvent être décodées en décomposant celle-ci avec un prisme (ou un réseau) pour obtenir ce qu'on appelle le spectre lumineux de cet objet.

La morphologie du spectre lumineux d'un objet révèle certaines de ses caractéristiques physiques comme sa température. À titre d'exemple, considérons une étoile, c'est-à-dire un objet dont la structure est simple. Une étoile est essentiellement une boule de gaz, dont le comportement physique est similaire à celui d'un émetteur parfait; l'énergie produite dans les régions centrales est transportée vers la surface et réémise sans perte. Les atomes de la couche de surface d'une étoile, la photosphère, sont chauffés à une température de plusieurs milliers de degrés et émettent des photons dans l'espace. Le changement de l'intensité lumineuse en fonction de la longueur d'onde dépend uniquement de la température de la photosphère. Par exemple, une étoile dont la couche de surface est d'environ 7 000 K émettra peu de rayons X et de rayonnement ultraviolet, davantage de lumière bleue et jaune, et moins de lumière rouge et infrarouge, comme l'illustre la figure suivante :

### 1.3.2.B. L'interaction lumière-matière

La distribution de l'intensité lumineuse d'un objet chauffé peut être décrite par la loi de Planck, telle que vu précédemment. Si la lumière émise par cet objet traverse un nuage de gaz mince, quasi transparent, et plus froid que l'objet en question, avant de nous atteindre, le résultat, sans surprise, n'est plus tout à fait le même. C'est ce qu'illustre la figure suivante :

<p align="center">
  <img src="/assets/images/Module1/spectre_abs.JPG" />
</p>
{%capture caption %} La lumière d'un corps noir traversant un nuage froid est absorbée partiellement à certaines longueurs d'onde. Crédit : ASTROLab {% endcapture %}
{% include figcaption.html caption=caption %}

L'intensité lumineuse en fonction de la longueur d'onde sera semblable à ce que présente la figure ci-dessous :

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_2_b.png" />
</p>
{%capture caption %} Spectre de la lumière d'un corps noir ayant traversé un nuage de gaz froid. {% endcapture %}
{% include figcaption.html caption=caption %}

On remarque que la forme globale, l'enveloppe, correspond encore à celle d'un corps noir à une température donnée. Par contre, à certaines longueurs d'onde, l'intensité est plus faible que celle prévue par la loi de Planck; il manque des photons. Ces déficits portent le nom de raies d'absorption et sont le résultat de l'interaction de la lumière et de la matière dans le nuage de gaz. Pour comprendre ce phénomène, examinons attentivement ce qui se produit lorsque la lumière traverse le nuage de gaz.

Les photons de lumière sont émis par l'objet chauffé; leur nombre en fonction de la longueur d'onde est donné par la loi de Planck. Ces photons tentent de se frayer un chemin à travers le nuage de gaz froid. En cours de route, certains d'entre eux sont absorbés par les atomes du gaz, alors que d'autres traversent sans problème, comme l'illustre la figure suivante :

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_2_c.png" />
</p>
{%capture caption %} La physique des raies d'absorption. {% endcapture %}
{% include figcaption.html caption=caption %}

Pour comprendre ce phénomène, revenons à la description d'un atome, tel que nous l'avons vu au début de la section. Le modèle simple, élaboré par le physicien Niels Bohr, suggère que le niveau d'énergie des orbitales soit quantifié, c'est-à-dire que les électrons d'un atome doivent circuler sur des niveaux fixes, et non n'importe où, entre deux niveaux. Chaque niveau correspond à une certaine énergie des électrons, et ces niveaux diffèrent d'un élément chimique à un autre.

Lorsqu'un photon tente de traverser les atomes du gaz, il peut être absorbé si son énergie est exactement celle qui est nécessaire à un électron d'un atome pour passer d'un niveau inférieur à un niveau supérieur. Les photons dont l'énergie ne correspond à aucune transition traversent sans problème, tandis que les autres sont absorbés et disparaissent du flux total. Ce mécanisme est illustré sur la figure ci-dessous :

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_2_d.png" />
</p>
{%capture caption %} L'absorption d'un photon dont l'énergie correspond à la transition entre les niveaux 2 et 3. {% endcapture %}
{% include figcaption.html caption=caption %}

Il est possible qu'un électron absorbe un photon dont l'énergie lui permette de sauter deux, trois ou davantage de niveaux plutôt qu'un seul. Évidemment, lorsqu'un électron se retrouve sur un niveau supérieur, il pourra redescendre vers un niveau inférieur en émettant un photon d'énergie équivalente. Cette désexcitation est très rapide; elle se produit environ 10-8 secondes après l'absorption initiale. On pourrait croire alors que les photons enlevés du flux seront remplacés quasi immédiatement par des photons de désexcitation, mais il n'en est rien. En fait, l'absorption des photons est spatialement sélective, c'est-à-dire que des photons se dirigeant vers l'observateur sont absorbés (ceux venant de la gauche sur la figure), tandis qu'au moment de la réémission, ils sont envoyés dans toutes les directions possibles. Il y a donc une déplétion nette causant ainsi les raies d'absorption.

Nous avons déjà vu que l'énergie d'un photon est reliée à sa longueur d'onde selon la relation suivante : $E_{photon} = \frac{hc}{\lambda}$.

Donc, un photon absorbé lors d'une transition d'énergie donnée correspond à une raie d'absorption à la longueur d'onde équivalente. Puisque les niveaux d'énergie des orbitales sont caractéristiques d'un élément chimique donné, les raies d'absorption observées représentent la signature de cet élément dans le spectre lumineux du gaz.

La figure suivante et l'applet ci-dessous présentent les niveaux d'énergie de l'atome d'hydrogène ainsi que la longueur d'onde associée à chaque transition. Les transitions qui amènent un électron du niveau fondamental (n=1) vers les niveaux supérieurs requièrent plus d'énergie et absorbent des photons ultraviolets. Celles qui partent du niveau n=2 demandent moins d'énergie et les raies d'absorption se produisent dans le domaine visible. Finalement, les transitions à partir des niveaux n=3, 4, 5,... exigent peu d'énergie et absorbent des photons infrarouges ou de longueur d'onde plus grande.

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_2_e.png" />
</p>
{%capture caption %} L'absorption d'un photon dont l'énergie correspond à la transition entre les niveaux 2 et 3. {% endcapture %}
{% include figcaption.html caption=caption %}

La situation se complique un peu avec l'hélium puisqu'il y a deux électrons en jeu. Chacun des électrons peut absorber un photon et se retrouver à un niveau supérieur. Il y a plus de transitions possibles et donc plus de raies d'absorption dans le spectre de l'hélium. Parfois, un des deux électrons est arraché à l'atome d'hélium. On parle alors d'un atome d'hélium ionisé. Il ne reste plus qu'un électron pour absorber des photons.

On pourrait produire une liste similaire pour les autres éléments chimiques du Tableau périodique présenté plus haut. Plus un atome possède d'électrons, plus il y a de transitions possibles et donc plus il y a de raies d'absorption potentiellement observables dans le spectre.

Comme nous le verrons dans les prochains modules, les raies d'absorption constituent un puissant outil pour l'étude des propriétés intrinsèques des étoiles et des planètes. Elles donnent des informations sur la température, la pression et la composition chimique du gaz à la surface de ces objets.

<div class="savoir">
  <b>Pour en savoir plus</b>
  <ul>
    <li><a href="http://www.kcvs.ca/details.html?key=atomicTransition/">Modular Approach to Physics</a></li>
  </ul>
</div>

### 1.3.2.C. La brillance des objets dans le ciel

#### La magnitude apparente

Un simple coup d'œil à la voûte étoilée nous permet de constater que les étoiles n'ont pas toutes la même brillance apparente. Les astronomes classent les étoiles en fonction de leur brillance en utilisant un système très ancien qu'on appelle l'**échelle des magnitudes**.

L'astronome grec **Hipparque** (190-120 av. J.-C.) est l'un des premiers à répertorier et classer les étoiles selon leur brillance apparente et leur couleur. Pour ce faire, il utilise un système constitué de six catégories différentes. Les étoiles les plus brillantes sont classées dans un premier groupe, les étoiles de première magnitude. Les étoiles un peu moins brillantes se retrouvent dans un deuxième groupe, les étoiles de deuxième magnitude, et ainsi de suite jusqu'aux étoiles à peine visibles à l'œil nu, les étoiles de sixième magnitude. On remarque que, sur cette échelle, plus la magnitude est grande, moins une étoile est brillante. Puisque ce système classe la brillance des étoiles telle que perçue par un observateur à la surface de la Terre, on parle donc de **magnitude apparente**. L'utilisation des télescopes et des récepteurs modernes pour capter la lumière nous a révélé deux caractéristiques importantes de ce système. Le premier est que l'intervalle de cinq magnitudes (un à six), dans la classification d'Hipparque, correspond presque à un facteur 100 en énergie reçue par unité de temps et unité de surface en provenance des étoiles : ainsi une étoile de première magnitude nous apparaît environ 100 fois plus brillante qu'une étoile de sixième magnitude. Deuxièmement, la réponse physiologique de l'œil humain est telle qu'une différence d'une magnitude représente un rapport d'environ 2,5 dans le flux perçu ; on dit que la réponse de l'œil est **logarithmique**. Donc, une étoile de deuxième magnitude est approximativement 2,5 fois moins brillante qu'une étoile de première magnitude, une étoile de troisième magnitude est approximativement 2,5 fois moins brillante qu'une étoile de deuxième magnitude, et ainsi de suite. On constate d'ailleurs qu'une étoile de sixième magnitude est 2,5 x 2,5 x 2,5 x 2,5 x 2,5 = $(2.5)^5 \approx 100 $ moins brillante qu'une étoile de première magnitude.

Les astronomes ont choisi, pour des raisons historiques, de conserver le système d'Hipparque. Dans la version moderne de l'échelle des magnitudes, une différence de 5 magnitudes est **exactement** égale à un rapport de 100 de la brillance apparente. Donc, une différence d'une magnitude correspond à un facteur 2,512 du flux. La relation entre la magnitude apparente (m) et le flux (I) d'une étoile prend la forme analytique suivante : $ m = -2.5 \log_{10} I $

ou bien, dans le cas de la différence de magnitude apparente entre deux étoiles : $ m_2-m_2=-2.5 \log_{10}\left(\frac{I_2}{I_1}\right) $.

Le signe négatif indique que la magnitude d'une étoile brillante est plus petite que celle d'une étoile plus faible. Sur l'échelle contemporaine, on retrouve aussi des objets en apparence très brillants, tels que certaines planètes, la Lune et le Soleil, dont la magnitude apparente est inférieure à un, ainsi que des étoiles plus faibles, visibles seulement à l'aide d'un télescope, et dont les magnitudes apparentes sont supérieures à six. Évidemment, les magnitudes ne sont pas non plus limitées aux seuls nombres entiers. La figure suivante présente d'ailleurs un aperçu de l'échelle des magnitudes apparentes.



<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_3_a.png" />
</p>
{%capture caption %}L'échelle des magnitudes apparentes. {% endcapture %}
{% include figcaption.html caption=caption %}

#### La magnitude apparente

Les étoiles sur la voûte céleste sont toutes situées à des distances différentes d'un observateur sur Terre. Ainsi, si nous comparons les magnitudes apparentes de deux étoiles, il est difficile de savoir laquelle est intrinsèquement plus lumineuse, car elles sont très probablement à des distances différentes de nous. Pour pouvoir comparer leur luminosité, il faudrait qu'elles soient toutes les deux à la même distance de la Terre. Il est possible de faire cette comparaison si nous connaissons la distance de chacune des étoiles et que nous apportons une correction à leur magnitude apparente. Cette correction est facile à calculer, car le flux d'une source lumineuse diminue avec le carré de la distance (i.e. une source deux fois plus loin est quatre fois moins lumineuse).

La magnitude apparente (m) d'une étoile correspond à la brillance de cette étoile située à sa vraie distance (d) d'un observateur; la **magnitude absolue** (M) correspond à la brillance qu'elle aurait si elle était située à une distance standard de 32,6 AL de l'observateur. La relation entre la magnitude apparente et la magnitude absolue d'une étoile est donc $ m - M =  -2.5 \log_{10}\left(\frac{d}{32.6}\right) $.

On appelle la quantité **m-M le module de distance**. La magnitude apparente est facile à déterminer et, si on connaît la distance d'une étoile, on peut alors calculer sa magnitude absolue. Inversement, si on connaît la magnitude absolue d'une étoile, on peut trouver à quelle distance elle se trouve de nous.

On utilise la magnitude absolue pour comparer la luminosité réelle des étoiles entre elles. Il s'agit d'une propriété intrinsèque des étoiles. La figure suivante présente une échelle des magnitudes absolues sur laquelle on retrouve des étoiles connues. Remarquez que le Soleil n'est plus qu'une étoile très banale sur cette échelle; il ne nous apparaît très brillant que parce qu'il est près de nous.

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_3_b.png" />
</p>
{%capture caption %}L'échelle des magnitudes absolues. {% endcapture %}
{% include figcaption.html caption=caption %}

### 1.3.2.D. La classification spectrale
#### La couleur des étoiles
Les magnitudes dont nous avons discuté jusqu'à maintenant sont des quantités mesurées par l'œil humain : ce sont des magnitudes visuelles. Dans le passé, on a également beaucoup utilisé les plaques photographiques comme récepteur : le noircissement de l'image d'une étoile sur la plaque est alors une mesure quantitative de l'intensité lumineuse incidente. On parle, dans ce cas, de magnitudes photographiques. Ces deux quantités ne sont pas identiques, puisque la sensibilité de l'œil diffère de celle d'une plaque photographique : la rétine de l'œil est plus sensible à la lumière de couleur jaune, et moins sensible aux couleurs rouge et bleue comme on peut le voir à la figure suivante. D'autre part, la sensibilité d'une plaque photographique dépend du type d'émulsion; certaines ne sont sensibles qu'à la lumière bleue, tandis que d'autres ne sont sensibles qu'au rayonnement infrarouge ou X.

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_4_a.png" />
</p>
{%capture caption %}L'échelle des magnitudes absolues. {% endcapture %}
{% include figcaption.html caption=caption %}

Outre les différences de brillances apparentes des étoiles sur la voûte céleste, un autre aspect nous frappe lorsqu'on regarde le ciel: les étoiles sont de couleurs différentes. En fait les étoiles émettent de la lumière dans toutes les couleurs mais avec des intensités différentes. Certaines émettent peu de lumière bleue et jaune mais beaucoup de lumière rouge, elles apparaissent alors rouges, d'autres émettent plus de bleu et paraissent de couleur blanche-bleutée.

De façon plus générale, comme nous l'avons vu précédemment, tout objet chaud émet de l'énergie dans tous les domaines du spectre électromagnétique, des ondes radios jusqu'au rayonnement   . Il est donc plus commode et plus exact de mesurer les magnitudes des étoiles dans différentes bandes de longueur d'ondes (couleurs), afin d'obtenir une idée plus exacte de la quantité d'énergie qu'elles émettent.

Un système très utile consiste à utiliser un ensemble de filtres de couleurs différentes. Par exemple, prenons trois filtres U, B, et V, connus aussi sous le nom de filtres de Johnson, que l'on place alternativement devant un détecteur photoélectrique numérique (par exemple une caméra CCD). Les filtres couvrent le domaine ultraviolet (U), le domaine bleu (B) et le domaine jaune-visuel (V) de la partie visible du spectre électromagnétique. La figure suivante présente la bande passante des trois filtres en fonction de la longueur d'onde.

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_4_b.png" />
</p>
{%capture caption %}La bande passante des filtres U, B, V. {% endcapture %}
{% include figcaption.html caption=caption %}

Ce système, plus précis que l'œil ou que la plaque photographique, permet de mesurer la magnitude photoélectrique. Évidemment, il existe des systèmes de magnitude photoélectrique à plus de trois couleurs. Grâce à un système de filtres colorés, il devient possible de quantifier la couleur d'une étoile. Ainsi, en poursuivant notre exemple à trois filtres, les différences de magnitudes U-B, U-V ou B-V sont appelées indices de couleur et mesurent la couleur d'une étoile. Une étoile bleue aura un indice B-V négatif puisqu'elle paraîtra plus brillante dans le filtre bleu (B) que dans le filtre jaune (V) (n'oubliez pas que plus un objet est brillant, plus sa magnitude est petite). À l'opposé, l'indice de couleur B-V d'une étoile rouge sera positif, car celle-ci sera plus brillante dans le filtre jaune que dans le filtre bleu.

Il est important de rappeler que les magnitudes U, B et V sont des magnitudes apparentes et sont toutes trois affectées également par la distance. Par contre, les différences U-B, U-V et B-V sont indépendantes de la distance à laquelle se trouve une étoile et mesurent donc les propriétés intrinsèques de cette étoile. Les indices de couleur constituent une façon de mesurer les conditions physiques qui règnent à la surface d'une étoile.
<div class="exemple">
  <b>Exemple</b>
  <ul>
  <p align="center">
    <img src="/assets/images/Module1/exemple_soleil_teff/exemple_soleil_teff.001.jpeg" />
  </p>
  {%capture caption %}Corrélation entre la température de surface d'une étoile et sa couleur B-V. La température de surface (ou effective) du Soleil est de 5 778 K.  {% endcapture %}
  {% include figcaption.html caption=caption %}
</ul>
</div>

Il est donc facile d'estimer la température de surface d'une étoile, en mesurant simplement sa magnitude apparente, en utilisant deux filtres colorés, et en utilisant la relation entre l'indice de couleur B-V et la température.

#### La classification spectrale
Depuis les débuts de la spectroscopie, au milieu du 19e siècle, les astronomes ont obtenu plusieurs centaines de milliers de spectres stellaires. Chacun présente une signature différente des autres! Par contre, malgré les différences que révèlent les spectres de deux étoiles quelconques, on remarque une certaine unité. En fait, puisqu'on ne connaissait pas l'origine des raies d'absorption, à l'époque, un travail colossal de classement a été effectué afin de réussir à classer la plupart des étoiles en séquences parmi lesquelles l'apparence des spectres change de façon continue. Annie Jump Canon (1863-1941), Williamina Fleming (1857-1911), Antonia Maury (1866-1952) et Henrietta Swan Leavit (1868-1921), toutes astronomes à l’observatoire de l’université Havard, ont classé des milliers de spectres et ont établi les fondations de la classification spectrale des étoiles, basée sur l'intensité des raies observées.


<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_4_d_1.jpg" />
</p>
{%capture caption %}Spectres des raies d'absorption de différentes étoiles. Crédit : National Optical Astronomy Observatory. {% endcapture %}
{% include figcaption.html caption=caption %}

Nous savons aujourd'hui que l'**intensité** des raies dans le spectre d'une étoile dépend particulièrement de la température de surface. Si celle-ci est trop basse, il y aura peu de photons suffisamment énergétiques pour produire des transitions électroniques. Si la température est très élevée, les électrons d'un atome seront tous dans les niveaux supérieurs ou encore seront arrachés de l'atome (l'atome sera ionisé), le nombre de transitions sera restreint. Dans les deux cas, l'intensité des raies d'absorption sera faible.

La **largeur** des raies dépend surtout de la pression qui règne dans l'atmosphère d'une étoile. Si la pression est forte ou, en d'autres termes, si la densité des atomes est grande, les raies seront élargies par les collisions des atomes entre eux. Dans le cas contraire, si la pression est basse, les raies seront étroites.

Finalement, l'intensité des raies d'absorption est reliée à la composition chimique superficielle de l'étoile. La présence de raies d'un élément chimique donné représente une mesure de son abondance dans l'atmosphère. Il est important de noter que l'absence de raies d'absorption d'un élément ne signifie pas nécessairement que ce dernier soit absent de l'atmosphère d'une étoile; il est possible que les deux autres facteurs, la température et la pression, ne permettent pas de transitions électroniques qui le rendent observable.

En résumé, les spectres des étoiles sont le résultat de la combinaison de **trois conditions physiques** caractérisant leur surface : **la température**, **la pression** et la **composition chimique superficielle**. La classification spectrale nous permet de retrouver ces facteurs physiques au moyen de **trois paramètres empiriques** : **le type spectral**, **la classe de luminosité** et **la population stellaire**.

#### Le type spectral

Le premier paramètre observationnel, le **type spectral**, est principalement une mesure de la température superficielle d'une étoile. Il est basé sur la comparaison de l'intensité relative des raies spectrales d'un ou de plusieurs éléments chimiques donnés. Historiquement, les spectres stellaires furent classés en utilisant une notation alphabétique. Cette notation a été reprise et simplifiée : on identifie maintenant sept types spectraux différents représentés par les lettres **O, B, A, F, G, K** et **M** (on peut utiliser la phrase mnémotechnique suivante pour retenir l'ordre : Oh Be a fine Girl (ou Guy) Kiss Me!). Les étoiles de type O sont les plus chaudes et celles de type M les plus froides. La figure suivante présente un exemple de chacun des types de la séquence.

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_4_e_1.png" />
</p>
{%capture caption %}Spectres des raies d'absorption de différentes étoiles. Crédit : National Optical Astronomy Observatory. {% endcapture %}
{% include figcaption.html caption=caption %}


On remarque que l'intensité des raies varie de façon continue d'une classe spectrale à l'autre. Les raies du spectre de type O sont très faibles; on identifie les raies d'hydrogène (H) et d'hélium ionisé (He II). Dans le spectre de type B, les raies sont plus fortes; il n'y a plus d'hélium ionisé, mais plutôt des raies d'hélium neutre (He I). Les spectres de type A et F montrent des raies d'hydrogène très fortes, alors que les raies d'hélium ont disparu. On voit également apparaître des raies d'éléments chimiques plus complexes tels le sodium (Na), le calcium (Ca), le magnésium (Mg) et le fer (Fe) dans les spectres de type G et K, tandis que les raies d'hydrogène deviennent plus faibles. Finalement, le spectre de type M correspond à une température si froide que les raies d'absorption des éléments individuels sont graduellement remplacées par de larges bandes d'absorption indiquant la présence de molécules comme l'oxyde de titanium (TiO) dans l'atmosphère de l'étoile.

On subdivise chaque type spectral en sous-classes, identifiées par un chiffre entier de 0 à 9, pour rendre la séquence plus continue. Nous aurons donc, par exemple, la séquence ... F8 - F9 - G0 - G1 - G2 ... qui débute à O2-O3, pour les plus chaudes et se terminent à M9, pour les plus froides. Sur cette échelle, le Soleil est de type G2.

Les intensités relatives des raies spectrales sont des mesures de la température. Cette échelle de température correspond approximativement à l'échelle de température des couleurs. Il y a donc une bonne corrélation entre le type spectral et l'indice de couleur B-V.

## La classe de luminosité

En comparant entre eux les spectres d'étoiles de même type, on s'est aperçu que l'intensité absolue de toutes les raies du spectre pouvait varier d'une étoile à l'autre. Dans certains cas, les raies d'absorption d'une étoile étaient toutes plus étroites que celles d'une autre. De plus, les étoiles dont les raies étaient plus étroites étaient aussi plus lumineuses. En principe, puisque les types spectraux étaient identiques, la température devait être la même. La luminosité totale d'une étoile dépend à la fois de sa température de surface et de son rayon. Si deux étoiles ont des surfaces à la même température, mais qu'une des deux est plus lumineuse que l'autre, alors il faut que son rayon soit plus grand.

Le gaz d'une étoile plus volumineuse est soumis à une pression plus faible, car sa densité est moins grande. Physiquement, ceci se traduit par des raies d'absorption plus étroites. L'intensité absolue des raies spectrales est donc une mesure de la pression gazeuse à la surface d'une étoile et, par le fait même, représente une mesure de son rayon. La largeur des raies définit donc un deuxième paramètre de la classification spectrale, la **classe de luminosité**. Les astronomes W. Morgan (1906-1994) et P. Keenan (1908-2000) ont identifié huit classes de luminosité qui sont présentées au tableau suivant :

| Classe  |  Identification    |
|:------------------:|:-------------:|
| Ia      |  Supergéante   |
| Ib      |  Supergéante    |   
| II      |  Géante brillante |  
| III     |  Géante |
| IV      |  Sous-géante|
| V       |  Séquence principale (naine)|
| VI      | Sous-naine |
| VII     | Naine blanche |
{%capture caption %} Les classes de luminosité. {% endcapture) %}
{% include table_caption.html caption=caption %}

Les deux spectres de type A3 de la figure ci-dessous illustrent l'effet de la taille d'une étoile sur l'intensité des raies spectrales. On voit nettement l'élargissement causé par la pression plus grande dans une étoile de la séquence principale (classe V), par rapport à une étoile supergéante (classe I). Notre Soleil est une étoile de classe V, et fait donc partie de la séquence principale.

<p align="center">
  <img src="/assets/images/Module1/image_1_3_2_4_f_1.png" />
</p>
{%capture caption %} Comparaison entre les spectres d'une étoile supergéante et d'une étoile de la séquence principale. {% endcapture %}
{% include figcaption.html caption=caption %}

#### Les populations stellaires

Le troisième facteur qui détermine l'intensité des raies d'un élément chimique donné est l'abondance de cet élément dans l'atmosphère de l'étoile. Cet effet est cependant difficile à mesurer, car on doit d'abord éliminer l'influence de la température et de la pression. Le troisième paramètre d'observation de la classification spectrale doit être relié à la composition chimique superficielle. L'analyse spectrale détaillée montre que la très grande majorité des étoiles se divise en deux groupes différents de compositions chimiques, **deux populations stellaires**.

La composition chimique est représentée grossièrement par les trois quantités suivantes :

X - la fraction de masse dans l'atmosphère sous forme d'hydrogène.

Y - la fraction de masse dans l'atmosphère sous forme d'hélium.

Z - la fraction de masse dans l'atmosphère sous forme d'**éléments lourds**.

<div class="attention">
  <b>Attention!</b>
  <ul>
  le terme « élément lourd », tout comme le terme « métal », qui est aussi occasionnellement utilisé, réfère - dans ce contexte et en général en astronomie - à tous les éléments chimiques, plus complexes et lourds que l'hydrogène et l'hélium
  </ul>
</div>

Puisqu'il s'agit de trois fractions, par définition, X + Y + Z = 1. On distingue deux types de populations stellaires, qui diffèrent par leur valeur de Z : les **étoiles de Population I sont dites riches en éléments lourds**, tandis que les **étoiles de Population II sont pauvres en ces éléments**. Le tableau suivant présente les valeurs approximatives de l'abondance d'hydrogène, d'hélium et d'éléments lourds pour les deux populations.


| Population  |  X    |  Y    |  Z    |
|:-----------:|:-----:|:-----:|:-----:|
| I           |  0.7  | 0.28  | 0.02  |
| II          |  0.719| 0.28  | 0.001  |
{%capture caption %} L'abondance des éléments chimiques des populations stellaire. {% endcapture) %}
{% include table_caption.html caption=caption %}
