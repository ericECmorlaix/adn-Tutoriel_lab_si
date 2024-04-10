
## CARTE JOYSTICK:BIT

[Joystick:bit v1.4 de ELECTROFREAKS](https://www.elecfreaks.com/learn-en/microbitExtensionModule/joystick_bit_v1.html)

<center><img src="https://nsirennes.fr/wp-content/uploads/2020/12/joystickbit_seule.png" width="70%" ></center>


- pin2 : `pin2.read_analog()` détecte le bouton pressé
- `buttons = {2: "A", 517: "B", 686: "C", 769: "D", 853: "E", 820: "F", 1021 : "aucun"}`
- pin0 et pin1 donnent la position du joystick :
    - `pin0.read_analog()` sur X : 3~1021 et Xcentre = 529
    - `pin1.read_analog()` sur Y : 3~1021 et Ycentre = 506

> /!\ Ces valeurs sont approximatives car elles varient d’une carte Joystick:bit à l’autre !

### Pour tester le Joystick:bit

#### Les coordonnées du joystick

<center><img src="https://nsirennes.fr/wp-content/uploads/2020/12/Mu_barre_menu-joystick.svg" width="60%" ></center>

```Python
from microbit import *
import radio
#######################################
# TEST : JOYSTICK:BIT
while True:
    press = pin2.read_analog()
    print("bouton : "+ str(press))
    X = pin0.read_analog()
    Y = pin1.read_analog()
    print("joystick : "+str(X)+" , "+str(Y))
    sleep(100)
```


#### Emetteur radio (carte Joystick:bit)


```Python
from microbit import *
import radio
 
#######################################
# JOYSTICK:BIT
def button_press():
    press = pin2.read_analog()
    if press > 938:  # le plus fréquent car aucun bouton : press=1021
        return ""
    elif press < 256:
        return "A"
    elif press < 597:
        return "B"
    elif press < 725:
        return "C"
    elif press < 793:
        return "D"
    elif press < 836:
        return "F"
    else:
        return "E"
 
def joystick_push():
    # Par défaut : x = 529 (3~1021)   y = 506 (3~1022)
    # map (1~1023) to (-1022~1022)
    x = 2 * pin0.read_analog() - 1024
    y = 2 * pin1.read_analog() - 1024
    if -100 < x < 100:
        x = 0
    if -100 < y < 100:
        y = 0
    return x, y
 
 
radio.config(channel=7, group=0, queue=1, power=7)
radio.on()
while True:
    X, Y = joystick_push()       
    message = str(X) + "|" + str(Y) + "|" + button_press()
    radio.send(message)      # ex : "-700|400|"
```

#### Récepteur radio (carte motor:bit)

```Python

from microbit import *
import radio
 
###################################
# MOTOR:BIT   M1=gauche   M2=droite
 
def drive(vitesseX, vitesseY): # vitesse : -1023 ~ 1023
    if vitesseX < 0:
        vitesseX = - vitesseX
        pin8.write_digital(0)  # direction M1
    else:
        pin8.write_digital(1)  # direction M1
 
    if vitesseY < 0:
        vitesseY = - vitesseY
        pin12.write_digital(1)  # direction M2
    else:
        pin12.write_digital(0)  # direction M2
 
    if vitesseX > 900:
        vitesseX = 900
    if vitesseY > 900:
        vitesseY = 900
    pin1.write_analog(vitesseX) # vitesse M1
    pin2.write_analog(vitesseY) # vitesse M2
 
 
radio.config(channel=7, group=0, queue=1, power=7)
radio.on()
ancien_bouton = ""
while True:
    msg_recu = radio.receive()
    if msg_recu is not None:
        [joystickX, joystickY, bouton] = msg_recu.split("|")
         
        # moteur
        joystickX = int(joystickX)
        joystickY = int(joystickY)
        drive(joystickY + joystickX//3 , joystickY - joystickX//3)
         
        # bouton
        # /!\ redondances car un appui bref de btn A donne "A" "A" "A" "A"
        if bouton != ancien_bouton:
            # faire qqch
        ancien_bouton = bouton
```
        
<!-- 

https://nsirennes.fr/os-archi/bbc-microbit/

        
        
         -->