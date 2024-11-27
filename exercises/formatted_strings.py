"""Demo of formatted strings (f-string)."""

# # def total_line(base: float) -> str:
# #     """Present base price and total with tax."""
# #     return "Base: " + str(base) + "w/ Tax" + str(base * 1.07)


# # def total_line(base: float) -> str:
# #     """Present base price and total with tax."""
# #     return f"Base: {base:.2f} w/ Tax: {base * 1.07:.2f}"


# def repeat(a: str) -> str:
#     """Use a formatted string to repeat param a."""
#     return f"{a}{a}"


# # print(f"Calling repeat: {repeat(a="X")}")
# print(f"Calling repeat: {repeat(a='X')}")

chr(129313)
"Hello\nworld\n!!!"


def print_age(age: int) -> None:
    print(f"You are {age}!")
    return None


print_age(age=21)
