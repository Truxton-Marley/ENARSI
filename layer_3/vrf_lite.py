import common_prompts as cp

questions = [
{
"question" : """
##############################
#######   VRF LITE      ######
##############################

VRF-Lite, no MPLS or MP-BGP needed.

ip vrf bunny            <---Old School
!
vrf definition bunny    <---New School
 !rd 101:100             <---Only needed for BGP VRF-Lite
 address-family ipv4
!
show ip vrf interface
!
ping vrf bunny 8.8.8.8
ip route vrf bunny 0.0.0.0 0.0.0.0 1.1.1.1
!
------------------------------------------

Create OSPF instance 11 for vrf bunny.

""",
"answer" : "router ospf 11 vrf bunny",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Create classic EIGRP AS 42 for vrf bunny AS 66

""",
"answer" : "router eigrp 42",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """address-family ipv4 vrf bunny autonomous-system 66""",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

router rip
!
 address-family ipv4 vrf bunny
  network 10.0.0.0
  no auto-summary
  version 2
 exit-address-family
!
-------------------------------

Set up rip for VRF-Lite with vrf bunny.

R1(config)#router rip
""",
"answer" : """address-family ipv4 vrf bunny""",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

BGP requires a RD on the VRF for VRF-Lite!

router bgp 42
!
 address-family ipv4 vrf bunny
  neighbor 2.2.2.2 remote-as 24
  neighbor 2.2.2.2 activate
  no synchronization
  network 1.1.1.1. mask 255.255.255.255
 exit-address-family
!
show bgp vpnv4 unicast all   |    show ip bgp vpnv4 all
show bgp vpnv4 unicast rd...
show bgp vpnv4 unicast vrf...
-------------------------------

Set up BGP for VRF-Lite with vrf bunny.

R1(config)#router bgp 42
""",
"answer" : """address-family ipv4 vrf bunny""",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Upgrade old school VRF configs to new school VRF configs.

vrf upgrade-cli multi-af-mode {common-policies | non-common-policies} [vrf <vrf_name>]

""",
"answer" : """vrf upgrade-cli multi-af-mode common-policies""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]
