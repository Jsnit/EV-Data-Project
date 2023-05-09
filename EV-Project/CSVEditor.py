# No longer working, until you unzip EV-Data.zip in order to get original file. This is the only way to save 350mb space

import csv

def copy_csv_with_exclusion(input_file, output_file, exclude_data):
    with open(input_file, 'r') as input_csv_file, open(output_file, 'w', newline='') as output_csv_file:
        reader = csv.reader(input_csv_file)
        writer = csv.writer(output_csv_file)
        
        for row in reader:
            if not exclude_data(row):
                writer.writerow(row)

def exclude_data(row):
    return row[8] == 'Plug-in Hybrid Electric Vehicle (PHEV)'

def main():
    input_file = '../EV-Data/Electric_Vehicle_Population_Data.csv'  
    output_file = '../EV-Data/Edited-Electric_Vehicle_Population_Data.csv' 

    copy_csv_with_exclusion(input_file, output_file, exclude_data)

if __name__ == "__main__":
    main()
