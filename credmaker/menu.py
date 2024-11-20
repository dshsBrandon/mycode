#!/usr/bin/env python3

import rclooper
import openstackrc_maker

def display_menu():
    print("Menu:")
    print("1. Manually create a file")
    print("2. Read csv_users.txt and turn it into admin.rc files")
    print("q. Quit")

def main():
    while True:
        display_menu()
        choice = input("Please choose an option: ")

        if choice == '1':
            rclooper.create_file()  
        elif choice == '2':
            openstackrc_maker.generate_admin_rc()
        elif choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
