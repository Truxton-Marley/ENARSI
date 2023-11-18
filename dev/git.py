import common_prompts as cp

questions_git = [
{
"question" : """
#####################
###       GIT     ###
#####################

VCS created in 2005 by Linux Community und Linus Torvalds.
Enable nonlinear development.

https://git-scm.com

Initial Setup:
git config --global init.defaultBranch main
git config --global user.name "Hans Schmidt"
git config --global user.email "hans.schmidt@erdapfel.de"
git config --global core.editor "vim"

git config --list

user@lochst$ git init   <---Creates a .git file
_________________________________________________________

git init

""",
"answer" : "git init",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

git config --global user.name "Hans Schmidt"
""",
"answer" : "git config --global user.name \"Hans Schmidt\"",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Create a checkout new branch:
git checkout -b mycode

# List all branches:
git branch

Create a checkout new branch?
""",
"answer" : "git checkout -b mycode",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Download the latest updates:
git fetch

# Revert changes for one file:
git checkout thispath/thisfile

# Restore file from a previous commit (update to checkout):
git restore --source f6538be thisfile

# Revert all changes since last commit:
git reset --hard

Download the latest updates?
""",
"answer" : "git fetch",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Revert all changes since the last commit?
""",
"answer" : "git reset --hard",
"prompt": cp.single_chevron,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
File Tracking

Untracked | Unmodified | Modified | Staged

git status  <---check files and their stage
git add     <---Stage an untracked or modified file

-----

git commit -m "my message"
git commit -v   <---Verbose, show changes
git commit -a
___

git add *

""",
"answer" : "git add *",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
DIFF

git diff
git diff --staged

git diff HEAD~<NUMBER>
git diff HEAD~2

git diff <HASH>

""",
"answer" : "git diff",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """diff --git a/quiz_tools.py b/quiz_tools.py
index be64d21..59957d3 100644
--- a/quiz_tools.py
+++ b/quiz_tools.py
@@ -1,7 +1,7 @@
 import random
 import time

-from os import system
+from os import system, name

 ###################################
 ###      Multiple Choice        ###
@@ -14,10 +14,12 @@ def print_encouragement():

 def clear_screen_slowly(wait=1):
     time.sleep(wait)
-    system("cls")
+    if name == "nt":
+        system("cls")
+    else:
+        system("clear")

 def ask_question(question):
-    #TODO: clean up clear screen; adjust for Linux
     if question.get("clear_screen"):
         clear_screen_slowly()
     print(question["question"], end="")

"""
},
{
"question" : """
Compare 2 commits back to current HEAD
""",
"answer" : "git diff HEAD~2",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Ignore Files
____________

.gitignore

!   <---Override an ignore
thisdir/**/*.js    <---Ignore all .js file in subdirectories of thisdir
Examples at:
https://github.com/github/gitignore


""",
"answer" : ".gitignore",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Git Log

git log
git log -3
git log -p
git log --oneline
git log --pretty=oneline
git log --pretty=full
git log --pretty=fuller
git log --graph

Show git log in graph format?
""",
"answer" : "git log --graph",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Git `checkout` command was split into `restore` and `switch`


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

git add README.md
git commit --amend  <---adjust last commit
git revert 84ad...HASH

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

git remote
git remote nowy-remote https://my-remote-storage.com
git fetch origin
git merge origin/main main
git pull        <---Alias for the prevoius two commands!
    git fetch origin    
    git merge origin/main main
git push origin main


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Git Tags
________

git tag     <---List all the tags in the repository

Tags:
    Lightweight
        git tag "1.0"
    Annotated
        git tag -a "1.0" -m "This is version 1.0"

Share you tags:
    git push tag "1.0"
    git push --tags

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Git Branches
____________

git branch meine-neue-branch    <---Create a new branch
git checkout meine-neue-branch  <---Point the head to the new branch
git checkout main
git log --branch

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
# {
# "question" : """
# """,
# "answer" : "",
# "prompt": cp.single_chevron,
# "clear_screen": True,
# "suppress_positive_affirmation": False,
# "post_task_output": """"""
# }'
]
