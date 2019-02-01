from firebase import firebase
import time
import datetime
# from grovepi import *
# import grovepi

#Firebase Application
firebase = firebase.FirebaseApplication('https://pi-sensor-data.firebaseio.com/', None)

#GrovePi sensors
sound_sensor = 0 #connect the sound sensor into the A0 analog port
light_sensor = 1 #connect the Light sensor into the A1 analog port
dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor

while True:
    try:
        #TimeStamp Method
        def getTime():
            ts = time.time()
            stamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            return stamp
            
        
        #Gets the value from the sound sensor
        def getSound():
            sound_value = {"time": getTime(),
                           "data": 1 }#grovepi.analogRead(sound_sensor)
            time.sleep(1)
            return sound_value
        
        #Gets the value from the light sensor
        def getLight():
            light_value = {"time": getTime(),
                           "data": 1 }#grovepi.analogRead(light_sensor)
            time.sleep(1)
            return light_value
            
        #Gets the value of temperature and humidity but only returns temperature
        def getTemp():
            temp = {"time": getTime(),
                           "data": 1 }#dht(dht_sensor_port,dht_sensor_type)
            time.sleep(1)
            return temp
            
        #Gets the value of temperature and humidity but only returns humidity
        def getHumidity():
            hum = {"time": getTime(),
                           "data": 1 }#dht(dht_sensor_port,dht_sensor_type)
            time.sleep(1)
            return hum
            
        #Sound Sensor
        if firebase.get('sensors/sound', 'running') == True:
            firebase.post('sensors/sound/sensor-data', getSound())
        else:
            print "Sound Sensor isn't running"
        
        #Light Sensor
        if firebase.get('sensors/light', 'running') == True:
            firebase.post('sensors/light/sensor-data', getLight())
        else:
            print "Light Sensor isn't running"
        
        #Temp Sensor 
        if firebase.get('sensors/temp', 'running') == True:
            firebase.post('sensors/temp/sensor-data', getTemp())
        else:
            print "Temp Sensor isn't running"
        
        #Humidity Sensor
        if firebase.get('sensors/humidity', 'running') == True:
            firebase.post('sensors/humidity/sensor-data', getHumidity())
        else:
            print "Humidity Sensor isn't running"
        
        
        print "Success"
        time.sleep(5)
    except:
        print "An Error occurred"