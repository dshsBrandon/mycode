#!/usr/bin/env python3

import pandas as pd

# Function to convert JSON to CSV
def json_to_csv(json_file, csv_file):
    df = pd.read_json(json_file)
    df.to_csv(csv_file, index=False)
    print(f"JSON data from {json_file} has been successfully converted to CSV at {csv_file}")

# Function to convert CSV to Excel
def csf_to_excel(csv_file, excel_file):
    df = pd.read_csv(csv_file)
    df.to_excel(excel_file, index=False)
    print(f"CSV data from {csv_file} has been successfully converted to Excel at {excel_file}")

# Function to convert Excel to JSON
def excel_to_json(excel_file, json_file):
    df = pd.read_excel(excel_file)
    df.to_json(json_file, orient='records')
    print(f"Excel data from {excel_file} has been successfully converted to JSON at {json_file}")

# Function to convert Excel to CSV
def excel_to_csv(excel_file, csv_file):
    df = pd.read_excel(excel_file)
    df.to_csv(csv_file, index=False)
    print(f"Excel data from {excel_file} has been successfully converted to CSV at {csv_file}")

def main():
    while True:
        print("Choose an operation:")
        print("1 - Convert JSON to CSV")
        print("2 - Convert CSV to Excel")
        print("3 - Convert Excel to JSON")
        print("4 - Convert Excel to CSV")
        print("q - Quit program")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            json_file = input("Enter the input JSON file name: ")
            csv_file = input("Enter the output CSV file name: ")
            json_to_csv(json_file, csv_file)
        elif choice == '2':
            csv_file = input("Enter the input CSV file name: ")
            excel_file = input("Enter the output Excel file name: ")
            csv_to_excel(csv_file, excel_file)
        elif choice == '3':
            excel_file = input("Enter the input Excel file name: ")
            json_file = input("Enter the output JSON file name: ")
            excel_to_json(excel_file, json_file)
        elif choice == '4':
            excel_file = input("Enter the input Excel file name: ")
            csv_file = input("Enter the output CSV file name: ")
            excel_to_json(excel_file, csv_file)
        elif choice.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
