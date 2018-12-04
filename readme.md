# PITracker

## Introduction
Poste Italiane Tracker (pitracker) is a script that allows you to query the PI API and get info about your pack.

## Why
I like to make my own script and program, since it encrease my ability to solve daily problems and make all my stuff automated without depending from others code.

## Configure
You can use a virtual environment to avoid messing up with libaries and modules. Please, use it everytime you can when using scripts.
Take a look at the [docs](https://docs.python-guide.org/dev/virtualenvs/).
### With Virtual Enviornment
- Create Virtual Enviornment
	- `virtualenv -p python3 venv`
- Activate the Virtual Environment
	- `source venv/bin/activate`
- Install the dependencies
	- `pip3 install -r ./requirements.txt`
### Without Virtual Environment
- Just run the pip command:
	- `pip3 install -r ./requirements.txt`
## Run
Since the script is configured to run as Python3, you can call the scripts in three ways:
- `python3 pitracker.py`
-  `python pitracker.py`
- `./pitracker.py`

## Examples
 - To get the full history of the tracking:
    - `./pitracker.py tr4ck1ngc0d3`
 - To get the last update of the tracking:
    - `./pitracker.py -l tr4ck1ngc0d3`
    - `./pitracker.py --last tr4ck1ngc0d3`
 - To execute a linux command everytime there is an update:
    - `./pitracker.py -e "linux command here" tr4ck1ngc0d3`
    - `./pitracker.py --execute "linux command here" tr4ck1ngc0d3`


## Thanks to
- Me [telegram](https://t.me/jackrendor)
- And me   [linkedin](https://it.linkedin.com/in/jackrendor)
- And Python Italia [Telegram Group](https://t.me/pythonita)
