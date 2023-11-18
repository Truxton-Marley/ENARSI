import common_prompts as cp

questions_dc = [
{
"question" : """
###################################
###      Data Center Stuff      ###
###################################

UCS - Unified Compute System
UCS Manager - Manage up to 160 Servers
    UCS XML API
    UCS PowerTool - PowerShell module accessing the UCS XML API
UCS Central - Manage even more servers
UCS Director - Manage application deployment

Fabric Interconnect - "The Brains" UCS Manager resides here
Chassis
Fabric Extenders (IO Modules) 
VIC - Virtual Interface Cards

What is a PowerShell module works via the UCS XML API?
""",
"answer" : "PowerTool",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//---------
UCS Manager
//---------

MIM - Management Information Model
    Holds all manageble objects (MO)

Visore
    Built in MO browser
    https://x.x.x.x/visore.html

All MOs available via UCS XML API
    Service Profile: logical construct of the complete configuration of a server, including HW
    Access API via HTTP or HTTPS
    https://x.x.x.x/nuova
    Send username and password and get cookie to use for subsequent requests

UCS Python SDK and PowerShell modules available

What is the object at the top of the MIT?
""",
"answer" : "sys",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Supports all traffic from Cisco UCS servers over a single link?
""",
"answer" : "singleconnect",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-----------
UCS Director
//-----------

UCS Director automates and orchestrates the provisioning of applications in the DC and Cloud
    Automate
        VM provisioning and maintenance
        Compute, Network, Storage deployment
        Bare-metal server deployment and OS installation
        Deployment of apps in the cloud
    REST API
        JSON or XML
        Username and API access key
            X-Cloupia-Request-Key
    SDK in Java

Task: atomic unit of work in Cisco UCS Director
Workflow: series of tasks to automate a complex operation
Libraries and catalogs: collections of predefined tasks and workflows

What is the most basic unit of work in UCS Director?
""",
"answer" : "task",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Contains all server settings, fabric extenders, and fabric interconnects?
""",
"answer" : "service profile",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Username and API access key: x-cloupia-request-key?
""",
"answer" : "x-cloupia-request-key",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-----------
Intersight
//-----------

Manage Cisco UCS and Hyperflex platforms
Works with UCS Manager
REST API
Python, PowerShell and Ansible SDKs

pip install intersight

""",
"answer" : "pip install intersight",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-------------------------------------
ACI Application Centric Infrastructure
//-------------------------------------

APIC - Application Policy Infrastructure Controller
    * Single point of automation and management
    * Policy Enforcement
    * Health Monitoring

Nexus 9000 switches
    Standalone mode | ACI Mode

EPG - Endpoint Group
    Collection of endpoints that have common policy requirements such as
    security, virtual machine mobility, QoS, or L4 - L7 services.
Logical Model | Concrete Model
MIM - Management Information Model
    MIT - Management Information Tree
        Each node is a MO
        Each object in the tree has a DN (Distiguised Name)

https://<system>/api/[mo|class]/[dn|class][:method].[xml|json]?{options}

SDKs: ACI toolkit, Cobra (Python), ACIrb (Ruby), plus Puppet, Ansible, PowerShell

Which python library can be used for basic automation in ACI?

""",
"answer" : "acitoolkit",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Which Python SDK can be used to configure ACI?
""",
"answer" : "cobra",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-------------------------------------
ACI REST API
//-------------------------------------

Authenticate via POST of the user object (name:password)
    Get a token back and use as a cookie

//-------------------------------------
POST: https://myapicip/api/aaaLogin.json
BODY RAW:
{
    "aaaUser" : {
        "attributes: {
            "name": "cisco",
            "pwd": "cisco",
        }
    }
}
//-------------------------------------
Returns a token:
APIC-Cookie: myToken

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# pip3 install acitoolkit
import acitoolkit.acitoolkit as aci

session = aci.Session(APIC_URL, USERNAME, PWD)
response = session.login()

endpoints = aci.Endpoint.get(session)

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
//-----------
NX-OS
//-----------

Built on Linux
Python SDK
NX-API REST interface
    `feature nxapi`
Netconf/YANG
    `feature netconf`
RESTCONF
    `feature restconf`
CentOS Guest Shell Linux containers (LXC)
BASH Shell

Enable Netconf on the NX-OS?
""",
"answer" : "feature netconf",
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
