#!/usr/bin/env python

# create a Python version of `xargs`
import sys
import subprocess

command = sys.argv[1:]
print(f'command is: {command}.')
def execute_command(cmd, number=None):
    if number:
        for line in sys.stdin.readlines():
            print(f'Top of for loop, line is: {line} and it\'s type is {type(line)}.')
            loop = line.split()
            exec_ = cmd + [line.strip()]
            status = subprocess.run(exec_)
    else:
        for line in sys.stdin.readlines():
            exec_ = command + [line.strip()]
            status = subprocess.run(exec_)

if len(command) < 1:
    print('You must provide at least one argument to this command.')
    sys.exit()
elif command[0] == '-n':
    _ = command.pop(0)
    num_args = int(command.pop(0))
    execute_command(command, number=num_args)
else:
    execute_command(command)    