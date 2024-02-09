import serial, time #import the libraries; serial library is used for the connection to micro:bit
port = "/dev/ttyACM0" #port value to connect the computer with micro: bit
baud = 115200
s = serial.Serial(port) #initialize the serial
s.baudrate = baud
while True:
    data = s.readline() # read the lines of data being sent via the serial connection
    print(data)
    time.sleep(1)