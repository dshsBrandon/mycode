#!/usr/bin/env python3

# Read in the content of the Dracula novel as a file object.
def part1():
    # Open the file
    with open("dracula.txt", "r") as file:
        # Read the contents of the file
        content = file.read()

# Loop over every line in Dracula, print each line out!
def part2():
    # open the file
    with open("dracula.txt", "r") as file:
        # Iterate over each line
        for line in file:
            #Print the line
            print(line.strip())

# Only print out the line if it has the word vampire in it!
def part3():
    # Open the file
    with open("dracula.txt", "r") as file:
        # Iterate over each line
        for line in file:
            # Check if 'vampire' is in the line
            if 'vampire' in line:
                # Print the line
                print(line.strip())

# Print the line no matter what case vampire is!
def part4():
    # Open the file
    with open("dracula.txt", "r") as file:
        # Iterate over each line
        for line in file:
            # Check if 'vampire' is in the line
            if 'vampire' in line.lower():
                # Print the line
                print(line.strip())

# How many lines contain the word vampire?
def part5():
    # Vampire count initialized
    vampire_count = 0

    # Open the file
    with open("dracula.txt", "r") as file:
        # Iterate over each line
        for line in file:
            # Check if 'vampire' is in the line
            if 'vampire' in line.lower():
                # Count the line
                vampire_count += 1

    # Print totla lines containing 'vampire'
    print(f"Total number of lines containing 'vampire': {vampire_count}")

def menu():
    print("\nMenu:") 
    print("1 - Read in the content of the Dracula novel as a file object.") 
    print("2 - Loop over every line in Dracula, print each line out!") 
    print("3 - Only print out the line if it has the word vampire in it! (case-sensitive)") 
    print("4 - Print the line no matter what case vampire is!") 
    print("5 - How many lines contain the word vampire?") 
    print("q - Quit")

def main():
    while True:
        menu()
        choice = input("Please choose an option: ")

        if choice == '1':
            part1()
        elif choice == '2':
            part2()
        elif choice == '3':
            part3()
        elif choice == '4':
            part4()
        elif choice == '5':
            part5()
        elif choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
