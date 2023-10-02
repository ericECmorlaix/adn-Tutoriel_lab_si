
- <https://www.robotique.tech/tutoriel/construction-des-objets-connectes-bases-sur-la-carte-esp32/>

- <https://github.com/SoproLab/Soprolab>

<!-- 
- https://www.youtube.com/@christianducros/videos
- https://github.com/christianDUCROS -->



## Préparation de l'ESP32 pour MicroPython

### Avec le logiciel [Thonny](https://thonny.org){target=_blank}

- **Installer** la dernière version du logiciel ;
- **Connecter** la carte ESP32 à votre PC via un cable USB ;
- **Démarrer** Thonny ;
- Dans le menu horizontal, **cliquer** sur `Exécuter` et **choisir** `Configurer l'interpréteur` ;
- **Choisir** le type d'interpréteur et le port série correspondants à la carte ;
- **Cliquer** sur le lien `Installer ou mettre à jour MicroPython (esptool)` ;

![ESP32_Flash_Thonny_01](./images/ESP32_Flash_Thonny_01.png){.center}

- **Renseigner** tous les champs (*lire les inscriptions idoines sur le µC*) puis **cliquer** sur `Installer` ;

![ESP32_Flash_Thonny_02](./images/ESP32_Flash_Thonny_02.png){.center}

> Si tout se passe bien, le prompt de l'interpréteur MicroPython doit apparaitre en console...

### Avec le logiciel [Mu](https://codewith.mu/en/download){target=_blank}

- **Installer** la dernière version du logiciel ;
- **Connecter** la carte ESP32 à votre PC via un cable USB ;
- **Démarrer** Mu Editor  et **Choisir** le mode `ESP MicroPython` ;
- **Cliquer** sur le rouage tout en bas à droite et **choisir** l'onglet `ESP Firmware flasher` puis **Suivre** les instructions...  ;

![ESP32_Flash_Mu](./images/ESP32_Flash_Mu.png){.center}

> Si tout se passe bien, **cliquer** sur le bouton `REPL` du menu et le prompt de l'interpréteur MicroPython doit apparaitre en console...

## Connecter l'ESP32 à un point d'accès

> Point d'accès = un réseau WLAN avec un des routeurs du labo de SI, un partage de connexion à votre smartphone...

- **Saisir** le programme MicroPython suivant :
```Python
# ESP32 : connexion à un point d'accès Wifi
import network
from time import sleep
import ubinascii
wlan = network.WLAN(network.STA_IF)  # On créer l'objet wlan pour gérer la connexion
wlan.active(True) # Activation de l'interface
if not wlan.isconnected() :  # On vérifie qu'on n'est pas déjà connecté
    print("Connexion au point d'accès...")
    # On demande une connexion en renseignant l'identifiant et le mot de passe du point d'accès
    wlan.connect('SSID', "Code")
    # Boucle d'attente...
    while not wlan.isconnected() :
        print('Connexion en cours...')
        time.sleep(0.5)
# Confirmation de connexion
print("Connecté en Wifi au point d'accès")
# Affiche l'adresse logique que l'ESP32 à obtenu du DHCP
print("Adresse IP de l'ESP32 = ", wlan.ifconfig()[0])
# Affiche l'adresse physique de l'ESP32
print("Adresse MAC de l'ESP32 = ", ubinascii.hexlify(wlan.config('mac')).decode('utf-8'))
```

<!-- ```Python
import network
import time
import ubinascii
wlan = network.WLAN(network.STA_IF)  # On créer l'objet wlan pour gérer la connexion
wlan.active(True) # Activation de l'interface
if not wlan.isconnected() :  # On vérifie qu'on n'est pas déjà connecté
    print("Connexion au point d'accès...")
    # On demande une connexion au point d'accès
    wlan.connect('WIFI_SI2', 'wifisi02')
    # Boucle d'attente...
    while not wlan.isconnected() :
        print('Connexion en cours...')
        time.sleep(0.5)
# Confirmation de connexion
print("Connecté en Wifi au point d'accès")
# Affiche l'IPV4 que l'ESP32 à obtenu du DHCP
print("Adresse IP de l'ESP32 = ", wlan.ifconfig()[0])
# Affiche l'adresse MAC de l'ESP32
print("Adresse MAC de l'ESP32 = ", ubinascii.hexlify(wlan.config('mac')).decode('utf-8'))
``` -->


??? example "A expérimenter vous même..."
    - **Saisir** l'instruction `wlan.ifconfig()` dans l'interpréteur pour obtenir plus d'informations concernant le réseau ;
    - Comment obtenir l'adresse de la passerelle ?
    - Tester la connexion de l'ESP32 vers la passerelle    
    - Scanner le réseau
    - Configurer un adresse IP statique compatible
    - Améliorer l'affichage de l'adresse MAC
    - En cas d'erreur de saisi ou d'indisponibilité du point d'accès on rentre dans une boucle infinie, ier le script pour limiter le délai d'attente à 30 secondes...

## Communication Client/Serveur

### Serveur = ESP32 / Client 1 = logiciel PC / Client 2 = 

    



