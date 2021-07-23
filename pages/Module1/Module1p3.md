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

### 1.3.1.D. Les sources d'information autres que la lumière.

## 1.3.2 La lumière des étoiles

### 1.3.2.A. La loi de Planck

### 1.3.2.B. L'interaction lumière-matière

### 1.3.2.C. La brillance des objets dans le ciel

### 1.3.2.D. La classification spectrale
