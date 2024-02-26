# Design a program for creating a machine which count number of 1’s and 0’s in a given string.

def count_ones_and_zeros(input_string):
    count_ones = 0
    count_zeros = 0

    for char in input_string:
        if char == '1':
            count_ones += 1
        elif char == '0':
            count_zeros += 1

    return count_ones, count_zeros

# Test the function
input_string = input("Enter a string: ")
ones, zeros = count_ones_and_zeros(input_string)
print("Number of 1's:", ones)
print("Number of 0's:", zeros)
