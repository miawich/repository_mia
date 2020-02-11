# Hangman: 02/03/20

import random as r
done = False
my_words = ["hike", "cafe", "plants", "music", "thermos", "kahlo"]
my_words = [x.upper() for x in my_words]
r.shuffle(my_words)
my_word = my_words.pop()
misses = []
right = []
abcs = [chr(x) for x in range(65, 65 + 26)]
correct = False
winning = len(my_word) + 2
#  im not quite sure what the problem is here but it ended up working
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
end_of_game = gallows[6]

print("welcome to hangman!")

while not done:
    print(gallows[len(misses)])
    print("wrong letters:", misses)

    for letter in my_word:
        if letter in right:
            print(letter, end=" ")
            correct = True
            for correct in right:
                winning -= 1
        else:
            print("_", end=" ")
            correct = False

    print()

    choice = input("choose your letter:").upper()

    if choice in abcs:
        if choice not in my_word:
            misses.append(choice)
            print("incorrect")
        elif choice in my_word:
            right.append(choice)
    else:
        print("that isn't a letter")

    if len(misses) >= 6:
        done = True
        print("you lose")
        '''
        replay = input("would you like to play again?")
        if choice.upper() == "yes":
            done = False
            '''
    if winning <= 0:
        done = True
        print("that is correct, you win!")


