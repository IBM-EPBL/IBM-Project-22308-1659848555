import wiotp.sdk.device
import time
import os
import datetime
import random
myConfig = {
"identity": {
"orgId": "3wc7ia",
"typeId": 
"NodeMCU",
"deviceId": "12345"
},
"auth": {
"token": "12345678"
}
}
client = wiotp.sdk.device.DeviceClient (config=myConfig,
logHandlers=None)
client.connect ()
def myCommandCallback (cmd) :
print ("Message received from IBM IoT Platform: %s" %
cmd.data['command'])
m=cmd.data['command']
if (m=="motoron"):
print ("Motor is switched on")
elif (m=="motoroff"):
print ("Motor is switched OFF")
print (" ")
while True:
soil=random.randint (0,100)
temp=random.randint (-20, 125)
hum=random.randint (0, 100)
myData={'soil moisture':soil, 'temperature':temp, 'humidity':hum}
client.publishEvent (eventId="status", msgFormat="json",
data=myData, qos=0 , onPublish=None)
print ("Published data Successfully: %s", myData)
time.sleep (2)
client.commandCallback = myCommandCallback
client.disconnect (