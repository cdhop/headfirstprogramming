#!/usr/bin/python3

filename = 'guest_book.txt'
done = False

while done != True:
    print("Please enter your name")
    name = input("Enter 'quit' to exit: ")

    if name == 'quit':
        done = True
    else:
        print("Hello, " + name.title() + "!")
        with open(filename,'a') as file_object:
            file_object.write(name.title() + '\n')

