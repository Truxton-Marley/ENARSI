import common_prompts as cp

questions = [
{
"question" : """
############################
###        OSPFv2        ###
############################

# TODO: check out OSPF Loop-Free Alternate Fast Reroute???
#       It's on Boson, so maybe on exam.

OSPFv2
    RFCs - 1247 and 2329

Type 1 Hello Packet
Type 2 Database Description Packet (DBD)
Type 3 Link-State Request Packet
Type 4 Link-State Update Packet
Type 5 Link-State Acknowledgement

---

Set the router-id to 1.1.1.1.

R11(config)#router ospf 1
""",
"answer" : "router-id 1.1.1.1",
"prompt": "R11(config-router)#",
"clear_screen": False,
},
{
"question" : """
Sometimes some patchwork is needed to make Area 0 contiguous.

LSAs learned over a Virtual-Link have the DNA (DoNotAge) option set.

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
"post_task_output": """
Virtual Link OSPF_VL0 to router 11.11.11.11 is up
  Run as demand circuit
  DoNotAge LSA allowed.
  Transit area 1, via interface GigabitEthernet0/11
 Topology-MTID    Cost    Disabled     Shutdown      Topology Name
        0           2000      no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT,
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:08
    Adjacency State FULL (Hello suppressed)
    Index 1/2/4, retransmission queue length 0, number of retransmission 0
    First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
    Last retransmission scan length is 0, maximum is 0
    Last retransmission scan time is 0 msec, maximum is 0 msec
"""
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
Enable MPLS on OSPF enabled links.

R1(config)router ospf 1
""",
"answer" : """mpls autoconfig""",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Set the password and enable clear-text authentication
for OSPF on interface gig 0/1.

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

R1(config)#key chain ciscokc
R1(config-keychain)#key 42
R1(config-keychain-key)#key-string cisco123
R1(config-keychain-key)#cryptographic-algorithm hmac-sha-256
!
R1(config)#interface gig 0/1
""",
"answer" : """ip ospf authentication key-chain ciscokc""",
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

Cost = Reference Bandwidth / Interface Bandwidth

Default Costs:
T1          64
Ethernet    10
Fast Eth    1
Gig Eth     1
10-Gig Eth  1

R1(config)#router ospf 1
""",
"answer" : "auto-cost reference-bandwidth 10000",
"prompt": cp.config_router,
"clear_screen": True,
},
{
"question" : """
Enable area 3 in addition to area 0 on interface gig 0/0.

R1(config)#interface gig 0/0
""",
"answer" : "ip ospf multi-area 3",
"prompt": cp.config_if,
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

area <area-id> range <network> <mask> [advertise | not-advertise] [cost <cost>]

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
"post_task_output": """
Route in RIB generated by summary:
O        2.0.0.0/8 is a summary, 00:01:22, Null0

The summary route leads to Null0 and has an AD of 254!
R1#show ip route 2.0.0.0 255.0.0.0
Routing entry for 2.0.0.0/8
  Known via "ospf 1", distance 254, metric 20, type intra area
  Routing Descriptor Blocks:
  * directly connected, via Null0
      Route metric is 20, traffic share count is 1

"""
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
},
{
"question" : """
Let's use a filter list to filter routes coming out of area 3 into area 0.

Use the following prefix-list:

ip prefix-list mypl seq 5 deny 10.10.0.0/16 le 24
ip prefix-list mypl seq 10 permit 0.0.0.0/0 le 32

R1(config)#router ospf 1
""",
"answer" : "area 3 filter-list prefix mypl out",
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

IPv4 instance-ids: 64-95
IPv6 instance-ids: 0-31
opsfv3 <process_id> {ipv4|ipv6} area <area_id> [instance <instance_id>]

RFC 5340

router ospfv3 1
 router-id 1.1.1.1
 !
 address-family ipv6 unicast
  passive-interface Loopback 0
  router-id 1.1.1.1
  area 22 stub no-summary
  area 11 range 2001:11:11::/48
  maximum-paths 6
 exit-address-family

Type 8 LSA - Link-Local LSA
Type 9 LSA - Intra-Area Prefix LSA (improve SPF calculation when updateing prefixes)
Type 11 LSA - Grace LSA

Option bit in LSDB: E: capable of processing External LSAs
                    DC: Demand Circuit/Virtual Link, can suppress hellos
                    N: Supports Type 7 LSAs
                    MC: Capable of Multicast extendions

FF02::5 and FF02::6
Uses Link-Local addresses to form neighbor adjecencies and exchange LSAs.

Enable OSPFv3 process-id 1 on interface gig 0/3 for IPv6 in area 42 with new syntax.

R11(config)#interface GigabitEthernet 0/3
""",
"answer" : "ospfv3 1 ipv6 area 42",
"prompt": cp.config,
"clear_screen": False,
"post_task_output": """
Old syntax:

interface gig 0/3
  ipv6 ospf 1 area 42

Nex syntax:

interface gig 0/3
  ospfv3 1 ipv6 area 42

"""
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
},
{
"question" : """
OSPFv3 Authentication and Encryption

interface gig 0/3
 ospfv3 authentication ipsec spi 256 sha1 <40-char-Hex-String>
 ospfv3 authentication ipsec spi 256 md5 <32-char-Hex-String>
 ospfv3 encryption ipsec spi 256 esp aes-cbc 256 <Hex-string  256bit key (64 chars)>
!
router ospfv3 1
 area 0 authentication ipsec spi 256 sha1 <40-char-Hex-String>
 area 0 authentication ipsec spi 256 md5 <32-char-Hex-String>
!
Encryption options: ESP with des, 3des, aes-cbc [128, 192, 256]
______________________________________________________________

Configure OSPFv3 authentication on the following interface.

R1(config)#interface GigabitEthernet 0/1
""",
"answer" : """ospfv3 authentication ipsec spi 256 sha1 40-char-hex-string""",
"prompt": cp.config,
"clear_screen": True,
}
]

questions_4 = [
{
"question" : """
########################################
###        OSPF Show Commands        ###
########################################

OSPFv2
    RFCs - 1247 and 2329

Neighbor ID - OSPF Router-ID
State       - State of the Neighbor
Interface   - Local interface to neighbor

---

View OSPF neighbors.

R1#
""",
"answer" : "show ip ospf neighbor",
"prompt": cp.priv_exec,
"clear_screen": False,
"post_task_output": """
Neighbor ID     Pri   State           Dead Time   Address         Interface
255.255.255.5     0   FULL/  -        00:00:33    10.1.0.5        Tunnel0
255.255.255.2     1   FULL/BDR        00:00:35    10.1.126.2      GigabitEthernet0/1
255.255.255.6     1   FULL/DROTHER    00:00:30    10.1.126.6      GigabitEthernet0/1
255.255.255.5     0   FULL/  -        00:00:02    10.1.45.5       GigabitEthernet0/5
"""
},
{
"question" : """
Now view the OSPF neighbors with the detail option.

R1#
""",
"answer" : "show ip ospf neighbor detail",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """Neighbor 255.255.255.8, interface address 10.1.58.8
    In the area 8 via interface GigabitEthernet0/8
    Neighbor priority is 1, State is FULL, 6 state changes
    DR is 10.1.58.8 BDR is 10.1.58.5
    Options is 0x12 in Hello (E-bit, L-bit)
    Options is 0x52 in DBD (E-bit, L-bit, O-bit)
    LLS Options is 0x1 (LR)
    Dead timer due in 00:00:39
    Neighbor is up for 01:07:25
    Index 1/1/3, retransmission queue length 0, number of retransmission 2
    First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
    Last retransmission scan length is 9, maximum is 9
    Last retransmission scan time is 0 msec, maximum is 0 msec

"""
},
{
"question" : """
View the OSPF interfaces lets you check timers, network type, authentication,
area, DR/BDR and more.

View the OSPF interfaces.

R1#
""",
"answer" : "show ip ospf interface",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
GigabitEthernet0/1 is up, line protocol is up
  Internet Address 10.1.126.1/24, Area 0, Attached via Network Statement
  Process ID 1, Router ID 255.255.255.1, Network Type BROADCAST, Cost: 1
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           1         no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 255.255.255.1, Interface address 10.1.1261
  Backup Designated router (ID) 255.255.255.2, Interface address 10.1.126.2
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:03
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Index 1/3/3, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 10
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 2, Adjacent neighbor count is 2
    Adjacent with neighbor 255.255.255.2  (Backup Designated Router)
    Adjacent with neighbor 255.255.255.6
  Suppress hello for 0 neighbor(s)
GigabitEthernet0/5 is up, line protocol is up
  Internet Address 10.1.45.4/24, Area 0, Attached via Interface Enable
  Process ID 1, Router ID 255.255.255.4, Network Type POINT_TO_POINT, Cost: 1
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           1         no          no            Base
  Enabled by interface config, including secondary ip addresses
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 1, Dead 3, Wait 3, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:00
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 10
  Last flood scan time is 0 msec, maximum is 1 msec
  Neighbor Count is 1, Adjacent neighbor count is 1
    Adjacent with neighbor 255.255.255.5
  Suppress hello for 0 neighbor(s)
  Simple password authentication enabled
"""
},
{
"question" : """
Show the brief output for ospf interfaces.

R1#
""",
"answer" : "show ip ospf interface brief",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Lo0          1     0               10.0.0.1/32        1     LOOP  0/0
Gi0/0        1     0               10.1.14.1/24       10    P2P   1/1
Gi0/1        1     0               10.0.1.1/24        10    DROTH 2/2
Gi0/2        1     3               10.1.13.1/24       10    P2P   0/0
Gi0/3        1     3               10.1.12.1/24       10    P2P   0/0

"""
},
{
"question" : """
OSPF State Machine:
    Down
    Init        - Packet received, but own Router-ID not seen
    2-WAY       - Packet received and own Router-ID seen, elect DR/BDR by end
    ExStart     - Master/Slave are selected, initial Seq #
    ExChange    - Exchange DBDs
    Loading     - Exchange LSRs, LSUs, LSacks
    Full        - All good, LSDB complete and synch

OSPF Network:
    Broadcast   - DR/BDR, 10 | 40
    NBMA        - DR/BDR, 30 | 120, Requires "neighbor" command
    P2P         -   -   , 10 | 40
    P2MP        -   -   , 30 | 120
    P2MP NBMA   -   -   , 30 | 120, Requires "neighbor" command

Run a debug to watch the OSPF adjacency form.

R1#
""",
"answer" : "debug ip ospf adj",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
*Jan 29 15:33:58.780: OSPF-1 ADJ   Gi0/1: Remember old DR 10.0.0.1 (id)
*Jan 29 15:33:58.857: OSPF-1 ADJ   Gi0/1: Interface going Up
*Jan 29 15:33:58.865: OSPF-1 ADJ   Gi0/1: 2 Way Communication to 10.0.0.3, state 2WAY
*Jan 29 15:33:58.865: OSPF-1 ADJ   Gi0/1: 2 Way Communication to 10.0.0.2, state 2WAY
*Jan 29 15:33:58.869: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.2 seq 0x1C65 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jan 29 15:33:58.869: OSPF-1 ADJ   Gi0/1: Nbr state is 2WAY
*Jan 29 15:33:58.876: %OSPF-5-ADJCHG: Process 1, Nbr 10.0.0.14 on GigabitEthernet0/0 from LOADING to FULL, Loading Done
R1#
*Jan 29 15:34:03.788: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.2 seq 0x1C65 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jan 29 15:34:03.788: OSPF-1 ADJ   Gi0/1: Nbr state is 2WAY
R1#
*Jan 29 15:34:04.852: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.3 seq 0x11BF opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jan 29 15:34:04.852: OSPF-1 ADJ   Gi0/1: Nbr state is 2WAY
R1#
*Jan 29 15:34:08.716: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.2 seq 0x1C65 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jan 29 15:34:08.716: OSPF-1 ADJ   Gi0/1: Nbr state is 2WAY
*Jan 29 15:34:09.645: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.3 seq 0x11BF opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jan 29 15:34:09.645: OSPF-1 ADJ   Gi0/1: Nbr state is 2WAY
R1#
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1: Backup seen event before WAIT timer
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1: DR/BDR election
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1: Elect BDR 10.0.0.3
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1: Elect DR 10.0.0.2
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1: DR: 10.0.0.2 (Id)
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1:    BDR: 10.0.0.3 (Id)
*Jan 29 15:34:10.340: OSPF-1 ADJ   Gi0/1: Nbr 10.0.0.2: Prepare dbase exchange
*Jan 29 15:34:10.341: OSPF-1 ADJ   Gi0/1: Send DBD to 10.0.0.2 seq 0x88B opt 0x52 flag 0x7 len 32
*Jan 29 15:34:10.341: OSPF-1 ADJ   Gi0/1: Nbr 10.0.0.3: Prepare dbase exchange
R1#
*Jan 29 15:34:10.341: OSPF-1 ADJ   Gi0/1: Send DBD to 10.0.0.3 seq 0x11CC opt 0x52 flag 0x7 len 32
R1#
*Jan 29 15:34:13.717: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.2 seq 0x1C65 opt 0x52 flag 0x7 len 32  mtu 1500 state EXSTART
*Jan 29 15:34:13.717: OSPF-1 ADJ   Gi0/1: NBR Negotiation Done. We are the SLAVE
*Jan 29 15:34:13.717: OSPF-1 ADJ   Gi0/1: Nbr 10.0.0.2: Summary list built, size 13
*Jan 29 15:34:13.718: OSPF-1 ADJ   Gi0/1: Send DBD to 10.0.0.2 seq 0x1C65 opt 0x52 flag 0x2 len 292
*Jan 29 15:34:13.721: OSPF-1 ADJ   Gi0/1: Rcv DBD from 10.0.0.2 seq 0x1C66 opt 0x52 flag 0x1 len 52  mtu 1500 state EXCHANGE
*Jan 29 15:34:13.721: OSPF-1 ADJ   Gi0/1: Exchange Done with 10.0.0.2
*Jan 29 15:34:13.721: OSPF-1 ADJ   Gi0/1: Synchronized with 10.0.0.2, state FULL
*Jan 29 15:34:13.722: %OSPF-5-ADJCHG: Process 1, Nbr 10.0.0.2 on GigabitEthernet0/1 from LOADING to FULL, Loading Done

"""
},
{
"question" : """

OSPFv2 LSAs:
    Type 1 - Router
        LS-ID: Router-ID, Generated by all routers
    Type 2 - Network
        LS-ID: IP addr of DR, Generated by the DR
    Type 3 - Summary
        LS-ID: destination network, Generated by ABRs
    Type 4 - ASBR Summary
        LS-ID Router-ID of ASBR
    Type 5 - Autonomous System (External)
        LS-ID destination network, Generated by ASBRs
    Type 7 - NSSA

OSPFv3:
    Type 3 - Inter-area Prefix
    Type 4 - Inter-area Router
    Type 8 - Link
    Type 9 - Intra-area Prefix  <---Contains info previously found in Type 1 LSAs

LSAs are reflooded every 30 minutes.

This type of update is also referred to as a "paranoid update" as it is only used
to refresh the LSDB.

LSAs are purged if they reach the max age of 60 minutes. This triggers a new SPF
calulation. The LSA will also flood the LSA to other routers to inform them to
remove the LSA too.
__________________________________________________________________________________
    
View the OSPFv2 Database.

R1#
""",
"answer" : "show ip ospf database",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (255.255.255.1) (Process ID 1)

                Router Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum Link count
255.255.255.5   255.255.255.5   1276        0x8000000A 0x00F939 7
255.255.255.6   255.255.255.6   1210        0x8000000D 0x000F10 3

                Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
10.1.13.1       255.255.255.1   1504        0x80000003 0x003D4B
10.1.37.3       255.255.255.3   1299        0x80000003 0x004087
10.1.126.2      255.255.255.2   776         0x80000005 0x00C22D

                Summary Net Link States (Area 0)

Link ID         ADV Router      Age         Seq#       Checksum
10.1.8.8        255.255.255.5   1034        0x80000004 0x001F6C
10.1.58.0       255.255.255.5   1034        0x80000004 0x00FB61
10.1.108.0      255.255.255.5   1034        0x80000004 0x00DD4C

                Router Link States (Area 8)

Link ID         ADV Router      Age         Seq#       Checksum Link count
255.255.255.5   255.255.255.5   1034        0x80000007 0x002F38 1
255.255.255.8   255.255.255.8   1208        0x80000007 0x006725 3

                Net Link States (Area 8)

Link ID         ADV Router      Age         Seq#       Checksum
10.1.58.8       255.255.255.8   1208        0x80000004 0x003C07

                Summary Net Link States (Area 8)

Link ID         ADV Router      Age         Seq#       Checksum
10.1.0.0        255.255.255.5   785         0x80000004 0x001CDE
10.1.4.4        255.255.255.5   1034        0x80000004 0x007320

                Summary ASB Link States (Area 8)

Link ID         ADV Router      Age         Seq#       Checksum
255.255.255.6   255.255.255.5   785         0x80000004 0x002FFC

                Type-5 AS External Link States

Link ID         ADV Router      Age         Seq#       Checksum Tag
62.0.0.0        255.255.255.6   1210        0x80000004 0x00AEBC 626262
62.1.0.0        255.255.255.6   1210        0x80000004 0x00A2C7 626262
"""
},
{
"question" : """
View Type 1 LSAs.

R1#
""",
"answer" : "show ip ospf database router",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """          OSPF Router with ID (255.255.255.1) (Process ID 1)

                Router Link States (Area 0)

  Adv Router is not-reachable in topology Base with MTID 0

  LS age: 1705
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 255.255.255.1
  Advertising Router: 255.255.255.1
  LS Seq Number: 8000000A
  Checksum: 0x136C
  Length: 84
  Number of Links: 5

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.1.1.1
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 255.255.255.5
     (Link Data) Router Interface address: 10.1.0.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1000

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.1.0.0
     (Link Data) Network Mask: 255.255.255.0
      Number of MTID metrics: 0
       TOS 0 Metrics: 1000

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.1.13.1
     (Link Data) Router Interface address: 10.1.13.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.1.126.2
     (Link Data) Router Interface address: 10.1.126.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 1
"""
},
{
"question" : """
Show Type 1 LSAs for R1, OSPF process 1, area 0:

R1:  
Router-ID:        10.0.0.1
Router-Interface: 10.0.1.1

R4#
""",
"answer" : "show ip ospf 1 0 database router 10.0.0.1",
"prompt": "R4#",
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (10.0.0.4) (Process ID 1)

                Router Link States (Area 0)

  LS age: 77
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 10.0.0.1
  Advertising Router: 10.0.0.1
  LS Seq Number: 8000000C
  Checksum: 0x67EE
  Length: 72
  Area Border Router
  Number of Links: 4

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.0.0.1
     (Link Data) Network Mask: 255.255.255.255
      Number of MTID metrics: 0
       TOS 0 Metrics: 1

    Link connected to: another Router (point-to-point)
     (Link ID) Neighboring Router ID: 10.0.0.14
     (Link Data) Router Interface address: 10.1.14.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.1.14.0
     (Link Data) Network Mask: 255.255.255.0
      Number of MTID metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 10.0.1.1
     (Link Data) Router Interface address: 10.0.1.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 10

"""
},
{
"question" : """
View OSPF Type 2 Network LSAs.

R1#
""",
"answer" : "show ip ospf database network",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (255.255.255.1) (Process ID 1)

                Net Link States (Area 0)

  LS age: 1915
  Options: (No TOS-capability, DC)
  LS Type: Network Links
  Link State ID: 10.1.126.2 (address of Designated Router)
  Advertising Router: 255.255.255.2
  LS Seq Number: 80000005
  Checksum: 0xC22D
  Length: 36
  Network Mask: /24               <----The Mask!!!
        Attached Router: 255.255.255.2
        Attached Router: 255.255.255.1
        Attached Router: 255.255.255.6
"""
},
{
"question" : """
Show Type 2 LSAs for R1, OSPF process 1, area 0:

R1:  
Router-ID:        10.0.0.1
Router-Interface: 10.0.1.1

R4#
""",
"answer" : "show ip ospf 1 0 database network 10.0.1.1",
"prompt": "R4#",
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (10.0.0.4) (Process ID 1)

                Net Link States (Area 0)

  LS age: 987
  Options: (No TOS-capability, DC)
  LS Type: Network Links
  Link State ID: 10.0.1.1 (address of Designated Router)
  Advertising Router: 10.0.0.1
  LS Seq Number: 80000003
  Checksum: 0x53A5
  Length: 36
  Network Mask: /24
        Attached Router: 10.0.0.1
        Attached Router: 10.0.0.2
        Attached Router: 10.0.0.3

"""
},
{
"question" : """
Show Type 3 Summary LSAs

R1#
""",
"answer" : "show ip ospf database summary",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (255.255.255.1) (Process ID 1)

                Summary Net Link States (Area 0)

  LS age: 374
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.1.13.0 (summary Network Number)   <----Network advertised
  Advertising Router: 255.255.255.5                   <----ABR Router-ID
  LS Seq Number: 80000005
  Checksum: 0xFE88
  Length: 28
  Network Mask: /24                                   <----Network Mask
        MTID: 0         Metric: 3

"""
},
{
"question" : """
View Type 4 LSAs.

R1#
""",
"answer" : "show ip ospf database asbr-summary",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """

            OSPF Router with ID (255.255.255.1) (Process ID 1)

                Summary ASB Link States (Area 8)

  LS age: 1017
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(AS Boundary Router)
  Link State ID: 255.255.255.6 (AS Boundary Router address)  <---ASBR-Router-ID
  Advertising Router: 255.255.255.5                          <---ABR Router-ID
  LS Seq Number: 80000005
  Checksum: 0x2DFD
  Length: 28
  Network Mask: /0
        MTID: 0         Metric: 2
"""
},
{
"question" : """
View Type 5 LSAs. This is the only LSA to be flooded everywhere!

R1#
""",
"answer" : "show ip ospf database external",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (255.255.255.1) (Process ID 1)

                Type-5 AS External Link States

  LS age: 1555
  Options: (No TOS-capability, DC, Upward)
  LS Type: AS External Link
  Link State ID: 62.0.0.0 (External Network Number )
  Advertising Router: 255.255.255.6
  LS Seq Number: 80000005
  Checksum: 0xACBD
  Length: 36
  Network Mask: /16
        Metric Type: 2 (Larger than any link state path)
        MTID: 0
        Metric: 20     <---default metric of 20 for redistributed routes, but 1 for BGP routes!
        Forward Address: 10.10.10.13      <----IP address the route will be sent to, we route here really!
        External Route Tag: 626262

"""
},
{
"question" : """
Run the "show ip ospf" command.

R1#
""",
"answer" : "show ip ospf",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
R5#show ip ospf
 Routing Process "ospf 1" with ID 255.255.255.1
 Start time: 00:00:14.431, Time elapsed: 03:06:15.101
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability     <---Take a shorter path than Virtual-Link if possible
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 It is an area border router
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 5000 msecs
 Minimum hold time between two consecutive SPFs 10000 msecs
 Maximum wait time between two consecutive SPFs 10000 msecs
 Incremental-SPF disabled
 Minimum LSA interval 5 secs
 Minimum LSA arrival 1000 msecs
 LSA group pacing timer 240 secs
 Interface flood pacing timer 33 msecs
 Retransmission pacing timer 66 msecs
 EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
 Number of external LSA 9. Checksum Sum 0x0464E9
 Number of opaque AS LSA 0. Checksum Sum 0x000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 2. 2 normal 0 stub 0 nssa
 Number of areas transit capable is 0
 External flood list length 0
 IETF NSF helper support enabled
 Cisco NSF helper support enabled
 Reference bandwidth unit is 100 mbps     <----Reference Bandwidth
    Area BACKBONE(0)
        Number of interfaces in this area is 4 (1 loopback)
        Area has no authentication
        SPF algorithm last executed 00:25:28.774 ago
        SPF algorithm executed 20 times
        Area ranges are
           10.1.0.0/22 Active(420 - configured) Advertise
        Number of LSA 10. Checksum Sum 0x04F39D
        Number of opaque link LSA 0. Checksum Sum 0x000000
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
    Area 8
        Number of interfaces in this area is 1
        Area has no authentication
        SPF algorithm last executed 03:05:05.364 ago
        SPF algorithm executed 5 times
        Area ranges are
        Number of LSA 16. Checksum Sum 0x06FD64
        Number of opaque link LSA 0. Checksum Sum 0x000000
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0

"""
},
{
"question" : """
View Virtual-Links on R11

R11#
""",
"answer" : "show ip ospf virtual-links",
"prompt": "R11#",
"clear_screen": True,
"post_task_output": """Virtual Link OSPF_VL0 to router 10.0.0.4 is up
  Run as demand circuit
  DoNotAge LSA allowed.
  Transit area 1, via interface GigabitEthernet0/11
 Topology-MTID    Cost    Disabled     Shutdown      Topology Name
        0           2000      no          no            Base     <----65535 is the max, if it is above, link will show down cost will show 65535
  Transmit Delay is 1 sec, State POINT_TO_POINT,
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:08
    Adjacency State FULL (Hello suppressed)
    Index 1/2/4, retransmission queue length 0, number of retransmission 0
    First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
    Last retransmission scan length is 0, maximum is 0
    Last retransmission scan time is 0 msec, maximum is 0 msec

"""
},
{
"question" : """
Use the show ip ospf border-routers command.

R1#
""",
"answer" : "show ip ospf border-routers",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
            OSPF Router with ID (10.0.0.10) (Process ID 1)


                Base Topology (MTID 0)

Internal Router Routing Table
Codes: i - Intra-area route, I - Inter-area route

i 10.0.0.1 [2040] via 10.9.10.9, GigabitEthernet0/1, ABR, Area 0, SPF 9
i 10.0.0.2 [2030] via 10.9.10.9, GigabitEthernet0/1, ABR, Area 0, SPF 9
i 10.0.0.2 [10] via 10.2.10.2, GigabitEthernet0/0, ABR, Area 1, SPF 25
i 10.0.0.5 [30] via 10.2.10.2, GigabitEthernet0/0, ASBR, Area 0, SPF 9 (transit)
i 10.0.0.5 [2030] via 10.9.10.9, GigabitEthernet0/1, ABR, Area 0, SPF 9
i 10.0.0.4 [20] via 10.2.10.2, GigabitEthernet0/0, ASBR, Area 0, SPF 9 (transit)
i 10.0.0.4 [2020] via 10.9.10.9, GigabitEthernet0/1, ABR, Area 0, SPF 9
i 10.0.0.4 [2010] via 10.10.11.11, GigabitEthernet0/3, ABR/ASBR, Area 1, SPF 25
i 10.0.0.11 [20] via 10.9.10.9, GigabitEthernet0/1, ABR, Area 0, SPF 9
i 10.0.0.11 [10] via 10.10.11.11, GigabitEthernet0/3, ABR, Area 1, SPF 25
i 10.0.0.14 [2040] via 10.9.10.9, GigabitEthernet0/1, ABR, Area 0, SPF 9

"""
},
#{
# "question" : """

# R1#
# """,
# "answer" : "show ip ospf database network",
# "prompt": cp.priv_exec,
# "clear_screen": True,
# "post_task_output": """
# """
# },
]


questions_5 = [
{
"question" : """
OSPFv2 Loop-Free Alternate Fast Reroute, LFA FRR

# TODO: check out OSPF Loop-Free Alternate Fast Reroute???
#       It's on Boson, so maybe on exam.

- Quicker convergence when a link fails, bypass SPF
- Predetermined backup route added to CEF

First factor to check for a repair path:
  SRLG - Shared Risk Link Group
Second:
  Primary-Path - eliminate non-ECMP links
Third and so on:
  Interface-Disjoint
  lowest-metric
  linecard-disjoint
  node-protecting
  broadcast-interface-disjoint
  load-sharing

Primary selection factor to choose repair path?

""",
"answer" : "srlg",
"prompt": cp.priv_exec,
"clear_screen": True,
"post_task_output": """
"""
},
{
"question" : """
OSPFv2 Loop-Free Alternate Fast Reroute, LFA FRR

- Quicker convergence when a link fails, bypass SPF
- Predetermined backup route added to CEF

First factor to check for a repair path:
  SRLG - Shared Risk Link Group
Second:
  Primary-Path - eliminate non-ECMP links
Third and so on:
  Interface-Disjoint
  lowest-metric
  linecard-disjoint
  node-protecting
  broadcast-interface-disjoint
  load-sharing

fast-reroute {per-prefix | keep-all-paths} enable area 0 prefix-priority {high | low}

Enable OSPF LFA FRR for area 0 with low prefix-priority

R1(config)#router ospf 1
""",
"answer" : "fast-reroute per-prefix enable area 0 prefix-priority low",
"prompt": cp.config_router,
"clear_screen": True,
"post_task_output": """
"""
},
]