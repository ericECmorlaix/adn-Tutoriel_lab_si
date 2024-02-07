
## CARTE MOTEUR MOTOR:BIT

- <https://www.elecfreaks.com/motor-bit-for-micro-bit-motorbit.html>
- <https://www.elecfreaks.com/learn-en/microbitExtensionModule/motor_bit_v16.html?highlight=motor%20bit>

<img src="https://images.elecfreaks.com/catalog/product/cache/6b498889e7d5d1efdf5c1d5869f66fec/e/f/ef03406.jpg" width="45%" ><img src="https://images.elecfreaks.com/catalog/product/cache/6b498889e7d5d1efdf5c1d5869f66fec/i/m/img_4253.jpg" width="45%" >

Cette carte intègre un TB6612 qui est un circuit à double pont en H permettant d'alimenter deux Moteur à Courant Continu (MCC) (ou un Moteur Pas à Pas, ou 4 solénoïdes)

<center><img src="https://arduino.blaisepascal.fr/wp-content/uploads/2017/05/Pont_H_schema1.png" width="23%" ><img src="https://arduino.blaisepascal.fr/wp-content/uploads/2017/05/Pont_H_schema2.png" width="23%" ><img src="https://arduino.blaisepascal.fr/wp-content/uploads/2017/05/Pont_H_schema3.png" width="23%" ></center>

### Broches moteurs

- P8	: Direction de M1, sens positif de rotation en tension HIGH (digital = 1), sens négatif sur LOW (digital = 0) ;
- P1	: Vitesse de M1	en MLI (PWM) (analog = entre 0 et 1023) ;
- P2	: Vitesse de M2	en MLI (PWM) (analog = entre 0 et 1023) ;
- P12	: Direction de M2, sens positif de rotation en tension HIGH, sens négatif sur LOW.

```Python
from microbit import *
  
def avance(v):
    # le mode "avance" à la vitesse v (entier entre 0 et 1023)
    pin8.write_digital(1)  # direction M1
    pin12.write_digital(0) # direction M2
    pin1.write_analog(v) # vitesse M1
    pin2.write_analog(v) # vitesse M2
  
def recule(v):
    pin8.write_digital(0)  # direction M1
    pin12.write_digital(1) # direction M2
    pin1.write_analog(v) # vitesse M1
    pin2.write_analog(v) # vitesse M2
  
avance(300) # le robot avance pendant 2s (vitesse faible)
sleep(2000)
recule(300) # le robot recule pendant 2s
sleep(2000)
avance(0)   # le robot s'arrête
```

### Buzzer

- P0 : buzzer

### Broches jaunes

- P3-P7, P9-P11 : 8 broches alimentées en 3,3V .
- P3, P4, P10 : peuvent être utilisées en mode « Entrée de signal analogique ».

ATTENTION : pour utiliser les broches P3, P4, P6, P7, P9, P10 (dédiées aux 25 leds), il faut ajouter :

- `display.off()` pour désactiver l’affichage
- `display.on()` pour réactiver les leds


### Broches bleues

Si le commutateur VCC (juste au-dessus) est sur 5V, alors les broches rouges donnent du 5V et le niveau de signal des broches bleues est sur 5V aussi.
Si le commutateur VCC est sur 3,3V, alors les rouges délivrent du 3,3V et le niveau du signal des bleues est aussi 3,3V.

- P13-P16 : 4 ports GPIO
- P19-P20 : 1 connecteur de communication IIC

<!-- 

https://nsirennes.fr/os-archi/bbc-microbit/



CARTE JOYSTICK:BIT

Joystick:bit v2.0 de ELECTROFREAKS
pin2 : pin2.read_analog() détecte le bouton pressé
buttons = {2: "A", 517: "B", 686: "C", 769: "D", 853: "E", 820: "F", 1021 : "aucun"}
pin0 et pin1 donnent la position du joystick :
pin0.read_analog() sur X : 3~1021 et Xcentre = 529
pin1.read_analog() sur Y : 3~1021 et Ycentre = 506
/!\ Ces valeurs sont approximatives car elles varient d’une carte Joystick:bit à l’autre !

Tester la Joystick:bit

Les coordonnées du joystick
1
2
3
4
5
6
7
8
9
10
11
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
Emetteur radio (carte Joystick:bit)

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
Récepteur radio (carte motor:bit)

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
        ancien_bouton = bouton -->