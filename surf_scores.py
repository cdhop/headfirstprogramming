#!/usr/bin/python3

scores = {}
result_file = open("results.txt")
for line in result_file:
	(name,score) = line.split()
	scores[score] = name
result_file.close()

for each_score in sorted(scores.keys(), reverse = True):
	print('Surfer ' + scores[each_score] + ' scored ' + each_score)	

