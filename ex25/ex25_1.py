#!/usr/bin/env python

# my attempt at writing the `xargs` utility using argparse
import argparse
import subprocess
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description='utility that emulates `xargs`')
    parser.add_argument('command', help='*nix command for `xargs` to execute.')
    parser.add_argument('-p', '--prompt', 
                        help='prompt user before executing command.', action='store_true')

    return parser.parse_args()

def xargs(execute):
    # cmd = args_list.command
    
    # for line in sys.stdin.readlines():
    #     exec_ = [cmd] + [line.strip()]
    #     completed_proc = subprocess.run(exec_)
    completed_proc = subprocess.run(execute)

def get_args(args_list):
    cmd = args_list.command
    
    for line in sys.stdin.readlines():
        exec_ = [cmd] + [line.strip()]

    return exec_


def main():
    args = parse_args()
    ex = get_args(args)
    
    # if the `-p` flag is True
    if args.prompt:
    # Get ok from user before each call to xargs
        for cmd in ex:
            print(f'{cmd}?')
            ans = sys.stdin.read() # can't get this to work.  EOFError when using `input()`.
            if ans == 'y' or ans == 'Y':
                xargs(ex.pop(0))
            else:   
                continue
    # otherwise, just call xargs
    else:
        for cmd in ex:
            xargs(ex.pop(0))


if __name__ == '__main__':
    main()