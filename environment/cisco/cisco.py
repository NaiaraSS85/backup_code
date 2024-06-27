from netmiko import ConnectHandler
import csv
import pyjq
import json
import requests
import netmiko
import os
from datetime import datetime
#Open inventory file and list ips for cisco_nxos
with open('inventory.json') as fid:
    inventory = json.load(fid)
#####List hostnames
    devices=pyjq.all('.[] | select(.platform | contains("cisco_")) | [.hostname, .ip, .category, .platform, .port, .command]', inventory)
    print(devices)
#####Create txt file to save the configuration:
    for device in devices:
       today = datetime.today()
       filename =  device[0] + '-' + today.strftime("%Y_%m_%d")
       f=open('/home/rconfig/data/'+device[2]+'/'+device[0]+'/'+filename+'.txt', "w")
       connection = ConnectHandler(device[1], port=device[4], username='{DEVICE_USERNAME}', password='{DEVICE_PASSWORD}', device_type=device[3])
       print(connection)
       output = connection.send_command(device[5])
       f.write(output)
       f.close()
       print(f'Closing connection for "{device[0]}"')
       connection.disconnect()
