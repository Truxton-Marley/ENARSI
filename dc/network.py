import common_prompts as cp

# Labs based on Vinit Jain's:
#     https://learning.oreilly.com/videos/ccnp-data-center/9780136590279/
#     CCNP Data Center Core DCCOR 350-601 Complete Video Course

questions_nxos = [
{
"question" : """
#######################
###     Nexus     ###
#######################

###Preliminaries#####
conf t
license grace-period
!
int Ethernet x/x
 no mac-address
####################

Key Tenents: Resiliency, Virtualization, Efficiency, Extensibility

Linux Kernel

System Manager (sysmgr)
Interprocess Communication:
    MTS - Message Transactional Services, like the mail service
    SAP - Service Access Points, like a postbox for a process
PSS - Persistent Storage Service

show system internal sysmgr service all
show system internal sysmgr service uuid 0x0000
show cores <---look for crashed services

---

show system internal sysmgr service all
""",
"answer" : "show system internal sysmgr service all",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Name                    UUID     PID    SAP      state  Start count
  Tag  Plugin ID
----------------  ----------  ------  -----  ---------  -----------  -----------
-----  -----------
aaa               0x000000B5    3955    111  s0009              1             N/
A           0
cert_enroll       0x0000012B    3954    169  s0009              1             N/
A           0
ExceptionLog      0x00000050    4000     92  s0009              1             N/
A           0
ldap              0x0000015D    [NA]   [NA]  s0075           None             N/
A           0
psshelper_gsvc    0x0000021A    3905    398  s0009              1             N/
A           0
platform          0x00000018    3873     39  s0009              1             N/
A           0
radius            0x000000B7    4166    113  s0009              1             N/
A           0
securityd         0x0000002A    3953     55  s0009              1             N/
A           0
tacacs            0x000000B6    [NA]   [NA]  s0075           None             N/
A           0

NX-1# show system internal sysmgr service uuid 0x4E000119
UUID = 0x4E000119.
Service "__inst_014__ospf" ("ospf", 69):
        UUID = 0x4E000119, -- Currently not running --
        State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Mon Apr 25 05:31:
09 2022).
        The service has never been started since the last reboot.
        Tag = N/A
        Plugin ID: 1

NX-1#

"""
},
{
"question" : """
PSS - Persistent Storage Service
    -Store run-time data to make available during failures/recoveries
    -Key-Value pair database
    -volatile and non-volatile storage

show system internal flash

""",
"answer" : "show system internal flash",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """NX-1# show system internal flash
Mount-on                  1K-blocks      Used   Available   Use%  Filesystem
/                            409600     69468      340132     17   /dev/root
/proc                             0         0           0      0   proc
/sys                              0         0           0      0   none
/debugfs                          0         0           0      0   nodev
/cgroup                           0         0           0      0   vdccontrol
/isan                        716800    519548      197252     73   none
/etc                           5120      1628        3492     32   none
/nxos/tmp                     20480      1528       18952      8   none
/var/log                      51200        96       51104      1   none
/var/home                      5120         0        5120      0   none
/var/tmp                     307200       120      307080      1   none
/var/sysmgr                 1048576       144     1048432      1   none
/var/sysmgr/ftp              409600        80      409520      1   none
/dev/shm                    1048576    353700      694876     34   none
/volatile                    204800         0      204800      0   none
/debug                         2048        28        2020      2   none
/dev/mqueue                       0         0           0      0   none
/mnt/cfg/0                   325029     12450      295798      5   /dev/sda5
/mnt/cfg/1                   325029     12444      295804      5   /dev/sda6
/var/sysmgr/startup-cfg       40960      4268       36692     11   none
/dev/pts                          0         0           0      0   devpts
/mnt/pss                     325061      9060      299218      3   /dev/sda3
/bootflash                  3134728    202048     2773444      7   /dev/sda4
/smack                            0         0           0      0   smackfs
"""
},
{
"question" : """
Feature Manager:
    -Enable and disable services
    -feature bgp <---enable BGP
    -more complex features use: install feature-set [feature], feature-set [feature]

show system internal feature-mgr feature state

""",
"answer" : "show system internal feature-mgr feature state",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """NX-1# show system internal feature-mgr feature state
Feature               UUID        State     Reason
--------------------  ----------  --------  --------------------
bfd                   0x000002c2  disabled  feature never enabled
bfd_app               0x000002c9  disabled  feature never enabled
...
__inst_1__ospf        0x41000119  enabled   SUCCESS
...
"""
},
{
"question" : """
Line Cards
    -Line Cards run a microcode version of NX-OS
    -Has its own BIOS, POST, System Manager
    -OBFL: On-Board Failure Logging
    -ELAM: Embedded Logic Analyzer Module, tshoot dataplane
           and hardware plane forwarding problems (generally with TAC)

# Enter the CLI of the line card, generally only do with TAC:
attach module 10
show hardware inteernal dev-port-map
---
attach module 10
""",
"answer" : "attach module 10",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Files

bootflash:
slot0: <---(external USB)

dir bootflash:
dir bootflash://sup-standby/
dir logflash:

---
dir bootflash:
""",
"answer" : "dir bootflash:",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """NX-1# dir bootflash:
       4096    Feb 25 20:49:04 2016  .patch/
      16384    Feb 25 20:44:49 2016  lost+found/
       4096    Feb 26 10:11:16 2016  scripts/
   33615360    Feb 11 13:19:49 2016  titanium-d1-kickstart.7.3.0.D1.1.bin
  139230420    Feb 11 13:19:50 2016  titanium-d1.7.3.0.D1.1.bin
       4096    Feb 25 20:49:07 2016  virtual-instance/

Usage for bootflash://sup-local
  369954816 bytes used
 2840006656 bytes free
 3209961472 bytes total
NX-1#
"""
},
{
"question" : """
Test without a license

license grace-period
""",
"answer" : "license grace-period",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
VDC - Virtual Device Context

Divide physical switch into multiple logical switches
Supported on the Nexus 7000
_____________________________________________________

vPC Virtual Port Channels

Like Juniper MC-LAG
_____________________________________________________

Linux like use of > and >> and grep/egrep

show ip int brief >> bootflash:daily_interfaces.txt

---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Other Useful Features:

show cli list [str]
show cli syntax [cmd]
show running-config diff
show tech-support
show tech-support [feature]
show tech details (or tac-pac <---show tech details and compress / store in bootflash:)

---
show cli list bgp
""",
"answer" : "show cli list bgp",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
More Useful Features:

# Built in Debug-like per-feature output with:
show <featire> internal event-history
show ip ospf internal event-history adjacency

# Config Checkpoint:
checkpoint my_checkpoint
show diff rollback-patch checkpoint my_checkpoint running-config

# Python
python
quit()

# Bash
feature bash-shell
run bash
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]

questions_ospf = [
{
"question" : """
#######################
###     DC OSPF     ###
#######################

###Preliminaries#####
conf t
license grace-period
!
int Ethernet x/x
 no mac-address
####################

show run ospf
!
conf t
!
feature ospf
featrue ospfv3
!
router ospf 42
 router-id 42.42.42.42
 area 0.0.0.2 stub
 area 0.0.0.3 stub no-summary
 area 0.0.0.4 nssa [default-information-originate] [no-summary]
!
int lo0
 ip router ospf 42 area 0.0.0.0
!
int Ethernet2/1
 ip ospf network point-to-point
 ip router ospf 42 area 0.0.0.0
---

Enable the OSPF feature.

""",
"answer" : "feature ospf",
"prompt": cp.nx_config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Redistribute into OSPF:

Route-Maps required!!!

route-map bgp-to-ospf
 match ip address prefix-list b2o
!
ip prefix-list b20 permit 0.0.0.0/0 le 32
!
router ospf 42
 redistribute bgp 65530 route-map b20

""",
"answer" : "",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
See the Enarsi L3 course for more detail on OSPF and OSPFv3.
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
}
]

questions_bgp = [
    {
"question" : """
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]

questions_multicast = [
    {
"question" : """
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]

questions_overlays_otv = [
    {
"question" : """
OTV - Overlay Transport Virtualization

OTV 1.0:
[ Outer Frame | Outer IP (20-Bytes) | OTV Shim (8-Bytes) |  Inner Frame (14-Bytes) | Payload | CRC ]
    802.1q header becomes part of OTV Shim

OTV 2.5:
[ Outer Frame | Outer IP (20-Bytes) | UDP | OTV Shim (8-Bytes) |  Inner Frame (14-Bytes) | Payload | CRC ]

DCI - Datacenter Interconnect

MAC-in-IP
    -Uses IS-IS as the control protocol
        +Advertise MAC reachability information
        +OTV edge devices send IS-IS Hellos

Adds a 42 Byte header, DF-bit set
    MTUs:
    -1442 Bytes for multicast traffic
    -1450 Bytes for unicast traffic

OTV Edge Device
    -Join Interface
        +Uplink to the overlay
        +Forwards OTV control and data traffic
        +Layer 3
    -Internal Interfaces
        +Layer 2 torwards the site
        +No OTV config needed
        +STP edge, BPDUs stop here
    -Overlay Interface
        +Virtual Interface with OTV configuration
        +Multi-access multicast capable
        +Encapsulates L2 frames

Authoritative Edge Device
    -Ordinal Number, 0: even VLANs, 1: odd VLANs

Site Adjacency

Site VLAN
    -Dedicated for the OTV and not extended across the overlay
    -Needs to be the same VLAN at all OTV sites

Site-ID
    -Must be the same for all edge devices
    -Shared via IS-IS PDUs
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
OTV Multicast

feature otv
!
otv site-vlan 42
!
interface Overlay0
 description DC-1
 otv join-interface port-channel5
 otv control-group 239.12.12.12
 otv data-group 232.1.1.0/24
 otv extend-vlan 200-400
 no shutdown
!
# Must be in range 0x1 - 0xffffff
otv site-identifier 0x1
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
OTV Unicast
feature otv
!
otv site-vlan 42
!
interface Overlay0
 description DC-1
 otv join-interface port-channel5
 otv use-adjacency-server 10.10.10.10 unicast-only
 otv adjacency-server unicast-only
 otv extend-vlan 200-400
 no shutdown
!
# Must be in range 0x1 - 0xffffff
otv site-identifier 0x1
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
OTV Verify

show otv overlay 0
show otv adjacency
show otv internal adjacency
show tunnel internal implicit otv brief
show otv vlan
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]


questions_overlays_vxlan = [
{
"question" : """
Labs based on Vinit Jain's:
    https://learning.oreilly.com/videos/ccnp-data-center/9780136590279/
    CCNP Data Center Core DCCOR 350-601 Complete Video Course

VXLAN

VNID, VTEP, NVE

Flood and Learn:
    -Data-Plane learning mechanism
    -Use Multicast Traffic
    -VNIs are mapped to a multicast group
Ingress Replication:
    -Replicate BUM traffic to remote VTEPs as unicast
    -Static VTEP configuration
LISP: Like with SD-Access
EVPN: MP-BGP

VXLAN Header:
[ Flags (8-bits) | Reserved (24-bits) | Instance-ID (24-bits) | Reserved (8-bits)]

UDP Destination 4789

VTEPs:
    -Can be:
        +Switchport interfaces on the local LAN
        +L3 interfaces
        +SVIs

VXLAN Gateway:
    -VTEP that bridges traffic between VXLAN segments
---
pass
""",
"answer" : "",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Flood and Learn
(Data-Plane Learning)
!Relies on multicast

###Leafs:###
feature pim
feature isis
feature vn-segment-vlan-based
feature nv overlay

ip pim rp-address 111.111.111.111 group-list 224.0.0.0/4
ip pim ssm range 232.0.0.0/8

vlan 42
  vn-segment 4200
vlan 43
  vn-segment 4300

!
interface nve1
  no shutdown
  source-interface loopback1
  member vni 4200
    mcast-group 231.1.42.42
  member vni 4300
    mcast-group 231.1.43.43
!
show nve peers
show nve interface
---
show nve peers
""",
"answer" : "show nve peers",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Interface Peer-IP          State LearnType Uptime   Router-Mac
--------- ---------------  ----- --------- -------- -----------------
nve1      192.168.2.2      Down  DP        00:08:11 n/a
"""
},
{
"question" : """
---
show nve interface
""",
"answer" : "show nve interface",
"prompt": cp.nx_priv_exec,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """NX-OS# show nve vni data-plane
Codes: CP - Control Plane        DP - Data Plane
       UC - Unconfigured         SA - Suppress ARP
       SU - Suppress Unknown Unicast

Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
--------- -------- ----------------- ----- ---- ------------------ -----
nve1      4200     231.1.42.42       Up    DP   L2 [42]
nve1      4300     231.1.43.43       Up    DP   L2 [43]


"""
},
{
"question" : """
---
show nve vni data-plane
""",
"answer" : "show nve vni data-plane",
"prompt": cp.nx_priv_exec,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """Interface: nve1, State: Up, encapsulation: VXLAN
 VPC Capability: VPC-VIP-Only [not-notified]
 Local Router MAC: 5254.0002.fc2b
 Host Learning Mode: Data-Plane
 Source-Interface: loopback1 (primary: 192.168.1.1, secondary: 0.0.0.0)
"""
},
{
"question" : """
VXLAN Flood and Learn

Spine Mcast config:

feature pim

ip pim rp-address 111.111.111.111 group-list 224.0.0.0/4
ip pim ssm range 232.0.0.0/8
ip pim anycast-rp 111.111.111.111 11.11.11.11
ip pim anycast-rp 111.111.111.111 12.12.12.12
!
interface loopback0
  ip pim sparse-mode
!
interface Ethernet2/1
  ip pim sparse-mode
!
interface Ethernet2/2
  ip pim sparse-mode
---
pass
""",
"answer" : "",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Ingress Replication:
(Data-Plane Learning)

feature nv overlay

interface nve 1
 source-interface lo42
 member vni 10501
  ingress-replication protocol static
   peer-ip x.x.x.x
   peer-ip x.x.x.x
 
!
show nve peers
show nve interface
---
pass
""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
}
]

questions_overlays_evpn = [
{
"question" : """
EVPN
(Control-Plane Learning)

MP-BGP
Distributed Anycast Gateway

Tenant - VRF
    -1 L3 VNI
    -Multiple L2 VNIs per tenant

!Distributed Anycast Gateway
fabric forwarding anycast-gateway-mac aaaa.1111.aaaa
!
interface Vlan42
 no shutdown
 vrf context my-evpn-kunde
 ip address 10.42.42.254/24
 fabric forwarding mode anycast-gateway
!
---
fabric forwarding anycast-gateway-mac aaaa.1111.aaaa
""",
"answer" : "fabric forwarding anycast-gateway-mac aaaa.1111.aaaa",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
# {
# "question" : """

# """,
# "answer" : "",
# "prompt": cp.nx_priv_exec,
# "clear_screen": True,
# "suppress_positive_affirmation": False,
# "post_task_output": """"""
# },
# {
# "question" : """



# """,
# "answer" : "",
# "prompt": cp.nx_priv_exec,
# "clear_screen": True,
# "suppress_positive_affirmation": False,
# "post_task_output": """"""
# },
{
"question" : """
BGP EVPN Route Types:
    -Type 1 Ethernet Auto-Discovery Route
    -Type 2 MAC advertisement route -> L2 VNI MAC/MAC-IP
        + MAC - L2 VNI
        + MAC-IP - L3 VNI
    -Type 3 Inclusive Multicast Route
    -Type 4 Ethernet Segment Route
    -Type 5 IP Prefix Route -> L3 VNI Route

iBGP: Spines are Route Reflectors
eBGP: Spines in one AS, Leafs in the other

""",
"answer" : "",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
EVPN Configuration:

install feature-set fabric
feature-set fabric
feature fabric forwarding
feature isis    !<---Or OSPF
feature bgp
feature pim !<---Needed for Flood and Learn, not needed for Ingress Replication
feature nv overlay
feature vn-segment-vlan-based   !<---Not needed on spine
feature interface-vlan
!
nv overlay evpn
!
fabric forwarding anycast-gateway-mac 4242.4242.4242
!
vrf context evpn_a
 vni 4100
  rd auto
  add ipv4 unicast
   route-target both auto
!
! Anycast Gateway for L2 VNIs:
interface Vlan42
  no shutdown
  vrf member evpn_a
  no ip redirects
  ip address 10.42.42.254/24
  fabric forwarding mode anycast-gateway
!
interface Vlan43
  no shutdown
  vrf member evpn_a
  no ip redirects
  ip address 10.43.43.254/24
  fabric forwarding mode anycast-gateway
!
! L3 VNI:
interface Vlan41
  vrf member evpn_a
  ip forward
!
router bgp 42
  router-id 2.2.2.2
  neighbor 11.11.11.11
    remote-as 42
    update-source loopback0
    address-family l2vpn evpn
      send-community both
  neighbor 12.12.12.12
    remote-as 42
    update-source loopback0
    address-family l2vpn evpn
      send-community both
  vrf evpn_a
    address-family ipv4 unicast
      advertise l2vpn evpn
evpn
  vni 4200 l2
    rd auto
    route-target import auto
    route-target export auto
  vni 4300 l2
    rd auto
    route-target import auto
    route-target export auto
!
interface nve1
  no shutdown
  source-interface loopback1
  host-reachability protocol bgp
  member vni 4100 associate-vrf
  member vni 4200
    mcast-group 231.1.42.42
  member vni 4300
    mcast-group 231.1.43.43
---
pass
""",
"answer" : "",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Verification:

show mac address-table dynamic
show l2route evpn mac all
show bgp l2vpn evpn
show nve peers
---

show bgp l2vpn evpn summary
""",
"answer" : "show bgp l2vpn evpn summary",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """BGP summary information for VRF default, address family L2VPN EVPN
BGP router identifier 11.11.11.11, local AS number 42
BGP table version is 12, L2VPN EVPN config peers 2, capable peers 2
2 network entries and 2 paths using 288 bytes of memory
BGP attribute entries [2/288], BGP AS path entries [0/0]
BGP community entries [0/0], BGP clusterlist entries [0/0]

Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
1.1.1.1         4    42      17      36       12    0    0 00:05:37 1
2.2.2.2         4    42      38      45       12    0    0 00:08:33 1
Sp1#
"""
},
{
"question" : """
Verification:

show mac address-table dynamic
show l2route evpn mac all
show bgp l2vpn evpn
show nve peers

---
show bgp l2vpn evpn
""",
"answer" : "show bgp l2vpn evpn",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """BGP routing table information for VRF default, address family L2VPN EVPN
BGP table version is 12, local router ID is 11.11.11.11
Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-i
njected
Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

   Network            Next Hop            Metric     LocPrf     Weight Path
Route Distinguisher: 1.1.1.1:32809
*>i[2]:[0]:[0]:[48]:[5254.000b.53bc]:[32]:[10.42.42.11]/272
                      192.168.1.1                       100          0 i

Route Distinguisher: 2.2.2.2:32809
*>i[2]:[0]:[0]:[48]:[5254.001c.13c4]:[32]:[10.42.42.22]/272
                      192.168.2.2                       100          0 i
"""
},
{
"question" : """
Verification:

show mac address-table dynamic
show l2route evpn mac all
show bgp l2vpn evpn
show nve peers
---
show l2route evpn mac all
""",
"answer" : "show l2route evpn mac all",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Leaf1# show l2route evpn mac all
Topology    Mac Address    Prod   Next Hop (s)
----------- -------------- ------ ---------------
42          5254.001c.13c4 BGP    192.168.2.2
"""
},
{
"question" : """
Verification:

show mac address-table dynamic
show l2route evpn mac all
show bgp l2vpn evpn
show nve peers
---
show nve interface
""",
"answer" : "show nve interface",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Leaf1# show nve interface
Interface: nve1, State: Up, encapsulation: VXLAN
 VPC Capability: VPC-VIP-Only [not-notified]
 Local Router MAC: 5254.0002.fc2b
 Host Learning Mode: Control-Plane
 Source-Interface: loopback1 (primary: 192.168.1.1, secondary: 0.0.0.0)
"""
},
{
"question" : """
Verification:

show mac address-table dynamic
show l2route evpn mac all
show bgp l2vpn evpn
show nve peers
---
show bgp l2vpn evpn 10.42.42.22
""",
"answer" : "show bgp l2vpn evpn 10.42.42.22",
"prompt": cp.nx_priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Leaf1# show bgp l2vpn evpn 10.42.42.22
Route Distinguisher: 1.1.1.1:32809    (L2VNI 4200)
BGP routing table entry for [2]:[0]:[0]:[48]:[5254.001c.13c4]:[32]:[10.42.42.22]
/272, version 4
Paths: (1 available, best #1)
Flags: (0x00021a) on xmit-list, is in l2rib/evpn, is not in HW,

  Advertised path-id 1
  Path type: internal, path is valid, is best path
             Imported from 2.2.2.2:32809:[2]:[0]:[0]:[48]:[5254.001c.13c4]:[32]:
[10.42.42.22]/272
  AS-Path: NONE, path sourced internal to AS
    192.168.2.2 (metric 81) from 11.11.11.11 (11.11.11.11)
      Origin IGP, MED not set, localpref 100, weight 0
      Received label 4200 4100
      Extcommunity:
          RT:42:4200
          ENCAP:8
          Router MAC:5254.000e.2d38
      Originator: 2.2.2.2 Cluster list: 11.11.11.11

  Path-id 1 not advertised to any peer

Route Distinguisher: 2.2.2.2:32809
BGP routing table entry for [2]:[0]:[0]:[48]:[5254.001c.13c4]:[32]:[10.42.42.22]
/272, version 5
Paths: (2 available, best #2)
Flags: (0x000202) on xmit-list, is not in l2rib/evpn, is not in HW, , is locked

  Path type: internal, path is valid, not best reason: Neighbor Address
  AS-Path: NONE, path sourced internal to AS
    192.168.2.2 (metric 81) from 12.12.12.12 (12.12.12.12)
      Origin IGP, MED not set, localpref 100, weight 0
      Received label 4200 4100
      Extcommunity:
          RT:42:4200
          ENCAP:8
          Router MAC:5254.000e.2d38
      Originator: 2.2.2.2 Cluster list: 12.12.12.12

  Advertised path-id 1
  Path type: internal, path is valid, is best path
  AS-Path: NONE, path sourced internal to AS
    192.168.2.2 (metric 81) from 11.11.11.11 (11.11.11.11)
      Origin IGP, MED not set, localpref 100, weight 0
      Received label 4200 4100
      Extcommunity:
          RT:42:4200
          ENCAP:8
          Router MAC:5254.000e.2d38
      Originator: 2.2.2.2 Cluster list: 11.11.11.11

  Path-id 1 not advertised to any peer

Leaf1#
"""
},
]



questions_aci = [
{
"question" : """
ACI - Cisco's core SDN solution for the data center


ACI - Application Centric Infrastructure
    - Basic Network Policy, Automation...
NAE - Network Assurance Engine
    - SLAs...
Tetration - 
    - L4-L7 Services...

---

Fabric
    -Spine and Leaf / Clos
        * 9500 Spines | 9300 Leafs
    -Unnumbered interfaces
    -IS-IS
    -Anycast Gateways (Leaf layer)
    -eVXLAN / MP-BGP

---
Logical Constructs:
    -Tenant
    -L3 Private Network (Context/VRF)
    -Bridge Domain (Container for subnets)
    -Subnet
    -End-Point Group (Container of objects requiring the same policy)
    -Contract

---
pass
""",
"answer" : "",
"prompt": "> ",
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Nexus 9000 has two modes of operation: NX-OS & ACI Mode

ACI Mode:
    -Only programmable via Policy-Engine in the APIC Controller
    -No CLI config
    -Object Oriented Schema, XML or JSON

---
pass
""",
"answer" : "",
"prompt": "> ",
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
ACI Programmability

Cobra SDK

The Object Model:
    Logical Model
    Concrete Model

Everything within an ACI Fabric is an object.
MO - Managed Objects
MIT - Management Information Tree
    -MOs connected via Parent/Child relationship
RN - Relative Name
    -tn-: Tenant, ctx-: Context/VRF, BD-: Bridge Domain, ap-: AppProfile, etc.
DN - Distinguished Name
    -uni/tn-Cats/ap-Toys/epg-Feathers
        fvAp is the parent class, Toys is the specific fvAp object: ap-Toys/epg-Feathers
        fvTenant is the next parent class and Cats si the specific fvTenant object: tn-Cats/ap-Toys/epg-Feathers
        Root is the parent of fvTenant: uni/tn-Cats/ap-Toys/epg-Feathers
    -used to make API requests

Sample API Get request:
    https://sandboxapicdc.cisco.com/api/class/fvAp.json?
    List all Application Profiles and JSON formatted listing of their attributes

---
pass
""",
"answer" : "",
"prompt": "> ",
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
# {
# "question" : """


# """,
# "answer" : "",
# "prompt": cp.priv_exec,
# "clear_screen": True,
# "suppress_positive_affirmation": False,
# "post_task_output": """"""
# },
]