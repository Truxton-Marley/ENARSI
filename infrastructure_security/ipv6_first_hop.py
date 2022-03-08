import common_prompts as cp

questions = [
{
"question" : """
#######################################
###     IPv6 First Hop Security     ###
#######################################

May require a programmed TCAM

Create a policy for IPv6 DHCPv6 Guard.
Name it dhcp-routers.
Assign the role to server.

""",
"answer" : "ipv6 dhcp guard policy dhcp-routers",
"prompt": "SW1(config)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "device-role server",
"prompt": "SW1(config)#",
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Now that we have the DHCPv6 Guard Policy configured,
we will need to apply it to our DHCP server facing
interfaces.

!
ipv6 dhcp guard policy dhcp-routers
  device-role server
!
SW1(config)#
SW1(config)#interface gig 0/1
""",
"answer" : "ipv6 dhcp guard attach-policy dhcp-routers",
"prompt": "SW1(config-if)#",
"clear_screen": True,
"suppress_positive_affirmation": False
}
]
#"post_task_output": """"""