#!/usr/bin/python3

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','error.txt']
for filename in filenames:
    count_words(filename)
