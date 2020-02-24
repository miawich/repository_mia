dictionary_list = []
dictionary = open('Problems/Searching/dictionary.txt', 'r')
for word in dictionary:
    dictionary_list.append(word)
dictionary.close()

print("--- Linear Search ---")
dictionary = open('Problems/Searching/AliceInWonderLand.txt', 'r')
