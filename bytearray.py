"""
Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.
"""
# Creating bytearray
array = bytearray((19, 20, 21, 22, 24))
print("Creating Bytearray:")
print(array)

# accessing elements
print("Accessing Elements:", array[1])

# modifying elements
array[4] = 23
print("After Modifying:")
print(array)

# Appending elements
array.append(24)
print("After Adding Elements:")
print(array)