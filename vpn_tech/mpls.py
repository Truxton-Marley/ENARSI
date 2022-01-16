import common_prompts as cp

questions = [
{
"question" : """
######################
###      MPLS      ###
######################

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
address-family ipv4 unicast""",
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
]
#"post_task_output": """"""
