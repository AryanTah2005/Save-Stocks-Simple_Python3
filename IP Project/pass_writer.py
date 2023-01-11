from getch import *
import sys
echo = '*'
def getpass(label):
    print(label, end='', flush=True)

    password = ''

    while True:
        inp = getch()

        if inp == '\n':
            break
        elif inp == '\003':
            raise KeyboardInterrupt
        elif inp == '\04':
            raise EOFError
        else:
            print(echo, end='', flush=True)
            password += inp
    print('')
    return password