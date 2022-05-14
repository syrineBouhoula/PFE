import paho.mqtt.client as mqtt
import time
import datetime
from datetime import date
import smtplib
import timeit

filename="Alert execution time.csv"
#csv = open(filename, 'w')	
#csv.write("execution time average\n")
#csv.close

def alert():
 smtpUser = 'testingwork166@gmail.com'
 smtpPass = '94859534'

 toAdd = 'sirinebouhoula@gmail.com'
 fromAdd = smtpUser

 subject = 'Temperature alert'
 header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
 body = 'The temperature is higher than 20!!'
 print( header + '\n' + body)

 s = smtplib.SMTP('smtp.gmail.com',587)

 s.ehlo()
 s.starttls()
 s.ehlo()

 s.login(smtpUser, smtpPass)
 s.sendmail(fromAdd, toAdd, header + '\n' + body)

 s.quit()
# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("Robot/temp")
    client.subscribe("Robot/hum")

def on_message(client, userdata, msg):
    if msg.topic == "Robot/temp" :
      print(msg.topic+" "+str(msg.payload))
      temp = str(msg.payload)
      if temp >"20":
       alert()
    if msg.topic == "Robot/hum" :
      print(msg.topic+" "+str(msg.payload))
      
start = timeit.default_timer()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883, 60)

end = timeit.default_timer()
print("average",end-start)
csv = open(filename, 'a')
csv.write(str(end-start) + "\n")
csv.close() 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()


	
