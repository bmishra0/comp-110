"""Who is ready for some smart people time with WORDLE?"""

__author__: str = "730644820"


def contains_char(the_word: str, the_character: str) -> bool:
    """what does it actually have or contains?"""
    assert len(the_character) == 1
    index: int = 0

    while index < len(the_word):
        if the_word[index] == the_character:
            return True
        index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Apparently we need colors so here are some I guess."""
    assert len(guess) == len(secret)

    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    index: int = 0
    result: str = ""

    while index < len(secret):
        if guess[index] == secret[index]:
            result = result + green_box
        elif contains_char(secret, guess[index]):
            result = result + yellow_box
        else:
            result = result + white_box
        index = index + 1

    return result


def input_guess(expectated_length: int) -> str:
    """how long is your word?"""
    guess: str = input(f"Enter a {expectated_length} character word:")
    while len(guess) != expectated_length:
        guess = input(f"That wasn't {expectated_length} chars! Try again:")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    total_turns: int = 6
    turns: int = 1
    win: bool = False
    while turns <= total_turns and not win:

        turn_count: str = f"=== Turn {turns}/{total_turns} ==="
        print(turn_count)

        guess: str = input_guess(expectated_length=len(secret))

        result: str = emojified(guess, secret)
        print(result)

        if guess == secret:
            win = True
        else:
            turns = turns + 1

    if win:
        print(f"You won in {turns}/{total_turns} turns!")
    else:
        return print(f"X/{total_turns} - Sorry, try again tommorrow!")


if __name__ == "__main__":
    main(secret="codes")
