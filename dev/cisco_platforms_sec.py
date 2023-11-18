import common_prompts as cp

questions_sec = [
{
"question" : """
###################################
###     Security Platforms      ###
###################################
Firepower, Umbrella, ISE, Thream, Threat Grid, AMP

Firepower
    REST API via the FMC (Firepower Management Center)
    Authentication via Token (X-Auth-Access-Token)
    FMC API Explorer
    ASA + Firepower IPS = FP Threat Defense

# cURL call to get device records:
curl -X 'GET' \
  'https://fmcrestapisandbox.cisco.com/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords' \
  -H 'accept: application/json' \
  -H 'X-auth-access-token: 4fa67e3a-b463-4d8a-8bf8-049d914494e5'
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
Cisco Umbrella
//------------

Cloud based secure gateway using DNS and Cisco Talos
    Can be integrated with AMP
    Management API, Reporting API,
    Console Reporting API, Network Device Management API,
    Enforcement API, Investigate API
    Base64 / Basic Auth and requires HTTPS and auth header

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
Cisco ISE
//------------

Network Access Control (NAC) and policy enforcement solution:
    ID all devices and users connected to the network
    User-initiated provisioning
    Policy management and enforcement
    Integrate with external services (MDM/AD/LDAP)
    Session API, ERS (External RESTful Services)
    Base64 / Basic Auth and requires HTTPS and auth header

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//----------------
Cisco Threat Grid
//----------------

Malware analysis and threat intelligence
    https://panacea/threatgrid.com/api/<ver>/<api-endpoint>?q=<query>&apikey
    Grab API Key from the user dashboard

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-----------------------------------
Cisco AMP Advanced Malware Protection
//-----------------------------------

* AMP for Endpoint (formerly Secure Endpoint):
    See once, block everywhere
    Create Client ID key pair
    https://clientid:apikey@1.1.1.1/    <---Here or Base64 in Authorization Header
    https://clientid:apikey@1.1.1.1/v1/computers    <---Return list of all computers 

""",
"answer" : "",
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
