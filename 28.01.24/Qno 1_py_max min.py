 # You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

# Where:
# - max denotes the largest integer in 
# - min denotes the smallest integer in 

# Example



# Pick any two elements, say .

# Testing for all pairs, the solution  provides the minimum unfairness.

# Note: Integers in  may not be unique.

# Function Description

# Complete the maxMin function in the editor below.
# maxMin has the following parameter(s):

# int k: the number of elements to select
# int arr[n]:: an array of integers
# Returns

# int: the minimum possible unfairness
# Input Format

# The first line contains an integer , the number of elements in array .
# The second line contains an integer .
# Each of the next  lines contains an integer  where .

# Constraints




# Sample Input 0

# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# Sample Output 0

# 20
import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    result = arr[k-1] - arr[0]
    for i in range(n-k+1):
        if arr[i+k-1] - arr[i] < result:
            result = arr[i+k-1] - arr[i]
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
  
  #logic 2
  
  def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None for both max and min if the list is empty

    max_value = max(numbers)
    min_value = min(numbers)

    return max_value, min_value

# Sample Input
numbers = [3, 7, 1, 9, 5, 2, 8]

# Find maximum and minimum values
max_value, min_value = find_max_min(numbers)

# Display results
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
