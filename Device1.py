import os 
from netmiko import ConnectHandler
import json 
import textfsm
from netmiko.ssh_exception import  NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
cisco_iosSW1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.115',
    'username': 'alin',
    'password': 'cisco',
    'secret': 'cisco',
    'port':'22',
    }




net_connect =ConnectHandler(**cisco_iosSW1)
time.sleep(1)
net_connect.enable()
time.sleep(1)



def ospfconfigSW1():
    with open('SW1_Config_OSPF') as f:
    	linesSW1 = f.read().splitlines()
    print (linesSW1)


    	#net_connectSW1 = ConnectHandler(**cisco_iosSW1)
    	#net_connect.enable()
    output = net_connect.send_config_set(linesSW1)

    print ("Please wait... the ospf configuration for SW1 is almost done")
   
    print("the config is done!")
    return "The OSPF configuration for device1(Switch1) is done !"
#ospfconfigSW1()


def DeleteOSPFSW1():
      with open('Delete_OSPF_config_SW1') as f:
        linesSW1 = f.read().splitlines()
        #net_connect.enable()
        output = net_connect.send_config_set(linesSW1)
        print (output)
        return "The OSPF Protocol was removed from the SW1 device ! Check The neighbor statement!"

#DeleteOSPFSW1()
      

def MonitoringOSPFSW1():
        #net_connect = ConnectHandler(**cisco_iosSW1)
        vecini=[]            
        #net_connect.enable()
        output = net_connect.send_command('show ip ospf neigh',use_textfsm=True)
        print (json.dumps(output, indent=4))
        for neighbor in output:
            if neighbor['state'] == 'FULL/  -':
                print(f"ospf report: the {neighbor['neighbor_id']} device is the only neighbor")
                vecini.append(f"ospf protocol is Running! : the {neighbor['neighbor_id']} device is the only neighbor")
        return vecini		
#MonitoringOSPFSW1()

def MonitoringDownInterfacesSW1():
        interfete=[]
        
        #net_connect.enable()
        output = net_connect.send_command('show ip int brief', use_textfsm=True)
        #print (json.dumps(output,indent 2))
        print("The next interfaces are in a down state")
        
        for interface in output:
            if interface['status']== 'down':
                print(f"{interface['intf']} is down")
                interfete.append(f"{interface['intf']} is down") # adaug la lista o linie noua cu continutul din print
        
        return interfete
#MonitoringDownInterfacesSW1() 



def MonitoringUPInterfaces():
        interfete=[]
        #net_connect = ConnectHandler(**cisco_iosSW1)
        #net_connect.enable()
        output = net_connect.send_command('show ip int brief', use_textfsm=True)
        print (json.dumps(output,indent=2))

        #print("The next interfaces are in an UP state")
        for interface in output:
            if interface['status']== 'up':
            	print(f"{interface['intf']} is up")
            	interfete.append(f"{interface['intf']} is up") 
        return interfete        
#MonitoringUPInterfaces()
def MonitoringRoutesSW1():
     
        #net_connect.enable()
        output = net_connect.send_command('show ip route')
        print (output)
        return output       

        net_connect.disconnect()
        net_connect.close_session_log()
#MonitoringRoutesSW1()

def VLAN():
		
	vlan1=[]
	output=net_connect.send_command("sh vlan brief", use_textfsm=True)
	#print (json.dumps(output,indent=2))
	for vlan in output:
		if vlan['name']=='WEB':
			print(f"vlan {vlan['vlan_id']} is currently configured")
			vlan1.append(f"vlan {vlan['vlan_id']} is currently configured")
	return vlan1 
	#vlan.append(json.dumps(output,indent=2))        #print(f"{interface['intf']} is up")
	#print(output)
	#return output


def CVLAN():
	user=20;
	for i in range(user):
		print ("Creating Vlans" + str(i))
		config_commands = ['vlan ' + str(i),'name WEB vlan' + str(i)]
		output = net_connect.send_config_set(config_commands)
		message = "Success ! 20 Vlans were created on this device ! Please verify in the Monitoring section!"
	return message

def Loop1():
	for n in range (2,20):
		print ("Creating Loop" + str(n))
		config_commands = ['int loop' + str(n)]
		output = net_connect.send_config_set(config_commands)
		message = "Succes! 20 Loopbacks were configured in this device!"
	return message
