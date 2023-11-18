import random
from os import system

# Dev
import dev.pex
import dev.git
import dev.cisco_platforms
import dev.cisco_platforms_sec
import dev.cisco_platforms_dc
import dev.ansib
import dev.app_dep_sec
import dev.curl
import dev.mdp
import dev.sw_dev_design
import dev.apis

# Quiz Tools
from quiz_tools import ask_questions
from quiz_tools import clear_screen_slowly


module_dev = [
    #dev.pex.questions_pexpect,
    # Section 1 Software Development and Design:
    dev.sw_dev_design.questions_sw_dev_des,
    dev.git.questions_git,
    # Section 2: Understanding APIs:
    dev.apis.questions_apis,
    # Section 3: Cisco Platforms and Development
    dev.cisco_platforms.questions_meraki,
    dev.cisco_platforms.questions_dna,
    dev.cisco_platforms.questions_sdwan,
    dev.cisco_platforms.questions_uc,
    dev.cisco_platforms_sec.questions_sec,
    dev.cisco_platforms_dc.questions_dc,
    dev.mdp.questions_restconf,
    # Section 4: Application Deployment and Security
    dev.app_dep_sec.questions_app_deployment_security,
    dev.app_dep_sec.questions_docker,
    # Section 5: Infrastructure and Automation
    dev.mdp.questions_mdp,
    dev.ansib.questions_ansible,
]

modules = [ module_dev ]

#ask_questions(module_dev[-6])

for i in range(4):
    questions = modules[0]
    random_index = random.randint(0, len(questions) - 1)
    ask_questions(questions[random_index])
    clear_screen_slowly(wait=2)

print("\nThat's it for now. Updates to follow.\n")
