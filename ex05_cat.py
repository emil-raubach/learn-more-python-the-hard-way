# this is Zed's solution to this exercise.  I shoulda use parseargs darnit!
import argparse
parser = argparse.ArgumentParser(description="Quick and dirty 'cat command'")

parser.add_argument('files', metavar='F', type=str, nargs='+')
parser.add_argument('-n', '--numbers', action='store_true',
                    help='Print line numbers')


args = parser.parse_args()


print(">>> parsed args:  ", args)

line_number = 1
for in_file_name in args.files:
    in_file = open(in_file_name)
    if args.numbers:
        for line in in_file.readlines():
            print(f"\t{line_number}\t{line}", end="")
            line_number += 1
    else:
        print(in_file.read())
