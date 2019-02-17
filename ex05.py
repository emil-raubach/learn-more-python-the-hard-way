# My attempt at recreating the command line 'cat' command

# import stuff
from sys import argv
import argparse

# need a way to combine the files into a new file when the '>' operator is used.
# Need to iterate over list of strings typed into the command line and check for
# the presence of the '>'; if it's there then combine the previous items in the
# list and put them into a new file with the name in the item after '>'.
def check_input(input_string):
    position = 0
    for string in input_string:
        if string == '>':
            return position # what?  call combine files and set to a new file?
        else:
            position += 1

    return None

# maybe a better way to check for the '>' character using argv
# def redirect_position():
#     (_, *args) = argv

#     for i, arg in enumerate(args):
#         if arg == '>':
#             return i
    
#     return None    


# get file name from the stdin and read it, then print it out to the screen
# Let's make this a callable function!!!
def combine_files(args=None):
    # see if '>' was passed to the cmd line
    check = check_input(args)
    if check is not None:
        redirect_position = check

    outfile = []

    for filename in args[1:]:
        with open(filename) as f:
            outfile.append(f.read())

    return outfile


def print_files(outfile):
    for file in outfile:
        print(file)


output = combine_files(argv)
print_files(output)
