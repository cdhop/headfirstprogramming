#!/usr/bin/python3

numbers = list(range(1,6))
for value in numbers:
    print(value)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

