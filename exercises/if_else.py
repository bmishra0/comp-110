# """Example of  the if/else Conditional Statement"""


# def sign(x: int) -> str:
#     """Return the sign of the x parameter"""
#     if x > 0:
#         return "positive"
#     else:
#         if x < 0:
#             return "negative"
#         else:
#             return "zero"


# def absolute_value(x: int) -> float:
#     "Returns the absolute value of X."
#     if x > 0:
#         return x
#     else:
#         return -1.0 * x


# def pizza_price(size: str, toppings: int) -> float:
#     """Calculate the price of the pizza"""
#     price: float

#     if size == "small":
#         price = 10.0
#     else:
#         price = 15.0

#     price = price + (toppings * 0.75)
#     price = price * 1.07

#     return price


# def print_0_to_n(n: int) -> int:
#     counter: int = 0
#     while counter < n:
#         print(counter)
#         counter = counter + 1

# #     print(f"Final: {counter}")
# #     return counter


# print(print_0_to_n(n=110))


def reverse(a_str: str) -> str:
    """Reverse a string"""
    idx: int = 0
    result: str = ""
    while idx < len(a_str):
        result = a_str[idx] + result
        idx = idx + 1

    return result


print(reverse(a_str="bee"))
