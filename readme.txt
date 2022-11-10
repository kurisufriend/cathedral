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

the technically correct mode of installation is running `tools/init.py` as root, /not/ cloning the repo yourself

requires aiohttp ~= 3.7.4, acl, git

included plugins:
* users.py
    - displays all users registered on the system @ users.host/*
* fiefdom.py
    - userpage system, serves the user's ~/.web directory @ host/~user