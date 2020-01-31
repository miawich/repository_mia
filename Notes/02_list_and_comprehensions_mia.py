#  01/30/20: lists
import random
my_names = ["abe", "bev", "cam", "doug", "eid", "fjord"]

print(len(my_names))
print(min(my_names))
print(max(my_names))

#  to copy use the colon
my_copy = my_names[:]
my_copy.append("greg")
print(my_copy)
print(my_names)

print()

print(my_names.index("cam"))
my_names.append("deb")

my_names.sort()
print(my_names)
my_names.reverse()
print(my_names)

print()

#  modifying lists
del my_names[4]
print(my_names)

my_names.pop()
print(my_names)

end_of_list = my_names.pop()
print(my_names)
print(end_of_list)

front_of_list = my_names.pop(0)
print(front_of_list)
print(my_names)

print()

#  concatenation
first = "francis"
last = "parker"
print(first + last)   # can be done on lists

# iterating through lists
my_list = []
for i in range(10):
    my_list.append(i)

print(my_list)

# for each only looks at copy of the list
for item in my_list:
    item += 1
    print(item)

print(my_list)

print()

# add one to every item in the list
# this is how we modify a list in a loop
for i in range(len(my_list)):
    my_list[i] += 1

print(my_list)

print()

my_list = [x + 1 for x in range(10)]
print(my_list)

# 01/31/20: list comprehension
my_list = []

for i in range(101):
    my_list.append(i)

print(my_list)

#  using list comprehension

my_list = [x for x in range(101)]
print(my_list)

print()

for i in range(101):
    my_list.append(i ** 2)

print(my_list)

my_list = [x ** 2 for x in range(101)]
print(my_list)

#  make the same list but filter out the odd
my_list = []
for i in range(101):
    if i ** 2 % 2 == 0:
        my_list.append(i ** 2)

print(my_list)

my_list = [x ** 2 for x in range(101) if x ** 2 % 2 == 0]
print(my_list)

#  roll a single die 100 times and add it to the list

my_list = []

for i in range(100):
    my_list.append(random.randrange(1, 7))

print(my_list)

my_list = [random.randrange(1, 7) for x in range(100)]
print(my_list)

# roll two dice
my_list = []

for i in range(100):
    my_list.append([random.randrange(1, 7), random.randrange(1, 7)])

print(my_list)

my_list = [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)]
print(my_list)

# go back through it and make

my_sums = [sum(x) for x in my_list]
print(my_sums)

# hundred rolls but only the doubles

my_doubles = [x for x in my_list if x[0] == x[1]]
print(my_doubles)
print(len(my_doubles))

#  all at once: roll a hundred pairs and only add doubles

my_list = [x for x in [[random.randrange(1, 7), random.randrange(1, 7)]for x in range(100)] if x[0] == x[1]]
print(my_list)

#  working with strings is similar to lists
first = "francis"
last = "parker"
print(first[0])
first = first.upper()
print(first + last)
print(last[-2:])

for letter in first:
    print(letter)

print()

if "N" in first:
    print("YES")
