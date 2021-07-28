import paho.mqtt.client as receive #import library
import rssi
import time

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
	
MQTT_SERVER = "192.168.50.117" #specify the broker address
MQTT_PATH = "temp2" #this is the name of topic, like temp
client = receive.Client()
client.connect(MQTT_SERVER, 1883, 60)
name = 'EEEEEE'#str(input('which Wi-Fi AP will you measure?'))
number = 100
cnt = 0
interface1 = 'wlan0'
interface2 = 'wlan2'
interface3 = 'wlan1'
while True:
        print('start scan 1')
        rssi_scanner1 = rssi.RSSI_Scan(interface1)#difference port
        ap_info1 = rssi_scanner1.getAPinfo(networks=[name], sudo=True)
        print(ap_info1)
        #print(type(ap_info1))
        rssi_scanner2 = rssi.RSSI_Scan(interface2)#sum port
    
        ap_info2 = rssi_scanner2.getAPinfo(networks=[name], sudo=True)
        rssi_scanner3 = rssi.RSSI_Scan(interface3)
        ap_info3 = rssi_scanner3.getAPinfo(networks=[name], sudo=True)
        for cell in ap_info1:
            
            #print(cell['ssid'], cell['signal'])
            if cell['ssid'] == name:
                r1 = cell['signal']
                print('signal1: ',r1) 
                #print ('1',cell['ssid'].encode('utf-8'),cell['signal'],cell.frequency.encode('utf-8'),cell.channel,cell.address.encode('utf-8'))
        for cell in ap_info2:
            if cell['ssid'] == name:
                r2 = cell['signal']
                print('signal2: ',r2)
                #print ('2',cell.ssid.encode('utf-8'),cell.signal,cell.frequency.encode('utf-8'),cell.channel,cell.address.encode('utf-8'))
        for cell in ap_info3:
            if cell['ssid'] == name:
                r3 = cell['signal']
                print('default: ',r3)
        r = r1-r2
        print(r)
        client.on_message = on_message
        client.publish(MQTT_PATH, r)
        client.loop_start()
        cnt = cnt + 1



