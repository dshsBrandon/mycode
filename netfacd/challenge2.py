#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces

def find_ip(interface_name):
    """passed interface name (string), returns the IP of that interface (string)"""
    return (netifaces.ifaddresses(interface_name)[netifaces.AF_INET])[0]['addr']     # the IP address

def main():
    """runtime"""

    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:

            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
           

            print('IP: ', find_ip(i))   # display IP address information for adapter
       
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

if __name__ == "__main__":
    main()

