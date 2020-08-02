#!/usr/bin/env python

"""A binary calculator to  convert decimal to binary and compute binary operations
"""
from _tracemalloc import start


def convert_to_binary(input_num):
        return 1


def convert_to_list(input_num):  # Split binary number into individual digits in a list
    input_num = [int(x) for x in str(input_num)]
    return input_num


def add_binary(num1, num2):
    num1 = convert_to_list(num1)
    num2 = convert_to_list(num2)
    
    if len(num1) < len(num2):  # Swap numbers to assure num1 is longer than num2
        num1, num2 = num2, num1
     
    #num1, num2 = num1.reverse(), num2.reverse()  # Reverse order to process right to left
    num1.reverse()
    num2.reverse()
    
    combined_number = []
    carried_number = 0
      
    for x in range(len(num2)): # Check binary cases, and create new combined number by appending to combined_number
        if num1[x] == num2[x] == 1:
            if carried_number != 0:
                combined_number.append(1)
                carried_number = 0
            else:
                combined_number.append(0)
                carried_number = 1
        elif num1[x] != num2[x]:
            if carried_number == 1:
                combined_number.append(0)
                carried_number = 1
            else:
                combined_number.append(1)
        elif num1[x] == num2[x] == 0:
            if carried_number == 1:
                combined_number.append(1)
            else:
                combined_number.append(0)
                
    if carried_number != 0:  # Resolve a carried number if one number is longer than the other
        start = len(num1)
        
        while True:
            if num1[start] == 0:
                combined_number.append(1)
                carried_number = 0
                break
            else:
                start += 1
                combined_number.append(0)
    
    finalized_number = ''
    for x in combined_number:
        finalized_number += str(x)
    
    return finalized_number
                    
    
def flip_negative(negative_binary):
    num_list = convert_to_list(negative_binary) 
    
    pos = 0
    
    for num in num_list:
        if num == '1':
            num_list[pos] = '0'
        elif num == '0': 
            num_list[pos] = '1'
        else:
            print('Number is not binary')
            return 1
        
    # negative_binary = [str(x) for x in int(num_list)] #Convert list of digits back into an integer
    
    negative_binary = add_binary(negative_binary, 1)  # Add 1 to the flipped number, finalizing the negative process
    
    pos += 1

print(add_binary(1001, 101101))