# osrs-api
API that pulls data from Old School Runescape's databas to process.

Very basic server deployed using the following command:
- gunicorn -w 2 myapp:app

Runs a REST service that builds a string used to GET data from Jagex's Grand Exchange api. Item values and trends are then read, 
categories of interest picked out, and further disseminated to waiting clients. requirement.txt / setup.py are currently missing,
so dependencies will have to be hand jammed with pip3 installs if you wish to run this.

Currently it's set up to work locally with my React.js front end built using npm found here:

- https://github.com/tossbaws/tb_tools
