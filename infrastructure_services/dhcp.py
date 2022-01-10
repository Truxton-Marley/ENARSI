import common_prompts as cp

questions = [
{
"question" : """

####################
###     DHCP     ###
####################

Create an off box DHCP Database to store DHCP bindings
in case of device reboot.

""",
"answer" : "ip dhcp database ftp://admin:cisco@1.1.1.1",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

Let's now look at DHCPv6.
First we will configure an IOS device to act
as a Stateless DHCPv6 Server.

Name the pool slaac.
Set the domain name to acme.com
set the dns-server t0 2001::42

R1(config)#
""",
"answer" : "ipv6 dhcp pool slaac",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : """domain-name acme.com
dns-server 2001::42""",
"prompt": cp.config_dhcpv6,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

Let's now apply the config to int gig 0/1:
  First set the interface to tell devices to use SLAAC.
  Then set the interface to use our "slaac" DHCPv6 pool.

R1#show run | sec dhcp
ipv6 dhcp pool slaac
 dns-server 2001::42
 domain-name acme.com
 !
R1#configure terminal
R1(config)#interface gig0/1
""",
"answer" : """ipv6 nd other-config-flag
ipv6 dhcp server slaac""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Moving on to STATEFUL DHCPv6:

Name the pool stateful.
Set the prefix to 2001:cafe:1:1::/64

R1(config)#
""",
"answer" : "ipv6 dhcp pool stateful",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : "",
"answer" : "address prefix 2001:cafe:1:1::/64",
"prompt": cp.config_dhcpv6,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """

Let's now apply the config to int gig 0/1:
  First set the interface to tell devices to use STATEFUL DHCPv6.
  Then set the interface to use our "stateful" DHCPv6 pool.

R1#show run | sec dhcp
ipv6 dhcp pool stateful
 address prefix 2001:cafe:1:1::/64
 dns-server 2001::42
 domain-name acme.com
 !
R1#configure terminal
R1(config)#interface gig0/1
""",
"answer" : """ipv6 nd managed-config-flag
ipv6 dhcp server stateful""",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Good job, now let's configure a client
to use SLAAC and install a dynamic default
route.

R1(config)interface gig 0/0/2
""",
"answer" : "ipv6 address autoconfig default",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False
}
]
#"post_task_output": """"""