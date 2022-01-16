import common_prompts as cp

questions = [
{"question" : """
##############################
###     Redistribution     ###
##############################

Set the default metric for EIGRP process 42 using the following parameters:

bandwidth: 1000 kbps
delay: 100 microseconds
Reliability: 255
Load: 1
IP MTU: 1500

R1(config)#router eigrp 42
""",
"answer" : "default-metric 1000 10 255 1 1500",
"prompt": cp.config_router,
"clear_screen": False,
},
{"question" : """
######################################
##### Route Filtering Exercise 1 #####
######################################

Let's do some route filtering with a route-map.

First create ACL 1 to match 192.168/16.

""",
"answer" : "access-list 1 permit 192.168.0.0 0.0.255.255",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False,
},
{"question" : """
Now create route-map BUNNY deny 10 and match ACL 1.

access-list 1 permit 192.168.0.0 0.0.255.255

""",
"answer" : "route-map BUNNY deny 10",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{"question" : "",
"answer" : "match ip address 1",
"prompt": cp.config_route_map,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{"question" : """
Now we need to let  all other traffic through. Add a "permit 20".

R1(config)#access-list 1 permit 192.168.0.0 0.0.255.255
R1(config)#route-map BUNNY deny 10
R1(config-route-map)#match ip address 1
R1(config-route-map)#exit
R1(config)#
""",
"answer" : "route-map BUNNY permit 20",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{"question" : """

Let's apply the route map to EIGRP 42 routes redistributed into OSPF process 1:

Create E1 route, don't forget "subnets", and then, of course, the route-map.
Also, add a tag of 42.

R1(config)#access-list 1 permit 192.168.0.0 0.0.255.255
R1(config)#route-map BUNNY deny 10
R1(config-route-map)#match ip address 1
R1(config-route-map)#exit
R1(config)#route-map BUNNY permit 20
R1(config-route-map)#exit
R1(config)#router ospf 1
""",
"answer" : "redistribute eigrp 42 metric-type 1 subnets route-map BUNNY tag 42",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
# {"question" : """

# ######################################
# ##### Route Filtering Exercise 2 #####
# ######################################

# Let's do some route filtering with a route-map

# First create ACL 1 to match 192.168/16
# """,
# "answer" : "access-list 1 permit 192.168.0.0 0.0.255.255",
# "prompt": cp.config,
# "clear_screen": True,
# "suppress_positive_affirmation": True
# },
]
