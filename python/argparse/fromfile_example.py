import argparse

my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

my_parser.add_argument('a',
                       help='a first argument')

my_parser.add_argument('b',
                       help='a second argument')

my_parser.add_argument('c',
                       help='a third argument')

my_parser.add_argument('d',
                       help='a fourth argument')

my_parser.add_argument('e',
                       help='a fifth argument')

my_parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='an optional argument')

# Execute parse_args()
args = my_parser.parse_args()

print('If you read this line it means that you have provided '
      'all the parameters')


# Now that you have specified a prefix char to get arguments from an external file, 
# open a terminal and try to execute the previous program:
# $ python fromfile_example.py @args.txt
# >>> If you read this line it means that you have provided all the parameters

# In this example, you can see that argparse has read the arguments from the args.txt file.