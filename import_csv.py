import csv
import pyfortiapi

device = pyfortiapi.FortiGate(ipaddr="192.168.173.75",
                                username="admin",
                                password="admin123")


with open('/home/andy/Entwicklung/Python/fortinet/objects.csv', 'r') as f:
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
            print ("Interface",row)
            device.
            
        else:
             print ("Unkown Object",row)
rc=device.get_firewall_address("test1")
print(rc)
