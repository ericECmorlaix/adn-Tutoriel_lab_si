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
