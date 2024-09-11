"""CQ02 Conditionals"""

__author__ = "730477537"


def guess_a_number() -> None:
    """inputs will be made by user and nothing is returned"""
    secret: int = 7
    player_guess = int(
        input("Guess a number:")
    )  # be careful to label if int instead of just not identifying
    print(
        "Your guess was " + str(player_guess)
    )  # concatonation can be done outside of parentheses
    if player_guess == secret:
        print("You got it!")
    elif player_guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
