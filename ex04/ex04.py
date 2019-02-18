from sys import argv

# Set the flags, how about -flag1, -flag2, and -flag3?
FLAG_ONE = False
FLAG_TWO = False
FLAG_THREE = False

# Variables that can be set based on the command line args
variable_one = ''
variable_two = ''
variable_three = ''


# Make sure argv is not empty
if argv is None:
    print("You have to add something man!")

# Check to see if --help or -h was passed to the command line
for arg in argv:
    if arg == '--help' or arg == '-h':
        print("What can I do for you?")
        response = input('> ')
        print(f"Ok, I can {response} if that's what you really want!")
    elif '-flag1' in arg:
        FLAG_ONE = True
        print("Flag #1 is True!")
    elif '-flag2' in arg:
        FLAG_TWO = True
        print("Flag #2 is True!")
    elif '-flag3' in arg:
        FLAG_THREE = True
        print("Flag #3 is True!")
    else:
        pass
