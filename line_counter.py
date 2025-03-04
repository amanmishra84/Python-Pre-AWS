#!/usr/bin/env python3

#impor the sys module
import sys

#check if the user has provided the file names
file_names = sys.argv[1:]

#check if the user has provided the file names
if len(file_names) == 0:
    print('Please provide the file names')
    sys.exit()
    
#loop through the file names and count the number of lines in each file
for file_name in file_names:
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print(f'{file_name} contains: {len(lines)} lines')
    except FileNotFoundError:
        print(f'File {file_name} not found')
    except Exception as e:
        print(f'An error occurred while processing {file_name}: {e}')



