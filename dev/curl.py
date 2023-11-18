import common_prompts as cp

questions_curl = [
{
"question" : """
#####################
###     curl      ###
#####################

Here is a list of common curl arguments:

arg	description
-u	Specifies the username and password.
-k	Allows curl to explicitly allow insecure SSL connections.
-i	Returns response headers.
-s	Silent or quiet mode. Don't show progress meter or error messages.
-X, --request	Sends GET, HEAD, or POST requests to a server.

curl -i https://deckofcardsapi.com/api/deck/new/

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Webex API

https://developer.webex.com/docs/getting-started
https://developer.webex.com/docs/getting-started#accounts-and-authentication

curl https://webexapis.com/v1/people/me -X GET \
-H "Authorization:Bearer $TOKEN" \
| python -m json.tool

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Curl + RESTCONF examples:

curl -k \
-H "Authorization: Basic cm9vdDpEX1ZheSFfMTAm" \
-H "Accept: application/yang-data+json" \
"https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

curl -k \
-H "Authorization: Basic cm9vdDpEX1ZheSFfMTAm" \
-H "Accept: application/yang-data+json" \
"https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"

curl -k \
-H "Authorization: Basic cm9vdDpEX1ZheSFfMTAm" \
-H "Accept: application/yang-data+json" \
"https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1?fields=name;description"

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
