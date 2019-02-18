# replica of the `sort` command line tool; first implementation will just
# take the input from a single file.

import argparse

# command line interface using argparse
def parse_args():
    parser = argparse.ArgumentParser(
        description='Command line interface to sort file contents')

    parser.add_argument('file', metavar='F', type=str, nargs=1)
    parser.add_argument('-r', action='store_true', help='reverse sort')
    parser.add_argument('-f', action='store_true', help='case insensitive sort')
    parser.add_argument('-b', action='store_true', 
                        help='sort that ignores leading whitespace')

    return parser.parse_args()


# get the filename from the commandline args
def file_to_list(args):
    file_to_string = []

    if args.file:
        with open(args.file[0]) as f: # could change to take more files
            for line in f.readlines():
                file_to_string.append(line)
        return file_to_string
    else:
        return None


def sort_input(args, list_from_file):
    rv = [] # keep it to only one `return` statement

    if args.f and not args.r and not args.b:
        rv = sorted(list_from_file, key=str.lower)
    elif args.r and not args.b:
        rv = sorted(list_from_file, reverse=True)
    elif args.b:
        stripped_list = [l.strip(' ') for l in list_from_file]
        rv = sorted(stripped_list)
    else:
        rv = sorted(list_from_file)

    return rv


if __name__ == "__main__":
    args = parse_args()
    # print(">>> args=", args)
    sorted_string = file_to_list(args)
    # print(">>> list created from the input file=", sorted_string)
    sorted_input = sort_input(args, sorted_string)
    # print(*sorted_input) # why is there a leading space on lines 2+?
    for input in sorted_input:
        print(input, end='')