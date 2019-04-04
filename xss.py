# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import ast
import requests
import urllib.parse
import urllib.request
import sys

print ("                         _  __  __ ")
print ("                        (_)/ _|/ _|")
print ("__  _____ ___  __ _ _ __ _| |_| |_ ")
print ("\ \/ / __/ __|/ _` | '__| |  _|  _|")
print (" >  <\__ \__ | (_| | |  | | | | |  ")
print ("/_/\_|___|___/\__, |_|  |_|_| |_|  ")
print ("               __/ |               ")
print ("              |___/                ")
print ("\r")
print ("Please using HTTP/HTTPS")
print ("Ex: http://wwww or https://wwww")
print ("Creator - Ataide Junior")
print ("\r")

##txt payloads

fname = "payloads.txt"

with open(fname) as f:
    content = f.readlines()
payloads = [x.strip() for x in content] 
url = input('Url: ')
vuln = []
for payload in payloads:
    payload = payload
    xss_url = url+payload
    r = requests.get(xss_url)
    if payload.decode('utf-8') in r.text.lower():
        print('Exploitable =D '+payload)
        if(payload not in vuln):
            vuln.append(payload)
    else:
        print ("No Exploitable= ")
print ("--------------------\nLista de Payloads:")
print ('\n'.join(vuln))
