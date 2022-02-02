import common_prompts as cp

questions = [
{
"question" : """
########################
###       DMVPN      ###
########################

GRE - RFC 2784
    - IP 47
    - At least 24 Bytes extra overhead
NHRP

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
  ip nhrp map multicast dynamic

  ip nhrp registration no-unique
  ip nhrp holdtime <seconds>

Set NHRP authentication to use the password cisco123

""",
"answer" : "ip nhrp authentication cisco123",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Reduce the following commands to one command:

ip nhrp nhs 10.0.0.1
ip nhrp map 10.0.0.1 1.1.1.1
ip nhrp map multicast 1.1.1.1

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
ip nhrp map multicast 1.1.1.1""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
NHRP
____

NHRP Message Types:
  Registration, Resolution, Redirect, Purge, Error

NHRP Mapping Flags:
  * Unique
      NHRP mapping entry cannot be overwritten with an entry with same tunnel,
      different NBMA address. Watch out on cheaper links or devices behind NAT.
  * Registered
      Created by receiving an NHRP registration request. Dynamic and refreshed.
  * Used
      Data packets are actually used with this entry
  * Router
  * Local
  * Implicit
  * No Socket
  * NAT
      Remote Node supports new NHRP NAT extention type for dynamic spoke-to-spoke
      communitcation behind NATs. Does not mean this router is behind a NAT.
  * Incomplete
      Sent a resolution request and is awaiting a resolution response.
  
  # show ip route next-hop-override
  * rib
      NHRP route installed in the routing table (Route with H prefix).
  * nhop
      % Next Hop Override
  T1 - NHRP Route is installed
  T2 - Next Hop Override

show ip nhrp
show ip nhrp nhs detail
debug nhrp packet
show ip nhrp multicast
ping 224.0.0.10 | 224.0.0.5 | 224.0.0.9   <--Test routing protocols
_____________________________

Run show ip nhrp.

""",
"answer" : """show ip nhrp""",
"prompt": "R3-Spoke-Phase2#",
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """172.16.123.1/32 via 172.16.123.1
   Tunnel0 created 00:01:02, never expire
   Type: static, Flags: used
   NBMA address: 1.1.1.1
172.16.123.2/32 via 172.16.123.2
   Tunnel0 created 00:00:07, expire 00:09:52
   Type: dynamic, Flags: router used nhop
   NBMA address: 2.2.2.2
172.16.123.3/32 via 172.16.123.3
   Tunnel0 created 00:00:07, expire 00:09:52
   Type: dynamic, Flags: router unique local
   NBMA address: 3.3.3.3
    (no-socket)
172.16.123.4/32 via 172.16.123.4
   Tunnel0 created 00:00:03, expire 00:09:56
   Type: dynamic, Flags: router used nhop
   NBMA address: 4.4.4.4
"""
},
{
"question" : """
Run show ip nhrp nhs detail
""",
"answer" : "show ip nhrp nhs detail",
"prompt": "R3#",
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Legend: E=Expecting replies, R=Responding, W=Waiting
Tunnel0:
172.16.123.1  RE priority = 0 cluster = 0  req-sent 3  req-failed 0  repl-recv 3 (00:02:25 ago)
"""
},
{
"question" : """
Turn off the NHRP unique Flag.

R3(config)#interface Tunnel 0
""",
"answer" : "ip nhrp registration no-unique",
"prompt": cp.config_if,
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
  ip nhrp map multicast dynamic

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
},
{
"question" : """
Set OSPF network type on hubs and spoke for DMVPN phase 3:

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
  ip nhrp shortcut

R1(config)#interface Tunnel 42
""",
"answer" : "ip ospf network point-to-multipoint",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
More show and debugs:

debug crypto ikev2  }
debug crypto ipsec  }   } debug dmvpn detail crypto  <---newer command, three for one.
debug crypto engine }

debug dmvpn condition peer <peer_ip>

------------------------------------

show dmvpn detail
  -Check DMVPN info AND IPsec phase 1 and 2 all at once.

""",
"answer" : "show dmvpn detail",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """
Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
        N - NATed, L - Local, X - No Socket
        T1 - Route Installed, T2 - Nexthop-override
        C - CTS Capable, I2 - Temporary
        # Ent --> Number of NHRP entries with same NBMA peer
        NHS Status: E --> Expecting Replies, R --> Responding, W --> Waiting
        UpDn Time --> Up or Down Time for a Tunnel
==========================================================================

Interface Tunnel0 is up/up, Addr. is 172.16.123.4, VRF ""
   Tunnel Src./Dest. addr: 4.4.4.4/MGRE, Tunnel VRF ""
   Protocol/Transport: "multi-GRE/IP", Protect "ipsecprof"
   Interface State Control: Disabled
   nhrp event-publisher : Disabled

IPv4 NHS:
172.16.123.1  RE priority = 0 cluster = 0
Type:Spoke, Total NBMA Peers (v4/v6): 3

# Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb    Target Network
----- --------------- --------------- ----- -------- ----- -----------------
    2 1.1.1.1            172.16.123.1    UP 00:13:38     S    172.16.123.1/32
      1.1.1.1            172.16.123.4    UP 00:00:06    I2    172.16.123.4/32
    1 2.2.2.2            172.16.123.2    UP 00:00:17     D    172.16.123.2/32
    1 3.3.3.3            172.16.123.3    UP 00:00:08     D    172.16.123.3/32


Crypto Session Details:
--------------------------------------------------------------------------------

Interface: Tunnel0
Session: [0x11708818]
  Session ID: 2
  IKEv2 SA: local 4.4.4.4/500 remote 1.1.1.1/500 Active
          Capabilities:(none) connid:2 lifetime:23:59:12
  Crypto Session Status: UP-ACTIVE
  fvrf: (none), Phase1_id: 1.1.1.1
  IPSEC FLOW: permit 47 host 4.4.4.4 host 1.1.1.1
        Active SAs: 2, origin: crypto map
        Inbound:  #pkts dec'ed 47 drop 0 life (KB/Sec) 4310556/3551
        Outbound: #pkts enc'ed 47 drop 0 life (KB/Sec) 4310557/3551
   Outbound SPI : 0x 623029E, transform : esp-aes esp-sha-hmac
    Socket State: Open
"""
}
]
#"post_task_output": """"""
