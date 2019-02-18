# import statements
import argparse


# setup the argparse stuff for the CLI

parser = argparse.ArgumentParser("Quick and dirty 'cut' command")

parser.add_argument('-d', '--delim', type=str, nargs=1, help='delimiter')
parser.add_argument('-f', '--field', type=int, nargs=1, help='cut by field')
parser.add_argument('file', metavar='F', type=str, nargs=1, help='file to cut text')

args = parser.parse_args()

# get the file
with open(args.file[0]) as f: # using the slicing index is cheating to get it to work...
    print(">>> start of with block. args.file=", repr(args.file))
    print(">>> args.field and args.delim=", repr(args.field), repr(args.delim))
    if args.field and args.delim: # this only looks at one line; need a loop.
        # read a line from the file and split it using the delim
        line = f.readline()
        print(">>> line=", line)
        split_line = line.split(args.delim[0])
        print(">>> split_line=", split_line)
        # loop through the list, and build another list based on
        # the field number.
        rv = []
        for i, field in enumerate(split_line):
            if i == (args.field[0]-1):
                rv.append(field)

        print(rv)
    elif args.field:
        # read the whole file to stdout.
        print(f.read())
