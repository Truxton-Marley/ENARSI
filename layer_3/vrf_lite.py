import common_prompts as cp

questions = [
{
"question" : """
##############################
#######   VRF LITE      ######
##############################

Create OSPF instance 11 for vrf bunny.

""",
"answer" : "router ospf 11 vrf bunny",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Create classic EIGRP AS 42 for vrf bunny AS 66

""",
"answer" : "router eigrp 42",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """address-family ipv4 vrf bunny autonomous-system 66""",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]
