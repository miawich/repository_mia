'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re


def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
length = 0
longest = 0
file = open('dictionary.txt', 'r')
for word in file:
    if len(word) >= length:
        length = len(word)
        longest = word
print(longest)
# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"
words_in_alice = 0
file = open('../Searching/AliceInWonderLand.txt', 'r')
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        words_in_alice += 1
print(words_in_alice)

file = open('../Searching/AliceInWonderLand.txt', 'r')

word_lens = []
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        word_lens.append(len(word))
ave_len = sum(word_lens) / len(word_lens)
print(ave_len)

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?
file = open('../Searching/AliceInWonderLand.txt', 'r')

alice = 0
words_in_alice = []
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        words_in_alice.append(word)
for word in words_in_alice:
    if word == "ALICE" or word == "ALICE'S":
        alice += 1
print(alice)

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
file = open('../Searching/AliceInWonderLand.txt', 'r')
from collections import *

sevens = []
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        word_length = len(word)
        if word_length == 7:
            sevens.append(word)

mode = Counter(sevens)
mode.most_common()
print(mode.most_common(1))

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?

file = open('../Searching/AliceInWonderLand.txt', 'r')

words_in_alice = []
cheshire = []
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        words_in_alice.append(word)
for word in words_in_alice:
    if word == "CHESHIRE":
        cheshire.append(word)
print(len(cheshire))

# How many times does "Cat" occur?

file = open('../Searching/AliceInWonderLand.txt', 'r')
words_in_alice = []
cat = []
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        words_in_alice.append(word)
for word in words_in_alice:
    if word == "CAT":
        cat.append(word)
print(len(cat))

# How many times does "Cheshire" immediately followed by "Cat" occur?
file = open('../Searching/AliceInWonderLand.txt', 'r')
words_in_alice = []
cheshire_cat = 0
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        words_in_alice.append(word)
for word in words_in_alice:
    if word == "CHESHIRE":
        word_index = words_in_alice.index(word)
        next_word = words_in_alice.index(word_index + 1)
        if next_word == "CAT":
            cheshire_cat += 1

print(cheshire_cat)