import crypt

def authenticate(u, p):
    f = [i.split(":") for i in open("/etc/shadow").read().split("\n")]
    d = dict(zip([i[0] for i in f], [i[1:] for i in f]))
    if u not in d:
        return False
    return d[u][0] == crypt.crypt(p, d[u][0])

def get_real_users():
    f = [i.split(":") for i in open("/etc/shadow").read().split("\n")]
    return [i[0] for i in filter(lambda a: len(a) > 1, f) if not(i[1] in ["*", "!"])]