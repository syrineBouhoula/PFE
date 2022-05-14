import paho.mqtt.client as mqtt
import time
import datetime
from datetime import date

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Robot/temp")
    client.subscribe("Robot/hum")

filename="sensorData.csv"
#csv = open(filename, 'w')	
#csv.write("TimeStamp,Temperature,Humidity\n")
#csv.close
# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
    if msg.topic == "Robot/temp" :
      entry = time.time()
      print(msg.topic+" "+str(int(msg.payload)))
      temp = str(msg.payload)
      csv = open(filename, 'a')
      try:
        csv.write(str(entry) + ",")
        csv.write(str(int(msg.payload)))
      finally:
        csv.close()
    if msg.topic == "Robot/hum" :
      print(msg.topic+" "+str(int(msg.payload)))
      hum = str(int(msg.payload))
      csv = open(filename, 'a')
      try: 
        csv.write("," + hum + "\n")
      finally:
        csv.close()
    #entry = 
    #entry = entry +";"+ temp +";" + "\n"
    #csv = open(filename, 'a')
    #try: 
    #    csv.write(entry)
    #finally:
     #   csv.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
