# -*- coding: utf-8 -*-
#XSS JVZIOR

print "_  _ ____ ____ ____ ____ _ ____ ____ "
print " \/  [__  [__  | __ |__/ | |___ |___   "
print "_/\_ ___] ___] |__] |  \ | |    |     "                                   

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
