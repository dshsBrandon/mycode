#!/usr/bin/env python3
## create file object in "r"ead mode
def main():
    # Prompt for file to load
    filename = input("Please enter the name of the file to load: ")

    # Explore the file
    with open(filename, "r") as configfile:
        ## readlines() creates a list by reading target
        ## file line by line
        configlist = configfile.readlines()
    
        ## file was just auto closed (no more indenting)

    ## each item of the list now has the "\n" characters back
    print(configlist)

    ## count lines
    lines = len(configlist)
    print(f"Number of lines: {lines}")

main()
