import common_prompts as cp

questions = [
{
"question" : """

####################
###     SNMP     ###
####################

Start by creating an SNMP View.
Name the view and include iso.

""",
"answer" : "snmp-server view god iso included",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question": """
Create SNMPv3 Group kitties with AuthPriv.
Give it both read and write access to the SNMP view "god".

snmp-server view god iso included
!
R1(config)#
""",
"answer": "snmp-server group kitties v3 priv read god write god",
"prompt": cp.config,
"clear_screen": True
},
{
"question": """
Create SNMPv3 User bunny, a member of kitties,
Authentication md5, password cisco123
Encryption AES 256, password cisco123:

snmp-server view god iso included
snmp-server group kitties v3 priv read god write god
!
R1(config)#
""",
"answer": "snmp-server user bunny kitties v3 auth md5 cisco123 priv aes 256 cisco123",
"prompt": cp.config,
"clear_screen": True
}
]
