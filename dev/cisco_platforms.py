import common_prompts as cp

questions_nso = [
{
"question" : """
NSO - Network Services Orchestrator

Uses YANG data model
Multivendor

Components:
    CDB - Configuration Database
    Service Manager
    Device Manager
    Mapping Logic

API Northbound:
    Netconf, Restconf, CLI,
    JSON/RPC, Web GUI, SNMP

API Southbound:
    NEDs
    Netconf, Restconf, CLI,
    OpenFlow, SNMP

SDKs available

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

# Get a list of all devices:
GET https://1.1.1.1/restconf/data/tailf-ncs:devices/device
{
    "Authorization": "Basic yd76eGhey85",
    "Accept": "application/yang-data+json"
}

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]


questions_uc = [
{
"question" : """
###################################
###     UC and Webex Stuff      ###
###################################

* AXL (Administrative XML) API: SOAP interface to manage CUCM objects
* Zeep SOAP client library for Python
    pip install zeep
* CiscoAXL SDK for Python
    pip install ciscoaxl

* CUCM UDS (User Data Services): REST API using XML data format

Provides access to user resources adn entities, such as a user's devices, subscribed services,
and speed dials from the UC config database?
""",
"answer" : "uds",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Which method does an XML API always use?
""",
"answer" : "POST",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Cisco AXL is which type of API?
""",
"answer" : "xml/soap",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Cisco Finesse Call Center

* Call center product offering
* Finesse APIs (Desktop, Configuration, Servicability, Notification Service), uses XML encoding,
    and Basic Auth (Base64).

Finesse APIs use which encoding?
""",
"answer" : "xml",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Finesse APIs use which authentication?
""",
"answer" : "basic auth",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//---------
Webex Teams
//---------

Rest based API.

Four ways to acces Webex Teams API:
    Personal Access Tokens, Integrations, Bots, Guest issuers

Integration uses (Oauth), register the integration, request permissions for OAuth
Guest Issuers: uses JSON Web Token

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Create new Webex room and team:

import json
import requests

# New Room (now called a space):
url='https://api.ciscospark.com/v1/rooms'
headers = { 'Authorization: 'Bearer {TOKEN}', 'Content-Type': 'application/json'}
payload = {'title': 'New Room'} # teamID is optional
response = requests.post(url, data=json.dumps(payload), headers=headers)
# Should return a 200
print(response.json())

# New Team
url='https://webexapis.com/v1/teams'
payload = {'name': 'New Team'}

Content-Type is?
""",
"answer" : "application/json",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Add a member to a Webex room:
url='https://webexapis.com/v1/memberships'
headers = { 'Authorization: 'Bearer {TOKEN}', 'Content-Type': 'application/json'}
payload = {
    'roomId': 'dsa76Fd83Fgeei83ndyu3',
    'personEmail': 'bobby@bobby.com',
    'personDisplayName': 'Bobby',
    'isModerator': 'false',
    }
response = requests.post(url, data=json.dumps(payload), headers=headers)

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Add a message to a Webex room:
url='https://webexapis.com/v1/messages'
headers = { 'Authorization: 'Bearer {TOKEN}', 'Content-Type': 'application/json'}
payload = {
    'roomId': 'dsa76Fd83Fgeei83ndyu3',
    'text': 'This is the new message',
    }
response = requests.post(url, data=json.dumps(payload), headers=headers)

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Webex REST API endpoints overview:

/people
/rooms
    teamId, type, sortBy, max
/memberships
/messages
/teams
/webhooks

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//------------
Webex Meetings
//------------

URL API: CRM, LMS
XML API: Automation, Instant Messaging

Manage devices through the xAPI

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]


questions_sdwan = [
{
"question" : """
###########################
###     SD-WAN API      ###
###########################

vManage - Central Management, Web Interface and REST API
vSmart - SD-WAN fabric controller
vBond - Fabric orchestrator, connects edge devices to vSmart controller
vEdge - Edge devices

# Swagger/OpenAPI documenation available directly from vManage via:
https://<vmanage>:<port>/apidocs

19.2 - Session ID
19.3 and up - authorization Token, also a X-XSRF-Token

Python SDK available

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

# Get JSessionID; returns a session cookie:
POST, /j_security_check
    For Cisco SD-WAN authentication, the Conten-Type:application/x-www-form-urlencoded
        J_username, and J_password
    Returns a 200 OK and a cookie names JSESSIONID

# Get XSRF Token:
GET, /dataservice/client/token

# Get all devices:
GET, /dataservice/device

//---
Get a list of all devices?
""",
"answer" : "/dataservice/device",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
import requests

url = "https://sandbox-sdwan-2.cisco.com:443/j_security_check"

payload='j_username=devnetuser&j_password=RG!_Yw919_83'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=HgYQAr1DbwK1SUMApab1PDAXANfBYzFIo6WR-KGX.81ac6722-a226-4411-9d5d-45c0ca7d567b'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

//---
What content-type is used for SD-WAN initial authentication to acquire a JSESSIONID cookie?
""",
"answer" : "x-www-form-urlencoded",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]

questions_dna = [
{
"question" : """
########################
###     DNA API      ###
########################

APIs:
    Intent API
    Integration API
    Multi-vendor SDK
    Events and Notifications API + Webhooks

# Get a Token
curl --location --request POST 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token' \
--header 'Authorization: Basic ZGV2bmV045jdfurtnsftunrtjnF='

Once you get an authentication token, all subsequent requests will utilize the x-auth-token HTTP header with our token as the value.

/dna/system/api/v1/auth/token
""",
"answer" : r"/dna/system/api/v1/auth/token",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

# Get the devices:
curl --location 'https://sandboxdnac.cisco.com/api/v1/network-device' \
--header 'x-auth-token: eyJhbnl0w'

// 200 OK
{
    "response": [
        {
            "description": "Cisco IOS Software [Cupertino], Catalyst L3 Switch Software (CAT9KV_IOSXE), Experimental Version 17.9.20220318:182713 [BLD_POLARIS_DEV_S2C_20220318_081310-10-g847b433944c4:/nobackup/rajavenk/vikagarw/git_ws/polaris_dev 101] Copyright (c) 1986-2022 by Cis",
            "memorySize": "NA",
            "lastUpdateTime": 1699551723688,
            "bootDateTime": "2023-10-11 17:05:03",
            "macAddress": "52:54:00:01:c2:c0",
            "softwareType": "IOS-XE",
            "softwareVersion": "17.9.20220318:182713",
            "hostname": "sw1",
            "serialNumber": "9SB9FYAFA2O",
            "family": "Switches and Hubs",
            "inventoryStatusDetail": "<status><general code=\"SUCCESS\"/></status>",
            "collectionInterval": "Global Default",
            "managementState": "Managed",
            "upTime": "29 days, 0:37:59.00",
            "roleSource": "AUTO",
            "lastUpdated": "2023-11-09 17:42:03",
            "snmpLocation": "",
            "associatedWlcIp": "",
            "reachabilityStatus": "Reachable",
            "series": "Cisco Catalyst 9000 Series Virtual Switches",
            "uptimeSeconds": 2589580,
            "type": "Cisco Catalyst 9000 UADP 8 Port Virtual Switch",
            "location": null,
            "role": "DISTRIBUTION",
            "instanceUuid": "32446e0a-032b-4724-93e9-acbbab47371b",
            "instanceTenantId": "5e8e896e4d4add00ca2b6487",
            "id": "32446e0a-032b-4724-93e9-acbbab47371b"
        },
    ],
    "version": "1.0"
}

""",
"answer" : r"/api/v1/network-device",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]


questions_meraki = [
{
"question" : """
###########################
###     Meraki API      ###
###########################
https://developer.cisco.com/meraki/api-v1/introduction/

- Dashboard
- Webhook
- Captive Portal
- Scanning
- Camera

X-Cisco-Meraki-API-Key: <API_KEY>   <---v0
Authorization: "Bearer <API_KEY>"   <---What I now see in the documentation
    Incorrect API key returns 404

//-------------
Get Organization

curl -L --request GET \
--url https://api.meraki.com/api/v1/organizations/ \
--header 'Authorization: Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6' \
--header 'Accept: application/json'
//-------------
200 OK
    {
        "id": "1215707",
        "name": "API Demo Organization",
        "url": "https://n394.meraki.com/o/Yja5Xd/manage/organization/overview",
        "api": { "enabled": true },
        "licensing": { "model": "co-term" },
        "cloud": {
            "region": {
                "name": "North America"
            }
        },
        "management": { "details": [] }
    }
]

/api/v1/organizations/

""",
"answer" : "/api/v1/organizations/",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-------------------
Meraki with Requests
//-------------------

url = "https://api.meraki.com/api/v1/organizations"
payload = None
headers = {
    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
    "Accept": "application/json"
}
response = requests.request('GET', url, headers=headers, data=payload)
print(response.text.encode('utf8'))

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Get Network Devices in Meraki
/networks/{networkId}/devices

curl -L --request GET \
--url https://api.meraki.com/api/v1/networks/N_24329156/devices \
--header 'Authorization: Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6' \
--header 'Accept: application/json'

//-------------

import meraki
# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/
dashboard = meraki.DashboardAPI(API_KEY)
network_id = 'L_646829496481105433'
response = dashboard.networks.getNetworkDevices(
    network_id
)
print(response)

//-------------

import requests
url = "https://api.meraki.com/api/v1/networks/N_24329156/devices"
payload = None
headers = {
    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
    "Accept": "application/json"
}
response = requests.request('GET', url, headers=headers, data = payload)
print(response.text.encode('utf8'))

//-------------

/api/v1/networks/{networkId}/devices

""",
"answer" : r"/api/v1/networks/{networkId}/devices",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]

