import common_prompts as cp

questions = [
{
"question" : """
###################
###     PBR     ###
###################

PBR can match on ip address or length.
set:
  set ip next-hop x.x.x.x
  set interface...
  set ip default next-hop x.x.x.x  <---Only use next-hop if no viable route in RIB
  set default interface...
Verify:
  show ip policy
  debug ip 
  
PBR is applied to incoming traffic on an interface only!!!
______________________________________

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
{
"question" : """
Using the "set ip default next-hop" enables us to only use the PBR next-hop
if there is no route in the RIB for the network.

Set the next-hop to 22.22.22.22 only for when their is no RIB entry.
!
R1(config)#route-map PBR permit 10
R1(config-route-map)# match ip address 110
""",
"answer" : "set ip default next-hop 22.22.22.22",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]
