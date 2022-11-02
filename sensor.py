import serial.tools.list_ports
from serial.tools import list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select Port: COM")
print(val)


for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portList[x])

serialInst.baurate = 9600
serialInst.port = portVar
serialInst.open()


packet = serialInst.readline()
var1 = ''
list = [var1.apped(packet)]
var1.apped(packet)
print(list)