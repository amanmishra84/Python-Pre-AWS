#!/usr/bin/env python

import os
 
dir_path = input("Enter File Path: ")
search_str = input("Enter Search String: ")

try:
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        dir_list = os.listdir(dir_path)
        text_files = [file for file in dir_list if file.endswith('.txt')]
        for text_file in text_files:
            count = 0
            with open(os.path.join(dir_path, text_file), 'r') as file:
                for line in file:
                    count+=line.lower().count(search_str.lower())
            if count > 0:
                print(f'{search_str} found {count} times in the file: {text_file}')
        
    else:
        print("Directory does not exist or file path given")
except Exception as e:
    print(f'Error: {e}')
