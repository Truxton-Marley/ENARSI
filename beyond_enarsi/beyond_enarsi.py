import common_prompts as cp

# TOC
# PPP
# EPC

# TODO: add, IOS versions, IS-IS, EPC, VXLAN, LISP, L2TP

questions_ppp = [
{
"question" : """
###################
###     ppp     ###
###################

HDLC and PPP are used for Serial Intefaces.
HDLC was originally Cisco proprietary and does not play well with others.
Therefore, PPP is generally the preferred solution.

PPP Features:
    PPP compression
    PPP multilink
    PPP authentication

Set the following interface to use PPP.

R1#configure terminal
R1#(config)interface Serial 0/0/1
""",
"answer" : "encapsulation ppp",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Authentication
--------------

PAP - Username and Password sent in plain text
    - Uses local database or TACACS+ database
CHAP - Three way exchange of a shared secret
    -  -> Send challenge
    -  <- Return encrypted challenge and hostname
    -  -> Lookup hostname and use appropriate key to verify encrypted challenge

ppp authentication {chap | chap pap | pap chap | pap} [if-needed] [<list-name> | default] [callin]

configure the following interface to use CHAP then PAP.

""",
"answer" : """ppp authentication chap pap""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Configure the router to send credentials to match the following:
!
username bunny password cisco123
!
R1#configure terminal
R1#(config)#interface Serial 0/0/1
R1#(config-if)#encapsulation ppp
R1#(config-if)#ppp authentication pap
""",
"answer" : """ppp pap sent-username bunny password cisco123""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
PPPoE
-----

{CPE} ->[Ethernet|PPP|IP Packet]-> {DSL Modem} ->[PPP|IP Packet]->  {ISP / Internet}

Enable PPPoE and bind interface Dialer 5 to Gig 0/0/1.

R1#show run interface Dialer 5
interface Dialer 5
 encapsulation ppp
 ip address negotiated
 ppp chap hostname bunny
 ppp chap password cisco123
 ip mtu 1492
 dialer pool 42       <---Needs to match on the physical interface!!!
!
R1#configure terminal
R1#(config)#interface GigabitEthernet 0/0/1
R1#(config-if)#no ip address
""",
"answer" : """pppoe enable
pppoe-client dial-pool-number 42""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

And now the other way around.

1) Set ip address to negotiated
2) use pool 42
3) set the ip mtu

R1#show run int GigabitEthernet 0/0/1
interface GigabitEthernet 0/0/1
 no ip address
 pppoe enable
 pppoe-client dial-pool-numer 42

R1#configure terminal
R1#(config)#interface dialer 5
R1#(config-if)#encapsulation ppp
R1#(config-if)#ppp chap hostname bunny
R1#(config-if)#ppp chap password cisco 123
""",
"answer" : """ip address negotiated
dialer pool 42
ip mtu 1492""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
# {
# "question" : "",
# "answer" : """address ipv4 1.1.1.1
# key cisco123""",
# "prompt": cp.config_server_tacacs,
# "clear_screen": False,
# "suppress_positive_affirmation": False
# },
# {
# "question" : "",
# "answer" : """address ipv4 1.1.1.1
# key cisco123""",
# "prompt": cp.config_server_tacacs,
# "clear_screen": False,
# "suppress_positive_affirmation": False
# },
# {
# "question" : "",
# "answer" : """address ipv4 1.1.1.1
# key cisco123""",
# "prompt": cp.config_server_tacacs,
# "clear_screen": False,
# "suppress_positive_affirmation": False
# },
]

questions_epc = [
{
"question" : """
###################
###     EPC     ###
###################

Embedded Packet Capture

monitor capture buffer MYBUFFER filter access-list MYACL max-size 1514
monitor capture point ip cef MYCAPTURE gig 0/3 both
monitor capture point associate MYCAPTURE MYBUFFER
monitor capture MYCAPTURE start
monitor capture MYCAPTURE stop
monitor capture MYBUFFER export <location>
______________________________________________________________________

Start a capture named "pcap".

R1#
""",
"answer" : "monitor capture pcap start",
"prompt": cp.priv_exec,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]