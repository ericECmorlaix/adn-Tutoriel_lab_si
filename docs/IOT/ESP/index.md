




## Ressources générales :

- [Une mine de vidéos en Français](https://www.youtube.com/@christianducros/videos){target=_blank}
> Son dépot GitHub : <https://github.com/christianDUCROS>{target=_blank}

- [Raspberry ME recherche MicroPython et ESP](https://www.raspberryme.com/?s=micropython+ESP)



## IDE



- [IDE MicroPython pour ESP32 et ESP8266](https://www.raspberryme.com/ide-micropython-pour-esp32-et-esp8266/)

- [Premiers pas avec l’IDE Thonny MicroPython (Python) pour ESP32 et ESP8266](https://www.raspberryme.com/premiers-pas-avec-lide-thonny-micropython-python-pour-esp32-et-esp8266/)

- [MicroPython : programmer ESP32/ESP8266 à l’aide de l’éditeur Mu](https://www.raspberryme.com/micropython-programmer-esp32-esp8266-a-laide-de-lediteur-mu/)

- [Arduino Lab for MicroPython ](https://docs.arduino.cc/micropython/)

## Communication

### MQTT

Première expérimentation avec pour serveur MQTT le broker de <https://test.mosquitto.org/> et pour clients les applications [IoT MQTT Panel](https://apps.apple.com/fr/app/iot-mqtt-panel/id6466780124) sur tablette|smartphone et [MQTT Explorer](https://mqtt-explorer.com/) sur PC.

- _Dans `IoT MQTT Panel` le prof crée une connexion `Toto` client du broker `test.mosquitto.org` sur le port `1883` en `TCP` et un tableau de bord comportant un slider pour publier des valeurs de 0 à 100% vers le topic `lnddm/s2int/Toto`_
- _Dans `MQTT Explorer` le prof crée une connexion `Titi` client du broker `test.mosquitto.org` sur le port `1883` en `TCP` pour souscrire au topic `lnddm/s2int/Toto`_
- _Dans `MQTT Explorer` le prof  publie sur le topic `lnddm/s2int/Titi` le message `Bonjour`_
- _Dans `IoT MQTT Panel` chaque élève crée une connexion `Prenom` client du broker `test.mosquitto.org` sur le port `1883` en `TCP` et un tableau de bord comportant un texte pour souscrire au topic `lnddm/s2int/Titi` puis une jauge pour souscrire au topic `lnddm/s2int/Toto`_
- _Dans `MQTT Explorer` chaque élève publie sur le topic `lnddm/s2int/Prenom` et souscrit au topic de son binôme..._

Seconde expérience avec un ESP32 pour publier les valeurs de température et d'humidité mesurées par un capteur DHT22

```python
# Complete project details at https://RandomNerdTutorials.com/micropython-mqtt-publish-dht11-dht22-esp32-esp8266/

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
from machine import Pin
import dht
esp.osdebug(None)
import gc
gc.collect()


ssid = 'WIFI_SI5'
password = 'wifisi05'
mqtt_server = 'test.mosquitto.org'

# Identifiant unique pour le client ESP basé sur son adresse MAC 
client_id = ubinascii.hexlify(machine.unique_id())

# Définition des topics
topic_pub_temp = b'lnddm/s2int/esp/dht/temperature'
topic_pub_hum = b'lnddm/s2int/esp/dht/humidity'

# 
last_message = 0
message_interval = 5


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))

def connect_mqtt():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server)
  #client = MQTTClient(client_id, mqtt_server, user="mqtt", password="bac")
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def read_sensor():
  try:
    sensor.measure()
    temp = sensor.temperature()
    # uncomment for Fahrenheit
    #temp = temp * (9/5) + 32.0
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      temp = (b'{0:3.1f}'.format(temp))
      hum =  (b'{0:3.1f}'.format(hum))
      return temp, hum
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
      temp, hum = read_sensor()
      print(temp)
      print(hum)
      client.publish(topic_pub_temp, temp)
      client.publish(topic_pub_hum, hum)
      last_message = time.time()
  except OSError as e:
    restart_and_reconnect()

```



Troisième vers LED RGB

Quatre un broker local avec Home assistant sur Rasberry Pi

TP





#### Raspberry Pi/ESP/Home Assistant




Module `umqtttsimple.py` à enregistrer dans les fichiers de l'ESP

```python
try:
    import usocket as socket
except:
    import socket
import ustruct as struct
from ubinascii import hexlify

class MQTTException(Exception):
    pass

class MQTTClient:

    def __init__(self, client_id, server, port=0, user=None, password=None, keepalive=0,
                 ssl=False, ssl_params={}):
        if port == 0:
            port = 8883 if ssl else 1883
        self.client_id = client_id
        self.sock = None
        self.server = server
        self.port = port
        self.ssl = ssl
        self.ssl_params = ssl_params
        self.pid = 0
        self.cb = None
        self.user = user
        self.pswd = password
        self.keepalive = keepalive
        self.lw_topic = None
        self.lw_msg = None
        self.lw_qos = 0
        self.lw_retain = False

    def _send_str(self, s):
        self.sock.write(struct.pack("!H", len(s)))
        self.sock.write(s)

    def _recv_len(self):
        n = 0
        sh = 0
        while 1:
            b = self.sock.read(1)[0]
            n |= (b & 0x7f) << sh
            if not b & 0x80:
                return n
            sh += 7

    def set_callback(self, f):
        self.cb = f

    def set_last_will(self, topic, msg, retain=False, qos=0):
        assert 0 <= qos <= 2
        assert topic
        self.lw_topic = topic
        self.lw_msg = msg
        self.lw_qos = qos
        self.lw_retain = retain

    def connect(self, clean_session=True):
        self.sock = socket.socket()
        addr = socket.getaddrinfo(self.server, self.port)[0][-1]
        self.sock.connect(addr)
        if self.ssl:
            import ussl
            self.sock = ussl.wrap_socket(self.sock, **self.ssl_params)
        premsg = bytearray(b"\x10\0\0\0\0\0")
        msg = bytearray(b"\x04MQTT\x04\x02\0\0")

        sz = 10 + 2 + len(self.client_id)
        msg[6] = clean_session << 1
        if self.user is not None:
            sz += 2 + len(self.user) + 2 + len(self.pswd)
            msg[6] |= 0xC0
        if self.keepalive:
            assert self.keepalive < 65536
            msg[7] |= self.keepalive >> 8
            msg[8] |= self.keepalive & 0x00FF
        if self.lw_topic:
            sz += 2 + len(self.lw_topic) + 2 + len(self.lw_msg)
            msg[6] |= 0x4 | (self.lw_qos & 0x1) << 3 | (self.lw_qos & 0x2) << 3
            msg[6] |= self.lw_retain << 5

        i = 1
        while sz > 0x7f:
            premsg[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        premsg[i] = sz

        self.sock.write(premsg, i + 2)
        self.sock.write(msg)
        #print(hex(len(msg)), hexlify(msg, ":"))
        self._send_str(self.client_id)
        if self.lw_topic:
            self._send_str(self.lw_topic)
            self._send_str(self.lw_msg)
        if self.user is not None:
            self._send_str(self.user)
            self._send_str(self.pswd)
        resp = self.sock.read(4)
        assert resp[0] == 0x20 and resp[1] == 0x02
        if resp[3] != 0:
            raise MQTTException(resp[3])
        return resp[2] & 1

    def disconnect(self):
        self.sock.write(b"\xe0\0")
        self.sock.close()

    def ping(self):
        self.sock.write(b"\xc0\0")

    def publish(self, topic, msg, retain=False, qos=0):
        pkt = bytearray(b"\x30\0\0\0")
        pkt[0] |= qos << 1 | retain
        sz = 2 + len(topic) + len(msg)
        if qos > 0:
            sz += 2
        assert sz < 2097152
        i = 1
        while sz > 0x7f:
            pkt[i] = (sz & 0x7f) | 0x80
            sz >>= 7
            i += 1
        pkt[i] = sz
        #print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt, i + 1)
        self._send_str(topic)
        if qos > 0:
            self.pid += 1
            pid = self.pid
            struct.pack_into("!H", pkt, 0, pid)
            self.sock.write(pkt, 2)
        self.sock.write(msg)
        if qos == 1:
            while 1:
                op = self.wait_msg()
                if op == 0x40:
                    sz = self.sock.read(1)
                    assert sz == b"\x02"
                    rcv_pid = self.sock.read(2)
                    rcv_pid = rcv_pid[0] << 8 | rcv_pid[1]
                    if pid == rcv_pid:
                        return
        elif qos == 2:
            assert 0

    def subscribe(self, topic, qos=0):
        assert self.cb is not None, "Subscribe callback is not set"
        pkt = bytearray(b"\x82\0\0\0")
        self.pid += 1
        struct.pack_into("!BH", pkt, 1, 2 + 2 + len(topic) + 1, self.pid)
        #print(hex(len(pkt)), hexlify(pkt, ":"))
        self.sock.write(pkt)
        self._send_str(topic)
        self.sock.write(qos.to_bytes(1, "little"))
        while 1:
            op = self.wait_msg()
            if op == 0x90:
                resp = self.sock.read(4)
                #print(resp)
                assert resp[1] == pkt[2] and resp[2] == pkt[3]
                if resp[3] == 0x80:
                    raise MQTTException(resp[3])
                return

    # Wait for a single incoming MQTT message and process it.
    # Subscribed messages are delivered to a callback previously
    # set by .set_callback() method. Other (internal) MQTT
    # messages processed internally.
    def wait_msg(self):
        res = self.sock.read(1)
        self.sock.setblocking(True)
        if res is None:
            return None
        if res == b"":
            raise OSError(-1)
        if res == b"\xd0":  # PINGRESP
            sz = self.sock.read(1)[0]
            assert sz == 0
            return None
        op = res[0]
        if op & 0xf0 != 0x30:
            return op
        sz = self._recv_len()
        topic_len = self.sock.read(2)
        topic_len = (topic_len[0] << 8) | topic_len[1]
        topic = self.sock.read(topic_len)
        sz -= topic_len + 2
        if op & 6:
            pid = self.sock.read(2)
            pid = pid[0] << 8 | pid[1]
            sz -= 2
        msg = self.sock.read(sz)
        self.cb(topic, msg)
        if op & 6 == 2:
            pkt = bytearray(b"\x40\x02\0\0")
            struct.pack_into("!H", pkt, 2, pid)
            self.sock.write(pkt)
        elif op & 6 == 4:
            assert 0

    # Checks whether a pending message from server is available.
    # If not, returns immediately with None. Otherwise, does
    # the same processing as wait_msg.
    def check_msg(self):
        self.sock.setblocking(False)
        return self.wait_msg()
```

Code ESP client MQTT publieur (emetteur)
```python
# Complete project details at https://RandomNerdTutorials.com/micropython-mqtt-publish-dht11-dht22-esp32-esp8266/

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
from machine import Pin
import dht
esp.osdebug(None)
import gc
gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'
mqtt_server = '192.168.X.XXX'

client_id = ubinascii.hexlify(machine.unique_id())

topic_pub_temp = b'esp/dht/temperature'
topic_pub_hum = b'esp/dht/humidity'

last_message = 0
message_interval = 5

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')

sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))

def connect_mqtt():
  global client_id, mqtt_server
  #client = MQTTClient(client_id, mqtt_server)
  client = MQTTClient(client_id, mqtt_server, user="mqtt", password="bac")
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def read_sensor():
  try:
    sensor.measure()
    temp = sensor.temperature()
    # uncomment for Fahrenheit
    #temp = temp * (9/5) + 32.0
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      temp = (b'{0:3.1f}'.format(temp))
      hum =  (b'{0:3.1f}'.format(hum))
      return temp, hum
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')

try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    if (time.time() - last_message) > message_interval:
      temp, hum = read_sensor()
      print(temp)
      print(hum)
      client.publish(topic_pub_temp, temp)
      client.publish(topic_pub_hum, hum)
      last_message = time.time()
  except OSError as e:
    restart_and_reconnect()
```





<iframe width="560" height="315" src="https://www.youtube.com/embed/xpsZa3N3Ogo?si=Z1gpy_mkCGR-08uE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- [MicroPython and Home Assistant](https://www.pythontutorials.net/blog/micropython-home-assistant/){target=_blank}

https://www.raspberryme.com/micropython-mqtt-publie-dht11-dht22-avec-esp32-esp8266/


https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/

https://www.youtube.com/@christianducros/search?query=MQTT

https://github.com/peterhinch/micropython-mqtt
https://github.com/FredThx/FmPyIOT/tree/master






#### Installer un "broker" sur Raspberry Pi

Il s

https://www.lesalexiens.fr/domotique/tutoriel-installer-mosquitto-mqtt-sur-raspberry-pi/

##### Dans Home Assistant

<iframe width="560" height="315" src="https://www.youtube.com/embed/cQ8vqJgCVC8?si=1zmdvnXr92VrJtRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/NAvHHA4OS20?si=ORH0M4NY72nRqrtF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### S

```
# Connaitre son IP
ifconfig
# Faire la mise à jour
sudo apt update
sudo apt upgrade
```

Se connecter à distance
```
# Créer un compte utilisateur distant
sudo adduser <username>
...
# Lui donner les droits d'administration
sudo adduser <username> sudo
# Installer un serveur de bureau distant
sudo apt install xrdp
```
Depuis un PC Windows faire "Connexion bureau à distance" et saisir l'IP du raspberry pi

### ESP-NOW

Communication sans routeur : <https://www.raspberryme.com/micropython-esp-now-avec-esp32-demarrage/>

- [Micropython: ESP-Now avec ESP32 – Recevez des données (plusieurs à un)](https://www.raspberryme.com/micropython-esp-now-avec-esp32-recevez-des-donnees-plusieurs-a-un/)
- [Micropython: ESP32 ESP-Now Communication bidirectionnelle](https://www.raspberryme.com/micropython-esp32-esp-now-communication-bidirectionnelle/)
