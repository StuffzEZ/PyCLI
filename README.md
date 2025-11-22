# PyCLI
A python package for making CLIs.

## Installing
1) Download the latest installer
2) Put it in your python project's directory   
    yourProject/
    ├─ main.py # Your Project's File
    ├─ install_pycli.py # PyCLI installer
3) Run the installer
    ```bash
    python install_pycli.py
    ```
4) Delete `install_pycli.py`
5) Import PyCLI in your project
    ```
    import pycli
    ```

## Example Script (Broken Down)

```python
# Import the PYCLI script
import pycli

def myFunc(name): # Function to be executed when helloWorld command is called
    print(f'{pycli.Colours.OKCYAN}Hello World! ' + name)

"""
You have to have print(f'striiiiinggg') because of colouring. (Like above)
You can colour by inserting something like {pycli.Colours.OKCYAN} into your string.
All of the colours (and styles) are: HEADER, OKBLUE, OKCYAN, OKGREEN, WARNING, FAIL, ENDC (reset colouring), BOLD and UNDERLINE
You put colours before what you want to colour
"""

# Change the Message displayed when your CLI runs. Can do multi-line by using \n to create a new line (REQUIRED)
pycli.setCLIName(f"{pycli.Colours.BOLD}{pycli.Colours.OKGREEN}================ HelloMyCLI ================{pycli.Colours.ENDC}")

# Change the CLI user instead of root in root@PyCLI:~$ (OPTIONAL)
pycli.setCLIUser("thePerson123")

# Change the thing displayed instead of PyCLI in root@PyCLI:~$ (OPTIONAL)
pycli.setCLIMachine(f"{pycli.Colours.BOLD}{pycli.Colours.OKGREEN}HelloMyCLI{pycli.Colours.ENDC}")

# Add a command (REQUIRED)
pycli.addCommand("helloWorld", myFunc) # Executes myFunc() and passes arguments to the function (eg. helloWorld ben -> myFunc("ben"))

# Starts the main CLI loop. Put AFTER everything else (REQUIRED)
pycli.startCLI()
```