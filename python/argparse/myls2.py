import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(prog='myls', # With the prog keyword, spec. name of the program that used in help 
                                    usage='%(prog)s [options] path', # define how myls is used
                                    # will show usage: myls [options] path
                                    # instead of default usage: myls [-h] path
                                    description='List the content of a folder',
                                    epilog='Enjoy the program! :)',
                                    # prefix_chars='/' - will work with /h instead of -h
                                    )

#vBy default, the standard prefix char is the dash (-) character, but if you want to use a different character, 
# then you can customize it by using the prefix_chars keyword                                    

# Add the positional arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Add the optional arguments                  
my_parser.add_argument('-l',
                       '--long',
                       action='store_true',
                       help='enable the long listing format')


# Execute the parse_args() method
args = my_parser.parse_args()

# args variable is a Namespace object, which has a property for each argument that has been gathered from the command line.

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))

for line in os.listdir(input_path):
    if args.long:  # Simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = '%10d  %s' % (size, line)
    print(line)

# shell comands:
# $ python myls.py
# usage: myls.py [-h] path
# myls.py: error: the following arguments are required: path

# $ python myls.py -h
# usage: myls.py [-h] path

# List the content of a folder

# positional arguments:
# path        the path to list

# optional arguments:
# -h, --help  show this help message and exit