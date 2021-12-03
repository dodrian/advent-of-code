#!/usr/bin/python3

with open("input.txt", "r") as f:
  previous = int(f.readline())
  count = 0
  for line in f:
    depth = int(line)
    if depth > previous:
      count = count + 1
    previous = depth
  print(count)
