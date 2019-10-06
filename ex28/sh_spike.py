import subprocess


while True:
    user_input = input('> ')
    command = user_input.strip().split(' ')
    print("command is=", command)
    if command[0] == 'exit':
        break
    else:
        status = subprocess.run(command)