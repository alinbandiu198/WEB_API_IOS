
from flask import Flask , render_template , redirect, url_for,request 
from Device1 import  ospfconfigSW1, DeleteOSPFSW1, MonitoringOSPFSW1, MonitoringDownInterfacesSW1,MonitoringUPInterfaces,MonitoringRoutesSW1,VLAN,CVLAN,Loop1
from Device2 import ospfconfigSW2,MonitoringOSPFSW2,MonitoringUPInterfacesSW2,MonitoringDownInterfacesSW2,MonitoringRoutesSW2
from napalm_script import  CPU1,CPU2
from netmiko import ConnectHandler 
import netmiko
import json 




app=Flask(__name__)
app.static_folder = 'static'



@app.route('/', methods=['GET', 'POST'])
def index():
        print("Cisco WEB API....")
        output="Welcome to My Cisco WEB API!Please Choose What you want to do from the buttons above"
        if request.method=='POST':
                if request.form["buton_config"]=="Configure OSPF for Switch1":

                        output=ospfconfigSW1()
                        return render_template('index.html',output=output)
                elif request.form["buton_config"]=="OSPF-Switch2":
                        output=ospfconfigSW2()
                        return render_template('index.html',output=output)

                elif  request.form["buton_config"]=="CPU1":
                        output=CPU1()
                        
                        return render_template('index.html',output=output)


                elif request.form["buton_config"]=="CVLAN":
                        output=CVLAN()
                        return render_template('index.html',output=output)

                elif request.form["buton_config"]=="loop1":
                        output=Loop1()
                        return render_template('index.html',output=output)

                
                elif request.form["buton_config"]=="Show Working Interfaces -SW1":
                        output=MonitoringUPInterfaces()
                        output='\n'.join(map(str,MonitoringUPInterfaces()))  #extract doar stringurile din lista
                        return render_template('index.html',output=output)
                
               
                elif request.form["buton_config"]=="View OSPF Neighbor on Switch1":
                        output=MonitoringOSPFSW1()
                        output='\n'.join(map(str,MonitoringOSPFSW1()))
                        return render_template('index.html',output=output) 
                elif request.form["buton_config"]=="Vlans":
                        output=VLAN()
                        output='\n'.join(map(str,VLAN()))
                        
                        return render_template('index.html',output=output)


                
                elif request.form["buton_config"]=="Show DOWN Interfaces-SW1": 
                        output='\n'.join(map(str,MonitoringDownInterfacesSW1()))
                        return render_template('index.html',output=output)

                       
                elif request.form["buton_config"]=="View OSPF Neighbor on Switch2":
                        output='\n'.join(map(str,MonitoringOSPFSW2()))
                        return render_template('index.html',output=output)


                elif request.form["buton_config"]=="Routing Table For Switch1":
                        output=MonitoringRoutesSW1()
                        return render_template('index.html',output=output)

                elif request.form["buton_config"]=="Routing Table For Switch2":
                        output=MonitoringRoutesSW2()
                        return render_template('index.html',output=output)

                elif request.form["buton_config"]=="Disable OSPF for SW1":
                        output=DeleteOSPFSW1()
                        return render_template('index.html',output=output)









        else:
                return render_template('index.html',output=output)
        return render_template('index.html',output=output)
                             


if __name__ == '__main__':
        app.run(host="0.0.0.0",port=8080,debug=True)





