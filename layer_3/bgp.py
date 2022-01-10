import common_prompts as cp

questions = [
{
"question" : """

######################
###       BGP      ###
######################

Let's get the ball rolling by disabling IPv4 as the default address family.


R1(config)#router bgp 100
""",
"answer" : "no bgp default ipv4-unicast",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the BGP router-id to 1.1.1.1

""",
"answer" : "bgp router-id 1.1.1.1",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the BGP timers to 60 180 for peer 2.2.2.2
""",
"answer" : "neighbor 2.2.2.2 timers 60 180",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter the IPv4 unicast address family.

""",
"answer" : "address-family ipv4 unicast",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter the IPv6 unicast address family.
""",
"answer" : "address-family ipv6 unicast",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False   
},
{
"question" : """
Enter the IPv4 address family for VRF lila
""",
"answer" : "address-family ipv4 vrf lila",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter the VPNv4 address family.
""",
"answer" : "address-family vpnv4",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set BGP to use asdot notation for 4-bytes AS numbers.
""",
"answer" : "bgp asnotation dot",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the default BGP local-preference to 150
""",
"answer" : "bgp default local-preference 150",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the weight to 2000 for all routes received from 2.2.2.2
""",
"answer" : "neighbor 2.2.2.2 weight 2000",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Force BGP to compare MED values from different AS peers.
""",
"answer" : "bgp always-compare-med",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Remove any private AS numbers before sending to peer at 2.2.2.2
""",
"answer" : "neighbor 2.2.2.2 remove-private-as",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create a soft reset inbound to store the routes. Memory intensive.
""",
"answer" : "neighbor 2.2.2.2 soft-reconfiguration inbound",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Have the router resend all BGP info to 2.2.2.2 without resetting the connections.
""",
"answer" : "clear ip bgp 2.2.2.2 soft out",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create a summary route to 10.0/16 and suppress specific routes.
""",
"answer" : "aggregate-address 10.0.0.0 255.255.0.0 summary-only",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set peer 2.2.2.2 to be a RR client.
""",
"answer" : "neighbor 2.2.2.2 route-reflector-client",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]
#"post_task_output": """"""