import random

# List of possible words
words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 
         'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 
         'watermelon', 'cherry', 'papaya', 'berry', 'peach', 
         'lychee', 'muskmelon']

# Hangman ASCII stages
HANGMANPICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# Pick a random word
word = random.choice(words)
guessed = ['_'] * len(word)  # initially all blanks
used_letters = []            # store guessed letters
wrong_guesses = 0            # count of wrong attempts
max_wrong = len(HANGMANPICS) - 1  # max allowed wrong attempts

print("Welcome to Hangman! Guess the fruit name.\n")

# Game loop
while wrong_guesses < max_wrong and ''.join(guessed) != word:
    print(HANGMANPICS[wrong_guesses])
    print("Word: ", ' '.join(guessed))
    print("Used letters:", ', '.join(used_letters))
    
    guess = input("Enter a letter: ").lower()
    
    # validations
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single LETTER.\n")
        continue
    if guess in used_letters:
        print("You already guessed that letter!\n")
        continue
    
    used_letters.append(guess)
    
    if guess in word:
        # reveal guessed letters
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
        print("Good guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

# End of game
if ''.join(guessed) == word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print(HANGMANPICS[wrong_guesses])
    print("😢 You lost! The word was:", word)
