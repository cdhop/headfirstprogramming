#!/usr/bin/python3

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name =  first_name + " " + last_name
    return full_name.title()

done = False

while done != True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to quit")

    first_name = input("First name: ")
    if first_name == 'q':
        done = True
        continue
    
    last_name = input("Last name: ")
    if last_name == 'q':
        done = True
        continue

    formatted_name = get_formatted_name(first_name, last_name)
    print("\nHello, " + formatted_name + "!")
 
