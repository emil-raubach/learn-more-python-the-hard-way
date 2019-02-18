# my attempt at recreating the command line program `uniq`
import sys

# needs input from something else like another command; I don't know that 
# I can recreate piping on the command line in my little script in 45 mins.
import argparse
from ex10 import file_to_list, sort_input
# import pdb; pdb.set_trace()

# def parse_arguments():
#     parser = argparse.ArgumentParser()

#     parser.add_argument('file', metavar='F', type=str, 
#                         nargs=1, help="Input file name")

#     return parser.parse_args()

def unique(): # maybe use the `set()` data structure...
    # take the output of the sort function and remove duplicate lines
    # iterate through the input_text, compare next line to previous
    output_text = []

    if (sys.stdin.isatty()):
        sys.exit(1)

    for line in sys.stdin:
        # print(">>> line=", line)
        # skip the first comparison
        stripped_line = line.strip()
        # print(">>> stripped_line=", stripped_line)
        output_text.append(stripped_line + '\n')
        # print(">>> output_text=", output_text)

    return sorted(set(output_text), key=str.lower)


if __name__ == "__main__":
    # args = parse_arguments()
    # print(">>> args=", args)
    # sorted_string = file_to_list(args)
    # print(">>> list created from the input file=", sorted_string)
    # sorted_input = sort_input(args, sorted_string)
    # print(*sorted_input) # why is there a leading space on lines 2+?
    # for input in sorted_input:
    #     print(input, end='')
    rv = unique()
    print(''.join(rv)) # this! this is the way to print lists of strings!
    # for r in rv:
    #     sys.stdout.write(*rv)