#!/usr/bin/env python

# create a Python version of `xargs`
import sys
import subprocess

command = sys.argv[1:]
print('command=', command)
for line in sys.stdin.readlines():
    print('top of for-loop')
    exec_ = command + [line.strip()]
    print('command + line.strip()=', command, ' and ', line.strip())
    status = subprocess.run(exec_)
    print("I don't understand the `status` variable...", status, "I think it just captures the `CompletedProcess` variable or something.")