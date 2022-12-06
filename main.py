import random

# list of ASCII Art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Create list of words
word_list = ["aardvark", "baboon", "camel", "dog", "cat", "lizard", "dolphin"]
# Randomly pick word from list
chosenWord = random.choice(word_list)

print('Welcome!! Up for a game of Hangman?\n')
print(stages[6])

# create empty list to display cells for word
display = []
for letter in chosenWord:
    display.append("_")

# create empty string to keep track of used letters
usedLetters = ""

# End game condition
endGame = False

lives = len(stages) - 1
print(f'\n{display}')

# while loop to continue requesting input from user until out of lives or word is guessed
while endGame != True: 
    guess = input("Please guess a letter: ").lower()
    usedLetters += guess
    
    print("---------------------------")
    print(f'\nUsed letters: {usedLetters}')
    
    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    
    if guess in chosenWord:
        print('Correct!!')
        print(f'\n{stages[lives]}')
        
    else:
        print("Wrong, you lose a life")
        lives -= 1
        print(f'\n{stages[lives]}')
        
    print(f'\n{display}')
    
    if "_" not in display:
        print("You Win!!")
        endGame = True
    
    if lives == 0:
        print(f"You Lose!! The word was {chosenWord}")
        endGame = True