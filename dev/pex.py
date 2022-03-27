import common_prompts as cp

# TOC
# PPP
# EPC

# TODO: add, IOS versions, IS-IS, EPC, VXLAN, LISP, L2TP

questions_pexpect = [
{
"question" : """
#######################
###     pexpect     ###
#######################

Read the docs:
https://pexpect.readthedocs.io/en/stable/overview.html

Based on / "in the spirit of" Don Libre's Tcl Expect module.
Pexpect spawns a child process and watches over it.

send()
sendline()
expect()        <---"The string you specify is a regular expression, so you can match complicated patterns.
                     The match property is set to the re match object."
interact()
child.before    <---"The before property will contain all text up to the expected string pattern"
child.after     <---"The after string will contain the text that was matched by the expected pattern."
---
Install:

pip install pexpect
---
import pexpect
dir(pexpect)

""",
"answer" : "dir(expect)",
"prompt": cp.config_if,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """['EOF', 'ExceptionPexpect', 'Expecter', 'PY3', 'TIMEOUT', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__revision__', '__spec__', '__version__', 'exceptions', 'expect', 'is_executable_file', 'pty_spawn', 'run', 'runu', 'searcher_re', 'searcher_string', 'spawn', 'spawnbase', 'spawnu', 'split_command_line', 'sys', 'utils', 'which']
"""
},
{
"question" : """
###################
###     pexpect     ###
###################
import pexpect
child = pexpect.spawn("telnet 172.16.1.20")

child.expect("Username")
child.sendline("admin")

child.expect("Password")
child.sendline("cisco1233")

child.expect("#")
child.sendline("show version")


""",
"answer" : """child.expect("#")
child.sendline("show version")""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
###################
###     pexpect     ###
###################
import pexpect
child = pexpect.spawn("telnet 172.16.1.20")

child.expect("Username")
child.sendline("admin")

child.expect("Password")
child.sendline("cisco1233")

child.logfile = sys.stdout.buffer

child.interact()

""",
"answer" : """child.expect("#")
child.sendline("show version")""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

i = child.expect (['Permission denied', 'Terminal type', '[#\$] '])
if i==0:
    print('Permission denied on host. Can\'t login')
    child.kill(0)
elif i==1:
    print('Login OK... need to send terminal type.')
    child.sendline('vt100')
    child.expect('[#\$] ')
elif i==2:
    print('Login OK.')
    print('Shell command prompt', child.after)

child.kill(0)
""",
"answer" : """child.kill(0)""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

https://pexpect.readthedocs.io/en/stable/overview.html
"There are two special patterns to match the End Of File (EOF) or a Timeout condition (TIMEOUT).
You can pass these patterns to expect(). These patterns are not regular expressions. Use them
like predefined constants.

If the child has died and you have read all the child’s output then ordinarily expect() will
raise an EOF exception. You can read everything up to the EOF without generating an exception
by using the EOF pattern expect. In this case everything the child has output will be available
in the before property.
"

child.expect(TIMEOUT)
child.expect(EOF)

""",
"answer" : """child.expect(TIMEOUT)
child.expect(EOF)""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

child.expect("password:", timeout=120)

""",
"answer" : """child.expect("password:", timeout=120)
child.sendline("show version")""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

https://pexpect.readthedocs.io/en/stable/overview.html
"Find the end of line – CR/LF conventions
Pexpect matches regular expressions a little differently than what you might be used to.

The $ pattern for end of line match is useless. The $ matches the end of string, but Pexpect
reads from the child one character at a time, so each character looks like the end of a line.
Pexpect can’t do a look-ahead into the child’s output stream. In general you would have this
situation when using regular expressions with any stream.

The best way to match the end of a line is to look for the newline: "\r\n" (CR/LF). Yes, that
does appear to be DOS-style. It may surprise some UNIX people to learn that terminal TTY device
drivers (dumb, vt100, ANSI, xterm, etc.) all use the CR/LF combination to signify the end of line.
Pexpect uses a Pseudo-TTY device to talk to the child application, so when the child app prints
"\n" you actually see "\r\n".

UNIX uses just linefeeds to end lines of text, but not when it comes to TTY devices! TTY devices
are more like the Windows world. Each line of text ends with a CR/LF combination. When you intercept
data from a UNIX command from a TTY device you will find that the TTY device outputs a CR/LF combination.
A UNIX command may only write a linefeed (\n), but the TTY device driver converts it to CR/LF. This
means that your terminal will see lines end with CR/LF (hex 0D 0A). Since Pexpect emulates a terminal,
to match ends of lines you have to expect the CR/LF combination:"

child.expect("\r\n")

""",
"answer" : """child.expect("\r\n")""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

https://pexpect.readthedocs.io/en/stable/overview.html
"
try:
    i = child.expect ([pattern1, pattern2, pattern3, etc])
except:
    print("Exception was thrown")
    print("debug information:")
    print(str(child))
"

Pass

""",
"answer" : """""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

https://pexpect.readthedocs.io/en/stable/overview.html
"
It is useful to log the child’s input and out to a file or the screen. The following will
turn on logging and send output to stdout (the screen):

child = pexpect.spawn(foo)
child.logfile = sys.stdout.buffer
"

""",
"answer" : """child.logfile = sys.stdout.buffer""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

str(child)

""",
"answer" : """str(child)""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
#######################
###     pexpect     ###
#######################

from pexpect import pxssh

child = pxssh.pxssh()
child.login("1.1.1.1", "admin", "cisco", auto_prompt_reset=False)
child.sendline("show ip int brief")
child.expect("#")
child.before
child.logout()

""",
"answer" : """""",
"prompt": cp.config_if,
"clear_screen": False,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]