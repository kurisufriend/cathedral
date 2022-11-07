import subprocess
import crypt
import json
import secrets
from sys import argv

def get_real_users():
    f = [i.split(":") for i in open("/etc/shadow").read().split("\n")]
    return [i[0] for i in filter(lambda a: len(a) > 1, f) if not(i[1] in ["*", "!"])]

def add_user(u, p):
    p = crypt.crypt(p, crypt.mksalt())
    subprocess.run(["useradd", "-m", "-p", p, u])
    # adding a new user resets the permission table...
    subprocess.run(["setfacl", "-m", "u:cathedral:r", "/etc/shadow"])

"""
e.g.
[
    "jsmith@myorg.net",
    "jdoe@myorg.net",
    ...
]
"""
def generate_list_from_emails(infile):
    cur = get_real_users()
    key = []

    f = open(infile).read()
    f = json.loads(f)

    for addy in f:
        usr = addy.split("@")[0]
        if usr in cur:
            continue
        opwd = secrets.token_urlsafe(10)
        pwd = crypt.crypt(opwd, crypt.mksalt())
        key.append((usr, opwd))
        add_user(usr, pwd)
    print(key)

generate_list_from_emails(argv[1])