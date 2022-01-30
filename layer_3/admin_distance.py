import common_prompts as cp

questions = [
{
"question" : """
####################################
#######   Admin Distance      ######
####################################

255 will not install into the RIB!!!

0   Connected
5   EIGRP Summary
20  eBGP
90  EIGRP
110 OSPF
115 IS-IS
120 RIP
170 EIGRP External
200 iBGP
---
distance <new_AD> <source-address> <wildcard-mask> [ACL]
    * Only works on EIGRP internal, not External routes
    * For OSPF, source-address == Router-ID
###

Let's set the distance for EIGRP, Internal: 90, External: 170

R1(config)#router eigrp 42
""",
"answer" : "distance eigrp 90 170",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Let's set the distance for EIGRP routes learned from neighbor interfaces
in the range of 10.0.0.0/16 to have an AD of 88

R1(config)#router eigrp 42
""",
"answer" : "distance 88 10.0.0.0 0.0.255.255",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Let's set the distance for OSPF:
  External: 120
  Inter-Area: 115
  Intra-Area: 110

R1(config)#router ospf 42
""",
"answer" : "distance ospf external 120 inter-area 115 intra-area 110",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Routes learned from 12.12.0.0/16 should have an AD of 89.

R1(config)#router ospf 42
""",
"answer" : "distance 89 12.12.0.0 0.0.255.255",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the AD for BGP:
    External: 22
    Internal: 222
    Local: 44

Syntax:
distance bgp <external_routes_ad> <internal_routes_ad> <local_routes_ad>

R1(config)#router bgp 42
""",
"answer" : "distance bgp 22 222 44",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
}
]
#"post_task_output": """"""
