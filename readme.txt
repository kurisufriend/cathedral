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
                 /|  「cathedral」  |\                                                                
                / |               | \                                                               
                | |               | |                                                               
                | |               | |                                                               
                | |       __      | |                                                               
                | |      |  |     | |                                                               
                | |      | .|     | |                                                               
                |_|______|__|_____|_|                                                               

the core of a plugin-based usergroup system.
establishes a central auth for users, and loads plugins to carry out various functions based on events.

the technically correct mode of installation is downloading `tools/init.py`, /not/ cloning the repo yourself

requires aiohttp ~= 3.7.4, acl, git

events:
USER_CREATE
READY