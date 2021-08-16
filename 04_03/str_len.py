"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def iterative_str_len(a_str):
    length = 0
    for i in a_str:
        length += 1
    return length



def recursive_str_len(a_str):
    if not a_str:
        return 0
    return 1 + recursive_str_len(a_str[1:])


input_str = "I love recursion"
print(len(input_str))  # Standard Pythonic way
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
