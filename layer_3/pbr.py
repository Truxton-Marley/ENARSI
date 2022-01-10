import common_prompts as cp

questions = [
{
"question" : """

###################
###     PBR     ###
###################

Create a route-map named PBR to match ACL 110
set the next-hop to be 22.22.22.22.

R1(config)#access-list 110 permit 10.10.0.0 0.0.255.255 any
R1(config)#
""",
"answer" : "route-map PBR permit 10",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """match ip address 110
set ip next-hop 22.22.22.22""",
"prompt": cp.config_route_map,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Brillant work thus far!!!
Now let's apply our PBR route-map to interface gig 0/0/1

access-list 110 permit 10.10.0.0 0.0.255.255 any
!
route-map PBR permit 10
  match ip address 110
  set ip next-hop 22.22.22.22
!
R1(config)interface gig 0/0/1
""",
"answer" : "ip policy route-map PBR",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
What if we want to apply PBR to locally generated traffic?

access-list 110 permit 10.10.0.0 0.0.255.255 any
!
route-map PBR permit 10
  match ip address 110
  set ip next-hop 22.22.22.22
!
R1(config)#
""",
"answer" : "ip local policy route-map PBR",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]
