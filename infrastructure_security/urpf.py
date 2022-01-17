import common_prompts as cp

#uRPF
questions = [
{"question" : """
####################
###     uRPF     ###
####################

Configure uRPF in Strict Mode on an interface:
""",
"answer" : "ip verify source unicast reachable-via rx",
"prompt": cp.config_if
},
{"question" : """
Configure uRPF in Loose Mode on an interface:
""",
"answer" : "ip verify source unicast reachable-via any",
"prompt": cp.config_if
},
{"question" : """
Configure uRPF in Loose Mode on an interface and permit the default:
""",
"answer" : "ip verify source unicast reachable-via any allow-default",
"prompt": cp.config_if
},
{
"question" : """
Nice piece of work getting that uRPF going.
But how would we verify it?
Let's first check stastics on ip traffic.

""",
"answer" : "show ip traffic",
"prompt": cp.user_exec,
"clear_screen": True,
"post_task_output": """
IP statistics:
  Rcvd:  25 total, 25 local destination
         0 format errors, 0 checksum errors, 0 bad hop count
         0 unknown protocol, 0 not a gateway
         0 security failures, 0 bad options, 0 with options
  Opts:  0 end, 0 nop, 0 basic security, 0 loose source route
         0 timestamp, 0 extended security, 0 record route
         0 stream ID, 0 strict source route, 0 alert, 0 cipso, 0 ump
         0 other
  Frags: 0 reassembled, 0 timeouts, 0 couldn't reassemble
         0 fragmented, 0 fragments, 0 couldn't fragment
         0 invalid hole
  Bcast: 0 received, 0 sent
  Mcast: 21 received, 338 sent
  Sent:  344 generated, 0 forwarded
  Drop:  0 encapsulation failed, 0 unresolved, 0 no adjacency
         0 no route, 0 unicast RPF, 0 forced drop             <-------LOOK HERE
         0 options denied
  Drop:  0 packets with source IP address zero
  Drop:  0 packets with internal loop back IP address
         0 physical broadcast
  Reinj: 0 in input feature path, 0 in output feature path
<output omitted for brevity>
""",
"suppress_positive_affirmation": False
},
{
"question" : """
We can also verify it by checking out cef specific
info for the interface. Let's check gig 0/2

""",
"answer" : "show cef int gig 0/2",
"prompt": cp.user_exec,
"clear_screen": True,
"post_task_output": """
GigabitEthernet0/2 is up (if_number 4)
  Corresponding hwidb fast_if_number 4
  Corresponding hwidb firstsw->if_number 4
  Internet address is 10.12.1.1/24
  ICMP redirects are always sent
  Per packet load-sharing is disabled
  IP unicast RPF check is enabled
  Input features: uRPF                   <----LOOK HERE
  IP policy routing is disabled
  BGP based policy accounting on input is disabled
  BGP based policy accounting on output is disabled
  IPv6 CEF switching enabled
  Hardware idb is GigabitEthernet0/2
  Fast switching type 1, interface type 27
  IP CEF switching enabled
  IP CEF switching turbo vector
  IP prefix lookup IPv4 mtrie 8-8-8-8 optimized
  Input fast flags 0x4000, Output fast flags 0x0
  ifindex 4(4)
  Slot  Slot unit 2 VC -1
  IP MTU 1500

""",
"suppress_positive_affirmation": False
},
]
