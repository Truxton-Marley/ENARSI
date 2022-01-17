import common_prompts as cp

questions = [
{
"question" : """
################################
###    Device Management    ####
################################

Let's start off with a TFTP file copy to the device.

Copy the file newimage.bin from the TFTP server at 1.1.1.1
to the device's local flash.

""",
"answer" : "copy tftp://1.1.1.1/newimage.bin flash:newimage.bin",
"prompt": cp.priv_exec,
"clear_screen": False,
},
{
"question" : """
Set up R1 to be a TFTP Server for the file newimage.bin located in its flash.

R1(config)#
""",
"answer" : "tftp-server:newimage.bin",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the source interface for FTP to lo0.
Then set the FTP username to admin.
Next set the FTP password to cisco123.

""",
"answer" : """ip ftp source-interface lo0
ip ftp username admin
ip ftp password cisco123""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": True
},
{
"question" : """
Copy the file newimage.bin from an http server at 1.1.1.1
to the device's local flash.
Use the username admin and password cisco123.

""",
"answer" : "copy http://admin:cisco123@1.1.1.1/newimage.bin flash:newimage.bin",
"prompt": cp.priv_exec,
"clear_screen": False,
"suppress_positive_affirmation": False
},
{
"question" : """
Now let's use SCP.

Be sure AAA is enabled and local username and password.
Also, SSH needs to be enabled.

Let's assume AAA and SSH are set up and enable SCP on the device now.

R1(config)#
""",
"answer" : "ip scp server enable",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the enable password with sha256 encryption.

R1(config)#
""",
"answer" : "enable algorithm-type sha256 secret cisco123",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the enable password with the scrypt algorithm.

R1(config)#
""",
"answer" : "enable algorithm-type scrypt secret cisco123",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Set the router to only use SSHv2
Then set it to provide two login attempts.
The default is three.

R1(config)#
""",
"answer" : """ip ssh version 2
ip ssh authentication-retries 2""",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
},
{
"question" : """
Next let's set the source-interface for SSH to lo0

ip ssh version 2
ip ssh authentication-retries 2
!
R1(config)#
""",
"answer" : "ip ssh source-interface lo0",
"prompt": cp.config,
"clear_screen": True,
"suppress_positive_affirmation": False
}
]
