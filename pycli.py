"""
PyCLI Main Script
© StuffzEZ & OptionallyBlueStudios 2025
"""

import threading
import subprocess
import sys
import time
import re

#######################
#     Variables       #
#######################

DEBUG_MODE = False
CLI_Name = "My CLI Name - Change with setCLIName()"
CLI_commands = {}
CLI_machine = "PyCLI"
CLI_user = "root"

########################
#      PackageAPI      #
########################

def getDependency(package):
    try:
        __import__(package)
    except ImportError:
            def do_install():
                print("[WARNING] Missing Dependencies." + f" Installing {package}... Please wait.")
                try:
                    # Suppress pip output unless DEBUG_MODE is True
                    if DEBUG_MODE:
                        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                    else:
                        subprocess.check_call(
                            [sys.executable, "-m", "pip", "install", package],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL
                        )
                except Exception as e:
                    print(f"Failed to install {package}:\n{e}")
                    time.sleep(3)
                else:
                    print(f"Successfully installed {package}!")
                    time.sleep(1.5)
            t = threading.Thread(target=do_install)
            t.start()
            t.join()

##################
#      Main      #
##################


def setCLIName(cliname):
    global CLI_Name
    CLI_Name = cliname
    if DEBUG_MODE:
        print("CLI Name Set To:", CLI_Name)

def setCLIUser(cliname):
    global CLI_user
    CLI_user = cliname
    if DEBUG_MODE:
        print("CLI User Set To:", CLI_Name)

def setCLIMachine(cliname):
    global CLI_machine
    CLI_machine = cliname
    if DEBUG_MODE:
        print("CLI Machine Set To:", CLI_Name)

def debugOFF():
    global DEBUG_MODE
    DEBUG_MODE = False
    print(f"DEBUG_MODE is now OFF")

def debugON():
    global DEBUG_MODE
    DEBUG_MODE = True
    print(f"DEBUG_MODE is now ON")

def addCommand(name, func):
    CLI_commands[name] = func

# Main CLI Loop

# ANSI color codes
class Colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def strip_colors(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def startCLI():
    print(CLI_Name)
    while True:
        WHITE = '\033[97m'
        RESET = '\033[0m'

        # no colours :(
        clean_name = strip_colors(CLI_machine)
        user_input = input(f"{WHITE}{CLI_user}@{RESET}{clean_name}{WHITE}:~$ {RESET}")
        
        if not user_input.strip():
            continue  # skip empty input

        parts = user_input.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd in CLI_commands:
            try:
                CLI_commands[cmd](*args)
            except TypeError as e:
                print(f"{Colours.FAIL}[ERROR]{Colours.ENDC} {e}")
            except Exception as e:
                print(f"{Colours.FAIL}[EXCEPTION]{Colours.ENDC} {e}")
        else:
            print(f"{Colours.FAIL}[ERROR]{Colours.ENDC} Unknown command: {cmd}")
