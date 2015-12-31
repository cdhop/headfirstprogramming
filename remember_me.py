#!/usr/bin/python3

import json

def get_stored_username(filename):
    """Get stored username if available."""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user(filename):
    """Greet the user by name."""
    username = get_stored_username(filename)
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(filename)
        print("We'll remember you when you come back, " + username + "!")

filename = 'username.json'
greet_user(filename)
