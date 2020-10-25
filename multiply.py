# Dan Wu
# 10/26/2020
# Write a function that takes two positive integers as parameters and returns the product of those two numbers.

def multiply(num_1,num_2):
    """returns the product of two given integers"""
    if num_2 == 1:
        return num_1
    else:
        return num_1 + multiply(num_1,num_2-1)



