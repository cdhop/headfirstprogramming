#!/usr/bin/python3

motorcycles = ['ducati','honda', 'suzuki']

print(motorcycles)
print(motorcycles[0].title())

motorcycles.append('harley')

print(motorcycles)

motorcycles.remove('suzuki')

print(motorcycles)
print(motorcycles.pop().title())

motorcycles.insert(0,'BMW')
motorcycles.insert(0,'yamaha')

print(motorcycles)
print(sorted(motorcycles))
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

print(str(len(motorcycles)))
print(motorcycles[-1].title())
