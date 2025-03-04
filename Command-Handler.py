#!/usr/bin/env python3

command = input('Enter a command(start/stop/exit): ')

match command:
    case 'start':
        print('Entered command is start')
    case 'stop':
        print('Entered command is stop')
    case 'exit':
        print('Entered command is exit')
    case _:
        print('Please Enter command either start, stop or exit')

