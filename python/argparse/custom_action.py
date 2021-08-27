# custom_action.py
import argparse

class VerboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        # If you want your parameters to accept a list of items you can specify nargs=n for how many arguments to accept.
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('Here I am, setting the ' \
              'values %r for the %r option...' % (values, option_string))
        setattr(namespace, self.dest, values)

# Under the hood, argparse calls the function and passes it parser (the parser itself), 
# namespace (an object which is the collection of all already-parsed arguments), 
# values (the value(s) passed to the argument; 

# The dest option of the add_argument() gives a name to the argument. If not given, it is inferred from the option.

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-i', '--input', action=VerboseStore, type=int)

args = my_parser.parse_args()

print(vars(args))

# shell:
# $ python custom_action.py -i 42
# Here I am, setting the values 42 for the '-i' option...
# {'input': 42}

# about Action class https://docs.python.org/3/library/argparse.html#action-classes
# class argparse.Action(option_strings, dest, nargs=None, const=None, default=None, 
# type=None, choices=None, required=False, help=None, metavar=None)

# about nargs https://docs.python.org/3/library/argparse.html#nargs
# example:
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('nums', nargs=2)
# args = parser.parse_args()

# print("~ Nums: {}".format(args.nums))

# $ python test.py 5 2
# ~ Nums: ['5', '2']