# -*- coding: utf-8 -*-
#XSS JVZIOR

print "                          _  __ "
print " __  _____ ___  __ _ _ __(_)/ _|"
print "\ \/ / __/ __|/ _` | '__| | |_ "
print " >  <\__ \__ \ (_| | |  | |  _|"
print "/_/\_\___/___/\__, |_|  |_|_|   "
print "              |___/            "

import requests
fname = "payloads.txt"
with open(fname) as f:
    content = f.readlines()
payloads = [x.strip() for x in content] 
url = raw_input("URL: ")
vuln = []
for payload in payloads:
    payload = payload
    xss_url = url+payload
    r = requests.get(xss_url)
    if payload.lower() in r.text.lower():
        print("Vulneravel: " + payload)
        if(payload not in vuln):
            vuln.append(payload)
    else:
        print "Nao vulneravel =( "

print "--------------------\nLista de Payloads:"
print '\n'.join(vuln)