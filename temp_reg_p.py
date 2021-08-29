#run this script from the terminal. 'cd' to the file location and run 'python3 temp_reg.py'
import os
import time
import Adafruit_DHT

#set sensor name (DHT22) and pin number.
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
#name and set the location of your csv file. The file name is humiditytest.csv. For evvery 
try:
    f = open('/home/pi/humidity_test3.csv', 'a+')
    if os.stat('/home/pi/humidity_test3.csv').st_size == 0:
            f.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    #register temperature, humidity, and the time (hour and minute)
    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        print("{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n".format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    #set time in seconds for every n number of seconds you want to register a temperature reading
    time.sleep(30)