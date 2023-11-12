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

### Modèles de conctruction

- [Instructions pour différents modèles](https://education.lego.com/en-us/product-resources/mindstorms-ev3/downloads/building-instructions#building-core){target=_blank} ;

- <https://www.lego.com/fr-fr/themes/mindstorms/buildarobot>{target=_blank} ;

### [La mine d'Antonsmindstorms](https://www.antonsmindstorms.com/){target=_blank} ;

???- example "MINDSTORMS EV3 Racecar with PS4 controller"

    - [how-to-connect-a-ps4-dualshock-4-controller-to-your-mindstorms-ev3-brick-with-bluetooth](https://antonsmindstorms.com/2020/02/14/how-to-connect-a-ps4-dualshock-4-controller-to-your-mindstorms-ev3-brick-with-bluetooth/){target=_blank} ;

    ```python
    #!/usr/bin/env pybricks-micropython

    from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                    InfraredSensor, UltrasonicSensor, GyroSensor)
    from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                    SoundFile, ImageFile, Align)
    from pybricks.tools import print, wait, StopWatch

    import struct

    # Declare motors 
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    steer_motor = Motor(Port.A)
    forward = 0
    left = 0


    # Auto center steering wheels.
    steer_motor.run_until_stalled(250)
    steer_motor.reset_angle(80)
    steer_motor.run_target(300,0)


    # A helper function for converting stick values (0 - 255)
    # to more usable numbers (-100 - 100)
    def scale(val, src, dst):
        """
        Scale the given value from the scale of src to the scale of dst.
    
        val: float or int
        src: tuple
        dst: tuple
    
        example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
        """
        return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]


    # Open the Gamepad event file:
    # /dev/input/event3 is for PS3 gamepad
    # /dev/input/event4 is for PS4 gamepad
    # look at contents of /proc/bus/input/devices if either one of them doesn't work.
    # use 'cat /proc/bus/input/devices' and look for the event file.
    infile_path = "/dev/input/event4"

    # open file in binary mode
    in_file = open(infile_path, "rb")

    # Read from the file
    # long int, long int, unsigned short, unsigned short, unsigned int
    FORMAT = 'llHHI'    
    EVENT_SIZE = struct.calcsize(FORMAT)
    event = in_file.read(EVENT_SIZE)

    while event:
        (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)
        
        if ev_type == 1: # A button was pressed or released.
            if code == 310 and value == 0:
                steer_motor.reset_angle(steer_motor.angle()-5)
            if code == 311 and value == 0:
                steer_motor.reset_angle(steer_motor.angle()+5)
                
        elif ev_type == 3: # Stick was moved
            if code == 0: 
                left = scale(value, (0,255), (40, -40))
            if code == 4: # Righ stick vertical
                forward = scale(value, (0,255), (100,-100))
            
        # Set motor voltages. 
        left_motor.dc(forward)
        right_motor.dc(forward)

        # Track the steering angle
        steer_motor.track_target(left)

        # Finally, read another event
        event = in_file.read(EVENT_SIZE)

    in_file.close()
    ```

### CAD :
- <https://grabcad.com/br.barry.parker-1/models>{target=_blank} ;