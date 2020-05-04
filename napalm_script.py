
import json
from napalm import get_network_driver
import os
 
driver=get_network_driver("ios")
optional_args = {'secret': 'cisco'}
device1=driver(hostname="192.168.122.115", username="alin", password="cisco", optional_args=optional_args)
print("opening")
device1.open()
device2=driver(hostname="192.168.122.100", username="alin", password="cisco", optional_args=optional_args)
device2.open()


def CPU1():
	cpu1=[]
	out = json.dumps(device1.get_environment(),indent=2)
	for cpu in out:
		if cpu["cpu"]=="0":
			print(f"the ussage {cpu['0']} is used")
			cpu1.append(f"the cpu is currently: {cpu['0']} used")

	return cpu1
CPU1()
	
	

CPU1()
def CPU2():
	out=device2.get_environment()
	out1 = out['cpu']
	rel1=print(json.dumps(out1,indent=4))
	return rel1













def IpDevice2():
	out2=device2.get_interfaces_ip()
	print(json.dumps(out2,indent=4)) 









