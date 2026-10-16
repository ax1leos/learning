# CS50P Week 4 — Libraries

## Lecture notes

### Key ideas

- models
- random library
- from ... import ...
- import ...
- random.randint(); random.choice(); random.shuffle()
- statistics library
- statistics.mean(); 
- command-line arguments
- sys library
- sys.argv
- packages
- pip
- APIs
- JSON

### My explanations (in my own words)

1. What is the difference between `import random` and `from random import choice`?

import random imports the entire random module. To use a function, you must type the module name first: random.choice(). • from random import choice imports only the choice function. You can use it directly without typing the module name: choice().


2. What is `sys.argv` used for and how is it used?

It is a list that stores command-line arguments passed to a Python script when you run it from the terminal. sys.argv[0] is always the name of your script. sys.argv[1], sys.argv[2], etc., are the additional words or numbers you type after the script name.

3. What does `pip install` do and where do installed packages go?

It downloads and installs third-party Python libraries and packages from the internet (PyPI). • Installed packages end up in a specific folder inside your Python installation directory called site-packages.


## Problems solved

- 
- 

