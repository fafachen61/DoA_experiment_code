import paho.mqtt.client as receive #import library
import wifi
import time

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
	
MQTT_SERVER = "192.168.50.117" #specify the broker address
MQTT_PATH = "temp2" #this is the name of topic, like temp
client = receive.Client()
client.connect(MQTT_SERVER, 1883, 60)
name = str(input('which Wi-Fi AP will you measure?'))
number = 100
cnt = 0
while True:
    try:
        cells1 = wifi.Cell.all('wlan1')#difference port
        cells2 = wifi.Cell.all('wlan2')#sum port
        for cell in cells1:
            if cell.ssid == name:
                r1 = cell.signal
                print ('1',cell.ssid.encode('utf-8'),cell.signal,cell.frequency.encode('utf-8'),cell.channel,cell.address.encode('utf-8'))
        for cell in cells2:
            if cell.ssid == name:
                r2 = cell.signal
                print ('2',cell.ssid.encode('utf-8'),cell.signal,cell.frequency.encode('utf-8'),cell.channel,cell.address.encode('utf-8'))
        r = r1-r2
        print(r)
        client.on_message = on_message
        client.publish(MQTT_PATH, r)
        client.loop_start()
        cnt = cnt + 1
    except:
        print('pass')

    time.sleep(1000)



