"""A raffle app!"""

from random import randint


def main() -> None:
    """ "Entrypoint of our program."""
    print("welcome to the GREAT Raffle App!")
    prize: str = input("what is being raffled?")
    contestants: list[str] = collect_names("who is playing?")
    suspense()
    winner: str = pick_winner(contestants)
    print(f"{winner} wins {prize}")


def collect_names(prompt: str) -> list[str]:
    """collect names of people in the raffle."""
    names: list[str] = []
    print(prompt)
    is_still_prompting: bool = True
    while is_still_prompting:
        name: str = input("Enter a name:")
        if len(name) == 0:
            is_still_prompting = False
        else:
            names.append(name)
    return names


def suspense() -> None:
    """Add suspense to the program!"""
    print("...drumroll please...")


def pick_winner(choices: list[str]) -> str:
    """Pick a winner from the choices."""
    winning_index: int = randint(0, len(choices) - 1)
    return choices[winning_index]


if __name__ == "__main__":
    main()
