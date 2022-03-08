import common_prompts as cp

questions = [
{
"question" : """
####################
###     CoPP     ###
####################

access-list 101 permit ospf any any
access-list 101 permit eigrp any any
access-list 101 permit bgp any any

Class-maps can be "match-any" or "match-all", with the default
of "match-all" if neither is specified.

Let's create a class-map to match ACL 101. Name it routing and
rely on its default match setting.

""",
"answer" : "class-map routing",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "match access-group 101",
"prompt": cp.config_cmap,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Next we need to create a Policy-Map named routing-policy
that matches our class-map, routing, and set the policier
to 8000 bps.

!
access-list 101 permit ospf any any
access-list 101 permit eigrp any any
access-list 101 permit bgp any any
!
class-map routing
  match access-group 101
!
R1(config)#
""",
"answer" : "policy-map routing-policy",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "class routing",
"prompt": cp.config_pmap,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "police 8000 conform-action transmit exceed-action drop",
"prompt": cp.config_pmap_class,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """
And lastly we will bind the policy-map to the
local control-plane with a service-policy.

!
access-list 101 permit ospf any any
access-list 101 permit eigrp any any
access-list 101 permit bgp any any
!
class-map routing
  match access-group 101
!
policy-map routing-policy
  class routing
    police 8000 conform-action transmit exceed-action drop
!
R1(config)#
""",
"answer" : "control-plane",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "service-policy input routing-policy",
"prompt": "R1(config-cp)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """
Let's now view the policy from user-exec mode.
show policy-map control-plane

!
access-list 101 permit ospf any any
access-list 101 permit eigrp any any
access-list 101 permit bgp any any
!
class-map routing
  match access-group 101
!
policy-map routing-policy
  class routing
    police 8000 conform-action transmit exceed-action drop
!
control-plane
  service-policy input routing-policy
!
""",
"answer" : "show policy-map control-plane",
"prompt": cp.user_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """
TODO: add output here
"""
},
]
#"post_task_output": """"""

# Single-rate, dual-bucket, three-color policier
# police 10000 4000 6000 conform-action transmit exceed-action transmit violate-actioin drop

