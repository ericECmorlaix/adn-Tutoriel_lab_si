# UART

Le module UART permet de détourner la communication série vers un composant externe pour établir ici une communication bluetooth via un HC-05.

## Expérimentation

- Installer l'application Androïd [Serial Bluetooth Terminal](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal&hl=fr&gl=US){target=_blank}

- Téléverser le programme suivant sur la carte BBC micro:bit ;

```Python
from microbit import *
import music

# Initialise une communication série externe vers le module bluetooth HC-05
# Sur Grove Shield tx=pin0, rx=pin14
# Sur Elecfreaks Octopus:bit tx=pin8, rx=pin12
uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin8, rx=pin12)
# Ce qui détourne et désactive la communication série "normale" via l'USB vers le PC
# Et donc également la console REPL (et Graphique)...



uart.write('hello world \n')
uart.write(b'hello world \n')
uart.write(bytes([1, 2, 3, 4, 5]))

message = "Hello from micro:bit"

while True:
    
    if button_a.is_pressed() :
        uart.write(message + "\n") # "\n" ajoute (concatène) un saut de ligne
        print(message) # fonctionne également du fait du détournement de la communication série, le saut de ligne est inclu.
        sleep(1000)
    if button_b.is_pressed() :
        uart.write(str(temperature()) + "\n") # "\n" ajoute (concatène) un saut de ligne après la température du BBC
        print(temperature()) # fonctionne également du fait du détournement de la communication série, le saut de ligne est inclu.
        sleep(1000)
    if uart.any() : # Dès que des données attendent
        reponse_bytes = uart.read()
        uart.write(reponse_bytes)
        print(reponse_bytes)
        if reponse_bytes == b'ON\r\n' :
            pin13.write_digital(1)            
        if reponse_bytes == b'OFF\r\n' :
            pin13.write_digital(0)            
        if reponse_bytes == b'PYTHON\r\n' :
            music.play(music.PYTHON)
    if pin14.read_digital()==0 :
        niveau = pin1.read_analog()
        pin2.write_analog(niveau)
        uart.write(str(niveau) + "\n")
        sleep(1000)        
        
```

- Adapter si besoin les paramètres de raccordement du HC-05

|Fil|Broche|Grove|ElecFreaks|
|:-:|:-:|:-:|:-:|
| blanc | Rx | P14 | P12 |
| jaune | Tx | P0 | P8 |


- Dans l'application Serial Bluetooth Terminal, enregistrer dans les mémoires des commandes à transmettre pour tester ce programme et expliquer ce qu'il fait...

    - en hexadécimal :
        - `03` créer une interruption du programme en cours et ouvre le REPL équivalent à ^C ;
        - `04` créer un redémarrage du programme `main.py` équivalent à ^D ;
    - en texte :
        - `ON` pour allumer la LED connectée sur pin0 ;
        - `OFF` pour l'éteindre ;
        - d'autres commandes comme par exemple `display.show(Image.HAPPY)` à transmettre en mode REPL.


## Fonctions utiles dans le module uart :

microbit.uart.init (baudrate = 9600, bits = 8, parity = None, stop = 1, *, tx = None, rx = None) - initialise la communication avec la série.
bauderate - représente la vitesse de communication avec la série, il peut prendre les valeurs suivantes: 9600, 14400, 19200, 28800, 38400, 57600, 115200.

bits - représente le nombre de bits qui seront transmis.

parity - montre comment vérifier la parité; peut prendre les valeurs: Aucun, microbit.uart.ODD, microbit.uart.EVEN.

stop - représente le nombre de bits d'arrêt, dans le cas de cette plaque, la valeur est 1.

- `uart.any` - renvoie True s'il attend des données, sinon il retournera False .
- `uart.read([nbytes])` - lecture de bits. Le paramètre nbytes est facultatif, mais s'il est spécifié, au plus nbytes seront lus.
- `uart.readinto(buf [, nbytes])` - renvoie le nombre de bits lus et stockés dans buf ou renvoie None à l'expiration du délai.
- `uart.readline()` - lit une ligne se terminant par une nouvelle ligne.
- `uart.write(buff)` - écrit le buffer.

source : [https://ocw.cs.pub.ro/courses/sde2/laboratoare/11_microbit_fr](https://ocw.cs.pub.ro/courses/sde2/laboratoare/11_microbit_fr){target=_blank}


## Ressources utiles :

- Octopus:bit : <https://wiki.elecfreaks.com/en/microbit/expansion-board/octopus-bit>{target=_blank}

- Exemples micropython : <https://wiki.elecfreaks.com/en/microbit/getting-started/microbit-tinker-kit/tinker_kit_case_34/#getting-started>{target=_blank}

- Source à regarder :
    - <https://ocw.cs.pub.ro/courses/start?do=search&id=microbit>{target=_blank}
    - <https://ocw.cs.pub.ro/courses/sde2/laboratoare/12_microbit_fr>{target=_blank}

- Affichage sur écran OLED via communication I2C :
    - [tutoriel détaillé](https://littlebirdelectronics.com.au/guides/88/0-96-oled-screen-with-micro-bit){target=_blank} ;
    - [GitHub du module microbit_ssd1306](https://github.com/fizban99/microbit_ssd1306){target=_blank}
    - Autres tutoriels :
        - <https://blog.martinfitzpatrick.com/oled-displays-i2c-micropython/>{target=_blank}
        - <https://www.instructables.com/Microbit-OLED-Game/>{target=_blank}
    - [Autre module kitronik](https://github.com/KitronikLtd/micropython-microbit-kitronik-oled){target=_blank}