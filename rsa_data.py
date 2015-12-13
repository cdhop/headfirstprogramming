#!/usr/bin/python3

def find_details(id2find):
    result = None
    rsa_data = open("surfing_data.csv")
    for line in rsa_data:
        surfer = {}
        (surfer['id'], surfer['name'], surfer['country'], surfer['average'], surfer['board'], surfer['age']) = line.split(";")
        if id2find == int(surfer['id']):
            result = surfer
    rsa_data.close()
    return(result)    
    
lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID:      " + surfer['id'])
    print("Name:    " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board:   " + surfer['board'])
    print("Age:     " + surfer['age'])
else:
    print("Could not find the surfer")
    
