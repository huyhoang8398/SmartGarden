#!/usb/bin/env python

import sys
import os
import time
import array

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
ser.write('D')

cMoisture = ser.read_until('\r')
ss_index = "13:"
print (cMoisture)

dataLora = ss_index + cMoisture 

sys.path.append(
	os.path.join(
		os.path.dirname(__file__),
		'..'
	)
)

import lib as pyrfm

conf={
	'll':{
		'type':'rfm95'
	},
	'pl':{
		'type':	'serial_seed',
		'port':	'/dev/ttyUSB1'
	}
}
ll=pyrfm.getLL(conf)

print('HW-Version: ', ll.getVersion())
if ll.setOpModeSleep(True,True):
    ll.setFiFo()
    ll.setOpModeIdle()
    ll.setModemConfig('Bw125Cr45Sf128');
    ll.setPreambleLength(8)
    ll.setFrequency(868)
    ll.setTxPower(13)
    # f = open("capa.txt", "r")
    # cMoisture = f.read() 
    ll.sendStr(cMoisture)
    ll.waitPacketSent()