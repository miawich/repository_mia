'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''
# Successful linear spellcheck (10pts)
import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def linear_search(key, my_list, line_number):
    """
    Searches for key inside of list and returns True if you find it.
    :param key: item to find
    :param my_list: list to find key in
    :return: bool found
    """

    i = 0
    while i < (len(my_list)) and key.upper() != my_list[i]:
        i += 1

    if i < len(my_list):
        return True
    else:
        print(key," at line", line_number, "not found.")
        return False


def binary_search(key, my_list, line_number):

    lower_bound = 0
    upper_bound = len(my_list) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if not found:
        print(key," at line", line_number, "not found.")


dictionary_list = []
dictionary = open('../Alice Spellcheck/dictionary.txt')
for word in dictionary:
    word.upper()
    dictionary_list.append(word.strip())
dictionary.close()

line_num = 0

print("--- Linear Search ---")
alice_file = open('../Alice Spellcheck/AliceInWonderLand200.txt')

for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    line_num += 1

    for word in words:
        linear_search(word, dictionary_list, line_num)

alice_file.close()

print()

# Successful binary spellcheck (10pts)
print("--- Binary Search ---")
alice_file = open('../Alice Spellcheck/AliceInWonderLand200.txt')

for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    line_num += 1

    for word in words:
        binary_search(word, dictionary_list, line_num)

alice_file.close()

# Binary and linear are written as functions (5pts)


# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.
print("--- Words in Looking Glass ---")

alice_file = open('../Alice Spellcheck/AliceInWonderLand200.txt')
atlg_file = open('../Alice Spellcheck/AliceThroughTheLookingGlass.txt')

alice_words = []

for word in alice_file:
    word.upper()
    alice_words.append(word.strip())

for line in atlg_file:
    line = line.strip().upper()
    words = split_line(line)
    line_num += 1

    for word in words:
        binary_search(word, alice_words, line_num)

alice_file.close()
atlg_file.close()

#  i thought this was the right idea but it just prints every word so oops!
