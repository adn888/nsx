import requests
import sys
import json
import login

#inject varliables from cli

vm = str(sys.argv[1])
id = str(sys.argv[2])

#variables
nsxmanager = "https://172.16.10.17"
nsxurla = "/api/v1/fabric/virtual-machines?included_fields=tags&included_fields=external_id&display_name=" + vm
nsxheaders = {"Content-Type": "application/json"}
nsxuser = login.username
nsxpass = login.password
nsxpayloads= {}

#get VMID

responsea = requests.request("GET", nsxmanager + nsxurla, headers=nsxheaders, auth=(nsxuser, nsxpass), data=nsxpayloads, verify=False)

a = responsea.json()

print (a)

vmid = str(a["results"] [0]["external_id"])


#variables for tag api call
nsxurlb = "/policy/api/v1/infra/tags/tag-operations/"+id
nsxpayloadb = {"tag":{"scope":"","tag":"quarantine"},"apply_to":[{"resource_type":"VirtualMachine","resource_ids":[""+vmid+""]}]}

#tag vm with quaratine

responseb = requests.request("PUT", nsxmanager + nsxurlb, headers=nsxheaders, auth=(nsxuser, nsxpass), data=json.dumps(nsxpayloadb), verify=False)

print(responseb.text.encode('utf8'))



