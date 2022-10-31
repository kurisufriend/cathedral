from sys import argv, exit
from json import loads

# so `spec` is supposed to be {strArgKey: (bRequired?, strDesc)}
def parse_args(spec):
    given = [i[2:] if i[0:2] == "--" else i for i in argv[1:]]

    if "help" in given:
        print(
            "\n".join(
                ["; ".join((opt, spec[opt][1], "required" if spec[opt][0] else "optional")) for opt in spec.keys()]
            )
        )

    settings = {}
    traveller = 0
    while traveller < len(given):
        opt = given[traveller]
        if opt in spec.keys():
            settings[opt] = given[traveller + 1]
            traveller += 1
        traveller += 1

    for req in filter(lambda a: spec[a][0], spec.keys()):
        if not(req in settings):
            print(f"missing required parameter: '{req}'")
            exit(-1)
    return settings

def fetch_cfg(filepath):
    try: return loads(open(filepath, "r").read())
    except:
        print(f"could not read config from path: '{filepath}',\nmake sure it is a valid JSON file")
        exit(-2)