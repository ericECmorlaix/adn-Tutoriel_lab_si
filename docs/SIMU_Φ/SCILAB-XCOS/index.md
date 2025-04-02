
> PB installation SIMM avec 2024-2025
> Solution avec scilab 5.5.2 : https://www.developpez.net/forums/i2170280/environnements-developpement/autres-edi/scilab/probleme-daffichage-courbes-scope/

Auteur : PascalPLC
Procédure d'installation de SCILAB 5.5.2
Bonjour,

L'utilisation de SIMM ou de COSELICA peut s'avèrer capricieuse avec les versions récentes de SCILAB.
Par contre, ça marche très bien avec SCILAB 5.5.2 en version 32 bits.

Si ça peut aider, voici la procédure d'installation de SCILAb 5.5.2 avec les modules iodelay, CPGE, Coselica, SIMM et mingw.

> C'est important d'installer les versions 32 bits de SCILAb et de gcc, y compris dans un environnement 64 bits, sinon, ça ne fonctionnera pas.
>
> Pour l'installation des modules, on utilise le gestionnaire de modules ATOMS, et pour gcc, le lien est le suivant : http://atoms.scilab.org/toolboxes/mi...c-4.6.3-32.exe

1. Installer SCILAB 5.5.2 32 bits
2. Installer ensuite les 4 modules suivants :
• Iodelay
• CPGE
• Coselica
• SIMM
3. Relancer SCILAB afin de vérifier que l’installation des 4 modules est réussie
4. Quitter SCILAB
5. Télécharger et installer la version 32 bits de gcc : gcc-4.6.3-32.exe
6. Important : L’installer dans le répertoire C:\Users\user\ où user est votre espace utilisateur de Windows
7. Redémarrer le PC pour que Windows prenne en compte le compilateur
8. Installer le module MingW dans SCILAB sans précaution particulière. Attention, un message d’erreur peut apparaître à la fin de l’installation de MingW. Ignorez-le.
9. Relancer SCILAB et la compilation des librairies de MingW va démarrer. Cela prend plusieurs minutes. Patientez jusqu’à la fin.
10. Relancer SCILAB.
11. Enjoy CPGE, COSELICA et SIMM

Voici à titre d'exemple la simulation d'un circuit RLC série excité par un échelon unitaire (R = 1.5ohm, L = 1H, C = 1F).

<img src="https://www.developpez.net/forums/attachments/p659950/environnements-developpement/autres-edi/scilab/probleme-daffichage-courbes-scope/rlc-serie-schema-xcos.png/">
<img src="https://www.developpez.net/forums/attachments/p659951/environnements-developpement/autres-edi/scilab/probleme-daffichage-courbes-scope/rlc-serie-courbe-reponse.png/">

Et voici les résultats de simulation du moteur CC avec charge :

<img src="https://www.developpez.net/forums/attachments/p659965/environnements-developpement/autres-edi/scilab/probleme-daffichage-courbes-scope/schema-simulation_moteur_electrique.v5.5.2.png/">
<img src="https://www.developpez.net/forums/attachments/p659966/environnements-developpement/autres-edi/scilab/probleme-daffichage-courbes-scope/courbes-simulation-moteur.v5.5.2.png/">

<!-- 

> Autre solution => **Ne fonctionne pas !!!**
Jerome Briot

Il faut installer dans l'ordre les toolbox suivantes sur une installation propre de Scilab (supprimer les fichiers relatifs à Scilab dans le dossier Appdata de Windows)

MinGw toolbox
Coselica
SIMM


Pour MinGw toolbox, il faut installer le compilateur gcc avant toute chose. Le lien de téléchargement de gcc est donné sur la page atoms de la toolbox.
La version de gcc a télécharger dépend de la version de Scilab utilisée.
https://atoms.scilab.org/toolboxes/mingw/10.3.0/files/gcc-10.3.0-64.exe
https://atoms.scilab.org/toolboxes/mingw/10.3.0/files/gcc-10.3.0-32.exe

Pour finir, vous n'êtes pas seul :aie:

=> [Convert a XCOS model from Scilab 5.5.2 to Scilab 2024](https://scilab.discourse.group/t/convert-a-xcos-model-from-scilab-5-5-2-to-scilab-2024/327)
 -->

## Ressources

Site de profs 

- [Espace dédié à la Modélisation Multiphysique](https://insyte.website/modelisationMultiPhysique.php#ancreScilab-Xcos){target=_blank}


- [https://scilab.developpez.com/tutoriels/debuter/apprendre-xcos-debutant/](https://scilab.developpez.com/tutoriels/debuter/apprendre-xcos-debutant/){target=_blank}
- [https://scilab.developpez.com/tutoriels/apprendre-xcos/](https://scilab.developpez.com/tutoriels/apprendre-xcos/){target=_blank}

<iframe width="560" height="315" src="https://www.youtube.com/embed/jbDocYc9guo?si=4AtQRZ4nNREPj4jl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


<iframe title="1. Modélisation Alimentation Moteur - Scilab-720p" width="560" height="315" src="https://tube-sciences-technologies.apps.education.fr/videos/embed/71e85ec1-a1c2-44aa-bdf1-233ad4c126df" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>

<iframe title="2. Insertion capteur - Scilab-720p" width="560" height="315" src="https://tube-sciences-technologies.apps.education.fr/videos/embed/e88a4fbc-c474-4513-8d68-e6b2968ec7ee" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>

<iframe title="3. Modélisation du piston - Scilab-720p" width="560" height="315" src="https://tube-sciences-technologies.apps.education.fr/videos/embed/c2d69762-4424-4703-9dec-64442792588d" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>


<iframe title="4. Modélisation du système bielle excentrique - Scilab-720p" width="560" height="315" src="https://tube-sciences-technologies.apps.education.fr/videos/embed/dd725a7f-2eca-494a-9a82-25bad13bfe64" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>



[https://fossee.in/](https://fossee.in/)