#  searching and read/write files

# forward slash goes into a directory. ".." goes up a directory
file = open('../resources/super_villains.txt', 'r')
print(file)
file.close()

# open a file to write w/ a 'w'
# overwrites the file

# 'a' appends the note
file = open('../resources/super_villains.txt', 'a')
file.write("Mia the Horrible\n")
file.close()

# go through the info in the file line by line
file = open('../resources/super_villains.txt', 'r')
for line in file:
    print(line.strip().upper())

file.close()

#  .strip() method strips out spaces, tabs, returns
print("hi\n".strip())
print("       hello".strip())


with open('../resources/super_villains.txt', 'r') as f:
    for line in f:
        print("hi", line)

with open('../resources/super_villains.txt', 'r') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# linear search

# python way
print("VARVARA TEMPEST" in villains)  # in keyword

# brute force way
i = 0
key = "VARVARA TEMPEST"
while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < (len(villains) - 1):
    print("Found", key, "at position", i)
else:
    print(key, "not found")


# making a function out of it!


def linear_search(key, my_list):

    '''
    searches for key inside of list and returns True if you find it.
    :param key: item in find
    :param my_list: list to find key in
    :return: bool found
    '''

    i = 0
    while i < (len(my_list) - 1) and key != my_list[i]:
        i += 1

    if i < len(villains) - 1:
        print("Found", key, "at position", i)
        return True
    else:
        print(key, "not found")
        return False


print(linear_search("The Soulless Toad", villains))

#  02/11/20:
#  binary search
key = "The Soulless Toad".upper()
lower_bound = 0
upper_bound = len(villains) - 1
found = False

while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    if villains [middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True
if found:
    print(key, "found at", middle_pos)
else:
    print(key,"was not found")


# GIFTED FUNCTION
# returns list of words in each line

import re  # regular expression


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


my_text = "Howdy y'all, i'm codin'!"
print(split_line(my_text))

file = open("../resources/alice_in_wonderland")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        print(word)