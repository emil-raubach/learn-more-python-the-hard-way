# Imports
import argparse
from pathlib import Path
import re

# Create a commandline interface
def parse_arguments():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('file', type=str, help='file or files to search')
    parser.add_argument('--pattern', type=str, help='regex pattern used in search')

    return parser.parse_args()

# get a file name (or names? or a glob pattern?)
def file_paths(filenames): # helper function?
    # find the path for the filenames input parameter and return it.
    # for simplicity I will just default to the current dir.
    paths = Path.cwd().rglob(filenames) # this returns a generator object
    if paths:
        path_list = []
        for path in paths:
            path_list.append(path)
        return path_list
    else:
        return None

# open the file(s)
def files(files_to_open): # helper function?
    # take a list of files (paths?), open them, and return the file objects.
    file_data = []
    for file in files_to_open:
        with open(file) as f:
            for line in f: # this isnt' working right..
                file_data.append(line)

    return file_data
# search through the contents of the file(s) line by line for a match to the
# input pattern
def search_file_data(file_data_list, search_pattern):
    # use the regex pattern to search through the list
    # this might not be the best way to do this...
    match_list = []
    for elem in file_data_list:
        # print(">>> start of for - elem=", elem)
        m = re.search(search_pattern, elem)
        # print(">>> after re.search(), m=", repr(m))
        if m:
            # print(">>> after 'if', m=", repr(m))
            match_list.append((m.group(), elem)) # maybe should return the whole string and the match item as tuple?
            # print(">>> match_list=", match_list)

    return match_list
# return the contents of each entire line that had a matching pattern, or
# return None


# test stuff
if __name__ == "__main__":
    args = parse_arguments()
    print(">>> args: ", args)
    file_list = file_paths(args.file)
    print(">>> file_list: ", file_list)
    rv = files(file_list)
    print(">>> rv: ", rv)
    matches = search_file_data(rv, 'this')
    print(">>> matches: ", matches)
