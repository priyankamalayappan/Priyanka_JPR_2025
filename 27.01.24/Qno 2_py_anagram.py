 # Two words are anagrams of one another if their letters can be rearranged to form the other word.

# Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

# Example

# Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

# Function Description

# Complete the anagram function in the editor below.

# anagram has the following parameter(s):

# string s: a string
# Returns

# int: the minimum number of characters to change or -1.
# Input Format

# The first line will contain an integer, , the number of test cases.
# Each test case will contain a string .

# Constraints


#  consists only of characters in the range ascii[a-z].
# Sample Input

# 6
# aaabbb
# ab
# abc
# mnop
# xyyx
# xaxbbbxx


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    count_s1 = {}
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1

    changes = 0
    for char in s2:
        if char in count_s1 and count_s1[char] > 0:
            count_s1[char] -= 1
        else:
            changes += 1

    return changes

# Sample Input
print(anagram("aaabbb"))   # Output: 3
print(anagram("ab"))       # Output: 1
print(anagram("abc"))      # Output: -1
print(anagram("mnop"))     # Output: 2
print(anagram("xyyx"))     # Output: 0
print(anagram("xaxbbbxx")) # Output: 1
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
  
  # logic 2

 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if both strings have the same set of characters
    return sorted(str1) == sorted(str2)

# Sample Input
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the input words are anagrams
if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
