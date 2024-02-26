#Design a program for creating a machine which accepts string having equal no. of 1’s and 0's

def equal_ones_and_zeros(s):
    state = 'start'
    count_ones = 0
    count_zeros = 0

    for char in s:
        if state == 'start':
            if char == '1':
                state = 'counting_ones'
                count_ones += 1
            elif char == '0':
                state = 'counting_zeros'
                count_zeros += 1
        elif state == 'counting_ones':
            if char == '1':
                count_ones += 1
            elif char == '0':
                state = 'counting_zeros'  # Fix: Change the state to 'counting_zeros'
                count_zeros += 1
        elif state == 'counting_zeros':
            if char == '0':
                count_zeros += 1
            elif char == '1':
                state = 'counting_ones'  # Fix: Change the state to 'counting_ones'
                count_ones += 1

    return count_ones == count_zeros
# Test cases
print(equal_ones_and_zeros('0101'))  # True
print(equal_ones_and_zeros('1100'))  # True
print(equal_ones_and_zeros('00111'))  # False
print(equal_ones_and_zeros('10010'))  # False
