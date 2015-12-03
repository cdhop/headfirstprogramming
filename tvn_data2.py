#!/usr/bin/python3

import sqlite3

def find_details(id2find):
	result = None
	db = sqlite3.connect("surfersDB.sdb")

	db.row_factory = sqlite3.Row
	cursor = db.cursor()
	cursor.execute( "select * from surfers where id=" + str(id2find) )
	rows = cursor.fetchall()

	for row in rows:
		if row['id'] == id2find:
			result = {}
			result['id']      = str(row['id'])
			result['name']    = row['name']
			result['country'] = row['country']
			result['average'] = str(row['average'])
			result['board']   = row['board']
			result['age']     = str(row['age'])
	cursor.close()
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
	
