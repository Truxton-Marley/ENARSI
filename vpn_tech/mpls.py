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
Transport Label, Service Label

LFIB - Label Forwarding Information Base, LIB - Label Information Base

Route-Distinguisher: Create unique address for overlapping address space

Route-Target:        Define what routes to share and learn
    - 64-bit *extended* community
        - requires send-community [extended | both]
L2:
    VPWS - Virtual Private Wire Service, Point-to-Point
    VPLS - Virtual Private Lan Service, Multipoint-to-Multipoing

-------------------------

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
 neighbor 2.2.2.2 update-source Loopback 0
 !
 address-family vpnv4
  neighbor 2.2.2.2 activate
  neighbor 2.2.2.2 send-community extended
  neighbor 2.2.2.2 next-hop-self
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
"answer" : "show mpls interfaces",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Interface              IP            Tunnel   BGP Static Operational
GigabitEthernet0/0     Yes (ldp)     No       No  No     Yes
GigabitEthernet0/1     Yes (ldp)     No       No  No     Yes
"""
},
{
"question" : """
View MPLS LDP label bindings.

""",
"answer" : "show mpls ldp bindings",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """  lib entry: 1.1.1.1/32, rev 12
        local binding:  label: 3003
        remote binding: lsr: 1.1.1.1:0, label: imp-null
        remote binding: lsr: 2.2.2.2:0, label: 2002
  lib entry: 2.2.2.2/32, rev 10
        local binding:  label: 3002
        remote binding: lsr: 1.1.1.1:0, label: 1002
        remote binding: lsr: 2.2.2.2:0, label: imp-null
  lib entry: 10.1.1.0/24, rev 5
        local binding:  label: imp-null
        remote binding: lsr: 1.1.1.1:0, label: imp-null
        remote binding: lsr: 2.2.2.2:0, label: 2003
  lib entry: 10.2.2.0/24, rev 6
        local binding:  label: imp-null
        remote binding: lsr: 1.1.1.1:0, label: 1003
        remote binding: lsr: 2.2.2.2:0, label: imp-null
  lib entry: 12.12.12.12/32, rev 8
        local binding:  label: imp-null
        remote binding: lsr: 1.1.1.1:0, label: 1001
        remote binding: lsr: 2.2.2.2:0, label: 2001
"""
},
{
"question" : """
View the MPLS fowarding table, i.e. the LFIB.

""",
"answer" : "show mpls forwarding-table",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
Label      Label      or Tunnel Id     Switched      interface
3002       Pop Label  2.2.2.2/32       1457          Gi0/1      10.2.2.2
3003       Pop Label  1.1.1.1/32       1802          Gi0/0      10.1.1.1
"""
},
{
"question" : """
show mpls ldp discovery.

""",
"answer" : "show mpls ldp discovery",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """ Local LDP Identifier:
    12.12.12.12:0
    Discovery Sources:
    Interfaces:
        GigabitEthernet0/0 (ldp): xmit/recv
            LDP Id: 1.1.1.1:0
        GigabitEthernet0/1 (ldp): xmit/recv
            LDP Id: 2.2.2.2:0
"""
},
{
"question" : """
Show MPLS neighbors.

""",
"answer" : "show mpls ldp neighbor",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """    Peer LDP Ident: 1.1.1.1:0; Local LDP Ident 12.12.12.12:0
        TCP connection: 1.1.1.1.646 - 12.12.12.12.43199
        State: Oper; Msgs sent/rcvd: 16/17; Downstream
        Up time: 00:07:48
        LDP discovery sources:
          GigabitEthernet0/0, Src IP addr: 10.1.1.1
        Addresses bound to peer LDP Ident:
          10.1.1.1        1.1.1.1
    Peer LDP Ident: 2.2.2.2:0; Local LDP Ident 12.12.12.12:0
        TCP connection: 2.2.2.2.646 - 12.12.12.12.36877
        State: Oper; Msgs sent/rcvd: 14/14; Downstream
        Up time: 00:05:36
        LDP discovery sources:
          GigabitEthernet0/1, Src IP addr: 10.2.2.2
        Addresses bound to peer LDP Ident:
          10.2.2.2        2.2.2.2
"""
},
{
"question" : """
Show all VRF aware routes in the MP-BGP table used with MPLS.

""",
"answer" : "show bgp vpnv4 unicast all",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """BGP table version is 17, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
              x best-external, a additional-path, c RIB-compressed,
              t secondary path,
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 1:1 (default for vrf KundeA)
 *>   10.12.12.0/24    0.0.0.0                  0         32768 ?
 *>i  10.21.21.0/24    2.2.2.2                  0    100      0 ?
 *>   11.11.11.11/32   10.12.12.254       2570240         32768 ?
 *>i  22.22.22.22/32   2.2.2.2            2570240    100      0 ?
"""
},
{
"question" : """
Set MPLS to use Loopback 0 for the MPLS router-id and force it to change.

""",
"answer" : "mpls ldp router-id lo0 force",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
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
"suppress_positive_affirmation": False,
"post_task_output": """"""
},