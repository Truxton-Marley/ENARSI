import common_prompts as cp

questions_sw_dev_des = [
{
"question" : """
#################################################
###     Software Development and Design       ###
#################################################

Lean - Toyota Production Systems, 1940-1970s

Jikoda - automation with a human touch
Kaizen - continuous improvement
Kanban

Eliminate waste, manage processes, deliver value
Change is limited.

Lean Principles:
    Identify the value
    Map the value stream
    Create Flow, Establish Pull, Seek Perfection
    Just-in-time; excess inventory wastes resources


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

Agile - Late 1990s
    Daily Standup
    Scrums

Manage uncertainty, deliver working software, focus on users.
Change is embraced.

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
SDLC

planning -> defining -> designing -> building -> testing -> deployment
Stage 1—Planning: Identify the current use case or problem the software is intended to solve. Get input from stakeholders,
end users, and experts to determine what success looks like. This stage is also known as requirements analysis.

Stage 2—Defining: This stage involves analyzing the functional specifications of the software—basically defining what the
software is supposed to do.

Stage 3—Designing: In this phase, you turn the software specifications into a design specification. This is a critical stage
because stakeholders need to be in agreement to build the software appropriately; if they are not, users will not be happy,
and the project will not be successful.

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# CSV
import csv

rawfile = open('myfile')
reader = csv.reader(rawfile)

data = list(reader)

for row in reader:
    print(row[0])

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
import xmltodict

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
import json

json.load()
json.loads()
json.dump()
json.dumps()

with open("json_file.json", "w") as file:
    json.dump(json_dict, file, indent=4)

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
import yaml

yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)

my_file.write(yaml.dump(yaml_dictm, default_flow_style=False))

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# TDD:
1.) Write Test
2.) Test Fails
3.) Write Code
4.) Test Passes
5.) Refactor
6.) Repeat

Automated Testing Tools:
    pyATS, NorNIR, NAPALM

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

pyATS - used for automated testing
""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]
