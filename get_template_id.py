import requests

url = "https://10.10.20.230/j_security_check"

payload='j_username=admin&j_password=C1sco12345'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


import requests

url = "https://10.10.20.230/dataservice/client/token"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


import requests

url = "https://10.10.10.230/dataservice/template/feature"

payload='X-XSRF-TOKEN=972F2C0D824E0BA5E54BAD24DBFFF8A568B50DB369BF30FB2F4CE50A4BAB6924DFCA0F5854D794A571137D59C24AADB67ED5'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
