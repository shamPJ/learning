import argparse

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument('-a', action='store')
my_parser.add_argument('-b', action='store_const', const=42)
my_parser.add_argument('-c', action='store_true')
my_parser.add_argument('-d', action='store_false')
my_parser.add_argument('-e', action='append')
my_parser.add_argument('-f', action='append_const', const=42)
my_parser.add_argument('-g', action='count')
my_parser.add_argument('-i', action='help')
my_parser.add_argument('-j', action='version')

args = my_parser.parse_args()

print(vars(args))

# Setting the Action to Be Taken for an Argument

# When you add an optional argument to your command line interface, you can also define what kind of action 
# to take when the argument is specified. This means that you usually need to specify how to store the value 
# to the Namespace object you will get when .parse_args() is executed.

# There are several actions that are already defined and ready to be used. Let’s analyze them in detail:

# store stores the input value to the Namespace object. (This is the default action.)
# store_const stores a constant value when the corresponding optional arguments are specified.
# store_true stores the Boolean value True when the corresponding optional argument is specified and stores a 
# False elsewhere.
# store_false stores the Boolean value False when the corresponding optional argument is specified and stores 
# True elsewhere.
# append stores a list, appending a value to the list each time the option is provided.
# append_const stores a list appending a constant value to the list each time the option is provided.
# count stores an int that is equal to the times the option has been provided.
# help shows a help text and exits.
# version shows the version of the program and exits.

# shell:

# $ python actions_example.py
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

# $ python actions_example.py -a 42
# {'a': '42', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

# $ python actions_example.py -a "test"
# {'a': 'test', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

# $ python actions_example.py -b
# {'a': None, 'b': 42, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

# $ python actions_example.py
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
# $ python actions_example.py -c
# {'a': None, 'b': None, 'c': True, 'd': True, 'e': None, 'f': None, 'g': None}
# $ python actions_example.py -d
# {'a': None, 'b': None, 'c': False, 'd': False, 'e': None, 'f': None, 'g': None}

# $ python actions_example.py -e me -e you -e us
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': ['me', 'you', 'us'], 'f': None, 'g': None}

# $ python actions_example.py -f -f
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': [42, 42], 'g': None}

# $ python actions_example.py -ggg
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 3}
# $ python actions_example.py -ggggg
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 5}