#!/usr/bin/env python3

import csv
import os

def read_csv(filepath,year):
    with open(filepath, 'r', newline='') as file:
        reader = csv.DictReader(file)
        yield reader.fieldnames
        for row in reader:
            if int(row['date'][0:4]) == year:
                yield row
    
def write_filtered_csv(input_path,output_path,year):
    filtered_rows = read_csv(input_path,year)

    if not os.path.exists(output_path):
        open(output_path,'w').close()

    with open(output_path,'w',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=next(filtered_rows))
        writer.writeheader()
        writer.writerows(filtered_rows)

input_file = input("Enter CSV file path: ")

if not input_file.endswith('.csv'):
    print("Error: The input file must be a CSV file.")
    exit(1)

output_file = 'filtered_sales.csv'
year = int(input("Enter year to filter: "))

write_filtered_csv(input_file,output_file,year)
print(f'Filtered data has been written to {output_file}')


