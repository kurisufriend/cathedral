from tower_manager import load_towers, handle_route
import asyncio
from aiohttp import web

class cathedral():
    def __init__(self, settings):
        self.cfg = settings
        self.towers = load_towers(self.cfg.get("PLUGIN_PATH"))
    async def handle_http(self, r):
        return web.Response(text=f"lol dongs {r.host}")
    async def start_http(self):
        srv = web.Server(self.handle_http)
        runner = web.ServerRunner(srv)
        await runner.setup()

        site = web.TCPSite(runner, "localhost", 1488)
        await site.start()

        print("serving...")
        await asyncio.sleep(3600*24*365)
    def erect(self):
        l = asyncio.get_event_loop()
        try: l.run_until_complete(self.start_http())
        except Exception as e:
            print(e)
        l.close()
