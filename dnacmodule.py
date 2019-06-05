import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import pprint

#getToken
def getToken(username, password, base_url):
    url = base_url + "/api/system/v1/auth/token"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, auth=(username, password), verify=False)
    # token
    token = response.json()
    token = token['Token']
    return(token)

#getDevices
def getDevices(base_url, token):
    url = base_url + "/dna/intent/api/v1/network-device"
    headers = {
    'Content-Type': 'application/json',
    'x-auth-token': token
    }
    response = requests.get(url, headers=headers, verify=False)
    response = response.json()
    response = response['response']
    return(response)