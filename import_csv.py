import os
import csv
import pyforti
import credendials

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
            del row[0]
            name=row[0]
            print ("Interface",row)
            del row[0]
            #device.update_system_interface(name,row)
            rc=device.get_interface(name)
            print (rc)
            
        else:
             print ("Unkown Object",row)
rc=device.get_firewall_address("test1")
print(rc)
