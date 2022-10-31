the core of a plugin-based usergroup system.
establishes a central auth for users, and loads plugins to carry out various functions based on events.

requires aiohttp ~= 3.7.4

events:
USER_CREATE
READY