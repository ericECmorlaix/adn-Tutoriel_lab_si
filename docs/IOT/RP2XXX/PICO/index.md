
# Pi Pico

## Broches Pi Pico W et Pico2 W

![picow-pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/picow-pinout.svg)

![pico2w-pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/pico2w-pinout.svg)

## Démarrage en MicroPython

- Télécharger le firmeware adapté à votreRaspberry Pi Pico ( W = avec Wi-Fi et Bluetooth LE, 2 = version avec RP2350) : <https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython>{target=_blank}
- Maintenir appuyé le bouton `BOOT` tout en connectant l'USB au PC ;
- Glisser/déposer le fichier du firmware sur le lecteur `RPXXXX (E:)` ;


> [Source](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython){target=_blank}

### Avec Thonny

- Démarrer le logiciel `Thonny` puis cliquer dans le menu sur `Exécuter` pour choisir le bon interpréteur et le port connecté ;

![Thonny Pi Pico W](../images/Pi_Pico_W-Thonny.png){.center width=80%}

- Enregistrer en `main.py` le code suivant pour tester la LED intégrée sur la Pi Pico W :

```Python
# Blink en boucle infinie
from machine import Pin
from time import sleep

ma_led = Pin("LED", Pin.OUT) # "LED" désigne la led "built-in"

print('La led "built-in" clignote...')
while True:
    try:
        sleep(1) # pause de 1 seconde
        ma_led.toggle() # bascule d'un état à l'autre

    except KeyboardInterrupt:
        break
ma_led.off()
print("FIN")
```

> Spécificité pour la LED embarquée sur la Pi Pico W cf [3.4. The on-board LED (page 16)](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf){target=_blank}

> **Faire** ++ctrl+"C"++ pour provoquer une interruption clavier ou **appuyer** sur le bouton "stop" ;


### Avec le simulateur WOKWI

[Wokwi](https://docs.wokwi.com/) est un simulateur électronique en ligne. Il permet de simuler différentes cartes à microcontroleur dont notamment les Pi Pico associées à d'autres composants électroniques et programmées en micropython.

<center><iframe name="Wokwi-pi-pico-hello" width="600px" height="600px" src="https://wokwi.com/projects/new/micropython-pi-pico" scrolling="yes" style="border:0px none #000000;box-shadow:0 6px 16px rgba(0,0,0,0.2);border-radius:10px;"></iframe></center>

??? example "Activité 1"
    
    Démarrer la simulation dans la fenêtre ci-dessus puis saisir dans l'interpréteur en console la série d'instructions suivantes :
    ```python
    >>>from machine import Pin
    >>>ma_led = Pin("LED", Pin.OUT)
    >>>ma_led.on()
    >>>ma_led.toggle()
    >>>ma_led.toggle()
    >>>ma_led.off()    
    >>>help()
    ```
??? example "Activité 2"

    Modifier le code pour qu'après l'affichage du message `Hello, Pi Pico!` la led "built-in" clignote...

> [Wokwi - Autres exemples en micropython](https://wokwi.com/micropython)

### Avec VSC

<https://tutoduino.fr/pico-python-visual-studio-code/>

Le plus pratique pour programmer en MicroPython une carte Pi Pico W avec Visual Studio Code est d'installer l'extension dédiée [MicroPico](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go){target=_blank} et d'en suivre les [instructions](https://github.com/paulober/MicroPico){target=_blank}...

![](../images/Pi_Pico_W-VSC.png){.center width=80%}

#### Extensions nécessaires

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance){target=_blank}
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance){target=_blank}
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode){target=_blank}

<!-- #### Autres solutions
- [micropython-stubs](https://github.com/Josverl/micropython-stubs){target=_blank}
- [micropython-stubber](https://github.com/Josverl/micropython-stubber){target=_blank} -->






## Ressources

### Officielles en Anglais

- [MicroPython - Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html){target=_blank}
- [Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf){target=_blank}
- [Connecting to the Internet with Raspberry Pi Pico W](https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf){target=_blank} ;

## Avec le module picozero

- [picozero_._readthedocs](https://picozero.readthedocs.io/en/latest/index.html){target=_blank} ;
- [Premiers pas avec picozero et Pi Pico W](https://projects.raspberrypi.org/fr-FR/projects/get-started-pico-w/0){target=_blank} ;
- [Autres projets avec picozero en Français](https://projects.raspberrypi.org/fr-FR/projects?search=pico){target=_blank}
- [Autres projets avec picozero en Anglais](https://projects.raspberrypi.org/en/projects?search=pico){target=_blank}


### Autres en Français

- [Christophe GUENEAU Pi Pico pour SI-NSI](https://www.gcworks.fr/tutoriel/pico/Accueil.html){target=_blank} ;

- [Christophe GUENEAU Pi Pico pour SI-NSI](https://www.gcworks.fr/tutoriel/pico/Accueil.html){target=_blank} ;

- [Une mine de vidéos en Français](https://www.youtube.com/@christianducros/videos){target=_blank}
> Son dépot GitHub : <https://github.com/christianDUCROS>{target=_blank}

<!-- - [Xavier HINAULT ancien = 2021 **attention à polyfill, ne pas renseigner la boite de dialogue**](https://www.micropython.fr/port_pi_pico/){target=_blank} ; -->


<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/VEdpqT8k8H4?si=CRl3XOHgzSS4OwhL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ZVS1ASrPGMA?si=LO9Kcc9uQk97nG_5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>

[raspberry pi pico programmer RTC + ntp (wifi) en python](https://youtu.be/HYu01QIXm2Q)


## Extensions matérielles

- Explorer Board de JOY-IT pour Raspberry PI Pico
    - [Manuel du propriétaire de la carte Explorer JOY-it RB-P-XPLR](https://fr.manuals.plus/joy-it/rb-p-xplr-explorer-board-manual#raspberry-pi-pico){target=_blank};
    - [Gotronic](https://www.gotronic.fr/art-platine-pico-explorer-p-xplr-38211.htm){target=_blank}, [Lextronic](https://www.lextronic.fr/carte-explorer-board-pour-pi-pico-77410.html){target=_blank}, [Kubbi](https://www.kubii.com/fr/malettes-plateformes-d-experimentation/4365-explorer-board-pour-raspberry-pi-pico-4250236825878.html){target=_blank};

- [Pico2 Explorer - Découverte et exploration de l'électronique avec MicroPython](https://wiki.mchobby.be/index.php?title=Pico-2-Explorer-FR){target=_blank} ; 


## Exemples d'applications

### Capteur d'humidité et de température de l'air DHTXX

#### Spécifications

Le capteur DHT11 peut détecter des températures de 0 °C à 50 °C (précision de ±2 °C) et une humidité relative de 20 % à 80 % (±5 %) (au maximum une fois par seconde).
Les stations météorologiques constituent probablement le principal domaine d’application d’un capteur tel que le DHT11. Pour tester le fonctionnement, il suffit de tenir la bouche près du capteur et d'expirer lentement. L'air respirable diffère de l'environnement en termes de température et d'humidité, ce qui devrait entraîner une modification significative des valeurs.

#### Exemple de code

```python
import machine
import dht # Module pour capteur DHTXX
import time

# Configuration du capteur DHT22 sur la broche 4
capteur_dht = dht.DHT22(machine.Pin(4))

# Fonction de lecture du capteur dht22
def read_dht22():
    # Lecture des données
    capteur_dht.measure()
    temp = capteur_dht.temperature()  # en °C
    humi = capteur_dht.humidity()      # en %

    # Affichage des résultats
    print(f"Température : {temp}°C")
    print(f"Humidité : {humi}%")

    # Le dht22 est plus précis mais plus lent que le dht11
    # Attendre 2 secondes entre chaque lecture
    time.sleep(2)

# Boucle principale
while True:
    read_dht22()
```

#### Simulation

[WOKWI DHT22-MicroPython-Pi_Pico](https://wokwi.com/projects/466727455524900865){target=_blank} ;

<center><iframe name="myiFrame" width="800px" height="800px" src="https://wokwi.com/projects/466727455524900865" scrolling="yes" style="border:0px none #000000;box-shadow:0 6px 16px rgba(0,0,0,0.2);border-radius:10px;"></iframe></center>

#### Activité possible

Modifier le code pour remplacer le DHT22 par un DHT11 connecté à la broche GPIO GP0 et faire l'essai sur une [Explorer Board JOY-IT]...


### Callback

```Python
# Blink avec callback
from machine import Pin, Timer

led = Pin("LED", Pin.OUT) # "LED" désigne la led built-in
timer = Timer() # Créé une instance de Timer()

def blink(timer) :
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```
> On observe que la LED clignote mais la carte reste disponible pour d'autres instructions

### Real Time Clock

Avec la classe [machine.RTC](https://docs.micropython.org/en/latest/rp2/quickref.html#real-time-clock-rtc){target=_blank} de MicroPython, il est possible d'utiliser l'horloge temps réel interne du Raspberry Pi Pico afin de connaître la date et l'heure à tout instant.

#### Récupérer les informations de l'horloge

```Python
# Obtenir la date et l'heure du µC
from machine import RTC
from utime import sleep

rtc = RTC()  # création d'un objet de type "Real Time Clock"

while True:
       
    t = rtc.datetime()   # obtention de la date et l'heure
    
    # Affichage au format tuple (year, month, day, weekday, hours, minutes, seconds, subseconds)
    print(t)
    # Affichage reformaté
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    print(f"Pour le µC nous sommes maintenant le {jours[t[3]]} {t[2]}/{t[1]}/{t[0]} et il est {t[4]}h{t[5]}min{t[6]}s" )  
    
    if t[0] == 2021 :
        print("(L'horloge n'est pas réglée !)")
    
    print()    
    sleep(1) # mise à jour chaque seconde
```
#### Régler l'horloge

L'horloge interne du Raspberry Pi Pico redémarre à la date du `vendredi 01/01/2021 à 0h0min0s` dès qu'on le réalimente.
Le script suivant permet à l'utilisateur de régler l'horloge manuellement :

```Python
# Régler la date et l'heure du µC
from machine import RTC
from utime import sleep

rtc = RTC()

print("Réglage manuel de la date et de l'heure")
annee = int(input ("Année (4 chiffres) : "))
mois = int(input ("Mois (1-12) : "))
jour = int(input("Jour (1-31) : "))
heure = int(input("Heure (0-23) : "))
minute = int(input("Minute (0-59) : "))
seconde = int(input("Seconde (0-59) : "))

# réglage de l'heure
rtc.datetime((annee, mois, jour, 0, heure, minute, seconde, 0))

while True:
       
    t = rtc.datetime()   # obtention de la date et l'heure

    # Affichage au format tuple (year, month, day, weekday, hours, minutes, seconds, subseconds)
    print(t)
    # Affichage reformaté
    jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    print(f"Pour le µC nous sommes maintenant le {jours[t[3]]} {t[2]}/{t[1]}/{t[0]} et il est {t[4]}h{t[5]}min{t[6]}s" )
    
    sleep(1) # mise à jour chaque seconde
```

> Thonny met à jour la date et l'heure du µC automatiquement...



https://electroniqueamateur.blogspot.com/2021/08/connaitre-la-date-et-lheure-avec-un.html

https://electroniqueamateur.blogspot.com/2021/08/horloge-temps-reel-ds3231-et-raspberry.html



![Alt text](./RTC_DS3231.png)
![Alt text](./RTC_GPIO.png)


https://micropython-urtc.readthedocs.io/en/latest/install.html
https://github.com/adafruit/Adafruit-uRTC

Ou https://github.com/balance19/micropython_DS3231
 -->




```Python


```





```Python
import time
from machine import Pin
from picozero import pico_led

relais_1 = Pin(18, Pin.OUT)    # create output pin on GPIO18

while True :
    pico_led.on()
    time.sleep(1)
    pico_led.off()
    relais_1.on()                 # set pin to "on" (high) level
    time.sleep(1)           # sleep for 1 second
    relais_1.off()                # set pin to "off" (low) level
    time.sleep(1)           # sleep for 1 second


import time
from machine import Pin

LED = Pin("LED", Pin.OUT)    # create output pin on GPIO25 the built-in LED

while True :
    LED.on()				# set pin to "on" (high) level
    time.sleep(1)			# sleep for 1 second
    LED.off()				# set pin to "off" (low) level
    time.sleep(1)           # sleep for 1 second


import time
from picozero import pico_led

while True :
    pico_led.on()
    time.sleep(1)
    pico_led.off()
    time.sleep(1)



```

```Python
# Serveur couronne de l'Avent
import network
import socket
from time import sleep
import machine
import codes_wlan
from picozero import pico_temp_sensor

# Gestion de l'horloge
import ntptime # Network Time Protocol
rtc = machine.RTC()


ssid = codes_wlan.ssid
password = codes_wlan.password


led = machine.Pin("LED", machine.Pin.OUT) # "LED" désigne la led built-in
relais = machine.Pin(18, machine.Pin.OUT)


def connect():
    # Connexion au WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(pm=0xa11140) # Pour augmenter la puissance du signal si besoin
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print(f"Pi Pico W connectée à l'adresse IP : {ip}")
    return ip

def open_socket(ip):
    # Ouvrir un socket
    address = (ip, 80)
    connexion = socket.socket()
    connexion.bind(address)
    connexion.listen(1)
    return connexion

def webpage(temperature, etat_led, etat_relais):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Pi Pico W</title>
            </head>
            <body>            
            <form action="./led-on">
            <input type="submit" value="Allumer la LED" />
            </form>
            <form action="./led-off">
            <input type="submit" value="Eteindre la LED" />
            </form>
            <p>La LED est {etat_led}</p>
            <form action="./relais-on">
            <input type="submit" value="Allumer le relais" />
            </form>
            <form action="./relais-off">
            <input type="submit" value="Eteindre le relais" />
            </form>
            <p>Le relais est {etat_relais}</p>
            <p>La température est de {temperature} °C</p>
            </body>
            </html>
            """
    return str(html)

def serveur(connexion, dt):
    #Start a web server
    etat_led = 'OFF'
    led.off()
    etat_relais = 'OFF'
    relais.off()
    temperature = 0
    while True:
        client = connexion.accept()[0]
        requete = client.recv(1024)
        requete = str(requete)
        try:
            requete = requete.split()[1]
        except IndexError:
            pass
        if requete == '/led-on?':
            led.on()
            etat_led = 'ON'
        elif requete =='/led-off?':
            led.off()
            etat_led = 'OFF'
        if requete == '/relais-on?':
            relais.on()
            etat_relais = 'ON'
        elif requete =='/relais-off?':
            relais.off()
            etat_relais = 'OFF'
        temperature = pico_temp_sensor.temp
        print(requete)
        html = webpage(temperature, etat_led, etat_relais)
        client.send(html)
        client.close()


try:
    # Connexion au WLAN
    ip = connect()
    # Réglage de l'horloge
    ntptime.settime() # Réglage de l'horloge à l'heure UTC obtenu d'internet (protocole NTP)
    t = rtc.datetime() # Tuple (year, month, day, weekday, hours, minutes, seconds, subseconds)
    print(f"RTC du RP2040 à l'heure UTC : {t}")
    # Réglage de l'horloge à l'heure de Paris
    saison = "été" if 3<t[1]<11 else "hiver"
    decalage = 2 if 3<t[1]<11 else 1 # 1h en hiver, 2h en été
    dt = rtc.datetime((t[0], t[1], t[2], t[3], t[4] + decalage, t[5], t[6], t[7]))
    print(f"RTC du RP2040 à l'heure d'{saison}) : {dt}")
    # Démarrage du serveur
    connexion = open_socket(ip)
    serveur(connexion, dt)
    
except KeyboardInterrupt:
    machine.reset()

```


## Autres applications liées

- Oscilloscope avec [Scoppy](https://youtu.be/nd_mglgRTa8?si=URH3pfjqhD-H_e59){target=_blank} sur [GitHub](https://github.com/fhdm-dev/scoppy){target=_blank}, [article](https://circuitdigest.com/news/diy-open-source-oscilloscope-using-a-raspberry-pi-pico-and-scoppy){target=_blank}, source [Vidéo C.DUCROS](https://youtu.be/nd_mglgRTa8?si=URH3pfjqhD-H_e59){target=_blank} ;
