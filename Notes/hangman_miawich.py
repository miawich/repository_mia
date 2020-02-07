# Hangman: 02/03/20
import random as r
done = False
my_words = ["boogie woogie", "coffee", "mountain", "soprano", "bill nye"]
my_words = [x.upper() for x in my_words]
r.shuffle(my_words)
my_word = my_words.pop()
misses = []
right = []


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
print("welcome to hangman!")

while not done:
    print(gallows[len(misses)])
    print("wrong letters:", misses)

    choice = input("choose your letter:").upper()

    if choice in abcs:
        if choice not in my_word:
            misses.append(choice)
        elif choice in my_word:
            right.append(choice)

    for letter in my_word:
        if letter in right:
            print(letter, end=" ")
            correct = True
        else:
            print("_", end=" ")
            correct = False








