#!/usr/bin/env python3

import sys

# Check if a filename was provided
if len(sys.argv) < 2:
    print("Usage: ./decode_ascii_2.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Open the file for reading
with open(filename, 'r') as f:
    # Read the file content, split it into individual numbers, and convert each number to an integer
    numbers = [int(num) for num in f.read().split()]

# Convert each integer to its corresponding ASCII character and join them into a single string
decoded_string = ''.join([chr(num) for num in numbers])

# Print the result
print(decoded_string)

