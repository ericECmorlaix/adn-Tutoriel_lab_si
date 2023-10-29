## Communication série

- <https://www.isnbreizh.fr/nsi/activity/microbitSerial/index.html>
- https://www.isnbreizh.fr/snt/activity/microbit/microbitSerial/microbitSerial.html

- <https://www.xanthium.in/Cross-Platform-serial-communication-using-Python-and-PySerial>

PC (Putty) <-> PC (Putty) (RS232 COM1)
PC (Putty) <-> BBC1
PC (Python) <-> BBC1
iPad <- ThingSpeak <- PC (Python) <-> BBC1
BBC1 (UART) <-> BBC2 (UART)
BBC <-> HCO5 <-> Smartphone
BBC <-> ESP8266 <-> ThingSpeak
BBC <-> ESP32 <->


Analyseur logique

- Communication série RS232

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/qYKCOauFzsk?si=NF1--78TA_c1bWI9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>

- Serial Communication on Pi / Arduino / micro:bit

<center>
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/MYoMM1FY6yM?si=9qqgh7h-odzSvMBb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>

```python
from microbit import *

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin8, rx=pin12)

id = "E"
display.scroll("I'm " + id)

while True :
    uart.write(id)
    sleep(2)
```

```python
from microbit import *

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin8, rx=pin12)

id = "F"
display.scroll("I'm " + id)

while True :
    if uart.any() :
        sleep(2)
        uart.write(id)
```




A voir : https://www.youtube.com/watch?v=cxfT407wRgc

```python
from microbit import *

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin1, rx=pin0)

code = "B"
display.scroll("code" + code)

while True :
    
    if uart.any() :
        uart.write(code)
        message = uart.read()
        display.scroll(message)
    sleep(2)
```



```python
from microbit import *


uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin0, rx=pin1)

code = "AAA"
display.scroll("code" + code)

while True :
    if uart.any() :
        message = uart.read()
        display.scroll(message)
    else :
        sleep(20)
        
    if button_a.is_pressed() :
        uart.write(code)
        sleep(50)
```






















