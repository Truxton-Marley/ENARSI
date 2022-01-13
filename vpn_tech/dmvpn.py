import common_prompts as cp

questions = [
{
"question" : """
########################
###       DMVPN      ###
########################

Phase I and II Hub:
interface tunnel 42
  bandwidth 100000
  ip address 10.0.0.1 255.255.255.0
  tunnel source gig 0/0/0
  tunnel mode gre multipoint
  tunnel key 42
  ip mtu 1400
  ip tcp adjust-mss 1360
  ip nhrp network-id 42

""",
"answer" : "",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Reduce the following commands to one command:

ip nhrp nhs 10.0.0.1
ip nhrp map 10.0.0.1 1.1.1.1
ip nrhp map multicast 1.1.1.1

""",
"answer" : "ip nhrp nhs 10.0.0.1 nbma 1.1.1.1 multicast",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Expand the following command to three commands:

ip nhrp nhs 10.0.0.1 nbma 1.1.1.1 multicast

""",
"answer" : """ip nhrp nhs 10.0.0.1
ip nhrp map 10.0.0.1 1.1.1.1
ip nrhp map multicast 1.1.1.1""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Modifiy the following Hub config to work
as DMVPN phase 3:

interface tunnel 42
  bandwidth 100000
  ip address 10.0.0.1 255.255.255.0
  tunnel source gig 0/0/0
  tunnel mode gre multipoint
  tunnel key 42
  ip mtu 1400
  ip tcp adjust-mss 1360
  ip nhrp network-id 42

""",
"answer" : "ip nhrp redirect",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Modifiy the following Spoke config to work
as DMVPN phase 3:

interface tunnel 42
  bandwidth 100000
  ip address 10.0.0.42 255.255.255.0
  tunnel source gig 0/1
  tunnel mode gre multipoint
  tunnel key 42
  ip mtu 1400
  ip tcp adjust-mss 1360
  ip nhrp network-id 42
  ip nhrp nhs 10.0.0.1 nbma 1.1.1.1 multicast

""",
"answer" : "ip nhrp shortcut",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
}
]
#"post_task_output": """"""
