# what do I need to do for this exercise?
# First thing to try would be to look for a file in the current directory.
# e.g., `find -name 'ex06.py'`
import argparse
import subprocess
import glob


parser = argparse.ArgumentParser(description=
                                 """Relplica program for the \"find\"
                                 command line utility""")
# could create a function that does all the logic / parsing and set it to `type`?
parser.add_argument('dir', metavar='D', type=str, nargs='?', 
                    default='.', help='Target directory to search')
parser.add_argument('look_for', metavar='L', type=str, nargs='+',
                    help='Search the filesystem')
parser.add_argument('-name', action='store_true')

args = parser.parse_args()

print(">>> parsed args: ", args)
print(">>> args.look_for=", args.look_for)

# for term in args.look_for, search the current dir; maybe print, exec or something..
# simple 'hack' woudl be to use the `find` command using the `subprocess` module.
# You would feed it a list that starts with `find`, then the target directroy,
# then an option, then the argument. e.g.,
# `subprocess.run(["find", ".", "-name", "*.py"], capture_output=True)`
for term in args.look_for[1:]:
    for item in sorted(glob.glob(term)):
        print(item)

# for term in args.look_for:
#     for item in glob.glob(term):
#         rv = subprocess.run(['find', term], capture_output=True)
