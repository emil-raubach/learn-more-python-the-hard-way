#!/usr/bin/env python
# My attempt at recreating the command line 'cat' command

# import stuff
from sys import argv
import tools

#TODO: implement a function to add line numbers to the output

# Use the `.split('>')` list method to get the infiles and outfiles
def check_input(input_string):
    "Returns the position of a delimiter in a string"
    position = 0
    for string in '>':
        if string == '>':
            return position # what?  call combine files and set to a new file?
        else:
            position += 1

    return None


# TODO:  Add a flag for this behavior; fix it to take mult. files.
def add_line_num(infile):
    "Print the contents of a file with line numbers added."
    with open(infile) as f:
        iter = 1
        for line in f.readlines():
            print(f"{iter}\t{line}", end="")
            iter += 1

if __name__ == "__main__":
    output = tools.print_files(argv)
    print(output)

    add_line_num(argv[1:]) # not working - needs to take a str, bytes or file obj
    