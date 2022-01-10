import common_prompts as cp

questions = [
{
"question": """

###################
###     BFD     ###
###################

Configure BFD on an interface:
""",
"answer": "bfd interval 50 min_rx 50 multiplier 3",
"prompt": cp.config_if,
"clear_screen": True
},
{
"question" : """

Let's set EIGRP to use BFD on all interfaces.

R1(config)#router eigrp 42
""",
"answer" : "bfd all-interfaces",
"prompt": cp.config_router,
"clear_screen": False,
"suppress_positive_affirmation": False
},
]
