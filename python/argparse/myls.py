import os
import sys

# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
# With the len(sys.argv) function you can count the number of arguments.

if len(sys.argv) > 2:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit()

input_path = sys.argv[1]

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))

# shell commands:
# $ python myls.py
# You need to specify the path to be listed

# $ python myls.py /mnt /proc /dev
# You have specified too many arguments

# $ python myls.py /mnt
# dir1
# dir2