"""
Change the letter to upper case if the letter is in the even index.
Change the letter to lower case if the letter is in the odd index.

before: "hi my name is john and i am learning python"
after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
"""


def alternating_with_enumerate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()

    return new_string


if __name__ == '__main__':
    string = input("Enter the string: ")
    print(alternating_with_enumerate(string))
