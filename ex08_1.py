# import statements
import argparse


# setup the argparse stuff for the CLI

parser = argparse.ArgumentParser("Quick and dirty 'cut' command")

parser.add_argument('-d', '--delim', type=str, nargs=1, help='delimiter')
parser.add_argument('-f', '--field', type=int, nargs=1, help='cut by field')
parser.add_argument('file', type=str, nargs=1, help='file to cut text')

args = parser.parse_args()
# Let's try some multiple assignment to unpack the command line args
print(args)
delimiter = args.delim[0]
file = args.file[0]
field = args.field[0]

print(f'The unpacked variables are: {delimiter}, {file}, and {field}.')

# get the file
with open(args.file[0]) as f: # using the slicing index is cheating to get it to work...
    print(">>> start of with block. args.file=", repr(file))
    print(">>> args.field and args.delim=", field, delimiter)
    if field and delimiter: # this only looks at one line; need a loop.
        # read a line from the file and split it using the delim
        line = f.readline() # `.readline()` returns ar string
        print(">>> line=", line)
        split_line = line.split(delimiter)
        print(">>> split_line=", split_line)
        # loop through the list, and build another list based on
        # the field number.
        rv = []
        for i, f in enumerate(split_line):
            if i == (field-1):
                rv.append(f)

        print(rv)
    elif args.field:
        # read the whole file to stdout.
        print(f.read())
