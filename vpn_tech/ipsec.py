import common_prompts as cp

questions_ikev1 = [
{
"question" : """
########################
###       IPsec      ###
########################

This section was largely infuenced by BRKSEC-3001, Frederic Detienne, Advanced IKEv2 Protocol, 2019, Barcelona

A collection of 12 RFCs

IKEv1:
    MM - Main Mode, 6 packet exchange, more secure, ids protected.
    Aggressive Mode - 3 packet exchange, less secure (DoS), exposes identity

    Xauth: username/password authentication

HAGLE, Hash, Auth, Group, Lifetime, Encryption

ISAKMP:
Phase 1:
    * Used for control plane
    * Prove ID
    * Negotiate data plane security settings
Phase 2 (Quick Mode):
    * Used for data plane
    * Transports the protected data

UDP 500
ESP - IP 50    <---Cannot work through PAT, hence NAT-T
AH  - IP 51    <---Cannot handle NAT

UDP 4500 if NAT has been detected in MM3+4

""",
"answer" : "crypto isakmp policy 10",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
!
isakmp policy 10
 authentication pre-share
 encryption
 group
 hash
!
Create the pre-share set and permit all addresses.
!
""",
"answer" : "crypto isakmp key cisco address 0.0.0.0",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]

questions_ikev2 = [
{
"question" : """
########################
###       IPsec      ###
########################

IKEv2
    EAP replaces Xauth
    Asymmetric authentication possible

Phase 1:
    * Used for control plane
    * Prove ID
    * Negotiate data plane security settings
Phase 2:
    * Used for data plane
    * Transports the protected data

Initiator       <->     Responder
IKE_SA_INIT Req  ->
IKE_SA_INIT Res  <-
IKE_AUTH         ->r
IKE_AUTH         <-

UDP 500
ESP - IP 50    <---Cannot work through PAT, hence NAT-T
AH  - IP 51    <---Cannot handle NAT

Create a Keyring
Create an IKEv2 Profile
Create a transform-set
Create the IPsec profile
Apply to the tunnel interface

------------------------------

crypto ikev2 keyring ciscokr
 peer tunnel42
  address 0.0.0.0 0.0.0.0
  pre-shared-key cisco123
 !
R1(config-ikev2-keyring-peer)#

Replicate the keyring seen above.

R1(config)#
""",
"answer" : "crypto ikev2 keyring ciscokr",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """""",
"answer" : "peer tunnel 42",
"prompt": "R1(config-ikev2-keyring)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """""",
"answer" : """address 0.0.0.0 0.0.0.0
pre-shared-key cisco123""",
"prompt": "R1(config-ikev2-keyring-peer)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """

1) Create a Keyring
2) Create an IKEv2 Profile
3) Create a transform-set
4) Create the IPsec profile
5) Apply to the tunnel interface

------------------------------

crypto ikev2 keyring ciscokr
 peer tunnel42
  address 0.0.0.0 0.0.0.0
  pre-shared-key cisco123
 !
crypto ikev2 profile i2prof
 match identity remote address 0.0.0.0
 authentication remote pre-share
 authentication local pre-share
 keyring local ciscokr

Replicate the above IKEv2 profile:
""",
"answer" : "crypto ikev2 profile i2prof",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """""",
"answer" : """match identity remote address 0.0.0.0
authentication remote pre-share
authentication local pre-share
keyring local ciscokr""",
"prompt": "R1(config-ikev2-profile)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """

1) Create a Keyring
2) Create an IKEv2 Profile
3) Create a transform-set
4) Create the IPsec profile
5) Apply to the tunnel interface

------------------------------

crypto ikev2 keyring ciscokr
 peer tunnel42
  address 0.0.0.0 0.0.0.0
  pre-shared-key cisco123
 !
crypto ikev2 profile i2prof
 match identity remote address 0.0.0.0
 authentication remote pre-share
 authentication local pre-share
 keyring local ciscokr
!
crypto ipsec transform-set trset esp-aes 256 esp-sha-hmac
 mode transport
!
crypto ipsec profile ipsecprof
 set transform-set trset
 set ikev2-profile i2prof

Replicate the above IPsec profile:
""",
"answer" : "crypto ipsec profile ipsecprof",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """""",
"answer" : """set transform-set trset
set ikev2-profile i2prof""",
"prompt": "R1(config-ikev2-profile)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """

1) Create a Keyring
2) Create an IKEv2 Profile
3) Create a transform-set
4) Create the IPsec profile
5) Apply to the tunnel interface

------------------------------

crypto ikev2 keyring ciscokr
 peer tunnel42
  address 0.0.0.0 0.0.0.0
  pre-shared-key cisco123
 !
crypto ikev2 profile i2prof
 match identity remote address 0.0.0.0
 authentication remote pre-share
 authentication local pre-share
 keyring local ciscokr
!
crypto ipsec transform-set trset esp-aes 256 esp-sha-hmac
 mode transport
!
crypto ipsec profile ipsecprof
 set transform-set trset
 set ikev2-profile i2pro
!
interface Tunnel 42
 tunnel protection ipsec profile ipsecprof

Now apply the IPsec profile to interface Tun 42.

R1(config)#interface Tunnel 42
""",
"answer" : "tunnel protection ipsec profile ipsecprof",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]
#"post_task_output": """"""
