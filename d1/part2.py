#!/usr/bin/env python

with open("input.txt") as f:
  data = [int(x) for x in f.readlines()]

summed = [sum(data[x-3:x]) for x in range(3, len(data)+1)]
print(summed)

count = 0
for i in range(1, len(summed)):
  if summed[i] > summed[i-1]:
    count += 1

print(count) 
