# attempt #2 at recreating the command line utility `find`
# use pathlib to deal with paths, file operations, and globbing.
from pathlib import Path
import argparse

# create a new instance of the ArgumentParser class
# copy Zed by encapsulating this in a function!
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='path to search')
    parser.add_argument('--expression', help='expression to evaluate', default='.')
    parser.add_argument('-n', '--name', action='store_true')

    return parser.parse_args()


my_args = parse_arguments()
# use a commandline arg to create a new Path() object.
path = Path(my_args.path)

print(">>> path is a ", repr(path))
print(">>> path=", Path) # debug print statement

if my_args.expression:
    result = path.rglob(my_args.expression)
# else:
#     result = path.glob(path.cwd())

i = 1
for r in result:
    print(f'Result #{i} of your search is {r}.')
    i += 1

# print('>>>The current path is:  ', path)
print('>>>args: ', my_args)
