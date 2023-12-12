#credit to https://drive.google.com/drive/folders/1jknduoqpTljcf2N9Dq9d9-YIXfz-4yYu
class Authentication:
    @staticmethod
    def get_jsessionid(vmanage_host, vmanage_port, username, password):
        api = "/j_security_check"
        base_url = "https://%s:%s" % (vmanage_host, vmanage_port)
        url = base_url + api
        payload = {'j_username': username, 'j_password': password}

        response = requests.post(url=url, data=payload, verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            print("headers, cookies")
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            [print("No Valid JSESSION ID returned\n")]
            exit()

    @staticmethod
    def get_token(vmanage_host, vmanage_port, jsessionid):
        headers = {'Cookie': jsessionid}
        base_url = "https://%s:%s" % (vmanage_host, vmanage_port)
        api = "/dataservice/client/token"
        url = base_url + api
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            print("token", response.text)
            return(response.text)
        else:
            return None

import requests, json, urllib3
urllib3.disable_warnings()
vmanage_port = "8443"
vmanage_host = "184.169.141.21"
vmanage_username = "admin"
vmanage_password = "admin1"

Auth = Authentication()
jsessionid = Auth.get_jsessionid(vmanage_host, vmanage_port, vmanage_username, vmanage_password)
print("main jsession id", jsessionid)

token = Auth.get_token(vmanage_host, vmanage_port, jsessionid)
print("main token", token)

if token is not None:
    header = {'Content-Type': "application/json", 'Cookie': jsessionid, 'X-XSRF-TOKEN': token}
else:
    header = {'Content-Type': "application/json", 'Cookie': jsessionid}

'''
  
#device list in json
url = "https://" + vmanage_host + ":" + vmanage_port + "/dataservice/device"
payload={}
response = requests.request("Get", url, headers=header, data=payload, verify=False)
print(response.text)

'''