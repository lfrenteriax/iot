import passw
import name
import paho.mqtt.client as mqtt
import os, urlparse
import led
import sensor
userName=name.name
boardName=name.board
led_state='on'
led.ledState(led_state)
sensor_val=0
ledV={'on':'Apagado','off':'Encendido'}
def publish(msg):
	print (msg)
	mqttc.publish(topic, msg)
def doAction(msg):
	global led_state
	n,f,v=msg.split(":")
	if n==(userName+boardName):
		if f=='led_state':
			#print (f,led_state)
			if led_state== 'on':
				led_state='off'
			elif led_state== 'off':
				led_state='on'
		#print (led_state)
                        led.ledState(led_state)
			publish(boardName+userName+':led_state:'+str(ledV[led_state]))
		elif f=='new':
			publish(boardName+userName+':led_state:'+str(led_state))
			publish(boardName+userName+':sensor_val:'+str(sensor_val))
# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    doAction(str(msg.payload));

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log


# Connect
mqttc.username_pw_set(passw.user, passw.psw)
mqttc.connect(passw.server, passw.port)
topic='/cloudmqtt'
# Start subscribe, with QoS level 0
mqttc.subscribe(topic, 0)

# Publish a message
mqttc.publish(topic, boardName+userName+":led_state:"+ str(led_state))
mqttc.publish(topic, boardName+userName+":sensor_val:"+str(sensor_val))
# Continue the network loop, exit when an error occurs
rc = 0
import time
while rc == 0:
	time.sleep(2)
	sensor_val=sensor.read()
	mqttc.publish(topic, boardName+userName+":sensor_val:"+str(sensor_val))
	rc = mqttc.loop()
print("rc: " + str(rc))




