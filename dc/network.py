import common_prompts as cp

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
"answer" : "",
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
VXLAN

""",
"answer" : "",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]