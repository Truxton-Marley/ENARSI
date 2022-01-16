import common_prompts as cp

questions = [
{"question" : """
#############################
#####   Classic EIGRP   #####
#############################

Set the router-id to 1.1.1.1

R1(config)#router eigrp 100
R1(config-router)#
""",
"answer" : "eigrp router-id 1.1.1.1",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{"question" : """
Set the Key-chain on interface gig 0/0/1 and
then enable md5 authentication.

R1#show run | sec key chain
!
key chain ciscokc
 key 42
  key-string cisco123
!
R1#
R1(config)#interface gig 0/0/1
""",
"answer" : """ip authentication key-chain eigrp 42 ciscokc
ip authentication mode eigrp 42 md5""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the hello timer to 5 seconds for interface gig 0/0/1.
Set the hold timer to 15 seconds.
R1#
R1(config)#interface gig 0/0/1
""",
"answer" : """ip hello-interval eigrp 42 5
ip hold-time eigrp 42 15""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Make interface gig 0/1 passive

R1(config)#router eigrp 100
R1(config-router)#
""",
"answer" : "passive-interface gig 0/1",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Summarize routes to 1.0.0.0/16 on interface gig 0/3 and include a leak-map, lm.

Use bit-length notation for the subnet mask, but note that dotted decimal is also vaild.
Manually set the AD for the metric to 5.
Manually set the metric with the following parameters: 1000 10 255 1 1500

R1(config)#interface gig 0/3
""",
"answer" : """ip summary-address eigrp 42 1.0.0.0/16 leak-map lm""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : """R1(config-if)#router eigrp 42
""",
"answer" : """summary-metric 1.0.0.0/16 distance 5
summary-metric 1.0.0.0/16 1000 10 255 1 1500""",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Set router to be an EIGRP stub with the default parameters, conneccted and summary.

eigrp stub [connected | receive-only | redistributed | static | summary]

R1(config)#router eigrp 100
""",
"answer" : "eigrp stub connected summary",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Disable Split-Horizon on interface Tunnel 0

R1(config)#interface tunnel 0
""",
"answer" : "no ip split-horizon eigrp 42",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the maximum hop-count to 100.

R1(config)#router eigrp 42
R1(config-router)#
""",
"answer" : "metric maximum-hops 100",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the SIA Timer to five minutes.

R1(config)#router eigrp 42
R1(config-router)#
""",
"answer" : "timers active-time 5",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set EIGRP to use no more than 50% of the bandwidth. This is the default.

R1(config)#router eigrp 42
R1(config-router)#
""",
"answer" : "ip bandwidth-percent eigrp 42 50",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Let's check out some show commands.

View EIGRP neighbors

R1#
""",
"answer" : "show ip eigrp neighbors",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """EIGRP-IPv4 Neighbors for AS(42)
H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
1   192.1.0.5               Tu0                      12 00:03:51  205  2097  0  15
0   192.1.146.4             Gi0/1                    11 00:04:03 1017  5000  0  13
"""
},
{
"question" : """
Show EIGRP interfaces with detail.

R1#
""",
"answer" : "show ip eigrp interfaces detail",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """
EIGRP-IPv4 Interfaces for AS(100)
                              Xmit Queue   PeerQ        Mean   Pacing Time   Multicast    Pending
Interface              Peers  Un/Reliable  Un/Reliable  SRTT   Un/Reliable   Flow Timer   Routes
Lo0                      0        0/0       0/0           0       0/0            0           0
  Hello-interval is 5, Hold-time is 15
  Split-horizon is enabled
  Next xmit serial <none>
  Packetized sent/expedited: 0/0
  Hello's sent/expedited: 0/1
  Un/reliable mcasts: 0/0  Un/reliable ucasts: 0/0
  Mcast exceptions: 0  CR packets: 0  ACKs suppressed: 0
  Retransmissions sent: 0  Out-of-sequence rcvd: 0
  Topology-ids on interface - 0
  Authentication mode is not set
  Topologies advertised on this interface:  base
  Topologies not advertised on this interface:

Gi0/1                    2        0/0       0/0         507       0/0         2448           0
  Hello-interval is 5, Hold-time is 15
  Split-horizon is enabled
  Next xmit serial <none>
  Packetized sent/expedited: 6/0
  Hello's sent/expedited: 133/3
  Un/reliable mcasts: 0/5  Un/reliable ucasts: 8/5
  Mcast exceptions: 0  CR packets: 0  ACKs suppressed: 0
  Retransmissions sent: 2  Out-of-sequence rcvd: 0
  Topology-ids on interface - 0
  Authentication mode is md5,  key-chain is "ciscokc"
  Topologies advertised on this interface:  base
  Topologies not advertised on this interface:
"""
},
{
"question" : """
View the EIGRP Topology tables.

R1#
""",
"answer" : "show ip eigrp topology",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """
#TODO: Add Topology Table output here.
"""
}
]

questions_2 = [
{"question" : """
######################################
#####   EIGRP Router Filtering   #####
######################################

distribute-list ?
  ACL # or Name
  gateway
  prefix
  route-map

####################

ip access-list 1 deny 10.10.10.0 0.0.0.255
ip access-list 1 permit any

Apply an inbound distribute-list using ACL 1.

R1(config)#router eigrp NAMED
R1(config-router)#address-family ipv4 as 42
R1(config-router)#topology base
""",
"answer" : "distribute-list 1 in",
"prompt": cp.config_router_af_topology,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
ip prefix-list PL seq 5 deny 20.20.20.0/24
ip prefix-list PL seq 10 permit 0.0.0.0/0 le 32

Apply an outbound distribute-list using the above PL.

R1(config)#router eigrp NAMED
R1(config-router)#address-family ipv4 as 42
R1(config-router)#topology base
""",
"answer" : "distribute-list prefix PL out",
"prompt": cp.config_router_af_topology,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

ip access-list 1 deny 10.10.10.0 0.0.0.255
ip access-list 1 permit any

offset-list {<ACL# | ACL-Name>} {in | out} <offset-value> [interface]

Apply an offset-list inbound using ACL 1 with an offset-value of 2000.
Limit the offset-list to int gig 0/3.

R1(config)#router eigrp NAMED
R1(config-router)#address-family ipv4 as 42
R1(config-router)#topology base
""",
"answer" : "offset-list 1 in 2000 int gig 0/3",
"prompt": cp.config_router_af_topology,
"clear_screen": True,
"suppress_positive_affirmation": False
}
]

questions_3 = [
{"question" : """
###########################
#####   NAMED EIGRP   #####
###########################

Enable MD5 authentication on all interfaces.

R1(config)#do show run | sec key chain
!
key chain ciscokc
 key 42
  key-string cisco123
!
R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
R1(config-router-af)#af-interface default
""",
"answer" : """authentication key-chain ciscokc
authentication mode md5""",
"prompt": cp.config_router_af_if,
"clear_screen": False,
},
{"question" : """
Set the hello timer to 5 seconds for all interfaces.
5 | 15 is the default for fast links.
60 | 180 is the default for slow links.

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
R1(config-router-af)#af-interface default
""",
"answer" : """hello-interval 5
hold-time 15""",
"prompt": cp.config_router_af_if,
"clear_screen": False,
},
{
"question" : """
Enable the IPv6 address family for AS 6.

ACHTUNG! ACHTUNG! This will enable EIGRP on all IPv6 enabled interfaces!!!

R1(config)#router eigrp NAMED
""",
"answer" : """address-family ipv6 unicast autonomous-system 6""",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{"question" : """
Summarize routes to 1.0.0.0/16 on interface gig 0/3 and include a leak-map, lm.
Manually set the AD to 5.
Manually set the metric with the following parameters: 1000 10 255 1 1500

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
R1(config-router-af)#af-interface gig 0/3
""",
"answer" : "summary-address 1.0.0.0/16 leak-map lm",
"prompt": cp.config_router_af_if,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{"question" : """R1(config-router-af-interface)#exit
R1(config-router-af)#topology base
""",
"answer" : """summary-metric 1.0.0.0/16 distance 5
summary-metric 1.0.0.0/16 1000 10 255 1 1500""",
"prompt": cp.config_router_af_topology,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{"question" : """
Set the SIA Timer to five minutes.

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
R1(config-router-af)#topology base
""",
"answer" : "timers active-time 5",
"prompt": cp.config_router_af_topology,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter vrf bunny AS 66 for EIGRP Named Mode.

R1(config)# do show run | sec vrf def
vrf definition bunny
 !
 address-family ipv4
 exit-address-family
!
R1(config)#router eigrp NAMED
""",
"answer" : """address-family ipv4 vrf bunny autonomous-system 66""",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create an ACL 101 to test EIGRP Traffic on a production network.
""",
"answer" : """access-list 101 permit eigrp any any log
access-list 101 permit ip any any""",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]

questions_4 = [
{"question" : """
######################################
#####   NAMED EIGRP STUB-SITES   #####
######################################

Set the following router to be an EIGRP IWAN stub router with RD 101:100.

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
""",
"answer" : "eigrp stub-site 101:100",
"prompt": "R1(config-router-af)",
"clear_screen": False,
},
{"question" : """
Now set interface gig0/3 to be a WAN-interface.

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
R1(config-router-af)#eigrp stub-site 101:100
R1(config-router-af)#af-interface GigabitEthernet 0/3
""",
"answer" : "stub-site wan-interface",
"prompt" : "R1(config-router-af-interface)",
"clear_screen": True,
}
]

questions_5 = [
{"question" : """
##########################
#####   IPv6 EIGRP   #####
##########################

Enable classic EIGRP IPv6 on interface gig 0/3


R1(config)#ipv6 unicast-routing
R1(config)#ipv6 router eigrp 42
R1(config-router)#eigrp router-id
R1(config-router)#interface GigabitEthernet 0/3
""",
"answer" : "ipv6 eigrp 42",
"prompt": cp.config_if,
"clear_screen": False,
},
{"question" : """

""",
"answer" : "ipv6 eigrp 42",
"prompt": cp.config_if,
"clear_screen": False,
},
]
#"post_task_output": """"""
