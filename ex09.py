# This is a very basic replica of the command line utility `sed`.
# The main functionality of this script will be to use the find/replace
# function and use regex.  e.g., `ls - l | sed "s/zedshaw/author/g"`.
import argparse

# Create the commandline interface using the argparse library
parser = argparse.ArgumentParser()

parser.add_argument('file', metavar='F',type=str, nargs=1, help="target file to edit")
parser.add_argument(
    'substitute', 
    type=str, 
    nargs=1, 
    help="string to search for in the file"
)
parser.add_argument(
    'replace', 
    type=str, 
    nargs='+', 
    help="string that will replace target"
)

args = parser.parse_args()

# Get the file to be edited, search for the target string and replace the first instance
try:
    if args.file:         
        with open(args.file[0]) as f: # Iterate through the file line by line  
            for line in f.readlines(): # Look for target pattern 
                for word in line.split():
                    # print(">>> word: ", word, "line: ", line, end="")
                    if word == args.substitute[0]:
                        word = args.replace[0]
                # If there is a match of the target pattern, 
                # replace it with the substitute pattern.
                # print the line to the stdout
                    print(word, end=" ")
                print()
except FileNotFoundError:
    print(f"The file {args.file[0]} does not exist.")