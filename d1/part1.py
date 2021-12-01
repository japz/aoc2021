#!/usr/bin/env python

with open("input.txt") as f:
  data = [int(x) for x in f.readlines()]

count = 0
for i in range(1, len(data)):
  if data[i] > data[i-1]:
    count += 1

print(count) 
