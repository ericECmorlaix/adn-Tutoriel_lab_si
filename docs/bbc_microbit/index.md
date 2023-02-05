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

Il existe différentes façon de programmer la carte BBC micro:bit, au lycée, nous allons privilégier celle basée sur [MicroPython](https://github.com/micropython){target=_blank} une version allégée de Python créée par [Damien George](https://github.com/dpgeorge){target=_blank} pour la programmation de certains microcontôleurs dont celui du BBC micro:bit.

> Le [code source du compilateur MicroPython pour BBC micro:bit](https://github.com/bbcmicrobit/micropython){target=_blank} a été réalisé par [des personnes bénévoles](https://github.com/bbcmicrobit/micropython/graphs/contributors){target=_blank} du monde entier, sous la direction de [Damien George](https://github.com/dpgeorge){target=_blank}, [Nicholas Tollervey](https://github.com/ntoll){target=_blank} et [Carlos Pereira Atencio](https://github.com/microbit-carlos){target=_blank}...

**On peut désormais utiliser le nouvel éditeur micropython officiel [https://python.microbit.org/](https://python.microbit.org/){target=_blank} qui possède un simulateur intégré...**

### Le processus consiste à :

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

    ### Autre processus :

    1. On peut débuter avec l'éditeur en ligne [https://app.edublocks.org/](https://app.edublocks.org/){target=_blank} pour générer un script en python à partir des blocs d'instructions. Le principe consiste à glisser/déposer des blocs d'instructions du menu de gauche dans la zone graphique pour obtenir le code Python correspondant.
    2. pour tester un programme par simulation, on peut copier/coller le code en Python dans le simulateur de [https://create.withcode.uk/](https://create.withcode.uk/){target=_blank} et puis on clique sur le bouton `Run` ou la combinaison de touches `Ctrl+Entrée` pour l'exécuter...
    3. Enfin, pour valider un programme sur le matériel réel :
        - on raccorde une carte BBC micro:bit avec un cable sur un port USB de l'ordinateur. Le PC doit reconnaitre la carte comme un nouveau lecteur nommé : `MICROBIT (E:)` ;
        - on ouvre l'ancien éditeur micropython officiel [https://python.microbit.org/v/2](https://python.microbit.org/v/2){target=_blank} ;
        - on clique sur le bouton `Connect`, et on sélectionne la carte `"BBC micro:bit CMSIS-DAP"` à associer, puis on clique sur le bouton `Connexion` pour établir la communication ;
        - Une fois connecté, on clique sur le bouton `Flash` pour charger le programme qui s'exécutera dès que la LED jaune située à l'arrière de la carte aura fini de clignoter ;
        - Pour revoir le résultat du programme une nouvelle fois, il faut redémarrer le BBC micro:bit en appuyant sur le bouton `RESET` situé à l'arrière de la carte...

    ### [L'éditeur Mu](https://codewith.mu/){target=_blank} sur PC

    A partir de Cortana, rechercher et lancer l'application de bureau `Mu`, au démarage choisir le mode `BBC micro:bit`

    Par rapport à l'éditeur en ligne, cette application offre des fonctionnalités supplémentaires très intéressantes accessibles par ces quatres boutons :

    <img src="https://codewith.mu/img/en/tutorials/microbit_buttons.png" alt="Boutons de Mu pour micro:bit" width=22%>

    **Remarque** : ces boutons ne fonctionnent que s'il y a une carte BBC micro:bit connectée par un câble USB au PC.

    Ces fonctions sont exposées dans ce rapide tutoriel : https://codewith.mu/en/tutorials/1.0/microbit

    Cliquer sur le bouton “Flash” permet en quelques secondes de téléverser votre code dans la mémoire flash du µC du BBC micro:bit en effaçant et remplaçant le programme précédent. En cas d'erreur dans votre code un message défilera sur la matrice à LED.

    <img src="https://codewith.mu/img/en/tutorials/microbit_flash.gif" alt="Boutons de Mu pour micro:bit" width=88%>

    Lorsqu'un programme MicroPython est téléversé dans un BBC micro:bit, il dispose d’un répertoire permettant de stocker des fichiers. Le bouton «Fichiers» de Mu facilite l’accès, la mise en place, la récupération et la suppression de fichiers sur votre appareil.

    Comme indiqué ci-dessous, cliquer sur «Fichiers» ouvre deux panneaux entre l’éditeur de texte et le pied de page de Mu. Le volet de gauche répertorie tous les fichiers du dossier BBC micro:bit, le volet de droite répertorie tous les fichiers de votre répertoire `mu_code` sur votre ordinateur. Faites glisser les fichiers de l'un à l'autre pour les copier. Pour supprimer un fichier sur le BBC micro:bit, cliquez dessus avec le bouton droit de la souris et sélectionnez «Supprimer».

    <img src="https://codewith.mu/img/en/tutorials/microbit_files.gif" alt="Boutons de Mu pour micro:bit" width=88%>

    **Remarque** : cette fonction n'est disponible que si vous avez préalablement chargé un fichier en MicroPython sur la carte.

    Le bouton «REPL» crée un nouveau volet entre l’éditeur de texte et le pied de page de Mu, qui se connecte à l'interpréteur MicroPython du périphérique BBC micro:bit. Le terme “REPL” est un acronyme et signifie “Lire, Évaluer, Imprimer, Boucler”, (Read-Evaluate-Print-Loop), ce qui décrit succinctement ce que le panneau fait pour vous. Il lit les instructions de Python que vous tapez, évalue leur signification, affiche le résultat obtenu, puis effectue une boucle pour attendre votre prochaine instruction Python.

    <img src="https://codewith.mu/img/en/tutorials/microbit_repl.gif" alt="Boutons de Mu pour micro:bit" width=88%>

    Comme vous pouvez le constater dans l'exemple ci-dessus, utiliser le REPL de MicroPython revient à avoir une conversation avec le BBC micro:bit en Python. Tout ce que vous pouvez faire dans un script Python classique, vous pouvez le faire dans le REPL. C’est une façon amusante d’explorer de façon ludique les capacités de MicroPython sur le BBC micro:bit.

    **C'est donc le moment d'essayer des choses... Par exemple, commencez par taper `help()`dans le REPL de l'éditeur Mu et laissez-vous guider par les propositions suggérées là... Saurez-vous y découvrir le Zen de MicroPython ?**


    Enfin, le bouton "Plot" ouvre le traceur de Mu. Si votre BBC micro:bit produit des tuples de nombres via la connexion série, le traceur les affiche sous forme de graphique. Ceci est extrêmement utile pour visualiser les données que vous pourriez mesurer via le BBC micro:bit. Pour plus d’informations à ce sujet, lisez [le tutoriel sur le traceur de Mu](https://codewith.mu/en/tutorials/1.0/plotter).

    <img src="https://codewith.mu/img/en/tutorials/microbit_plotter.gif" alt="Boutons de Mu pour micro:bit" width=88%>


    Le site de l'éditeur Mu : http://codewith.mu et son dépot GitHub : https://github.com/mu-editor/mu

    ### Communication avec le REPL, l'interpréteur Python embarqué d'un BBC micro:bit :

    On peut faire fonctionner la carte BBC micro:bit directement depuis son interpréteur Python via une communication série depuis un PC.

    #### Dans un terminal avec PuTTY  :

    Sur un PC Windows 10, faire un clic droit sur le menu `démarrer` et choisir `Gestionnaire de périphériques`, dérouler la liste des `Ports (COM et LPT)`, brancher et/ou débrancher le BBC micro:bit pour repérer sur quel numéro de COM est connectée votre carte.

    <img src="https://ericecmorlaix.github.io/img/W10-Gestionnaire00.png" alt="Gestionnaire de périphériques" width=30%>

    A partir de Cortana, rechercher et lancer l'application de bureau `PuTTY`. Choisir une connection de type `Serial` (Série), saisir le numéro du port COM de vore carte et régler la vitesse de communication à 115200 bauds (bits/seconde) puis cliquer sur le bouton `Open` pour ouvrir la connection et établir la communication entre le PC et le BBC micro:bit.

    <img src="https://ericecmorlaix.github.io/img/W10-PuTTY00.png" alt="application de bureau PuTTY" width=40%>

    Un fenêtre de terminal s'ouvre. Après avoir appuyé sur la touche `Entrée`de votre clavier,  Les trois chevrons `>>>` d'un interpréteur python doivent apparaitre :

    <img src="https://ericecmorlaix.github.io/img/W10-PuTTY01.png" alt="fenêtre de terminal" width=40%>

    Saisir alors quelques instructions en Python, et d'autre en microPython de la bibliothèque microbit...

    Ce qu'il faut bien comprendre ici, c'est que ces instructions ne s'exécutent pas sur votre PC mais à l'autre bout du câble USB dans le processeur (CPU) du micro-contrôleur (µC) de la carte BBC micro:bit.

    Génial, votre BBC micro:bit sait donc calculer, en fait, il sait faire à peu près tout ce qu'un programmme Python peut faire dans les limites de ses capacités de mémoire, 256 ko de mémoire stockage ([Flash](https://fr.wikipedia.org/wiki/M%C3%A9moire_flash)) plus 16 ko de mémoire vive ([RAM](https://fr.wikipedia.org/wiki/M%C3%A9moire_vive), Random Access Memory), et à la vitesse de 16 Mhz, sa fréquence d'horloge...

    Essayer des choses un peu plus évoluées, par exemple, définir une fonction telle que :

    ````python
    def maFonction():
        while True:
            if button_a.is_pressed():
                display.show(Image.HAPPY)
            elif button_b.is_pressed():
                break
            else:
                display.show(Image.SAD)
        display.clear()
    ````
    > **Rappel** : la touche `Tab` permet de faire de l'auto-complétion, saisir `d` suivi d'un `Tab` produit `display`...

    Revenir aux trois chevrons `>>>` en appuyant quatre fois sur `Entrée`, puis appeler votre fonction et tester votre programme...

    > Observer la réaction de la LED orange située à l'arrière du BBC micro:bit à chaque saisie d'un caractère dans la fenêtre de l'interpréteur... On devine le fonctionnement de la communication du PC vers le BBC micro:bit, c'est celle qu'utilise la fonctionnalité REPL dans l'éditeur Mu...

    <!-- 
        Pour en savoir plus à ce sujet :
    - Communication point à point de type RS232 et décodage d'une trame
    - essayer avec l'application Tera Term et se questionner sur la configuration du port série en baud rate of 115200, data 8 bits, parity none, stop 1 bit.
    - https://microbit-micropython.readthedocs.io/en/v1.0.1/devguide/repl.html 
    -->


    #### Dans les cellules de code d'un jupyter notebook :

    Pour tester directement depuis les cellules de ce bloc-note il vous faut démarrer un serveur jupyter notebook en local sur votre PC pour y ouvrir une copie de ce document.

    Dans le menu choisir `Kernel>Change Kernel>micro:bit`. Ce noyau est normalement disponible sur les PCs Windows 10 du labo de SI du lycée, si ce n'est pas votre cas, il suffit de suivre la procédure à cette adresse : https://github.com/takluyver/ubit_kernel

    On peut alors faire un premier test par exemple :


    ### Autres possibilités :
        
    - [microsoft makecode](https://makecode.microbit.org/){target=_blank}
    - [vittascience](https://fr.vittascience.com/microbit/?mode=mixed&console=bottom&toolbox=vittascience&simu=1){target=_blank} ;

???- info "Ressources :" 

    - http://numerique.ostralo.net/microbit/partie0_accueil/0_accueil.htm
    
    - https://www.isnbreizh.fr/nsi/activity/microbitRessources/index.html
    
    - https://fr.wikipedia.org/wiki/Micro:bit

    - https://microbit.org/get-started/user-guide/firmware/
    
    
    RTFD : https://microbit-micropython.readthedocs.io
    
    Le dépot GitHub des codes sources de MicroPython pour le BBC micro:bit et de l'éditeur en ligne :
    - https://github.com/bbcmicrobit
    
    MicroPython :
    - Site : http://micropython.org/
    - GitHub : 
    - Livre "Programmer avec MicroPÿthon" : https://github.com/ntoll/programming-with-micropython


    Support : 
    - https://support.microbit.org/support/home 
    - http://microbit.org/fr/guide/features/
    - https://tech.microbit.org/


    Modèle 3D du BBC micro:bit https://www.kitronik.co.uk/blog/bbc-microbit-cad-resources/
                                
    Des tutoriel et projets :
    - http://www.multiwingspan.co.uk/micro.php
    - https://learn.adafruit.com/bbc-micro-bit-lesson-number-0/intro
    - https://www.instructables.com/id/Microbit-Selfie-Remote/

    Quelques projets depuis une Rasberry Pi en MicroPython avec l'éditeur MU :
    - https://projects.raspberrypi.org/en/projects/getting-started-with-microbit
    - https://projects.raspberrypi.org/en/projects/microbit-selfies
    - https://projects.raspberrypi.org/en/projects/microbit-meteorologist
    - https://projects.raspberrypi.org/en/projects/micromine-bitcraft
    - https://github.com/raspberrypilearning/microbit-game-controller
                                
    Micro:bit with Arduino : https://learn.adafruit.com/use-micro-bit-with-arduino/overview