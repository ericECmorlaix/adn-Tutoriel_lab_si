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



