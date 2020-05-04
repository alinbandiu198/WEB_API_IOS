import os 
from netmiko import ConnectHandler
import json 
import textfsm
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

cisco_iosSW2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.100',
    'username': 'alin',
    'password': 'cisco',
    'secret': 'cisco',
    }


net_connect =ConnectHandler(**cisco_iosSW2)
net_connect.enable()


def Loopback():
	for n in range (2,20):
		print ("Creating Loop" + str(n))
		config_commands = ['int loop' + str(n)]
		output = net_connect.send_config_set(config_commands)
	
	return output




def ospfconfigSW2():
    with open('SW2_Config_OSPF') as f:
    	linesSW2 = f.read().splitlines()
    print (linesSW2)


    	#net_connectSW1 = ConnectHandler(**cisco_iosSW1)
    	#net_connect.enable()
    output = net_connect.send_config_set(linesSW2)

    print ("Please wait... the ospf configuration for SW1 is almost done")
   
    print("the config is done!")
    return "The OSPF configuration for device1(Switch2) is done !"
#ospfconfigSW1()
def MonitoringOSPFSW2():
        
        vecini=[]
       
        output = net_connect.send_command('show ip ospf neigh', use_textfsm=True)
        #print (output)
        for neighbor in output:
            if neighbor['state'] == 'FULL/  -':
                print(f"ospf report: the {neighbor['neighbor_id']} device is the only neighbor")
                vecini.append(f"ospf report: the {neighbor['neighbor_id']} device is the only neighbor")
        return vecini   
#MonitoringOSPFSW2()

def MonitoringUPInterfacesSW2():
        interfete=[] # definesc o lista goala

        output = net_connect.send_command('show ip int brief',use_textfsm=True)
        #print("the next interfaces are in an UP state:")
        for interface in output:
            if interface['status']== 'up':
                print(f"{interface['intf']} is up")
                interfete.append(f"{interface['intf']} is up") # adaug la lista o linie noua cu continutul din print
        return interfete

#print(MonitoringUPInterfacesSW2())

def MonitoringDownInterfacesSW2():
  
        output = net_connect.send_command('show ip int brief',use_textfsm=True)
        #print (output)
        print("The next interfaces are in a down state")
        for interface in output:
            if interface['status']== 'down':
                print(f"{interface['intf']} is down")
                interfete.append(f"{interface['intf']} is down") # adaug la lista o linie noua cu continutul din print
        return interfete

#MonitoringDownInterfacesSW2()
def MonitoringRoutesSW2():
     
        #net_connect.enable()
        output = net_connect.send_command('show ip route')
        print (output)
        return output       

        
#MonitoringRoutesSW1()
def VLAN():
		
	vlan=[]
	output=net_connect.send_command("sh vlan brief", use_textfsm=True)
	print (json.dumps(output,indent=2))
	vlan.append(json.dumps(output,indent=2))        #print(f"{interface['intf']} is up")
	print(output)
	return output
