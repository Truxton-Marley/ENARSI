import common_prompts as cp

questions = [
{
"question" : """

######################
###       BGP      ###
######################

Let's get the ball rolling by disabling IPv4 as the default address family.


R1(config)#router bgp 100
""",
"answer" : "no bgp default ipv4-unicast",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the BGP router-id to 1.1.1.1

""",
"answer" : "bgp router-id 1.1.1.1",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the BGP timers to 60 180 for peer 2.2.2.2

R1(config)#router bgp 42
""",
"answer" : "neighbor 2.2.2.2 timers 60 180",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter the IPv4 unicast address family.

R1(config)#router bgp 42
""",
"answer" : "address-family ipv4",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter the IPv6 unicast address family.

R1(config)#router bgp 42
""",
"answer" : "address-family ipv6",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False   
},
{
"question" : """
Enter the IPv4 address family for VRF lila

R1(config)#router bgp 42
""",
"answer" : "address-family ipv4 vrf lila",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enter the VPNv4 address family.

R1(config)#router bgp 42
""",
"answer" : "address-family vpnv4",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set BGP to use asdot notation for 4-bytes AS numbers.
""",
"answer" : "bgp asnotation dot",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the default BGP local-preference to 150

R1(config)#router bgp 42
""",
"answer" : "bgp default local-preference 150",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the weight to 2000 for all routes received from 2.2.2.2

R1(config)#router bgp 42
""",
"answer" : "neighbor 2.2.2.2 weight 2000",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Force BGP to compare MED values from different AS peers.

R1(config)#router bgp 42
""",
"answer" : "bgp always-compare-med",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Remove any private AS numbers before sending to peer at 2.2.2.2

R1(config)#router bgp 42
""",
"answer" : "neighbor 2.2.2.2 remove-private-as",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create a soft reset inbound to store the routes learned from 2.2.2.2. Memory intensive.

R1(config)#router bgp 42
""",
"answer" : "neighbor 2.2.2.2 soft-reconfiguration inbound",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Have the router resend all BGP info to 2.2.2.2 without resetting the connections.
""",
"answer" : "clear ip bgp 2.2.2.2 soft out",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create a summary route to 10.0/16 and suppress specific routes.

R1(config)#router bgp 42
""",
"answer" : "aggregate-address 10.0.0.0 255.255.0.0 summary-only",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create a summary route to 10.0/16 and suppress specific routes.

BUT include the original BGP Path Info

R1(config)#router bgp 42
""",
"answer" : "aggregate-address 10.0.0.0 255.255.0.0 summary-only as-set",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enable BGP synchronization. Use the short form of the command "synch".

This is a bad idea. It means an iBGP route will only be advertised to an
eBGP peer if the route is also known from an IGP.

R1(config)router bgp 42
""",
"answer" : "synch",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
View the BGP IPv4 Unicast Loc-RIB:
""",
"answer" : "show bgp ipv4 unicast",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """BGP table version is 13, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
              x best-external, a additional-path, c RIB-compressed,
              t secondary path,
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *    10.16.0.0/16     60.60.60.2                             0 64860 64616 i
 *>                    16.16.16.2               0             0 64616 i
 *>   10.18.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.19.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.20.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.21.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.60.0.0/16     60.60.60.2               0             0 64860 i
 *>   172.16.5.0/24    0.0.0.0                  0         32768 ?
 *>   172.16.10.0/24   0.0.0.0                  0         32768 ?
 *>   172.17.0.0       10.1.1.2                               0 65501 65515 i
 *>   192.168.1.0      10.1.1.2                               0 65501 64950 i
 *>   192.168.20.0     0.0.0.0                  0         32768 ?
 *>   192.168.100.0    10.1.1.2                               0 65501 64950 i
"""
},
{
"question" : """
View routes advertised to IPv4 Unicast peer 10.1.1.2
""",
"answer" : "show bgp ipv4 unicast neighbors 10.1.1.2 advertised-routes",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """BGP table version is 13, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,
              r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter,
              x best-external, a additional-path, c RIB-compressed,
              t secondary path,
Origin codes: i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

     Network          Next Hop            Metric LocPrf Weight Path
 *>   10.16.0.0/16     16.16.16.2               0             0 64616 i
 *>   10.18.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.19.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.20.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.21.0.0/16     0.0.0.0                  0         32768 ?
 *>   10.60.0.0/16     60.60.60.2               0             0 64860 i
 *>   172.16.5.0/24    0.0.0.0                  0         32768 ?
 *>   172.16.10.0/24   0.0.0.0                  0         32768 ?
 *>   192.168.20.0     0.0.0.0                  0         32768 ?
"""
},
]
#"post_task_output": """"""


questions_2 = [
{
"question" : """

###############################################
###       BGP Peer Groups and Templates     ###
###############################################

Set up the BGP Peer-Group "local"
Set the remote-as to 42.
Update the source to lo0.

R1(config)#router bgp 100
""",
"answer" : "neighbor local peer-group",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "neighbor local remote-as 42",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "neighbor local update-source lo0",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """
Now that we have created the Peer Group "local",
let's us it for our peer at 24.24.24.24

neighbor local peer-group
neighbor local remote-as 42
neighbor local update-source lo0
!
R1(config)router bgp 42
""",
"answer" : "neighbor 24.24.24.24 peer-group local",
"prompt": cp.config_router,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]

questions_3 = [
{
"question" : """

#######################################################
###           BGP AS-Paths and Filtering            ###
#######################################################

Filter inbound routes from 1.1.1.1 using ACL 101.

R1(config)#access-list 101 permit 10.1.0.0 0.0.255.255 host 255.255.255.255
R1(config)#access-list 101 permit 42.42.0.0 0.0.255.255 host 255.255.255.128
R1(config)#
R1(config)#router bgp 42
R1(config-router)#address-family ipv4
R1(config-router-af)#
""",
"answer" : "neighbor 1.1.1.1 distribute-list 101 in",
"prompt": cp.config_router_af,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Finish off the following Prefix-list to match all of the remaining
RFC routes.

R1(config)#ip prefix-list RFC1918 seq 5 deny 10.0.0.0/8 le 32
R1(config)#ip prefix-list RFC1918 seq 10 deny 172.16.0.0/12 le 32
R1(config)#
""",
"answer" : "ip prefix-list RFC1918 seq 15 deny 192.168.0.0/16 le 32",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : """
Filter routes from 1.1.1.1 inbound
using a prefix-list, RFC1918.

R1(config)#ip prefix-list RFC1918 se1 5 deny 10.0.0.0/8 le 32
R1(config)#ip prefix-list RFC1918 seq 10 deny 172.16.0.0/12 le 32
R1(config)#ip prefix-list RFC1918 seq 15 deny 192.168.0.0/16 le 32
R1(config)#ip prefix-list RFC1918 seq 15 permit 0.0.0.0/0 le 32
R1(config)#
R1(config)#router bgp 42
R1(config-router)#address-family ipv4
R1(config-router-af)#
""",
"answer" : "neighbor 1.1.1.1 prefix-list RFC1918 in",
"prompt": cp.config_router_af,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create AS Path ACL 1 to match all internally learned routes
""",
"answer" : "ip as-path access-list 1 permit ^$",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Apply AS Path ACL 1 to neighbor 1.1.1.1 outbound

R1(config)#router bgp 42
""",
"answer" : "neighbor 1.1.1.1 filter-list 1 out",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": True
}
]

questions_4 = [
{
"question" : """

###############################################
###           BGP Confederations            ###
###############################################

Set peer 2.2.2.2 to be a RR client.

Route Reflectors have three rules:
  1)Advertise routes learned from iBGP peers to RR Clients
  2)Advertise routes learned from RR Clients to iBGP peers 
  3)Advertise routes learned from eBGP peers to RR Clients and Non-Clients

R1(config)#router bgp 42
R1(config-router)#address-family ipv4
""",
"answer" : "neighbor 2.2.2.2 route-reflector-client",
"prompt": cp.config_router_af,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Please set up a router to participate in a BGP confederation:
Real AS: 42
Confederation AS: 65042
Directly Connected Confederation AS Peer: 65024

""",
"answer" : "router bgp 65042",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "bgp confederation identifier 42",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "bgp confederation peers 65024",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": True
},
]

questions_5 = [
{
"question" : """

###############################################
###             BGP Communities             ###
###############################################

Enable BGP to send standard communties to peer 2.2.2.2

R1(config)#router bgp 42
R1(config-router)#address-family ipv4
R1(config-router-af)#
""",
"answer" : "neighbor 2.2.2.2 send-community",
"prompt": cp.config_router_af,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enable BGP to send extended communties to peer 2.2.2.2

R1(config)#router bgp 42
R1(config-router)#address-family ipv4
R1(config-router-af)#
""",
"answer" : "neighbor 2.2.2.2 send-community extended",
"prompt": cp.config_router_af,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Enable BGP to send extended and standard communties to peer 2.2.2.2

R1(config)#router bgp 42
R1(config-router)#address-family ipv4
R1(config-router-af)#
""",
"answer" : "neighbor 2.2.2.2 send-community both",
"prompt": cp.config_router_af,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Display BGP communities using the new format.

R1(config)#
""",
"answer" : "ip bgp-community new-format",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Configure the RM to set the No-Advertise Community
Do not advertise to ANY BGP Peers!

R1(config)route-map my_rm permit 10#
""",
"answer" : "set community no-advertise",
"prompt": cp.config_route_map,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Configure the RM to set the No-Export Community
Do not advertise to any eBGP Peers, but other confed sub-ASs are allowed.

R1(config)route-map my_rm permit 10#
""",
"answer" : "set community no-export",
"prompt": cp.config_route_map,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Configure the RM to set the local-as Community
Do not advertise to any eBGP Peers, but NOT EVEN confed sub-ASs are allowed.

R1(config)route-map my_rm permit 10#
""",
"answer" : "set community local-as",
"prompt": cp.config_route_map,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Display all BGP IPv4 unicast routes with extended community 101:100

R1#
""",
"answer" : "show bgp ipv4 unicast community 101:100",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create a community list to match the community 101:100

R1(config)#
""",
"answer" : "ip community-list 1 permit 101:100",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]