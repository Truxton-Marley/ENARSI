import common_prompts as cp

questions_mdp = [
{
"question" : """
#####################
###     MDP       ###
#####################

NETCONF was originally proposed in RFC 4741 in 2006, and YANG in RFC 6020 in 2010.

YANG data models can represent either device data models or service data models.

When using NETCONF as a network management protocol, the device is running a server called a "NETCONF agent". You or a network 
management system use a client called a "NETCONF Manager" to connect to it.

Use pyang to explore data models.
""",
"answer" : "pyang",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
RFCs and drafts:
    NETCONF
        RFC 6241
        RFC 4741
    YANG
        RFC 7950
        RFC 6020
    RESTCONF
        RFC 8040
    gRPC
        grpc.io
    GitHub YANG repository
        YangModels/yang
""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
YANG is a language for describing data models. Although it can describe any data model, it was originally designed for networking data models.

YANG is a structured and strongly typed language, and both are beneficial qualities for a data modeling language. Some aspects of the language to note:

Every data model is a module, a self-contained top-level hierarchy of nodes.
Data types can be imported from another YANG module or defined within a module.
It uses containers to group related nodes.
It uses lists to identify nodes that are stored in sequence.
A leaf represents each individual attribute of a node.
Every leaf must have an associated type.

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Explore YANG model using pyang
developer:models > pyang -f tree ietf-interfaces.yang
ietf-interfaces.yang:6: error: module "ietf-yang-types" not found in search path
module: ietf-interfaces
  +--rw interfaces
  |  +--rw interface* [name]
  |     +--rw name                        string
  |     +--rw description?                string
  |     +--rw type                        identityref
  |     +--rw enabled?                    boolean
  |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
  |     +--ro admin-status                enumeration {if-mib}?
  |     +--ro oper-status                 enumeration
  |     +--ro last-change?                yang:date-and-time
  |     +--ro if-index                    int32 {if-mib}?
  |     +--ro phys-address?               yang:phys-address
  |     +--ro higher-layer-if*            interface-ref
  |     +--ro lower-layer-if*             interface-ref
  |     +--ro speed?                      yang:gauge64
  |     +--ro statistics
  |        +--ro discontinuity-time    yang:date-and-time
  |        +--ro in-octets?            yang:counter64
  |        +--ro in-unicast-pkts?      yang:counter64
  |        +--ro in-broadcast-pkts?    yang:counter64
  |        +--ro in-multicast-pkts?    yang:counter64
  |        +--ro in-discards?          yang:counter32
  |        +--ro in-errors?            yang:counter32
  |        +--ro in-unknown-protos?    yang:counter32
  |        +--ro out-octets?           yang:counter64
  |        +--ro out-unicast-pkts?     yang:counter64
  |        +--ro out-broadcast-pkts?   yang:counter64
  |        +--ro out-multicast-pkts?   yang:counter64
  |        +--ro out-discards?         yang:counter32
  |        +--ro out-errors?           yang:counter32
  x--ro interfaces-state
     x--ro interface* [name]
        x--ro name               string
        x--ro type               identityref
        x--ro admin-status       enumeration {if-mib}?
        x--ro oper-status        enumeration
        x--ro last-change?       yang:date-and-time
        x--ro if-index           int32 {if-mib}?
        x--ro phys-address?      yang:phys-address
        x--ro higher-layer-if*   interface-state-ref
        x--ro lower-layer-if*    interface-state-ref
        x--ro speed?             yang:gauge64
        x--ro statistics
           x--ro discontinuity-time    yang:date-and-time
           x--ro in-octets?            yang:counter64
           x--ro in-unicast-pkts?      yang:counter64
           x--ro in-broadcast-pkts?    yang:counter64
           x--ro in-multicast-pkts?    yang:counter64
           x--ro in-discards?          yang:counter32
           x--ro in-errors?            yang:counter32
           x--ro in-unknown-protos?    yang:counter32
           x--ro out-octets?           yang:counter64
           x--ro out-unicast-pkts?     yang:counter64
           x--ro out-broadcast-pkts?   yang:counter64
           x--ro out-multicast-pkts?   yang:counter64
           x--ro out-discards?         yang:counter32
           x--ro out-errors?           yang:counter32
developer:models > 

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Interface expressed using YANG model in XML:
<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name>GigabitEthernet1</name>
        <description>DONT'T TOUCH ME</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
                <ip>10.10.10.10</ip>
                <netmask>255.255.255.0</netmask>
            </address>
        </ipv4>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
    </interface>
    <interface>
        <name>GigabitEthernet2</name>
        <description>WAN Interface</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
                <ip>172.16.12.1</ip>
                <netmask>255.255.255.0</netmask>
            </address>
        </ipv4>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
    </interface>
    <interface>
        <name>GigabitEthernet3</name>
        <description>LAN Interface</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
                <ip>192.168.10.1</ip>
                <netmask>255.255.255.0</netmask>
            </address>
        </ipv4>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
    </interface>
</interfaces>
developer:yang > 
""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# NETCONF, generally combined with YANG using XML

SSH -> [<rpc><rpc-reply>] -> [<get><get-config><edit-config>, etc] -> [data]

ssh -oHostKeyAlgorithms=+ssh-dss developer@sandbox-iosxe-recomm-1.cisco.com -p 830 -s netconf

# Router says hello and gives list of capabilities:
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
  <capability>urn:ietf:params:netconf:base:1.1</capability>
  <capability>urn:ietf:params:netconf:capability:candidate:1.0</capability>
  <capability>urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring</capability>
  <capability>urn:ietf:params:xml:ns:yang:ietf-interfaces</capability>
  [output omitted and edited for clarity]
</capabilities>
<session-id>19150</session-id></hello>]]>]]>

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Say hello back:
<?xml version="1.0" encoding="UTF-8"?>
  <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
      <capability>urn:ietf:params:netconf:base:1.0</capability>
    </capabilities>
  </hello>]]>]]>

----------------
# Close session:
----------------
<?xml version="1.0" encoding="UTF-8"?>
  <rpc message-id="1239123" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <close-session />
  </rpc>
]]>]]>
""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Datastores:
<running>
<startup>
<candidate>
<URL>

# Operations:
<get>	Retrieve running configuration and device state information.
<get-config>	Retrieve all or part of specified configuration datastore.
<edit-config>	Load all or part of a configuration to the specified configuration datastore.
<copy-config>	Replace an entire configuration datastore with another.
<delete-config>	Delete a configuration datastore.
<commit>	Copy candidate datastore to running datastore.
<lock> / <unlock>	Lock or unlock the entire configuration datastore computer.
<close-session>	Close the NETCONF session gracefully.
<kill-session>	Force the NETCONF session to end.

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Python and ncclient

from ncclient import manager

m = manager.connect(
m = manager.connect(
 host=env_lab.IOS_XE_1["host"],
 port=env_lab.IOS_XE_1["netconf_port"],
 username=env_lab.IOS_XE_1["username"],
 password=env_lab.IOS_XE_1["password"],
 hostkey_verify=False
 )

for capability in m.server_capabilities:
 print(capability)

m.close_session()


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
from ncclient import manager
import xmltodict
import xml.dom.minidom

netconf_filter = '''
<filter>
    <interfaces xmlns='urn:ietf:params:xml:ns:yang:ietf-interfaces'>
    <interface></interface>
    </interfaces>
</filter>'''

netconf_reply = m.get_config(source = 'running', filter = netconf_filter)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

# Parse the returned XML to an Ordered Dictionary
netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]

for interface in interfaces:
    print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Create an XML configuration template for ietf-interfaces
netconf_interface_template = ''' 
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{name}</name>
            <description>{desc}</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                {type}
            </type>
            <enabled>{status}</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>'''

# Create the NETCONF data payload for this interface
netconf_data = netconf_interface_template.format(
        name = new_loopback["name"],
        desc = new_loopback["desc"],
        type = new_loopback["type"],
        status = new_loopback["status"],
        ip_address = new_loopback["ip_address"],
        mask = new_loopback["mask"]
    )

netconf_reply = m.edit_config(netconf_data, target = 'running')
""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Saving the config with NETCONF
from ncclient import manager, xml_

save_body = '''
<cisco-ia:save-config xmlns:cisco-ia='http://cisco.com/yang/cisco-ia'/>
'''

netconf_reply = m.dispatch(xml_.to_ele(save_body))

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

questions_restconf = [
{
"question" : """
########
RESTCONF
########

RFC 8040
Tightly coupled with YANG and uses JSON or XML

# enable:
ip http secure-sever
restconf
#

# Basic URI format:
https://<ADDRESS>/<ROOT>/data/<[YANG MODULE:]CONTAINER>/<LEAF>[?<OPTIONS>
https://<ADDRESS>/<ROOT>/operations/<[YANG MODULE:]CONTAINER>/<LEAF>[?<OPTIONS>

https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1?fields=name;description
https://{{host}}:{{port}}/restconf/data/ietf-yang-library:modules-state

*Per the RESTCONF standard, devices should expose a resource called /.well-known/host-meta to enable discovery of root programmatically.
*[YANG MODULE:]CONTAINER - The base model container being used.
    Inclusion of the module name is optional.
*[?\<OPTIONS>] - Some network devices may support options sent as query parameters that impact returned results.
    depth=unbounded: Follow nested models to end. Integer also supported.
    content=[all, config, nonconfig]: Query option controls type of data returned. Default is all.
    fields=expr: Limit what leafs are returned.

module: ietf-interfaces
   +--rw interfaces
   |  +--rw interface* [name]
   |     +--rw name                        string
   |     +--rw description?                string
   |     +--rw type                        identityref
   |     +--rw enabled?                    boolean
   |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/

curl --location 'https://192.168.3.49:443/restconf/data/ietf-interfaces:interfaces/' \
--header 'Content-Type: application/yang-data+json' \
--header 'Accept: application/yang-data+json' \
--header 'Authorization: Basic cGM6YnVubnlob3BzMTJidW5ueQ=='


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Add an interface:
URI: https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces
POST

  {
      "ietf-interfaces:interface": {
          "name": "Loopback100",
          "description": "Added with RESTCONF",
          "type": "iana-if-type:softwareLoopback",
          "enabled": true,
          "ietf-ip:ipv4": {
              "address": [
                  {
                      "ip": "172.16.100.1",
                      "netmask": "255.255.255.0"
                  }
              ]
          }
      }
  }

curl --location 'https://192.168.3.49:443/restconf/data/ietf-interfaces:interfaces' \
--header 'Authorization: Basic cGM6YnVuaierynsdddrudW5ueQ==' \
--header 'Accept: application/yang-data+json' \
--header 'Content-Type: application/yang-data+json' \
--data '{
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.100.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}'

Response.status_code should be `201 Created`
If the loopback already exists, you may get a `409 Conflict`

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Edit an Interface:
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2
PUT

// Body marked as raw in Postman:
{
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet2",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.255.255.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

Should return a `204 No Contenet`

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Delete an interface:
https://{{host}}:{{port}}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100
DELETE

curl --location --request DELETE 'https://192.168.3.49:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback100' \
--header 'Content-Type: application/yang-data+json' \
--header 'Accept: application/yang-data+json' \
--header 'Authorization: Basic cjhgerjebn9dherjcgseeW5ueQ=='

Should return a `204 No Content`

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Save the Configuration:

curl --location --request POST 'https://192.168.3.49:443/restconf/operations/cisco-ia:save-config/' \
--header 'Content-Type: application/yang-data+json' \
--header 'Accept: application/yang-data+json' \
--header 'Authorization: Basic yhrng8rjdrtijudrfnrutrfveQ=='

Should return a `200 OK`

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Sample Python PUT to update interface IP
import requests
import json

url = "https://192.168.3.49:443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet2"

payload = json.dumps({
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet2",
    "description": "Configured by RESTCONF",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.255.255.1",
          "netmask": "255.255.255.0"
        }
      ]
    }
  }
})
headers = {
  'Authorization': 'Basic yitste867DF9dsng$868cfhdkQ==',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

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
