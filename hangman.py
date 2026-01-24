from words import DIFFICULTY
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class Hangman:
    def __init__(self, difficulty, name):
        self.difficulty = difficulty
        self.name = name
        self.word = None
        self.blanks = None
        self.answer = None
        self.guesses = []
        self.misses = []
    
    def start_game(self):
        self.word = random.choice(DIFFICULTY[self.difficulty]).upper()
        self.blanks = ["_ " for _ in range(len(self.word))]
        self.answer = list(self.word)
        print(f"I have picked my word, my word is {len(self.word)} characters long: \n")
        print(self.show_blanks())
        print("Make a guess! \n\n")
        guess = input("What letter do you choose? ").upper()
        self.guess(guess)
    
    def guess(self, guess):
        if guess in self.guesses:
            new_guess = input("You already picked that letter! Try Again!\n")
            self.guess(new_guess)
        
        self.guesses.append(guess)

        if self.check_guess(guess):
            print(f"Correct! the letter {guess} is in my word!")
            
            for i in range(len(self.answer)):
                if self.answer[i] == guess:
                    self.blanks[i] = guess
        else:
            print(f"Gotcha! {guess} is not in my word!")
            self.misses.append(guess)
        
        if self.blanks == self.answer:
            print(f"Congratulations {self.name}! You won!")
            print("My word was: ")
            print(self.show_blanks())
            quit()
        else:
            print(self.show_blanks())
            print("\nWrong guesses:\n")
            print(self.misses)
            print("\nGallows:\n")
            print(HANGMANPICS[len(self.misses)])
        if len(self.misses) == 6:
            print(f"Tough luck {self.name}, but you lost!")
            print(f"My word was {self.word}")
            quit()
        else:
            print("Make another guess!\n")
            new_guess = input("What is your next guess? \n").upper()
            self.guess(new_guess)

    def show_blanks(self):
        new_blanks = ""
        for letter in self.blanks:
            new_blanks += letter + " "
        return new_blanks

    def check_guess(self, guess):
        for letter in self.answer:
            if letter == guess:
                return True
        return False