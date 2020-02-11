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

