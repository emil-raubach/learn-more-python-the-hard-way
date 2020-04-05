#!/usr/bin/env python
import sys
import subprocess


# Breaking the io out as its own function
# so it can be replaced with a lambda in the test.
def input_func():
    user_input = input('> ')
    return user_input


def parse_input(input_func):
    in_str = input_func()
    parsed_str = in_str.strip().split(' ')
    return parsed_str


def run_process(command):
    if command[0] == 'exit':
        sys.exit()  # had `break` before since this was in a while-loop.
    else:
        status = subprocess.run(command)
        # should return status (help with testing?)
        return status


def main():
    try:
        while True:
            input_str = parse_input(input_func)
            run_process(input_str)
    except (EOFError, KeyboardInterrupt) as e:
        print(f'\nbye! {e}')


if __name__ == "__main__":
    main()
