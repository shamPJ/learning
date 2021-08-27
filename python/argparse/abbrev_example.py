# abbrev_example.py
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()

print(args.input)

# This program prints out the value you specify for the --input argument. 
# We haven’t looked at the optional arguments yet, but don’t worry, we will discuss them in depth in just a moment. 
# For now, just consider this argument like any other positional argument we already saw, 
# with the difference that the name starts with a couple of dashes.

# Now let’s see how the Python argparse library can handle abbreviations, 
# by calling our program multiple times, specifying a different abbreviation of the input argument at each run:

# shell:

# $ python abbrev_example.py --input 42
# 42

# $ python abbrev_example.py --inpu 42
# 42

# $ python abbrev_example.py --inp 42
# 42

# $ python abbrev_example.py --in 42
# 42

# How to disable abbreviations:

# # abbrev_example.py
# import argparse

# my_parser = argparse.ArgumentParser(allow_abbrev=False)
# my_parser.add_argument('--input', action='store', type=int, required=True)

# args = my_parser.parse_args()

# print(args.input)