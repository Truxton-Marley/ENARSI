import random
from os import system

# Section 1: Layer 3 Technologies Imports 35%
import layer_3.admin_distance
import layer_3.eigrp
import layer_3.ospf
import layer_3.redistribution
import layer_3.pbr
import layer_3.vrf_lite
import layer_3.bfd
import layer_3.bgp
# Section 2: VPN Imports 20%
import vpn_tech.mpls
import vpn_tech.dmvpn
import vpn_tech.ipsec
# Section 3: Infrastructure Security Imports 20%
import infrastructure_security.acls
import infrastructure_security.urpf
import infrastructure_security.aaa
import infrastructure_security.copp
import infrastructure_security.ipv6_first_hop
# Section 4: Infrastructure Service Imports 25%
import infrastructure_services.device_management
import infrastructure_services.snmp
import infrastructure_services.logging
import infrastructure_services.dhcp
import infrastructure_services.ip_sla
import infrastructure_services.netflow
# Beyond ENARSI
import beyond_enarsi.beyond_enarsi


from quiz_tools import ask_questions
from quiz_tools import clear_screen_slowly

modules = [
    beyond_enarsi.beyond_enarsi.questions_ppp,
    #Layer 3
    layer_3.admin_distance.questions,
    layer_3.redistribution.questions,
    layer_3.eigrp.questions,
    layer_3.eigrp.questions_2,
    layer_3.eigrp.questions_3,
    layer_3.eigrp.questions_4,
    layer_3.eigrp.questions_5,
    layer_3.ospf.questions,
    layer_3.ospf.questions_2,
    layer_3.ospf.questions_3,
    layer_3.ospf.questions_4,
    layer_3.pbr.questions,
    layer_3.vrf_lite.questions,
    layer_3.bfd.questions,
    layer_3.bgp.questions,
    layer_3.bgp.questions_2,
    layer_3.bgp.questions_3,
    layer_3.bgp.questions_4,
    layer_3.bgp.questions_5,
    layer_3.bgp.questions_6,
    # VPN
    vpn_tech.mpls.questions,
    vpn_tech.dmvpn.questions,
    vpn_tech.ipsec.questions_ikev1,
    vpn_tech.ipsec.questions_ikev2,
    # Infrastructure Security
    infrastructure_security.acls.questions,
    infrastructure_security.acls.ipv6_questions,
    infrastructure_security.urpf.questions,
    infrastructure_security.aaa.questions,
    infrastructure_security.copp.questions,
    infrastructure_security.ipv6_first_hop.questions,
    infrastructure_services.device_management.questions,
    # Infrastructure Services
    infrastructure_services.snmp.questions,
    infrastructure_services.logging.questions,
    infrastructure_services.dhcp.questions,
    infrastructure_services.ip_sla.questions,
    infrastructure_services.netflow.classic_netflow_questions,
    infrastructure_services.netflow.flexible_netflow_questions
]

system('cls')

# for i in range(1,8):
#     ask_questions(modules[i])
#     clear_screen_slowly(wait=2)

random_index = random.randint(0, 19)
ask_questions(modules[random_index])
clear_screen_slowly(wait=2)

random_index = random.randint(0, 19)
ask_questions(modules[random_index])

random_index = random.randint(0, len(modules) - 1)
ask_questions(modules[random_index])
clear_screen_slowly(wait=2)

random_index = random.randint(0, len(modules) - 1)
ask_questions(modules[random_index])

print("\nThat's it for now. Updates to follow.\n")


# TODO: CoPP show output
# TODO: expand MPLS
