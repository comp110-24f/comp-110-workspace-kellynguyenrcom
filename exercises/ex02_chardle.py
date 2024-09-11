"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730477537"


def input_word() -> str:
    """word imported is 5 letters"""
    input_word: str = input("Enter a 5-character word: ")
    if len(input_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return input_word


def input_letter() -> str:
    """imput is a single letter"""
    input_letter: str = input("Enter a signle character: ")
    if len(input_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return input_letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)

    count: int = 0

    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    if count >= 2:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    stored_word = input_word()
    stored_letter = input_letter()
    contains_char(stored_word, stored_letter)


if __name__ == "__main__":
    main()
