#!/usr/bin/python3

done = False

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while done != True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        done = True
        continue
 
    second_number = input("Second number:")
    if second_number == 'q':
        done = True
        contine
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer) 
