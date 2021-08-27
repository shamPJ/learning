# nargs_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('input',
                       action='store',
                       nargs='?',
                       default='my default value')

args = my_parser.parse_args()

print(args.input)