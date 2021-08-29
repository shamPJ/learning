# nargs_example.py
# import argparse

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input',
#                        action='store',
#                        nargs='?',
#                        default='my default value')

# args = my_parser.parse_args()

# print(args.input)

# However, the nargs keyword can also accept the following:

# ?: a single value, which can be optional
# *: a flexible number of values, which will be gathered into a list
# +: like *, but requiring at least one value
# argparse.REMAINDER: all the values that are remaining in the command line

# So, for example, in the following program, the positional argument input takes a single value 
# when provided, but if the value is not provided, then the one specified by the default keyword is used:

# nargs_example.py
# import argparse

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input',
#                        action='store',
#                        nargs='?',
#                        default='my default value')

# args = my_parser.parse_args()

# print(args.input)

# $ python nargs_example.py 'my custom value'
# my custom value

# $ python nargs_example.py
# my default value

# nargs_example.py
# import argparse

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input',
#                        action='store',
#                        nargs='*',
#                        default='my default value')

# args = my_parser.parse_args()

# print(args.input)

# $ python nargs_example.py me you us
# ['me', 'you', 'us']

# $ python nargs_example.py
# my default value

# nargs_example.py
# import argparse

# my_parser = argparse.ArgumentParser()
# my_parser.add_argument('input', action='store', nargs='+')

# args = my_parser.parse_args()

# print(args.input)

# nargs_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('first', action='store')
my_parser.add_argument('others', action='store', nargs=argparse.REMAINDER)

args = my_parser.parse_args()

print('first = %r' % args.first)
print('others = %r' % args.others)

# $ python nargs_example.py me you us
# first = 'me'
# others = ['you', 'us']