 # Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is  and the maximum sum is . The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints


# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14

#!/bin/python3



import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        temp = 0
        for j in range(i,i+4):
            temp = temp + arr[j]
        hold[i] = temp
    
    print(hold[0],hold[-1])
    
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
  
  #logic 2

 def find_max_min_sum(numbers):
    if not numbers:
        return None, None, 0  # Return None for both max and min, and 0 for sum if the list is empty

    max_value = max(numbers)
    min_value = min(numbers)
    sum_value = sum(numbers)

    return max_value, min_value, sum_value

# Sample Input
numbers = [3, 7, 1, 9, 5, 2, 8]

# Find maximum, minimum, and sum of values
max_value, min_value, sum_value = find_max_min_sum(numbers)

# Display results
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Sum of values: {sum_value}")
