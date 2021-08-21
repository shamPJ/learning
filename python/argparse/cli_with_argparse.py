# Tutorial https://realpython.com/command-line-interfaces-python-argparse/
# The command line interface (also known as CLI) is a means to interact with a command line script. 
# The standard way for creating a CLI in Python is currently the Python argparse library.

# An argument is a single part of a command line, delimited by blanks.
# An option is a particular type of argument (or a part of an argument) that can modify the behavior of the command line.
# A parameter is a particular type of argument that provides additional information to a single option or command.

# $ ls -l -s -k /var/log or ls -lsk /var/log
# In this example, you have five different arguments:

# ls: the name of the command you are executing
# -l: an option to enable the long list format
# -s: an option to print the allocated size of each file
# -k: an option to have the size in kilobytes
# /var/log: a parameter that provides additional information (the path to list) to the command

