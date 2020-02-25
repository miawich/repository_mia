import re


def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dictionary_list = []
dictionary = open('Labs/Alice Spellcheck/dictionary.txt')
for word in dictionary:
    word.upper()
    dictionary_list.append(word)
dictionary.close()

print("--- Linear Search ---")
alice_file = open('Labs/Alice Spellcheck/AliceInWonderLand200.txt')

for line in alice_file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        def linear_search(key, my_list):
            """
            Searches for key inside of list and returns True if you find it.
            :param key: item to find
            :param my_list: list to find key in
            :return: bool found
            """
            key = word.upper()
            my_list = dictionary_list
            if key in my_list:
                if not key:
                    print(word)


