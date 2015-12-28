#!/usr/bin/python3

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry','hamster')
describe_pet('jazmine')
describe_pet(pet_name="Pearl")
describe_pet('arthur','cat')
describe_pet(pet_name='houdini',animal_type='cat')

