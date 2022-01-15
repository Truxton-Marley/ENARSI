import common_prompts as cp

questions = [
{
"question" : """

############################
###        OSPFv2        ###
############################

Create a virtual-link over the transit area 24
On R11 to R22.
R11 Router-ID: 11.11.11.11
R22 Router-ID: 22.22.22.22

R11(config)#router ospf 1
""",
"answer" : "area 24 virtual-link 22.22.22.22",
"prompt": "R11(config-router)#",
"clear_screen": False,
},
{
"question" : """
And now create the virtual-link on R22

R22(config)#router ospf 1
""",
"answer" : "area 24 virtual-link 11.11.11.11",
"prompt": "R22(config-router)#",
"clear_screen": False,
},
{
"question" : """
Set the OSPF dead-interval to 40 seconds

R1(config)#router ospf 1
""",
"answer" : "ip ospf dead-interval 40",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Set OSPF to use subsecond failover.
Send 4 packets per second.

BFD is a better option.

R1(config)#router ospf 1
""",
"answer" : "ip ospf dead-interval minimal hello-multiplier 4",
"prompt": cp.config_router,
"clear_screen": False,
},
{
"question" : """
Make all interfaces passive.

R1(config)#router ospf 1
""",
"answer" : "passive-interface default",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Set the password and enable clear-text authentication for OSPf
on interface gig 0/1

R1(config)interface gig 0/1
""",
"answer" : """ip ospf authentication-key cisco123
ip ospf authentication""",
"prompt": cp.config_if,
"clear_screen": True,
},
{
"question" : """
Enable clear-text authentication for area 1.

The password still needs to be set on the interface.

R1(config)#router ospf 1
""",
"answer" : "area 1 authentication",
"prompt": cp.config_router,
"clear_screen": False,
},
{
"question" : """
Set the password and enable MD5 authentication for OSPf
on interface gig 0/1.

The key # should be 42 and password cisco123.

R1(config)#interface gig 0/1
""",
"answer" : """ip ospf message-digest-key 42 md5 cisco123
ip ospf authentication message-digest""",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Enable MD5 authentication for area 1.

The password still needs to be set on the interface.

""",
"answer" : "area 1 authentication message-digest",
"prompt": cp.config_router,
"clear_screen": False,
},
{
"question" : """
Enable HMAC-SHA authentication on interface gig 0/1

R1(config)#key chain MY-KEY
R1(config-keychain)#key 42
R1(config-keychain-key)#key-string cisco123
R1(config-keychain-key)#cryptographic-algorithm hmac-sha-256
!
R1(config)#interface gig 0/1
""",
"answer" : """ip ospf authentication key-chain MY-KEY""",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Set the router-id to 1.1.1.1

R1(config)#router ospf 1
""",
"answer" : "router-id 1.1.1.1",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Set the network type to point-to-point.
This 'can' work with broadcast type networks.
It's also a good option for Ethernet links with only two routers.

R1(config)#interface gig 0/1
""",
"answer" : """ip ospf network point-to-point""",
"prompt": cp.config_if,
"clear_screen": True,
},
{
"question" : """
Set the reference bandwidth to recognize 10 Gbps links

R1(config)#router ospf 1
""",
"answer" : "auto-cost reference-bandwidth 10000",
"prompt": cp.config_router,
"clear_screen": True,
},
]

questions_2 = [
{
"question" : """
########################################
###        OSPF Summarization        ###
########################################

Summarize routes to 1.0.0.0/8 from area 42 into area 0
on an ABR with a cost of 24.

R1(config)#router ospf 1
""",
"answer" : "area 42 range 1.0.0.0 255.0.0.0 cost 24",
"prompt": cp.config_router,
"clear_screen": False,
},
{
"question" : """
Summarize external routes to 2.0.0.0/8 on an ASBR.

R1(config)#router ospf 1
R1(config-router)#redistribute eigrp 66 subnets
""",
"answer" : "summary-address 2.0.0.0 255.0.0.0",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Configure R1 as an OSPF Stub for area 3.

This will have to be done on every router in area 3.

It will also generate a Type 3 Default Route (O*IA).

Type 4 and 5 LSAs will no longer be permitted in area 3.

R1(config)#router ospf 1
""",
"answer" : "area 3 stub",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Now change area 3 to a Totally-Stubby area.
This change will only be made on ABRs.

Type 3, 4, and 5 LSAs will no longer be permitted into area 3.

R1(config)#router ospf 1
""",
"answer" : "area 3 stub no-summary",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Now change area 4 into an NSSA area.
We are on the ABR and will also need a default route.
This route should be of type O*N2.

A default route is automatically injected for a stub area,
but not for an NSSA area.

R1(config)#router ospf 1
""",
"answer" : "area 4 nssa default-information-originate",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Finally, let's change area 4 to a Totally-NSSA area.
Now we will automatically get a default route (O*IA).

R1(config)#router ospf 1
""",
"answer" : "area 4 nssa no-summary",
"prompt": cp.config_router,
"clear_screen": True,
}
]

questions_3 = [
{
"question" : """
############################
###        OSPFv3        ###
############################

Enable OSPFv3 process-id 1 on interface gig 0/3 for IPv6 in area 42.

R11(config)#interface GigabitEthernet 0/3
""",
"answer" : "ospfv3 1 ipv6 area 42",
"prompt": cp.config,
"clear_screen": False,
},
{
"question" : """
Set the OSPFv3 Hello-Interval to 10 seconds and the Dead-Interval to 40.

Defaults:
    Broadcast:           10 | 40
    NBMA:                30 | 120
    point-to-point:      10 | 40
    point-to-multipoint: 30 | 120

R22(config)#interface GigabitEthernet 0/3
""",
"answer" : """ospfv3 1 hello-interval 10
ospfv3 1 dead-interval 40""",
"prompt": cp.config_if,
"clear_screen": True,
},
{
"question" : """
Summarize routes to 2001:1:1::/48 on an ABR for area 24.

R1(config)#router ospfv3 1
R1(config-router)#address-family ipv6 unicast
""",
"answer" : """area 24 range 2001:1:1::/48""",
"prompt": cp.config_router_af,
"clear_screen": True,
}
]
