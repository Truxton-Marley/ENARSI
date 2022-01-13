import common_prompts as cp

questions = [
{
"question" : """

#########################
###      LOGGING      ###
#########################

Let's first turn off console logging.

""",
"answer" : "no logging console",
"prompt": cp.config,
"clear_screen": False,
},
{
"question" : """

Let's set the device up to send Syslog messages
to a collection server on UDP port 514 at 1.1.1.1.

Make sure only "Warnings" and lower are sent
to the collection server.

Also source the traffic from lo0.
!
logging buffered 32678 debugging
no logging console
!
""",
"answer" : """logging host 1.1.1.1
logging trap warnings
logging source-interface lo0""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

What if we want to limit the debug output
to just int gig 0/0?

We can view our SYSLOG config below.
!
logging buffered 32678 debugging
no logging console
!
logging host 1.1.1.1
logging trap warnings
!
R1#
""",
"answer" : "debug condition int gig 0/0",
"prompt": cp.user_exec,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """Condition 1 set"""
},
{
"question" : """
Let's also limit the debug ip the IP 2.2.2.2

""",
"answer" : "debug condition ip 2.2.2.2",
"prompt": cp.user_exec,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """Condition 2 set"""
},
{
"question" : """

How would we remove just condition 2?

R1#show debug

Condition 1: interface Gi0/0 (1 flags triggered)
        Flags: Gi0/0
Condition 2: ip 2.2.2.2 (0 flags triggered)

""",
"answer" : "no debug condition 2",
"prompt": cp.user_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """

Let's now remove all conditions.

R1#show debug

Condition 1: interface Gi0/0 (1 flags triggered)
        Flags: Gi0/0
Condition 2: ip 2.2.2.2 (0 flags triggered)

""",
"answer" : "no debug condition all",
"prompt": cp.user_exec,
"clear_screen": True,
"suppress_positive_affirmation": False
},
# {
# "question" : """""",
# "answer" : "",
# "prompt": cp.config,
# "clear_screen": False,
# "suppress_positive_affirmation": False
# },
]
#"post_task_output": """"""
