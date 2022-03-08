import common_prompts as cp


classic_netflow_questions = [
{
"question" : """
#################################
###     Classical NetFlow     ###
#################################

We are going to get it started by setting the flow-export
to version 5.

""",
"answer" : "ip flow-export version 5",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Send NetFlow data to 1.1.1.1 on port 9995.

Commmon ports for NetFlow are 2055, 9995 and 9996
UDP, but NetFlow has no official port.

""",
"answer" : "ip flow-export destination 1.1.1.1 9995",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

Set Netflow to monitor incoming
and outgoing traffic on gig 0/0.

R1(config)interface gig 0/0
""",
"answer" : """ip flow ingress
ip flow egress""",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Now let's check the cache flow.

R1(config)interface gig 0/0
R1(config-if)#ip flow ingress
R1(config-if)#ip flow egress
R1(config-if)#end
R1#
""",
"answer" : "show ip cache flow",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """pinecone#show ip cache flow
IP packet size distribution (135 total packets):
   1-32   64   96  128  160  192  224  256  288  320  352  384  416  448  480
   .000 .866 .037 .000 .007 .000 .088 .000 .000 .000 .000 .000 .000 .000 .000

    512  544  576 1024 1536 2048 2560 3072 3584 4096 4608
   .000 .000 .000 .000 .000 .000 .000 .000 .000 .000 .000

IP Flow Switching Cache, 278544 bytes
  1 active, 4095 inactive, 10 added
  187 ager polls, 0 flow alloc failures
  Active flows timeout in 30 minutes
  Inactive flows timeout in 15 seconds
IP Sub Flow Cache, 34056 bytes
  0 active, 1024 inactive, 0 added, 0 added to flow
  0 alloc failures, 0 force free
  1 chunk, 1 chunk added
  last clearing of statistics never
Protocol         Total    Flows   Packets Bytes  Packets Active(Sec) Idle(Sec)
--------         Flows     /Sec     /Flow  /Pkt     /Sec     /Flow     /Flow
UDP-other            9      0.0         2   161      0.0       1.0      15.2
Total:               9      0.0         2   161      0.0       1.0      15.2
"""
}
]

flexible_netflow_questions = [
{"question" : """
################################
###     Flexible NetFlow     ###
################################

Create a flow RECORD named rec1
""",
"answer" : "flow record rec1",
"prompt": cp.config,
"clear_screen": False
},
{
"question" : """
Now match on the protocol as well:

R1(config)#flow record rec1
R1(config-flow-record)#match ipv4 source address
R1(config-flow-record)#match ipv4 destination address
""",
"answer" : "match ipv4 protocol",
"prompt": cp.config_nf_rec,
"clear_screen": True
},
{
"question" : """
Good job, our config so far:

flow record rec1
  match ipv4 source address
  match ipv4 destination address
  match ipv4 protocol
  match transport source-port
  match transport destination-port

Let's collect info on the number of bytes.

""",
"answer" : "collect counter bytes",
"prompt": cp.config_nf_rec,
"clear_screen": True
},
{
"question" : """

flow record rec1
  match ipv4 source address
  match ipv4 destination address
  match ipv4 protocol
  match transport source-port
  match transport destination-port
  collect counter bytes

How about collecting info on the number of packets as well?

""",
"answer" : "collect counter packets",
"prompt": cp.config_nf_rec,
"clear_screen": False
},
{
"question" : """
Sehr gut! Now it's time to make a flow exporter.

Name it exp1.
Send NetFlow data to 1.1.1.1
Source the flow from gig 0/1
And, finally, use udp 2055
""",
"answer" : """flow exporter exp1""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """destination 1.1.1.1
source gig 0/1
transport udp 2055""",
"prompt": cp.config_nf_exp,
"clear_screen": False
},
{
"question" : """
Let's look at what we have so far! A Record and an Exporter.

flow record rec1
  match ipv4 source address
  match ipv4 destination address
  match ipv4 protocol
  match transport source-port
  match transport destination-port
  collect counter bytes
  collect counter packets
  collect interface input
  collect interface output
!
flow exporter exp1
  destination 1.1.1.1
  source gig 0/1
  transport udp 2055

We can tie them together with a NetFlow Monitor.
We could call it "mon1" and set the exporter to "exp1"
and the record to "rec1".

""",
"answer" : "flow monitor mon1",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """exporter exp1
record rec1""",
"prompt": cp.config_nf_mon,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """
That's the REM of our Flexible NetFlow config.
Time to put it to use.

flow record rec1
  match ipv4 source address
  match ipv4 destination address
  match ipv4 protocol
  match transport source-port
  match transport destination-port
  collect counter bytes
  collect counter packets
  collect interface input
  collect interface output
!
flow exporter exp1
  destination 1.1.1.1
  source gig 0/1
  transport udp 2055
!
flow monitor mon1
  exporter exp1
  record rec1

Now we need to assign the monitor to int gig 0/0
both in and out

R1(config)#interface gig 0/0
""",
"answer" : """ip flow monitor mon1 in
ip flow monitor mon1 out""",
"prompt": cp.config_if,
"clear_screen": True
}
]
