
import random

# List of secret words
words = [
    "python", "computer", "programming",
    "developer", "keyboard", "internet",
    "science", "software", "database"
]

# ASCII Hangman stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
      =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
      =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
      =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
      =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
      =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
      =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
      =========
    """
]


def play_hangman():

    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n===== WELCOME TO HANGMAN GAME =====")

    while wrong_guesses < max_attempts:

        # Display current word
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses)
        print("Remaining attempts:", max_attempts - wrong_guesses)
        print("Guessed letters:", sorted(guessed_letters))

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("Secret word:", secret_word)
            return

        guess = input("\nGuess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter. Try another!")
            continue

        guessed_letters.add(guess)

        # Check the guess
        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Display Hangman drawing
        print(hangman_stages[wrong_guesses])

    print("\n===== GAME OVER =====")
    print("You lost! Better luck next time.")
    print("The correct word was:", secret_word)


# Start the game
if __name__ == "__main__":
    play_hangman()
