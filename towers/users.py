# all plugins have two critical components: `hooks`, which is a list of regex matches that identify
#  the URL range this plugin catches, and `run`, which is called on match using the framework context
#  (i.e. the main class) and a copy of the HTTP request.

hooks = ["http.*:\/\/users.$HOST.*"]

def run(ctx, r):
    return {
        "content_type": "text/html",
        "body": "<h1>all users registered on system</h1>"+("<br>".join(ctx.auth.get_real_users()))
    }
