#!/usr/bin/python3

horizontal = 0
depth = 0

with open('input.txt') as f:
  for line in f:
    command = line.split(' ')
    if command[0] == 'forward':
      horizontal = horizontal + int(command[1])
    elif command[0] == 'up':
      depth = depth - int(command[1])
    elif command[0] == 'down':
      depth = depth + int(command[1])

print(f"Horizontal: {horizontal}, depth: {depth}\nh * d: {horizontal * depth}")

