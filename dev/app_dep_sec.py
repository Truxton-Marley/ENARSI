import common_prompts as cp

questions_docker = [
{
"question" : """
##############
# Containers #
##############

CGroups: enable you to portion resources from the system

# Search for `hello-world` in Docker Hub:
docker search hello-world
# Run image `hello-world`:
docker run hello-world
# Build the Dockerfile in the current directory:
docker build .
# Run image `ubuntu` in interactive mode:
docker run -ti ubuntu
# List all running containers:
docker ps
# List images stored locally:
docker images

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Show linked libraries (dependencies) of python:
ldd /usr/bin/python3
	linux-vdso.so.1 (0x00007ffffbf81000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f1d4ce5f000)
	libexpat.so.1 => /lib/x86_64-linux-gnu/libexpat.so.1 (0x00007f1d4ce2e000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f1d4ce12000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f1d4cbea000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f1d4d538000)

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
>docker images
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
<none>        <none>    5e431fb48573   10 minutes ago   78.1MB
ubuntu        latest    e4c58958181a   5 weeks ago      77.8MB
hello-world   latest    9c7a54a9a43c   6 months ago     13.3kB

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Sample Dockerfile contents:
FROM scratch
ADD ubuntu-xenial-core-cloudimg-amd64-root.tar.gz /
CMD ["/bin/bash"]

# Sample Dockerfile contents:
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
CMD ["/bin/bash"]

docker build .

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
Images are a combination of:

Files that form the filesystem of an instantiated container.

Metadata that indicates who created it, what command to run when instantiating the image, or what environment variables to
set in the resulting container.

Images are composed of stacked layers, where each layer adds, changes, or removes files and metadata. Layers can be shared
among images to optimize disk usage, transfer times, and memory use.

Images are read-only filesystems.

A container is an instantiation of an image, so you can think of images as templates for containers.

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# run the image ubuntu, make changes and then commit them:
docker run -it --name testapp ubuntu /bin/bash
docker commit testapp myapp


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
# Build and tag an image:
docker build -t thisapp .

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
docker history ubuntu:latest
IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
e4c58958181a   5 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>      5 weeks ago   /bin/sh -c #(nop) ADD file:63d5ab3ef0aab308c…   77.8MB
<missing>      5 weeks ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      5 weeks ago   /bin/sh -c #(nop)  LABEL org.opencontainers.…   0B
<missing>      5 weeks ago   /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B
<missing>      5 weeks ago   /bin/sh -c #(nop)  ARG RELEASE                  0B


""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
]

questions_app_deployment_security = [
{
"question" : """
#####################################################
###     Application Deployment and Security       ###
#####################################################

Unit Test:

#####################################################
import unittest

class Test_My_Code(unittest.TestCase):
    def test_area(self):
        # Test sides >= 0
        self.assertAlmostEqual(area_of_square(0), 0)
        self.assertAlmostEqual(area_of_square(1), 1)
        self.assertAlmostEqual(area_of_square(2), 4)

    def test_area(self):
        self.assertRaises(ValueError, area_of_square, -1)

if __name__ == '__main__':
    unittest.main()

#####################################################

>python3 -m unittest -v my_test_my_code.py

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """
DevOps
    Culture, Automation, Measurement, Sharing

1) Systems and Flows
    Reduce batch size
    Make work visible
    Reduce intervals of work
    Prevent defects from being passed downstream
    Optimize business goals

2) Feedback Loop
    Enalbe faster detection and recovery
    See problems as they occur
    Maximize opporutunities to learn

3) Continuous Experimentation and Learning
    Limited and disciplined experimentation and risk-taking
    Define time to fix issues
    No blame gaming
    Shared code repositories

""",
"answer" : "",
"prompt": cp.single_chevron,
"clear_screen": True,
"suppress_positive_affirmation": False,
"post_task_output": """"""
},
{
"question" : """

Continuous Integration / Continuous Delivery / Continuous Deployment

CI tools: Jenkins, Travis, Team City, Drone


Develop => Code Commit => Source Control => Build Trigger
    ==> { (Deploy to test env.) | (Report and Notify) | (Publish to Release Repo) } Unit Tests
    ==> Deploy to Production

""",
"answer" : "",
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
{
"question" : """

""",
"answer" : "",
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
