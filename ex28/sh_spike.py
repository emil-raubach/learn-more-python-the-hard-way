import subprocess
import readline

# readline.parse_and_bind('tab: complete')
# readline.parse_and_bind('set editing-mode vi')

# could even wrap this in a function... not sure the benefit.
# 'cause it could then be tested of course!
try:
    while True:
        user_input = input('> ')
        command = user_input.strip().split(' ')
        # print("command is=", command)
        if command[0] == 'exit':
            break
        else:
            status = subprocess.run(command)
except (EOFError, KeyboardInterrupt) as e:  # stole this - pretty sweet!
    print('\nShutting down...')