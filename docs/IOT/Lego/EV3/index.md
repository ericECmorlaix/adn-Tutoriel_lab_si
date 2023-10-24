## LEGO® MINDSTORMS Education EV3 MicroPython

### Ressource officielle version v2.0

Toutes les informations sont disponibles sur le site : [https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3){target=_blank}

La documentation est disponible en Anglais au [téléchargement en pdf](https://assets.education.lego.com/v3/assets/blt293eea581807678a/bltb470b9ea6e38f8d4/5f8802fc4376310c19e33714/getting-started-with-micropython-v2_enus.pdf?locale=en-us){target=_blank} ou [directement en ligne](https://pybricks.com/ev3-micropython/){target=_blank}

Une traduction librement interprétée est disponible sur le site [www.ostralo.net/](https://numerique.ostralo.net/robotLego_python/1_generalites.htm){target=_blank}.


### Mise en réseau par wifi :

- Créer un réseau LAN avec un routeur Wifi.

- Installer un dongle Wifi sur le port USB-A de la brique Lego EV3.

- Après démarrage du système, configurer le réseau WiFi depuis le menu de la brique...

> Si la connexion Wifi est valide, l'adresse IP du robot s'affiche sur l'écran (en haut)

- Pour tester le bon fonctionnement du robot, on peut se connecter via SSH. Les identifiants sont :
  * utilisateur : robot
  * mot de passe : maker
```
$ ssh robot@192.168.1.101
```

- Pour lancer un script micropython depuis la console du robot par SSH : 
```
$ brickrun pybricks-micropython /home/robot/hello.py
```

- Pour lancer un interpréteur depuis la console du robot par SSH afin d'exécuter une des fonctions de votre programme :
```
$ cd monProjet # aller dans le dossier du projet
$ brickrun pybricks-micropython # démarrer l'interpréteur Pybricks MicroPython
Pybricks MicroPython v1.11 on 2020-05-06; linux version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> from monProgramme import *
>>> maFonction()
```

### Modularité :

Développer petit à petit de façon modulaire, par fonctionnalité...

```python
#!/usr/bin/env pybricks-micropython

# Dépendances
from machin import bidule, truc

# Définitions
    
bar = 'titi'

def foo() :
    '''
        Docstring de foo()
    '''
    pass

# Tests
if __name__ == '__main__': 
    # appel à la fonction foo() pour un test
    foo()
    # affichage en console d'une variable
    print(bar)
```

L'usage de Programmation Orientée Objet peut être judicieux ici...


## Autres ressources :

- Le module Pybricks MicroPython pour EV3 est basé sur [ev3dev](https://www.ev3dev.org/news/2019/04/13/ev3-micropython/){target=_blank} ;
- [Tutoriel EV3 Python par Raphael Holzer](https://ev3-tutorial.readthedocs.io/en/latest/index.html){target=_blank} ;
- [https://sites.google.com/site/ev3devpython/](https://sites.google.com/site/ev3devpython/){target=_blank} ;
- [Instructions de construction de différents modèles](https://education.lego.com/en-us/product-resources/mindstorms-ev3/downloads/building-instructions#building-core){target=_blank} ;
- [La mine d'Antonsmindstorms](https://www.antonsmindstorms.com/){target=_blank} ;