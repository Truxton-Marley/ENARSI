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
# Dev
import dev.pex
import dev.git
# DC
import dc.network

# Quiz Tools
from quiz_tools import ask_questions
from quiz_tools import clear_screen_slowly

module_layer_3 = [
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
    layer_3.bgp.questions_6
]

module_vpn = [
    vpn_tech.mpls.questions,
    vpn_tech.dmvpn.questions,
    vpn_tech.ipsec.questions_ikev1,
    vpn_tech.ipsec.questions_ikev2
]

module_infra_security = [
    infrastructure_security.acls.questions,
    infrastructure_security.acls.ipv6_questions,
    infrastructure_security.urpf.questions,
    infrastructure_security.aaa.questions,
    infrastructure_security.copp.questions,
    infrastructure_security.ipv6_first_hop.questions,
    infrastructure_services.device_management.questions
]

module_infra_services = [
    infrastructure_services.snmp.questions,
    infrastructure_services.logging.questions,
    infrastructure_services.dhcp.questions,
    infrastructure_services.ip_sla.questions,
    infrastructure_services.netflow.classic_netflow_questions,
    infrastructure_services.netflow.flexible_netflow_questions
]

module_beyond_enarsi = [
    beyond_enarsi.beyond_enarsi.questions_ppp,
]

module_dev = [
    dev.pex.questions_pexpect,
    dev.git.questions_git
]

module_dc = [
    dc.network.questions_nxos,
    #dc.network.questions_overlays_otv,
    dc.network.questions_overlays_vxlan,
    dc.network.questions_overlays_evpn,
    dc.network.questions_aci
]

modules = [module_layer_3, module_vpn, module_infra_security,
           module_infra_services, module_beyond_enarsi, module_dev,
           module_dc]

system('cls')
print("""What would you like to practice today?

1) General Enarsi
2) Layer_3
3) VPN
4) Infrastructure Security
5) Infrastructure Services
6) Beyond Enarsi
7) Dev (new, in progress)
8) Data Center (new, in progress)
""")

# TODO: add error handling here, maybe move this to a function in
#       quiz tools.
subject = ""
try:
    subject = int(input("Please select a number: "))
except:
    print("Please enter a number from the list.")

system('cls')

for i in range(4):
    if subject == 1:
        questions = modules[random.randint(0, 4)]
    else:
        questions = modules[subject-2]
    random_index = random.randint(0, len(questions) - 1)
    ask_questions(questions[random_index])
    clear_screen_slowly(wait=2)

print("\nThat's it for now. Updates to follow.\n")
