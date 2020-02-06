# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(101)]
print(my_list)
# b) Make a list of even numbers from 20 to 40
my_list = [x for x in [x for x in range(20, 42)] if x % 2 == 0]
print(my_list)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list = [x ** 2 for x in range(101)]
print(my_list)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
for item in my_list:
    if item > 0:
        print(item)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list

from Problems.number_list import *
print(num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))
# Find and print the lowest number in num_list (1pt)
print(min(num_list))
# Find and print the average of num_list (2pts)
print(sum(num_list) / len(num_list))
# Remove the lowest number from num_list (2pt)
print()

num_list.sort()
num_list.pop(0)
print(num_list)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
print()

top_ten = num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
from collections import *
data = Counter(num_list)
data.most_common()   # Returns all items and their counts
print(data.most_common(1))  # Returns the highest occurring item

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't
'''
for number in num_list:
    if number/number and number/1:
        print(number)
'''
from math import sqrt
from Problems.number_list import *
for x in range(2, num_list):
    if not any(y for y in range(2, 1 + int(sqrt(x))) if not x % y):
        print(x)

# Find the number of palindromes
# Hint: This may be easier to do with strings

print()

for number in num_list:
    palindrome = str(number)
    if palindrome[0] == palindrome[-1] and palindrome[1] == palindrome[-2]:
        print(palindrome)
