#!/usr/bin/python3

filename = 'reasons.txt'
done = False

while done != True:
    reason = input("Why do you like programming? ")
    
    if reason != '':
        print("Sounds like a good reason to me!")
    
        with open(filename,'a') as file_object:
            file_object.write(reason + '\n')
    else:
        done = True
     

