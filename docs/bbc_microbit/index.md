# Programmation BBC micro:bit

## Mise en situation

![bbc-microbit gif](./images/bbc-microbit.gif){ .center}

BBC micro:bit est un mini-ordinateur programmable de poche (une carte à [microcontrôleur](https://fr.wikipedia.org/wiki/Microcontr%C3%B4leur)) conçu pour développer votre créativité avec la technologie.

???- info "Kesako ? ..."
    ![bbc-microbit-revue](./images/bbc-microbit-revue.png){ align=left width=70% }
    
    Ce petit appareil intègre beaucoup de fonctionnalités : il a 25 LED rouges qui peuvent afficher des messages, et deux boutons programmables pouvant être utilisés pour contrôler des jeux, ou, par exemple, faire une pause et sauter des chansons sur une liste de lecture ;

    Le BBC micro:bit peut détecter le mouvement, la température, la  luminosité, et vous dire dans quelle direction vous vous dirigez ;
    
    Il peut aussi utiliser une connexion Bluetooth à faible énergie pour interagir avec d'autres appareils et Internet.

    ![bbc-breadbit](./images/bbc-breadbit.png){ align=right width=70%}
    
    <br>
    Ce petit ordinateur possède la dernière technologie qui équipe les appareils modernes : téléphones mobiles, réfrigérateurs, montres intelligentes, alarmes antivol, robots, etc...

    Ainsi, il s'apparente à ce que l'on nomme l'Internet des objets : Internet of Things, abrégé IoT.

    Grâce à la connexion à l'IoT, nous pouvons interagir avec un large éventail de capteurs à travers le monde entier en temps réel et nous pouvons maintenant prendre des décisions intelligentes en utilisant nos appareils.

    <br>
    
    Un micro:bit est à la fois autonome et extensible. En plus d'utiliser ses LED intégrées, boutons et capteurs, nous pouvons élargir sa gamme de fonctions en l'insérant dans un connecteur comme ci-contre.

    Donc finalement, micro:bit est tout ce que vous pouvez imaginer. Vous pouvez le transformer en votre dispositif de messagerie, console de jeu, vêtement intelligent, alarme antivol, contrôleur de maison intelligente...  
    A peu près tout ce que votre imagination peut créer en utilisant des capteurs supplémentaires, en réalisant un boitier ou un support pour la carte, et en programmant son microcontroleur.


???- info "Historique ..."

    La BBC a initié en 2015 le projet Micro:bit, qui se veut être un nano-ordinateur à carte unique à processeur ARM destiné à l’éducation.  
    L’objectif de cette dernière : fournir à chaque écolier de 12 ans (« year 7 ») un support amusant et facile à utiliser.

    !!! cite ""
        Au début des années 80, le groupe de chaînes publiques au Royaume-Uni, la « British Broadcasting Corporation », dite BBC, lança un appel à projet pour créer un ordinateur éducatif à destination des écoliers et des écoles. Une jeune entreprise de Cambridge « Acorn » (« gland » en anglais) fut retenue pour créer cette plateforme. Le « BBC Micro » était né.

        <figure markdown>
          ![BBC_Micro](https://upload.wikimedia.org/wikipedia/commons/3/32/BBC_Micro_Front_Restored.jpg){ width="50%" .center }
          <figcaption markdown>
          [BBC Micro Model A/B (standard configuration)](https://en.wikipedia.org/wiki/BBC_Micro){target="_blank"}
          </figcaption>
        </figure>
              
        Dans la même période, ici en France, nous avons connu une initiative comparable avec le Plan Informatique pour Tous basé sur des micro-ordinateurs Thomson MO5 et TO7.
        
    !!! cite ""
        Plus récemment, quand les membres fondateurs du Raspberry Pi commencèrent à concrétiser leurs rêves d’un nano-ordinateur éducatif, ils voulurent y inscrire en guise de clin d’œil le label « BBC ». Ce droit ne leur fut pas octroyé ; néanmoins un journaliste high-tech de la célèbre « Corporation » sur son blog et sur la chaîne YouTube leur donna un coup de projecteur qui lancera le mouvement autour du Raspberry Pi.

        <figure markdown>
          ![Raspberry PI 400](https://images.prismic.io/rpf-products/877421eb-1c8f-4698-853e-9bf664e9b061_400%20Desktop%20KIt%20Main.jpg){ width="60%" .center }
          <figcaption markdown>
          [Le Nouveau Raspberry Pi 400 : un mini-ordinateur dans un clavier !](https://www.01net.com/actualites/raspberry-pi-400-le-mini-ordinateur-se-glisse-enfin-dans-un-clavier-2000549.html){target="_blank"}
          </figcaption>
        </figure>
        
        L'idée du Raspberry Pi 400 d'inclure un ordinateur complet dans un clavier s'inspire donc des  machines des années 80 telles que ce [BBC micro](https://fr.wikipedia.org/wiki/BBC_Micro) :

    
    
    L’histoire se répète donc trente ans plus tard, la BBC s’est « remis dans le bain » en lançant un objectif très ambitieux : envisager un « ordinateur de poche programmable permettant aux enfants d’explorer la créativité technologique ».

    ![Enfants et BBC micro:bit](https://cdn.sanity.io/images/ajwvhvgo/production/ff4586ca3cb7ca3296be2065879d6badc0a826a5-2248x1388.png?h=703&q=80&auto=format){ width="60%" .center }

    Elle voulait formuler une réponse à la fracture numérique et aux lacunes perçues des compétences informatiques des citoyens. Dans l’environnement fertile des startups technologiques du Royaume Uni et inspiré par l’énergie des « makers » et « programmeurs » autour des cartes « hackables » comme l’Arduino, le Raspberry Pi, Beaglebone et bien d’autres, la BBC a de nouveau monté une initiative d’éducation numérique dans la continuité du projet « Make It Digital » (créer le numérique). Ils ont su rapidement rassembler une trentaine de partenaires et des industriels.
    
    Aujourd’hui, ces partenaires sont réunis dans la [Fondation Micro:bit](https://microbit.org/about/){target=_blank} et présente [la version 2](https://microbit.org/new-microbit/){target=_blank}...

## Programmation

Il existe différentes façon de programmer la carte BBC micro:bit, ici, nous allons utiliser celles basées sur MicroPython une version allégée de Python créée par Damien George pour la programmation de certains microcontôleurs dont celui du BBC micro:bit.

On peut désormais utiliser le nouvel éditeur micropython officiel [https://python.microbit.org/](https://python.microbit.org/){target=_blank} qui possède un simulateur intégré...

Le principe consiste à :

1. glisser/déposer des bouts de code du menu de gauche dans la zone centrale d'édition ;
2. tester le résultat de ces instructions dans le simulateur ;
3. modifier le code dans l'éditeur pour répondre au besoin ;
4. vérifier le résultat de votre script dans le simulateur ;
5. transférer votre programme dans une carte BBC micro:bit raccordée au PC avec un cable USB ;
6. expérimenter sur le matériel réel ;
7. recommencer jusqu'à validation des exigences du cdcf...

> **Ressource** : [Python Editor : Guide](https://support.microbit.org/support/solutions/articles/19000135210-python-editor-guide#overview){target=_blank}

<figure>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/mREwMW69qKc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>


???- info "Autres solutions de programmation :"

    1. On peut débuter avec l'éditeur en ligne [https://app.edublocks.org/](https://app.edublocks.org/){target=_blank} pour générer un script en python à partir des blocs d'instructions. Le principe consiste à glisser/déposer des blocs d'instructions du menu de gauche dans la zone graphique pour obtenir le code Python correspondant.
    2. pour tester un programme par simulation, on peut copier/coller le code en Python dans le simulateur de [https://create.withcode.uk/](https://create.withcode.uk/){target=_blank} et puis on clique sur le bouton `Run` ou la combinaison de touches `Ctrl+Entrée` pour l'exécuter...
    3. Enfin, pour valider un programme sur le matériel réel :
        - on raccorde une carte BBC micro:bit avec un cable sur un port USB de l'ordinateur. Le PC doit reconnaitre la carte comme un nouveau lecteur nommé : `MICROBIT (E:)` ;
        - on ouvre l'ancien éditeur micropython officiel [https://python.microbit.org/v/2](https://python.microbit.org/v/2){target=_blank} ;
        - on clique sur le bouton `Connect`, et on sélectionne la carte `"BBC micro:bit CMSIS-DAP"` à associer, puis on clique sur le bouton `Connexion` pour établir la communication ;
        - Une fois connecté, on clique sur le bouton `Flash` pour charger le programme qui s'exécutera dès que la LED jaune située à l'arrière de la carte aura fini de clignoter ;
        - Pour revoir le résultat du programme une nouvelle fois, il faut redémarrer le BBC micro:bit en appuyant sur le bouton `RESET` situé à l'arrière de la carte...

    **Autres possibilités** :

    - [L'éditeur Mu](https://codewith.mu/){target=_blank} sur PC ;
    - [microsoft makecode](https://makecode.microbit.org/){target=_blank} ;
    - [vittascience](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience&simu=1){target=_blank} ;


<!-- 
http://2si.si.lycee.ecmorlaix.fr/Robotique/BBCmicrobit.html
 -->

