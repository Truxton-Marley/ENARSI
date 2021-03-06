import common_prompts as cp

questions = [
{
"question" : """
###################
###     AAA     ###
###################

Radius -
    Uses port 1812 and 1813 OR 1645 and 1646
    Does not encrypt the entire message, just the password
    Access-Request, Access-Accept, Access-Reject
!
radius server RAD1
 address ipv4 1.1.1.1 auth-port 1812 acct-port 1813
 key cisco123

Tacacs+ -
    Uses TCP 49
    Encrypts the entire message

Configure a TACACS+ server named TAC1.
It is located at 1.1.1.1 and uses the key
cisco123.

""",
"answer" : "tacacs server TAC1",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """address ipv4 1.1.1.1
key cisco123""",
"prompt": cp.config_server_tacacs,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Now that we have our TACACS+ server, TAC1, let's
add it to the AAA server group TG

R1(config)#tacacs server TAC1
R1(config-server-tacacs)#address ipv4 1.1.1.1
R1(config-server-tacacs)#key cisco123
R1(config-server-tacacs)#exit
R1(config)#
""",
"answer" : """aaa group server tacacs+ TG""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """server name TAC1""",
"prompt": cp.config_aaa_sg_tacacs,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Now let's create a default method list for login using
our TACACS+ server group TG with a backup of the local
database.

n.b.: this will get us to the '>' prompt and then
we will still need to get to privileged exec mode.

R1(config)#tacacs server TAC1
R1(config-server-tacacs)#address ipv4 1.1.1.1
R1(config-server-tacacs)#key cisco123
R1(config-server-tacacs)#exit
R1(config)#aaa group server tacacs+ TG
R1(config-sg-tacacs+)#server name TAC1
R1(config-sg-tacacs+)#exit
R1(config)#
""",
"answer" : "aaa authentication login default group TG local",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
To get us to the '#' prompt, we can set up a default
authorization method-list. This would work without the
previous authentication method-list as well.

""",
"answer" : "aaa authorization exec default group TG local",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
We can also use older syntax and create an unnamed TACACS+ Server.
Use destination 1.1.1.1
Timeout 10
Key cisco123

""",
"answer" : """tacacs-server host 1.1.1.1
tacacs-server timeout 10
tacacs-server key cisco123""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Now set the source interface to lo0.

R1(config )# do show run | in tacacs-server
tacacs-server host 1.1.1.1
tacacs-server timeout 10
tacacs-server key cisco123
!
R1(config)#
""",
"answer" : "ip tacacs source-interface lo0",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
}
]