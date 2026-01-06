import time
import os



class HangmanGame:
    def __init__(self):
        self.counter = 6
        self.user_input = ""
        self.input_chars = []
        self.displayed_word = []
        self.all_indices = []

    def print_hangman(self, counter):
        filename = f"Hangman_{counter:02}.txt"
        try:
            with open(filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Error: Could not find {filename}")

    def char_judge(self, guess_char, input_chars, counter):
        indices = []
        for index, char in enumerate(input_chars):
            if char.lower() == guess_char.lower():
                indices.append(index)
        if indices == []:
            counter -= 1
            print(f"Wrong! You have {counter} wrong guesses left.")
            self.print_hangman(counter)
        else:
            print(f"Correct! The character '{guess_char}' is in the word.")
        return indices, counter

    def update_displayed_word(self, displayed_word, input_chars, indices):
        for index in indices:
            displayed_word[index] = input_chars[index]
        return displayed_word
    
    def set_up_game(self):
        while True:
            counter = int(input("Please select how many wrong guesses allowed (6 to 11):"))

            if counter >= 6 and counter <= 11:
                time.sleep(1)
                print(f"You have selected {counter} wrong guesses allowed.")
                break
            else:
                print("Invalid input. Please enter a number between 6 and 11.")

        while True:
            self.user_input = str(input("Please enter a word (only letters): "))
            
            if self.user_input.isalpha():
                self.input_chars = list(self.user_input)
                self.displayed_word = ['_' for _ in self.input_chars]
                print(f"Success! You entered: {self.user_input}")
                time.sleep(2)
                break
            else:
                print("Invalid input. No numbers, spaces, or symbols allowed.")

        print("The word has been set. Now it's time for your opponent to guess it!")
        time.sleep(3)

    def screen_clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def guess_loop(self, counter, input_chars, user_input, displayed_word, all_indices):
        counter = self.counter
        input_chars = self.input_chars
        user_input = self.user_input
        displayed_word = self.displayed_word
        while counter > 0:
            guess_char = str(input("Please enter a character to guess: "))
            
            if len(guess_char) != 1 or not guess_char.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            print('Your guess is...')
            time.sleep(3)
            new_indices, counter = self.char_judge(guess_char, input_chars, counter)
            all_indices.extend(new_indices)
            displayed_word = self.update_displayed_word(displayed_word, input_chars, all_indices)          
            print("Current word:", ' '.join(displayed_word))
            
            if '_' not in displayed_word:
                print("Congratulations! You've guessed the word!")
                break
        if counter <= 0:
            print("Sorry, you've run out of guesses. The word was:", user_input)

    def play(self):
        self.set_up_game()       
        self.screen_clear()

        print("The word has", len(self.user_input), "characters.")
        time.sleep(3)
        displayed_word = ['_' for _ in self.input_chars]
        self.guess_loop(self.counter, self.input_chars, self.user_input, self.displayed_word, self.all_indices)


    

if __name__ == "__main__":
    game = HangmanGame()
    game.play()