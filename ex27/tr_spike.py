#!/usr/bin/env python
import sys


def translate(from_chars, to_chars):
    
    for line in sys.stdin.readlines():
        print(line.replace(from_chars, to_chars), end="")

def main():
    _, from_c, to_c = sys.argv
    translate(from_c, to_c)

if __name__ == "__main__":
    main()