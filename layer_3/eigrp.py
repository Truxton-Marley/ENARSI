import common_prompts as cp

questions = [
{"question" : """
#############################
#####   Classic EIGRP   #####
#############################

Multicast: 224.0.0.10, FF00::A
IP: 88
RTP: Reliable Transport Protocol
Tables: Neighbor, Topology, Routing

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
Set router to be an EIGRP stub with the default parameters, connected and summary.

eigrp stub [connected | receive-only | redistributed | static | summary]

eigrp stub receive-only  <---Good when there is NAT/PAT for all routes behind the router

R1(config)#router eigrp 100
""",
"answer" : "eigrp stub connected summary",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Routing Protocol is "eigrp 100"
    <out omitted>
    Metric weight K1=1, K2=0, K3=1, K4=0, K5=0
    Soft SIA disabled
    NSF-aware route hold timer is 240
    Router-ID: 150.1.6.6
    Stub, connected, summary          <----!!!
    Topology : 0 (base)
      Active Timer: 3 min
      Distance: internal 90 external 170
      Maximum path: 4
      Maximum hopcount 100
      Maximum metric variance 1
      <out omitted>

R1#show ip eigrp neighbors detail
EIGRP-IPv4 Neighbors for AS(100)
H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
2    10.1.146.6             Gi0/1                    12 00:02:45    6   100  0  10
   Version 23.0/2.0, Retrans: 0, Retries: 0, Prefixes: 2
   Topology-ids from peer - 0
   Topologies advertised to peer:   base

   Stub Peer Advertising (CONNECTED SUMMARY ) Routes    <----Neighbor is a stub!
   Suppressing queries

"""
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

R1(config)#interface gig 0/3
R1(config-if)#
""",
"answer" : "ip bandwidth-percent eigrp 42 50",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Let's check out some show commands.

Metric = [(K1 * Bandwidth + [(K2 * Bandwidth) / (256 – Load)] + K3 * Delay) * K5/(K4 + Reliability)] * 256
K4 & K5 set to 0:
Metric = (K1 * Bandwidth +[(K2 * Bandwidth) / (256 – Load)] + K3 * Delay) * 256
K3, K4, and K5 set to 0, the standard, the one that matters:
Metric = (Bandwidth + Delay) * 256

delay in tens of microseconds, but, Actung!, "show interface" displays
delay in microseconds, not tens of microseconds.

EIGRP classic metrics max out at 10 Gbps, hence newer EIGRP Wide 64-bit metric.

Use the classic, show ip protocols

R1#
""",
"answer" : "show ip protocols",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """*** IP Routing is NSF aware ***

Routing Protocol is "eigrp 100"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Default networks flagged in outgoing updates
  Default networks accepted from incoming updates
  EIGRP-IPv4 Protocol for AS(100)
    Metric weight K1=1, K2=0, K3=1, K4=0, K5=0
    Soft SIA disabled
    NSF-aware route hold timer is 240
    Router-ID: 150.1.1.1
    Topology : 0 (base)
      Active Timer: 3 min
      Distance: internal 90 external 170
      Maximum path: 4
      Maximum hopcount 100
      Maximum metric variance 1

  Automatic Summarization: disabled
  Maximum path: 4
  Routing for Networks:
    150.1.0.0
    155.1.0.0
  Passive Interface(s):
    Loopback0
  Routing Information Sources:
    Gateway         Distance      Last Update
    155.1.146.4           90      00:27:34
    Gateway         Distance      Last Update
    155.1.146.6           90      00:27:33
    155.1.0.5             90      00:27:33
  Distance: internal 90 external 170

"""
},
{
"question" : """
Let's check out some show commands.

View EIGRP neighbors.

SRTT     - there and back time for EIGRP packet
RTO      - Retransmission Time
Q        - Number of packets that are waiting to be sent. Bad, not good
Retrans  - Number of times a packet has been retransmitted
Retries  - Number of times an attempt was made to retransmit packets
Prefixes - Number of prefixes received from peer

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
Let's check out some show commands.

View EIGRP neighbors with detail.

SRTT     - there and back time for EIGRP packet
RTO      - Retransmission Time
Q        - Number of packets that are waiting to be sent. Bad, not good
Retrans  - Number of times a packet has been retransmitted
Retries  - Number of times an attempt was made to retransmit packets
Prefixes - Number of prefixes received from peer

R1#
""",
"answer" : "show ip eigrp neighbors detail",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """
R5#show ip eigrp neighbors detail
EIGRP-IPv4 VR(pc) Address-Family Neighbors for AS(100)
H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
3   182.1.0.1               Tu0                      11 00:00:57  431  2586  0  13
   Version 23.0/2.0, Retrans: 0, Retries: 0, Prefixes: 10
   Topology-ids from peer - 0
   Topologies advertised to peer:   base

2   182.1.0.4               Tu0                      13 00:02:25  355  2130  0  18
   Version 23.0/2.0, Retrans: 0, Retries: 0, Prefixes: 10
   Topology-ids from peer - 0
   Topologies advertised to peer:   base

1   182.1.45.4              Gi0/4                    13 00:02:37  161   966  0  17
   Version 23.0/2.0, Retrans: 1, Retries: 0, Prefixes: 8
   Topology-ids from peer - 0
   Topologies advertised to peer:   base

0   182.1.58.8              Gi0/8                    14 00:02:47  136   816  0  7
   Version 23.0/2.0, Retrans: 2, Retries: 0, Prefixes: 2
   Topology-ids from peer - 0
   Topologies advertised to peer:   base

Max Nbrs: 0, Current Nbrs: 0

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

show ip eigrp topology [all-links]

R1#
""",
"answer" : "show ip eigrp topology",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """R1#show ip eigrp topology
EIGRP-IPv4 Topology Table for AS(100)/ID(180.1.1.1)
Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,
       r - reply Status, s - sia Status

P 192.168.3.0/24, 1 successors, FD is 3328
        via 185.1.146.4 (3328/3072), GigabitEthernet0/1
        via 185.1.0.5 (26880256/2816), Tunnel0
P 62.54.4.4/32, 1 successors, FD is 2565376
        via 185.1.146.4 (2565376/2565120), GigabitEthernet0/1
P 185.1.146.0/24, 1 successors, FD is 2816
        via Connected, GigabitEthernet0/1
P 185.1.45.0/24, 1 successors, FD is 3072
        via 185.1.146.4 (3072/2816), GigabitEthernet0/1
        via 185.1.0.5 (26880256/2816), Tunnel0
P 185.1.5.5/32, 1 successors, FD is 3104
        via 185.1.146.4 (3104/2848), GigabitEthernet0/1
        via 185.1.0.5 (26880032/288), Tunnel0
P 185.1.67.0/24, 1 successors, FD is 3072
        via 185.1.146.6 (3072/2816), GigabitEthernet0/1
P 180.1.1.1/32, 1 successors, FD is 128256
        via Connected, Loopback0
P 185.1.108.0/24, 1 successors, FD is 3584
        via 185.1.146.4 (3584/3328), GigabitEthernet0/1
        via 185.1.0.5 (26880512/3072), Tunnel0

"""
},
{
"question" : """
Show some statistics about EIGRP traffic.

R1#
""",
"answer" : "show ip eigrp traffic",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """EIGRP-IPv4 Traffic Statistics for AS(100)
  Hellos sent/received: 2034/2039
  Updates sent/received: 15/13
  Queries sent/received: 1/0
  Replies sent/received: 0/1
  Acks sent/received: 11/12
  SIA-Queries sent/received: 0/0
  SIA-Replies sent/received: 0/0
  Hello Process ID: 380
  PDM Process ID: 379
  Socket Queue: 0/10000/3/0 (current/max/highest/drops)
  Input Queue: 0/10000/3/0 (current/max/highest/drops)

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
"answer" : "offset-list 1 in 2000 gig 0/3",
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
{
"question" : """
EIGRP Wide Metrics
__________________

EIGRP Wide metrics, 64-bits
  - Uses RIB Scaling
  - supports up to 4.2 Terabit links

# TODO: Update with a real question.
New k value?

""",
"answer" : """k6""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
# {
# "question" : """
# """,
# "answer" : """""",
# "prompt": cp.config,
# "clear_screen": True,
# "suppress_positive_affirmation": False
# },
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

EIGRPv6 uses the link-local address to form neighborships.

Enable classic EIGRP IPv6 on interface gig 0/3

R1(config)#ipv6 unicast-routing
R1(config)#ipv6 router eigrp 42 1.1.1.1
R1(config-router)#eigrp router-id
R1(config-router)#interface GigabitEthernet 0/3
""",
"answer" : "ipv6 eigrp 42",
"prompt": cp.config_if,
"clear_screen": False,
},
{"question" : """

Display the EIGRPv6 routing table

""",
"answer" : "show ipv6 route eigrp",
"prompt": cp.config,
"clear_screen": False,
},
]
#"post_task_output": """"""
