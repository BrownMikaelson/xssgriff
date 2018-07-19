# -*- coding: utf-8 -*-
#XSS JVZIOR
#https://www.linkedin.com/in/ataide-junior-050231b0/
#https://www.facebook.com/JRPENTESTER
#@ataidejuniior

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
        print('\033[31m'+'HOOOO vulneravel'+'\033[0;0m'+ payload)
        if(payload not in vuln):
            vuln.append(payload)
    else:
        print "Nao vulneravel =( "

print "--------------------\nLista de Payloads:"
print '\n'.join(vuln)
