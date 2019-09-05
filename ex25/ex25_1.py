#!/usr/bin/env python

# my attempt at writing the `xargs` utility using argparse
import argparse
import subprocess
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description='utility that emulates `xargs`')
    parser.add_argument('command', help='*nix command for `xargs` to execute.')
    return parser.parse_args()

def xargs(args_list):
    cmd = args_list.command
    
    for line in sys.stdin.readlines():
        exec_ = [cmd] + [line.strip()]
        completed_proc = subprocess.run(exec_)


def main():
    args = parse_args()
    
    print(">>> parsed args:  ", args)

    xargs(args)

if __name__ == '__main__':
    main()