"""CQ00"""

__author__ = "730477537"


def mimic(message: str) -> str:
    """returns message"""
    return message


def main() -> None:
    "print result of calling mimic"
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
