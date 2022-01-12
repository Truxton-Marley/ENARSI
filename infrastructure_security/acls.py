import common_prompts as cp

questions = [
{
"question" : """

#################################
###     ACLs w/ Time Range    ###
#################################

Create a time-range named feierabend that covers:
    22:00 - 6:00 on weekday
    the weekends

""",
"answer" : "time-range feierabend",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """periodic weekdays 22:00 to 23:59
periodic weekdays 0:00 to 6:00
periodic weekend 0:00 to 23:59""",
"prompt": cp.config_time_range,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Let's apply the time-range to the extended ACL "feierabend".
We can go crazy and just let all traffic go through. It's
a party!!!

R1#show time-range
time-range entry: feierabend (inactive)
   periodic weekdays 0:00 to 6:00
   periodic weekdays 22:00 to 23:59
   periodic weekend 0:00 to 23:59
R1#
R1#configure terminal
R1(config)#
R1(config)#ip access-list extended feierabend
""",
"answer" : "permit ip any any time-range feierabend",
"prompt": cp.config_ext_nacl,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Once again, you pulled through and suppled the config we needed!!!
Mario is proud and Princess Peach can reach the WWW in her free time.

Let's have a look at our work. Show all the configured ACLs.

""",
"answer" : "show ip access-lists",
"prompt": cp.config,
"clear_screen": True,
"post_task_output": """
Extended IP access list feierabend
    10 permit ip any any time-range feierabend (inactive)
""",
"suppress_positive_affirmation": False
},
{
"question" : """

#############################
###     Reflexive ACLs    ###
#############################

First things first.
Create a timeout for our Reflexive ACL of 120 seconds.

""",
"answer" : "ip reflexive-list timeout 120",
"prompt": cp.config,
"clear_screen": True,
},
{
"question" : """

Now for the inbound side of our ACL. Finish off the following
ACL with an evaluate statement name tcptraffic

R1(config)#ip access-list extended inbound
R1(config-ext-nacl)#permit icmp any any
R1(config-ext-nacl)#permit ospf any any
""",
"answer" : "evaluate tcptraffic",
"prompt": cp.config_ext_nacl,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Onward to the outbound ACL. Complete the ACL below
with a reflect statement named tcptraffic.

R1(config)#ip access-list extended inbound
R1(config-ext-nacl)#permit icmp any any
R1(config-ext-nacl)#permit ospf any any
R1(config-ext-nacl)evaluate tcptraffic
R1(config-ext-nacl)#exit
R1(config)#
R1(config)#ip access-list extended outbound
R1(config-ext-nacl)#permit icmp any any
R1(config-ext-nacl)#permit ospf any any
""",
"answer" : "permit tcp any any reflect tcptraffic",
"prompt": cp.config_ext_nacl,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Now we have the full config and just need to apply it to our WAN interface.
First apply the inbound ACL, then the outbound ACL.

R1(config)#ip access-list extended inbound
R1(config-ext-nacl)#permit icmp any any
R1(config-ext-nacl)#permit ospf any any
R1(config-ext-nacl)#evaluate tcptraffic
R1(config-ext-nacl)#exit
R1(config)#
R1(config)#ip access-list extended outbound
R1(config-ext-nacl)#permit icmp any any
R1(config-ext-nacl)#permit ospf any any
R1(config-ext-nacl)#permit tcp any any reflect tcptraffic
R1(config-ext-nacl)#exit
R1(config)#interface gig 0/0/1
""",
"answer" : """ip access-group inbound in
ip access-group outbound out""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
# {
# "question" : """

# """,
# "answer" : "show ip access-lists",
# "prompt": cp.config,
# "clear_screen": True,
# "post_task_output": """

# R1#show ip access-lists
# Extended IP access list feierabend
#     10 permit ip any any time-range feierabend (active)
# Extended IP access list inbound
#     10 permit icmp any any (35 matches)
#     20 permit ospf any any (19 matches)
#     30 permit eigrp any any
#     50 evaluate tcptraffic
#     60 deny ip any any (24 matches)
# Extended IP access list outbound
#     10 permit icmp any any (5 matches)
#     20 permit ospf any any
#     30 permit eigrp any any
#     40 permit tcp any any reflect tcptraffic (91 matches)
# Reflexive IP access list tcptraffic
# 
# """,
# "suppress_positive_affirmation": False
# },
]


ipv6_questions = [
{
"question" : """

########################
###     IPv6 ACLs    ###
########################

Create an IPv6 traffic-filter named sales

""",
"answer" : "ipv6 access-list sales",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Now create a permit statement to allow traffic from 2001:db8:1:1::/64 
to anywhere.

R1(config)ipv6 access-list sales
""",
"answer" : "permit ipv6 2001:db8:1:1::/64 any",
"prompt": cp.config_ipv6_acl,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Next apply the ACL to interface gig 0/0/1 inbound.

R1(config)ipv6 access-list sales
R1(config_ipv6_acl)permit ipv6 2001:db8:1:1::/64 any
R1(config_ipv6_acl)#exit
r1(config)interface gig 0/0/1
""",
"answer" : "ipv6 traffic-filter sales in",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
That's good for data plane traffic, but what
about control plane traffic on our lines?

Next apply the ACL to line vty 0 4 inbound.

R1(config)ipv6 access-list sales
R1(config_ipv6_acl)permit ipv6 2001:db8:1:1::/64 any
R1(config_ipv6_acl)#exit
r1(config)line vty 0 4
""",
"answer" : "ipv6 access-class sales in",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
]