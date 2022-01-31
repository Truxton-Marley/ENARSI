import common_prompts as cp

questions_ikev1 = [
{
"question" : """
##############################
###       IPsec/IKEv1      ###
##############################

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

------

Create ISAKMP policy 10.

""",
"answer" : "crypto isakmp policy 10",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
!

crypto isakmp policy 10
 encr aes 256
 hash sha256
 authentication pre-share
 group 14
!
Create the pre-share, cisco123, and permit all addresses.
!
""",
"answer" : "crypto isakmp key cisco123 address 0.0.0.0",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]

questions_ikev2 = [
{
"question" : """
##############################
###       IPsec/IKEv2      ###
##############################

IKEv2
    EAP replaces Xauth
    Asymmetric authentication possible

Initiator       <->     Responder
IKE_SA_INIT Req  ->
IKE_SA_INIT Res  <-
IKE_AUTH         ->
IKE_AUTH         <-

UDP 500
ESP - IP 50    <---Cannot work through PAT, hence NAT-T
AH  - IP 51    <---Cannot handle NAT

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
------------------------------

Replicate the keyring seen above.

""",
"answer" : "crypto ikev2 keyring ciscokr",
"prompt": cp.config,
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """""",
"answer" : "peer tunnel42",
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
"suppress_positive_affirmation": False
},
{
"question" : """
1) Create a Keyring
2) Create an IKEv2 Profile   <---
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
"clear_screen": True,
"suppress_positive_affirmation": True
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
4) Create the IPsec profile   <---
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
 mode transport      <----"mode tunnel" is default
!
crypto ipsec profile ipsecprof
 set transform-set trset
 set ikev2-profile i2prof

Replicate the above IPsec profile:

""",
"answer" : "crypto ipsec profile ipsecprof",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : """""",
"answer" : """set transform-set trset
set ikev2-profile i2prof""",
"prompt": "R1(ipsec-profile)#",
"clear_screen": False,
"suppress_positive_affirmation": True
},
{
"question" : """

1) Create a Keyring
2) Create an IKEv2 Profile
3) Create a transform-set
4) Create the IPsec profile
5) Apply to the tunnel interface  <---

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
 mode transport      <----"mode tunnel" is default
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
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Check IKEv2 Phase I.
""",
"answer" : """show crypto ikev2 sa""",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """ IPv4 Crypto IKEv2  SA

Tunnel-id Local                 Remote                fvrf/ivrf            Status
2         172.16.12.3/500       172.16.13.2/500       none/none            READY
      Encr: AES-CBC, keysize: 256, PRF: SHA512, Hash: SHA512, DH Grp:5, Auth sign: PSK, Auth verify: PSK
      Life/Active Time: 86400/156 sec

 IPv6 Crypto IKEv2  SA
"""
},
{
"question" : """
Check the IPsec SA.
""",
"answer" : """show crypto ipsec sa""",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """
interface: Tunnel42
    Crypto map tag: Tunnel42-head-0, local addr 172.16.12.3

   protected vrf: (none)
   local  ident (addr/mask/prot/port): (172.16.12.3/255.255.255.255/47/0)
   remote ident (addr/mask/prot/port): (172.16.13.2/255.255.255.255/47/0)
   current_peer 172.16.13.2 port 500
     PERMIT, flags={origin_is_acl,}
    #pkts encaps: 17573, #pkts encrypt: 17573, #pkts digest: 17573
    #pkts decaps: 17621, #pkts decrypt: 17621, #pkts verify: 17621
    #pkts compressed: 0, #pkts decompressed: 0
    #pkts not compressed: 0, #pkts compr. failed: 0
    #pkts not decompressed: 0, #pkts decompress failed: 0
    #send errors 0, #recv errors 0

     local crypto endpt.: 172.16.12.3, remote crypto endpt.: 172.16.13.2
     plaintext mtu 1458, path mtu 1500, ip mtu 1500, ip mtu idb GigabitEthernet0/1
     current outbound spi: 0xF29F0007(4070506503)
     PFS (Y/N): N, DH group: none

     inbound esp sas:
      spi: 0xC0A7CADD(3232221917)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 1, flow_id: SW:1, sibling_flags 80000000, crypto map: Tunnel42-head-0
        sa timing: remaining key lifetime (k/sec): (4349565/3375)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE(ACTIVE)

     inbound ah sas:

     inbound pcp sas:

     outbound esp sas:
      spi: 0xF29F0007(4070506503)
        transform: esp-256-aes esp-sha-hmac ,
        in use settings ={Transport, }
        conn id: 2, flow_id: SW:2, sibling_flags 80000000, crypto map: Tunnel42-head-0
        sa timing: remaining key lifetime (k/sec): (4349571/3375)
        IV size: 16 bytes
        replay detection support: Y
        Status: ACTIVE(ACTIVE)

     outbound ah sas:

     outbound pcp sas:

"""
},
{
"question" : """
Keepalives:

crypto ikev2 dpd keepalive <Keepalive_interval> <Retry_interval> <on-demand|periodic>
crypto ikev2 nat keepalive <interval>

crypto isakmp keepalive <Keepalive_interval> <Retry_interval> <on-demand|periodic>
crypto isakmp nat keepalive <interval>

""",
"answer" : """show access-lists 101""",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Extended IP access list 101
    10 permit udp host 10.1.1.1 host 10.2.2.2 eq isakmp log (hits 4)
    20 permit ip any any

"""
},
{
"question" : """

Apply inbound on Egress interface of Spoke to test:

access-list 101 permit udp host 10.1.1.1 host 10.2.2.2 eq isakmp log
access-list permit ip any any

View the above ACL on the CLI:

""",
"answer" : """show access-lists 101""",
"prompt": cp.priv_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Extended IP access list 101
    10 permit udp host 10.1.1.1 host 10.2.2.2 eq isakmp log (hits 4)
    20 permit ip any any

"""
},
]
#"post_task_output": """"""
