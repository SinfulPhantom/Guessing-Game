import random
import sys
from time import sleep


class Game:
    def __init__(self, lower, upper, number_of_guesses):
        super().__init__()
        self.lower = lower
        self.upper = upper
        self.number_of_guess = number_of_guesses
        self.name = None
        self.guess = None
        self.sleep_time = 2  # Sleeping to add effect.
        self.secret_number = None
        self.correctly_guessed = None
        self.ending_answer = None

    def welcome_sequence(self):
        print("Hello, what is your name?")
        self.name = input()

        print(f"Well, {self.name}, I am thinking of a number between {self.lower} and {self.upper}. Can you guess it?")
        sleep(self.sleep_time)
        print(f"You have {self.number_of_guess} guesses; use them wisely.")
        sleep(self.sleep_time)

        self.begin_guessing()

    def begin_guessing(self):
        self.secret_number = random.randint(self.lower, self.upper)
        self.correctly_guessed = False

        print(f"Alright, {self.name}, start guessing by entering an integer!")
        for guess_number in range(self.number_of_guess):
            self.grab_guess()
            if self.guess > self.secret_number:
                print("That's too high!")
            elif self.guess < self.secret_number:
                print("That's too low!")
            elif self.guess == self.secret_number:
                print(f"You correctly guessed the number in {guess_number} amount of tries!")
                self.correctly_guessed = True
                self.ending()
        self.ending()

    def ending(self):
        self.ending_answer = None

        if self.correctly_guessed:
            sleep(self.sleep_time)
            print(f"I'm impressed {self.name}. Guessing the correct number was not an easy task.")
        else:
            print(f"Unfortunately you ran out of guesses. The secret number was {self.secret_number}.")

        sleep(self.sleep_time)
        print(f"What do you say {self.name}, would you like to play again? (y/n):")
        self.ending_answer = input()

        if self.ending_answer == 'y':
            self.begin_guessing()
        else:
            print("Thanks for playing!")

            sleep(self.sleep_time)
            sys.exit()

    def grab_guess(self):
        try:
            self.guess = int(input())
        except ValueError:
            print("That's not an integer, try again...")
            self.grab_guess()


if __name__ == '__main__':
    Game(1, 20, 5).welcome_sequence()
