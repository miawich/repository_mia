# Hangman: 02/03/20
import random as r
done = False
my_words = ["boogie woogie", "coffee", "mountain", "soprano", "bill nye the science guy"]
my_word = my_words[r.randrange(0, 5)]
misses = []
right = []
fails = 0
gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]

abcs = [chr(x) for x in range(65, 65 + 26)]

while not done:
    print(gallows[fails])
    print("welcome to hangman!\n", gallows[0], "wrong letters:", misses)
    choice = input("choose your letter:").lower()
    letter = input(choice)
    for letters in my_word:
        if letter in my_word:
            print(letter)
        else:
            print("_")
    if choice in abcs:
        if choice != my_word:
            misses.append(choice)
            fails += 1
        if choice in right or choice in misses:
            print("you've already used this letter")


