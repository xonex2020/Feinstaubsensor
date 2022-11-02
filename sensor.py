import serial

ser = serial.Serial('COM3', baudrate=9600, stopbits=1, parity="N",  timeout=2)

while True:
    s = ser.read(1)
    if ord(s) == int("AA",16):
        s = ser.read(1)
        if ord(s) == int("C0",16):
            s = ser.read(7)
            a = []
            for i in s:
                a.append(i)
            print(a)
            pm2hb= s[0]
            pm2lb= s[1]
            pm10hb= s[2]
            pm10lb= s[3]
            cs = s[6]
            # we should verify the checksum... it is the sum of bytes 1-6 truncated...

            try:
                print("PM2.5 - ", float(pm2hb + pm2lb*256)/10.0 ," PM10 - ", float(pm10hb + pm10lb*256)/10.0)
            except:
                pass
    else:
        pass