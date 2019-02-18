# test my argv idea for ex05 `cat` command
from sys import argv

_, *args = argv

print('args = ', args)

for arg in args:
    if arg == '>':
        print('There\'s a ">" in the command line arguments.')
    else:
        pass