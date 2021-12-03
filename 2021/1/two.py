#!/usr/bin/python3

with open("input.txt", "r") as f:
  a = int(f.readline())
  b = int(f.readline())
  c = int(f.readline())
  previous = a + b + c
  count = 0
  for line in f:
    a = b
    b = c
    c = int(line)
    depth = a + b + c
    if depth > previous:
      count = count + 1
    previous = depth
  print(count)
