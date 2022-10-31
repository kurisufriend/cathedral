from sys import exit
import json
import subprocess

"""
scope:
* make /var/cathedral
* clone the repo to /var/cathedral/cathedral
* copy new template files to /etc/skel
* create new cathedral user
cathedral:.:.:.:/var/cathedral:/usr/bin/nologin
* give the new user recursive ownership of /var/cathedral
* allow new user access to /etc/shadow
* copy systemd service file to /etc/systemd/system
"""


if not(subprocess.run(["id", "-u"]) == 0):
    print("this script must be run as root")
    exit(-1)

# * make /var/cathedral
subprocess.run(["mkdir", "/var/cathedral"])

# * clone the repo to /var/cathedral
subprocess.run(["git", "clone", "https://github.com/kurisufriend/cathedral", "/var/cathedral"])

# * copy new template files to /etc/skel
subprocess.run(["cp", "-r", "/var/cathedral/tools/skel/*", "/etc/skel"])

# * create new cathedral user
subprocess.run(["useradd", "-c", "cathedral", "-d", "/var/cathedral", "-M", "-s", "/usr/bin/nologin"])

# * give the new user recursive ownership of /var/cathedral
subprocess.run(["chown", "-R", "cathedral:cathedral", "/var/cathedral"])

# * allow new user access to /etc/shadow
subprocess.run(["setfacl", "-m", "u:cathedral:r", "/etc/shadow"])

# * copy systemd service file to /etc/systemd/system
subprocess.run(["cp", "/var/cathedral/tools/cathedral.service", "/etc/systemd/system"])