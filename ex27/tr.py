#!/usr/bin/env python
import sys

def translate(from_c, to_c, in_str):
    return in_str.replace(from_c, to_c)

def main(args, in_str):
    return translate(args[1], args[2], in_str)

if __name__ == "__main__":
    print(main(sys.argv, sys.stdin.read()))