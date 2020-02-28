# sorting
import random
import time
# swapping values
a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a  # works only in python

# selection sort

my_list = [random.randrange(1, 100) for x in range(100)]
my_list_2 = my_list[:]
my_list_3 = my_list[:]
print(my_list)

print()

for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

print(my_list)

# insertion sort

for key_pos in range(1, len(my_list_2)):
    key_val = my_list_2[key_pos]  # key dancer
    scan_pos = key_pos - 1  # looking to the dancer to the left
    while scan_pos >= 0 and key_val < my_list_2[scan_pos]:
        my_list_2[scan_pos + 1] = my_list_2[scan_pos]  # move the scan position left
        scan_pos -= 1
    my_list_2[scan_pos + 1] = key_val  # commit the move

print(my_list_2)
my_list_3.sort()  # much quicker!!!
print(my_list_3)

# optional function parameters
print("Hello", end=" ")
print("World", end=" ")
print("Hello", "World", sep="Big", end="!!!\n")


def hello(name, time_of_day="morning"):
    print("hello", name, "good", time_of_day)


hello("mia")

# lambda function
# when you need a function, but dont want to make a function
# also called anonymous function

# lambda= parameter: return
double_me = lambda x: x * 2
print(double_me(5))
product = lambda a, b: a * b


my_list = [random.randrange(1, 100) for x in range(100)]
print(my_list)
print()

my_2dlist = [[random.randrange(1, 100) , random.randrange(1, 100)] for x in range(100)]
print(my_2dlist)
print()

# sort method(change the list in place)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
print()

my_2dlist.sort(key=lambda a: a[0])
print(my_2dlist)
print()

my_2dlist.sort(key=lambda a: a[1])
print(my_2dlist)
print()

my_2dlist.sort(reverse=True, key=lambda a: sum(a))
print(my_2dlist)
print()

# sorted function (returns a new list)
new_list = sorted(my_2dlist, reverse=True, key=lambda x: abs(x[0] - x[1]))
print(new_list)
