from os import listdir
from sys import path as working_path
from sys import exit

def load_towers(dir):
    working_path.append(dir)
    found = [name.split(".py")[0] for name in listdir(dir) if name.endswith(".py")]
    loaded = []

    for tower in found:
        try: lt = __import__(tower)
        except Exception as e:
            print(f"plugin '{tower}' could not be sucessfully loaded ({e})")
            continue
        
        if not(hasattr(lt, "run")) or not(hasattr(lt, "hooks")):
            print(f"plugin '{tower}' is missing critical elements and thus could not be loaded")
            continue

        loaded.append(lt)
        print(f"loaded plugin: '{tower}'")
        
    return loaded

def handle_route(towers, route):
    pass