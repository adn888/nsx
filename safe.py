import requests
import sys
import json


vm = str(sys.argv[1])
id = str(sys.argv[2])

url = "https://172.16.10.17/api/v1/fabric/virtual-machines?included_fields=tags&included_fields=external_id&display_name="+ vm

payload = {}
headers = {
  'Authorization': 'Basic USERNAME',
  'Cookie': 'PASSWORD'
}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)

#print(response.text.encode('utf8'))

a = response.json()

#print(a)

b = str(a['results'] [0]['external_id'])

url = "https://172.16.10.17/policy/api/v1/infra/tags/tag-operations/"+id

payload = "{\n  \"tag\": {\n    \"scope\": \"\",\n    \"tag\": \"quarantine\"\n   },\n  \"remove_from\": [\n    {\n         \"resource_type\": \"VirtualMachine\",\n         \"resource_ids\": [\n            \""+b+"\"\n          ]\n    }\n  ]\n}"
headers = {
  'Authorization': 'Basic USERNAME',
  'Content-Type': 'application/json',
  'Cookie': 'PASSWORD'
}

response = requests.request("PUT", url, headers=headers, data = payload, verify=False)

print(response.text.encode('utf8'))


