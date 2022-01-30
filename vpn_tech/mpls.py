import common_prompts as cp

questions = [
{
"question" : """
######################
###      MPLS      ###
######################

LDP - Label Distribution Protocol, sends hellos on 224.0.0.2 UDP 646
VPNv4 iBGP Peerings between PE routers
Redistribute Routes into the appropriate BGP VRF
    VPNv4 address = 64-bit RD + 32 bit IPv4 Address
Transport Label, VPN Label (VRF)

LFIB - Label Forwarding Information Base, LIB - Label Information Base

Route-Distinguisher Create unique address for overlapping address space
Route-Target        Define what routes to share and learn
    64-bit *extended* community
        requires send-community [extended | both]
L2:
    VPWS - Virtual Private Wire Service, Point-to-Point
    VPLS - Virtual Private Lan Service, Multipoint-to-Multipoing

Create a vrf, lila, and set the
RD to 101:100
Route-target import to 101:42
Router-target export to 101:42
and, lastly, enable IPv4 unicast.

""",
"answer" : "vrf definition lila",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """rd 101:100
route-target import 101:42
route-target export 101:42
address-family ipv4""",
"prompt": cp.config_vrf,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

What's the best command to get the following output???

...
!
vrf definition lila
 rd 101:100
 route-target export 101:42
 route-target import 101:42
 !
 address-family ipv4
 exit-address-family
!
!
interface GigabitEthernet0/2
 vrf forwarding lila
 ip address 10.12.1.1 255.255.255.0
!
end


""",
"answer" : "show run vrf",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

router bgp 42
 no bgp default ipv4-unicast
 neighbor 2.2.2.2 remote-as 42
 !
 address-family vpnv4
  neighbor 2.2.2.2 activated
  neighbor 2.2.2.2 send-community extended
 exit-address-family
 !
 address-family ipv4 vrf bunny
  redistribute ospf 42
 exit-address-family
!
Enable MPLS on interface gig 0/2

R1(config)#interface gig 0/2
""",
"answer" : "mpls ip",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Check out MPLS enabled interfaces.
""",
"answer" : "show mpls interface",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
View MPLS LDP label bindings.
""",
"answer" : "show mpls ldp bindings",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
View the MPLS fowarding table, i.e. the LFIB.
""",
"answer" : "show mpls forwarding-table",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
show mpls ldp discovery
""",
"answer" : "show mpls ldp discovery",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Show MPLS neighbors.
""",
"answer" : "show mpls neighbor",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set MPLS to use Loopback 0 for the MPLS router-id and force it to change.

""",
"answer" : "mpls ldp router-id lo0 force",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set MPLS to use explicit null labels for directly connected routes.

""",
"answer" : "mpls ldp explicit-null",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
limit the MPLS label range to 500-599. Good for labbing.

""",
"answer" : "mpls label range 500 599",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]
#"post_task_output": """"""

{
"question" : """

""",
"answer" : "",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},