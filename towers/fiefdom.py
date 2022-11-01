hooks = ["http.*:\/\/$HOST\/~.*"]

def run(ctx, r):

    user = r.path[1:].split("/")[0].replace("~", "")
    route = "/"+("/".join(r.path[1:].split("/")[1:]))

    if not(user in ctx.auth.get_real_users()):
        return {
            "body": f"<h3>404! no such user!</h3><br>consult <b>users.{ctx.cfg.get('host')}</b> to see all registered users", 
            "status": 404, "content_type": "text/html"
        }
    
    requested = "/index.html" if route == "/" else route
    try: f = open(f"/home/{user}/.web/{requested}").read()
    except:
        return {
            "body": f"<h3>404! no such path {requested}</h3><br>double check the path exists in your <b>~/.web</b> directory!", 
            "status": 404, "content_type": "text/html"
        }

    return {
        "content_type": "text/html",
        "body": f
    }