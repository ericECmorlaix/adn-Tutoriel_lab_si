
#

##

![Alt text](image.png)


```python
import esp32
from machine import Pin

r = esp32.RMT(2, pin=Pin(18), clock_div=80) # 80 pour avoir 80/80000000 = 1 µs
print(r.source_freq()) # 80000000 Hz

signal=(88,8,4,44,40,8,40,8,40,8,40) # les durées sont des multiples de 4 x 1 µs 
r.write_pulses(signal, start=0) # commence par l'état 0

trameDMXdec = [150,20,0,0,255,0,0,0,0,0,0,0,0,0,0,0] # les valeurs de 16 canaux

# Conception trameDMXstr chaine de caractères
le_break = '0'*22 # 22 états 0
le_mab = '11' # Mark After Break
code_depart = '0' + '0'*8 + '11' # 1 bit de start à 0 + une valeur = 0 en binaire sur huit bits + 2 bits de stop à 1
trameDMXstr = le_break + le_mab + code_depart

for i in range(0, len(trameDMXdec)) :
    trameX = '0' # bit de start
    for masque in [1,2,4,8,16,32,64,128] :
        if (trameDMXdec[i] & masque != 0) :
            trameX += '1'
        else :
            trameX += '0'
    trameX += '11' # 2 bits de stop
    trameDMXstr += trameX
    
print(trameDMXstr)

# Conception trameRMT à partir du découpage de trameDMXstr
trameRMT = [] # liste des durées Etats haut puis Etats bas
nb = 0
lecture_precedente = '0'

for i in range (0, len(trameDMXstr)) :
    if trameDMXstr[i] == lecture_precedente :
        nb += 4 # 4µs pour 250kHz
    else :
        trameRMT.append(nb)
        lecture_precedente = trameDMXstr[i]
        nb = 4
trameRMT.append(nb)
print(trameRMT)


```


## Ressources

- 
<figure>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/wOqQ_vYQVkE?si=4ttb0oR0OoDjTz48" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<figcaption>Trame DMX ESP32 micropython (sans bibliothèque) Protocole DMX en français par Christian DUCROS</figcaption>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/OBD4fCL1Pc4?si=eP2o9pZD3AuDt5Ol" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</figure>

- [DMX - DÉCOUVERTE DE LA TECHNOLOGIE DMX512 Dominique Meurisse (MCHobby)](https://arduino103.blogspot.com/2021/03/dmx-decouverte-de-le-technologie-dmx512.html){target=_blank}

- [Grove-DMX512](https://wiki.seeedstudio.com/Grove-DMX512/){target=_blank}
- [esp32-rmt](https://docs.micropython.org/en/latest/library/esp32.html#esp32-rmt){target=_blank}

- [PyDMX est un package capable d'envoyer des données DMX512 via un pilote](https://github.com/JMAlego/PyDMX){target=_blank}