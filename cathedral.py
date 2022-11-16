from tower_manager import load_towers, handle_route
import asyncio
from aiohttp import web
from re import compile, match
import auth

class cathedral():
    def __init__(self, settings):
        self.cfg = settings
        self.towers = load_towers(self.cfg.get("PLUGIN_PATH"))
        self.auth = auth
    async def handle_http(self, r):
        for t in self.towers:
            for h in t.hooks:
                print(str(r.host)[str(r.host).find(self.cfg.get("host")):])
                if compile(h.replace("$HOST", str(r.host)[str(r.host).find(self.cfg.get("host")):])).match(str(r.url)):
                    return web.Response(**t.run(self, r))
        return web.Response(body=f"usergroup homepage")
    async def start_http(self):
        srv = web.Server(self.handle_http)
        runner = web.ServerRunner(srv)
        await runner.setup()

        site = web.TCPSite(runner, self.cfg.get("host"), self.cfg.get("port"))
        await site.start()

        print(f"serving @ {self.cfg.get('host')}:{self.cfg.get('port')}...")
        await asyncio.sleep(3600*24*365)
    def erect(self):
        l = asyncio.get_event_loop()
        try: l.run_until_complete(self.start_http())
        except Exception as e:
            print(e)
        l.close()
