import common_prompts as cp

questions_ansible = [
{
"question" : """
#########################
###     Ansible       ###
#########################

Run on `Control Node` to manage `managed nodes`.

ansible.cfg:
    contains basic global configuration of ansible, such as path to python interpreter, switches to disable ssh key checking,...
inventory files:
    files to define all hosts that are managed by the control node
playbooks:
    YAML documents that contain a set of tasks that are performed by Ansible
modules:
    a reusable, standalone script, often written in Python, that Ansible runs on your behalf, either locally or remotely


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

# Sample Playbook:
# simple IOS config in ansible
---
- name: Sample IOS playbook for Ansible core 2.12 (First Play)
  hosts: iosxe

  tasks:
  - name: set ACL via CLI
    cisco.ios.ios_config:   <---MODULE
      lines:
        - 10 permit ip host 1.1.1.1 any log
        - 20 permit ip host 2.2.2.2 any log
        - 30 permit ip host 3.3.3.3 any log
        - 40 permit ip host 4.4.4.4 any log
        - 50 permit ip host 5.5.5.5 any log
      parents: ['ip access-list extended my_acl']
      before: no ip access-list extended my_acl

  - name: Configure the login banner
    cisco.ios.ios_banner:   <----MODULE
      banner: login
      text: this is my login banner
      state: present

- name: A Second play
  hosts: routers-secondary

  tasks:
  - name: do something else
    ...

What is the name of the module used in the first task?
""",
"answer" : "cisco.ios.ios_config",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

# Playbook using cisco.ios_facts module:
---
- name: Sample IOS playbook to retrieve facts
  hosts: iosxe
  gather_facts: no

  tasks:
  - name: retrieve ios facts
    cisco.ios.ios_facts:

  - name: display version and serial number
    debug:
      msg: "The IOS version is: {{ ansible_net_version }} and the SN is: {{ ansible_net_serialnum }}"
  
  - name: print out interface information
    debug:
      var: ansible_net_interfaces

ansible-playbook -i hosts 02-ios

# Modules:
cisco.ios.ios_facts
cisco.ios.ios_command
""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

anisble-doc cisco.ios.ios_facts
anisble-doc cisco.ios.ios_command
anisble-doc cisco.ios.ios_config
anisble-doc ansible.netcommon.netconf_config

Check the docs for cisco.ios.ios_facts
""",
"answer" : "ansible-doc cisco.ios.ios_facts",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]
