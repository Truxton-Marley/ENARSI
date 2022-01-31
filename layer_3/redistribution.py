import common_prompts as cp

questions = [
{
"question" : """
##############################
###     Redistribution     ###
##############################

Protocol    Default Seed Metric
RIP         0, treated as infinity
EIGRP       0, treated as infinity
OSPF        20, E2 for IGPs; 1, E2 for BGP
BGP         IGP metric value
IS-IS       0, no *not* treated as infinity
___________________________________________

Redistribute OSPF 13 into EIGRP 42 with the following metrics:

bandwidth: 1000 kbps
delay: 100 microseconds
Reliability: 255
Load: 1
IP MTU: 1500

R1(config)#router eigrp 42
""",
"answer" : "redistribute ospf 13 metric 1000 10 255 1 1500",
"prompt": cp.config_router,
"clear_screen": False,
},
{
"question" : """
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
{
"question" : """
Let's do some route filtering with a route-map.

First create ACL 1 to match 192.168/16.

""",
"answer" : "access-list 1 permit 192.168.0.0 0.0.255.255",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False,
},
{
"question" : """
Now create route-map BUNNY deny 10 and match ACL 1.

access-list 1 permit 192.168.0.0 0.0.255.255

""",
"answer" : "route-map BUNNY deny 10",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "match ip address 1",
"prompt": cp.config_route_map,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
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
{
"question" : """

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
{
"question" : """

Distribute-lists allow us to apply ACLs (or PLs or RMs) to redistibution.
Distribute-lists can be applied at different levels:
    * Incoming interface
    * Outgoing interface
    * Routing Protocol (***only outbound***,)

distribute-list <ACL> {[in | out]} [<interface> | <routing process> | <AS number>]
distirbute-list prefix...
distribute-list route-map...
distribute-list gateway...
_____________________________________________________

Copy the redistribute statement and distribute-list from below:

ip access-list 99 permit 10.42.10.0 0.0.0.255
ip access-list 99 permit 10.42.11.0 0.0.0.255
!
router ospf 24
 redistribute eigrp 88 metric 50 subnets
 distribute-list 99 out eigrp 88
!
R1(config)#router ospf 24
""",
"answer" : """redistribute eigrp 88 metric 50 subnets
distribute-list 99 out eigrp 88""",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Distribute-lists allow us to apply ACLs (or PLs or RMs) to redistibution.
Distribute-lists can be applied at different levels:
    * Incoming interface
    * Outgoing interface
    * Routing Protocol (***only outbound***,)

Now apply the distribute-list to interface gig 0/3 inbound instead.
In OSPF, this will prevent the routes from entering the RIB, but not the LSDB!!!

distribute-list <ACL> {[in | out]} [<interface> | <routing process> | <AS number>]
distirbute-list prefix...
distribute-list route-map...
distribute-list gateway...

ip access-list 99 permit 10.42.10.0 0.0.0.255
ip access-list 99 permit 10.42.11.0 0.0.0.255
!
R1(config)#router ospf 24
""",
"answer" : "distribute-list 99 in gig 0/3",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Apply the following ACL to routes from OSPF into EIGRP

ip access-list 99 permit 10.42.10.0 0.0.0.255
ip access-list 99 permit 10.42.11.0 0.0.0.255
!
R1(config)#router eigrp 42
R1(config-router)#redistribute ospf 89 metric 1000 10 255 1 1500
""",
"answer" : "distribute-list 99 out ospf 89",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Apply the following prefix-list to routes redistributed from EIGRP into OSPF.

ip prefix-list e2o seq 5 permit 10.10.11.0/24
ip prefix-list e2o seq 10 permit 10.10.12.0/24
!
R1(config)#router ospf 89
R1(config-router)#redistribute eigrp 42 metric 30 subnets metric-type 1
""",
"answer" : "distribute-list prefix e20 out eigrp 42",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
View all configured prefix-lists with detail.

ip prefix-list e2o seq 5 permit 10.10.11.0/24
ip prefix-list e2o seq 10 permit 10.10.12.0/24
!
R1#
""",
"answer" : "show ip prefix-list detail",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Prefix-list with the last deletion/insertion: e2o
ip prefix-list e2o:
   count: 2, range entries: 0, sequences: 5 - 10, refcount: 3
   seq 5 permit 10.10.11.0/24 (hit count: 1, refcount: 1)
   seq 10 permit 10.10.12.0/24 (hit count: 1, refcount: 2)
"""
},
{
"question" : """
Route-Maps:
    Match:
        * match ip address
        * match ip address prefix-list
        * match length <min> <max>
        * match interface
        * match ip next-hop
        * match ip route-source
        * match metric
        * match route-type...
        * match community
        * match tag...
    Set:
        * set metric
        * set metric-type
        * set default interface
        * set interface
        * set ip default next-hop [verify-availability]
        * set ip next-hop
        * set ip vrf
        * abd more!

Use the set statement to create E1 routes.

R1(config)#route-map EIGRP-TO-OSPF permit 10
R1(config-route-map)#match ip address prefix-list EIGRP-TO-OSPF
""",
"answer" : "set metric-type type-1",
"prompt": cp.config_route_map,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
IPv6 Redistribution does not automatically include connected routes.
_____________________________________

Redistribute OSPF 46 into EIGRPv6 66. Include the connected EIGRP enabled links.
    metric: 100 10 1 255 1500

R1(config)#ipv6 router eigrp 66
""",
"answer" : "redistribute ospf 46 metric 100 10 1 255 1500 include-connected",
"prompt": "R1(config-rtr)#",
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
By default BGP only redistribute external (eBGP) routes. Using the
"bgp redistribute-internal" command, we can instruct BGP to redistribute
iBGP routes as well.
_____________________________________

Set up BGP to redistribute iBGP routes as well as eBGP routes.

R1(config)#router bgp 42
""",
"answer" : "bgp redistribute-internal",
"prompt": "R1(config-rtr)#",
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
When redistributing from OSPF to BGP, external and NSSA routes are
not redistributed by default. Use "match external [1 | 2] to redistibute
these routes.
_____________________________________

redistibute OSPF (process 89) external routes into BGP.

R1(config)#router bgp 42
""",
"answer" : "redistribute ospf 89 match external",
"prompt": "R1(config-rtr)#",
"clear_screen": True,
"suppress_positive_affirmation": False
},
]
