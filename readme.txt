                          |                                                                         
                         -+-                                                                        
                          |                                                                         
                          |                                                                         
                         /^\                                                                        
                        /   \                                                                       
                       /     \                                                                      
                     _/       \_                                                                    
                    //         \\                                                                   
                   /-           -\                                                                  
                  /               \                                                                 
                 /|  [cathedral]  |\                                                                
                / |               | \                                                               
                | |               | |                                                               
                | |               | |                                                               
                | |       __      | |                                                               
                | |      |  |     | |                                                               
                | |      | .|     | |                                                               
                |_|______|__|_____|_|                                                               

the core of a plugin-based usergroup system.
establishes a central auth for users, and loads plugins to carry out various functions based on events.

requires aiohttp ~= 3.7.4, acl, git, useradd

the technically correct mode of installation is running `tools/init.py` as root, /not/ cloning the repo yourself
a good install should go something like the following:
    ensure you meet the requirements above ->
    read `tools/init.py` & run it as root ->
    navigate to the newly-created `/var/cathedral` directory and edit `config.json` to match your host ->
    add or edit the files in `tools/skel/` to reflect you/your system (these get copied to new user's home directories) ->
    generate a .json list of initial user e-mails (see `tools/test_mail_list.json for an example`) ->
    read `tools/add_users.py` & run it as root ->
    save the generated user:pass json from STDout, use it to give users their temp passwords ->
    start the service using systemd: `systemctl start cathedral` ->
    point a reverse proxy at your server, passing in HTTP traffic (optional, recommended) ->
    ensure SSH traffic reaches the box one way or another
added users should at this point be able to remote into the box using standard ssh procedures.


included plugins:
* users.py
    - displays all users registered on the system @ users.host/*
* fiefdom.py
    - userpage system, serves the user's ~/.web directory @ host/~user