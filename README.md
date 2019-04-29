# EMP-Fortran
Code transcribed into Python 3.7 from Fortran 4 to emulate EMP blasts in the atmosphere.

### How to run:
* Install [python 3.7](https://www.python.org/downloads/) or later
* Direct a terminal to the folder containing main.py
* Run the command `python main.py`

### How to copy:
The "Fork" button in the top right will allow you to create your own copy of the project to allow for further updates. 

# Method progress

### main.py
Installs all needed plugins (SciPy) on startup, then calls the testing script "d.py"

### d.py
Still work in progress. 

### convert.py
This converts... something.

### convo.py
Calculates Convolution Integral

### dawson.py
Calculates Dawson Integral values.

### gamma.py
Gamma energy?

### isomer.py
Calculates the isomer transition (unstable nitrogen isomers) - The slowest energy (between Prompt, NGamma, and Isomer).

### ngamma.py
Calculates the neutrons which are creating gammas - The second fastest energy (between Prompt, NGamma, and Isomer).

### prompt.py
Calculates the prompt gammas (spectrum right off the weapon) - The fastest energy (between Prompt, NGamma, and Isomer).

### reldens.py
Calculates the relative density of the air (Determines how many nitrogen atoms there are)

### source.py

### sourcen.py

# Problems?
Please report any issues to the issues tab and I will try and respond asap. 
