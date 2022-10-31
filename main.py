from sys import argv
from cli_params import parse_args, fetch_cfg
from cathedral import cathedral

args = parse_args({
    "cfg": (True, "path to config file")
})
settings = fetch_cfg(args["cfg"])
cathedral(settings).erect()