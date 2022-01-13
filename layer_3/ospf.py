import common_prompts as cp

questions = [
{
"question" : """

##########################
###        OSPF        ###
##########################

Create a virtual-link over the transit area 24
On R11 to R22.
R11 Router-ID: 11.11.11.11
R22 Router-ID: 22.22.22.22

R11(config)#router ospf 1
""",
"answer" : "area 24 virtual-link 22.22.22.22",
"prompt": "R11(config-router)#",
"clear_screen": False,
},
{
"question" : """
And now create the virtual-link on R22

R22(config)#router ospf 1
""",
"answer" : "area 24 virtual-link 11.11.11.11",
"prompt": "R22(config-router)#",
"clear_screen": False,
},
]