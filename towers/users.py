
hooks = ["http.*:\/\/users.$HOST.*"]

def run(ctx, r):
    return {
        "content_type": "text/html",
        "body": "<h1>all users registered on system</h1>"+("<br>".join(ctx.auth.get_real_users()))
    }