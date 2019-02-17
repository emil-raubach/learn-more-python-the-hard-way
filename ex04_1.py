# my second attempt at this exercise - this time using `argparse`
import argparse

# create an instance of the ArgumentParser class
parser = argparse.ArgumentParser(
    description='Learning how to use argparse to use command line arguments.')

# positional args
parser.add_argument('do_something', type=str, help='What?')
parser.add_argument('more_stuff', metavar='D', type=int)

# flags
parser.add_argument('-f', '--foo', action='store_true', help='foo')
parser.add_argument('-b', '--bar', action='store_true', help='bar')
parser.add_argument('-baz', '--bazbaz', action='store_true', help='baz')

# optional args
parser.add_argument('--option1', type=int, help='It\'s option #1!')
parser.add_argument('--option2', type=int, help='It\'s option #2!')
parser.add_argument('--option3', type=int, help='It\'s option #3!')


args = parser.parse_args()

print(">>> parsed args: ", args)
