import random


def guess_the_number(low: int = 1, high: int = 100) -> int:
    """
    Plays a guessing game where the user must guess a random number between
    `low` and `high`. Returns the randomly generated number.

    Args:
        low (int): The lowest possible number in the range (default 1).
        high (int): The highest possible number in the range (default 100).

    Returns:
        int: The randomly generated number.

    """
    random_number = random.randint(low, high)
    user_guess = None
    attempts = 0

    while user_guess != random_number:
        try:
            user_guess = int(input(f"Guess a number between {low} and {high}: "))
        except ValueError:
            print("Just integers\n")
            continue

        attempts += 1
        if user_guess < random_number:
            print("Your guess is too low. Try again!\n")
        elif user_guess > random_number:
            print("Your guess is too high. Try again!\n")
        else:
            print(f"Congratulations, you guessed the number correctly in {attempts} attempts\n!")

    return random_number
