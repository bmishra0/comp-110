def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello," + name + "!"


greet(name="campers")
greet(name="Bee")
if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
