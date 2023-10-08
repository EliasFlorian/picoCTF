#filename: decode_ascii.py

#open the file for reading
with open('output.txt', 'r') as f:
    # Read the file content, split it into individual numbers, and convert each number to an integer
    numbers = [int(num) for num in f.read().split()]


# Convert each integer to its corresponding ASCII character and join them into a single string
decoded_string = ''.join([chr(num) for num in numbers])


# Print the result
print(decoded_string)
