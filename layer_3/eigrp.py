import common_prompts as cp

questions = [
{"question" : """
######################################
#####   NAMED EIGRP STUB-SITES   #####
######################################

Set the following router to be an EIGRP IWAN stub router with RD 101:100.

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
""",
"answer" : "eigrp stub-site 101:100",
"prompt": "R1(config-router-af)",
"clear_screen": False,
},
{"question" : """
Now set interface gig0/3 to be a WAN-interface.

R1(config)#router eigrp PINECONE
R1(config-router)#address-family ipv4 unicast autonomous-system 42
R1(config-router-af)#eigrp stub-site 101:100
R1(config-router-af)#af-interface GigabitEthernet 0/3
""",
"answer" : "stub-site wan-interface",
"prompt" : "R1(config-router-af-interface)",
"clear_screen": True,
}
]
