import requests
import sys
import json


vm = str(sys.argv[1])
id = str(sys.argv[2])

url = "https://172.16.10.17/api/v1/fabric/virtual-machines?included_fields=tags&included_fields=external_id&display_name="+ vm

payload = {}
headers = {
  'Authorization': 'Basic YWRtaW46Vk13YXJlMSFWTXdhcmUxIQ==',
  'Cookie': 'JSESSIONID=B3461C2F4C8D0D7E47AD00AF5DE2E60D'
}

response = requests.request("GET", url, headers=headers, data = payload, verify=False)

#print(response.text.encode('utf8'))

a = response.json()

#print(a)

b = str(a['results'] [0]['external_id'])

url = "https://172.16.10.17/policy/api/v1/infra/tags/tag-operations/"+id

payload = "{\n  \"tag\": {\n    \"scope\": \"\",\n    \"tag\": \"quarantine\"\n   },\n  \"apply_to\": [\n    {\n         \"resource_type\": \"VirtualMachine\",\n         \"resource_ids\": [\n            \""+b+"\"\n          ]\n    }\n  ]\n}"
headers = {
  'Authorization': 'Basic YWRtaW46Vk13YXJlMSFWTXdhcmUxIQ==',
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=691A435A96611A3D4BE58994BF3C1FC2'
}

response = requests.request("PUT", url, headers=headers, data = payload, verify=False)

print(response.text.encode('utf8'))




#print(response.text.encode('utf8'))

#if __name__ == "__main__":




