import os
import csv
import socket
import pyforti
import credendials


def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask

def netmask_to_cidr(netmask):
    return (sum([bin(int(x)).count('1') for x in netmask.split('.')]))




device = pyforti.FortiGate(ipaddr=credendials.fgt,
                                username=credendials.un,
                                password=credendials.pw)
path=os.getcwd()

file='objects.csv'
myobjects=(path+'/'+file)

os.path.join(path,path,file)
with open(myobjects, 'r') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    
    for row in reader:
        if row[0]=="address":
            del row[0]
            print ("address",row)
            name=row[0]
            ip_mask= row[1]
            rc=device.add_firewall_address(name,ip_mask)
            if (rc!=200):
                print ("Objekt: "+name+" konnte nicht angelegt werden")
                              
        elif row[0]=="route":
            del row[0]
            print ("route",row)
            rc=device.add_route(row)
            if (rc!=200):
                print ("Route konnte nicht angelegt werden")
            
        elif row[0]=="address_group":
            
            del row[0]
            print ("Group",row)
            name=row[0]
            del row[0]
            rc=device.add_firewall_group(name,row)
            if (rc!=200):
                print ("Address_group: "+name+" konnte nicht angelegt werden")
        elif row[0]=='interface':
            rc=device.get_interface()
            print (rc)
            del row[0]
            name=row[0]
            del row[0]
            ip,netmask=row[0].split()
            cidr=netmask_to_cidr(netmask)
            mydict={'ip':ip+'/'+str(cidr)}
            
            rc=device.update_system_interface(name,mydict)
            print (rc)
            name="port3"
            rc=device.get_interface("port3")
            print (rc)
            
        else:
             print ("Unkown Object",row)
rc=device.get_firewall_address("test1")
print(rc)
rc=device.get_dhcp_server()
print (rc)