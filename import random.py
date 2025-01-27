import random

def number_guessing_game():
    print("Welcome to my Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 10000
    number_to_guess = random.randint(1, 10000)

    attempts = 0  # To track the number of attempts
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Take the user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 10000:
                print("Please guess a number between 1 and 10000.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()