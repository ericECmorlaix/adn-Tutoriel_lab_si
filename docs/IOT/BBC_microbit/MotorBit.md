
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


