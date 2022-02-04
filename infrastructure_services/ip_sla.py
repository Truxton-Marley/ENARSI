import common_prompts as cp

questions = [
{
"question" : """
######################
###     IP SLA     ###
######################


Create a basic ICMP-ECHO IP SLA (42).
Destination address 42.42.42.42
Send it every 10 seconds.

R1(config)#ip sla 42
R1(config-ip-sla)#icmp-echo 42.42.42.42
R1(config-ip-sla-echo)#frequency 10  
R1(config-ip-sla-echo)#exit
R1(config)# ip sla schedule 42 life forever start-time now

R1#show ip sla statistics

""",
"answer" : "ip sla 42",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "icmp-echo 42.42.42.42",
"prompt": "R1(config-ip-sla)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "frequency 10",
"prompt": "R1(config-ip-sla-echo)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """
That was a basic IP SLA.

The default run-time for an IP SLA is one hour.
ip sla schedule operation-number [life {forever | seconds}] [start-time {hh:mm [:ss]
                                 [month day | day month] | pending | now | after hh:mm:ss}]
                                 [ageout seconds]

Let's schedule it to run forever now and start now.

R1(config)#ip sla 42
R1(config-ip-sla)#icmp-echo 42.42.42.42
R1(config-ip-sla-echo)#frequency 10  
R1(config-ip-sla-echo)#exit

""",
"answer" : "ip sla schedule 42 life forever start-time now",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},

{
"question" : """
Now it's time to measure Jitter.

Create an IP SLA (66) to measure UDP Jitter.
Use destination 66.66.66.66:17000 with codec
g711ulaw and a frequency of 10.

""",
"answer" : "ip sla 66",
"prompt": "R1(config)#",
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "udp-jitter 66.66.66.66 17000 codec g711ulaw control enable",
"prompt": "R1(config-ip-sla)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "frequency 10",
"prompt": "R1(config-ip-sla-jitter)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """
UDP-Jitter will require an ip sla responder.
Let's set one up on R2.

R1:
ip sla 66
  udp-jitter 66.66.66.66 17000 codec g711ulaw control enable
R1#telnet R2
R2#configure terminal
R2(config)#
""",
"answer" : "ip sla responder",
"prompt": "R2(config)",
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
We can also test TCP. Let's test TCP connections to 66.66.66.66:17000
with source IP 33.33.33.33 and source port 33333

R2(config)#ip sla 66
""",
"answer" : "tcp-connect 66.66.66.66 17000 source-ip 33.33.33.33 source-port 33333",
"prompt": "R2(config)",
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Create Track Object 1 and attach IP SLA 42 to check reachability.

R1(config)#
""",
"answer" : "track 1 ip sla 42 reachability",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Attach Track Object 1 to the default route to 1.1.1.1
""",
"answer" : "ip route 0.0.0.0 0.0.0.0 1.1.1.1 track 1",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]
