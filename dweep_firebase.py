from firebase import firebase
import time
import datetime
from threading import Thread

# from grovepi import *
# import grovepi

#Firebase Application
firebase = firebase.FirebaseApplication('https://pi-sensor-data.firebaseio.com/', None)

#GrovePi sensors
sound_sensor = 0 #connect the sound sensor into the A0 analog port
light_sensor = 1 #connect the Light sensor into the A1 analog port
dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor


##Have Different Threads that listen for any change and automaticaly change the variables for speed and on/off


#TimeStamp Method
def getTime():
    ts = time.time()
    stamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    return stamp
            
        
#Gets the value from the sound sensor
def getSound():
    speed = firebase.get('sensors/sound', 'speed')
    if firebase.get('sensors/sound', 'running') == True:
       
        sound_value = {"time": getTime(), "data": 1 }#grovepi.analogRead(sound_sensor)
        
        firebase.post('sensors/sound/sensor-data', sound_value)
        
        print("Sound Sensor Value added")
    else:
        print "Sound Sensor isn't running"
    time.sleep(speed)
    return
            
        

#Gets the value from the light sensor
def getLight():
    speed = firebase.get('sensors/light', 'speed')
    if firebase.get('sensors/light', 'running') == True:
        
        light_value = {"time": getTime(),"data": 1 }#grovepi.analogRead(light_sensor)
        
        firebase.post('sensors/light/sensor-data', light_value)
        
        print "Light Sensor Value added"
    else:
        print "Light Sensor isn't running"
    time.sleep(speed)
    return
            
        
#Gets the value of temperature and humidity but only returns temperature
def getTemp():
    speed = firebase.get('sensors/temp', 'speed')
    if firebase.get('sensors/temp', 'running') == True:
        
        temp = {"time": getTime(),"data": 1 }#dht(dht_sensor_port,dht_sensor_type)
        
        firebase.post('sensors/temp/sensor-data', temp)
        
        print "Temp Sensor Value added"
    else:
        print "Temp Sensor isn't running"
    time.sleep(speed)
    return

            
        
#Gets the value of temperature and humidity but only returns humidity
def getHumidity():
    speed = firebase.get('sensors/humidity', 'speed')
    if firebase.get('sensors/humidity', 'running') == True:
        
        hum = {"time": getTime(),"data": 1 }#dht(dht_sensor_port,dht_sensor_type
        
        firebase.post('sensors/humidity/sensor-data', hum)
        
        print "Humidity Sensor Value added"
    else:
        print "Humidity Sensor isn't running"
    time.sleep(speed)
    return


class Sound_Sensor(Thread):
    def run(self):
        while True:
            getSound();

class Light_Sensor(Thread):
    def run(self):
        while True:
            getLight();
            
class Temp_Sensor(Thread):
    def run(self):
        while True:
            getTemp();
            
class Humidity_Sensor(Thread):
    def run(self):
        while True:
            getHumidity();
            
def run():
    Sound_Sensor().start()
    Light_Sensor().start()
    Temp_Sensor().start()
    Humidity_Sensor().start()
    
run()