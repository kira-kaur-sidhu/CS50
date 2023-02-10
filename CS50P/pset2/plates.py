# Vanity Plates
# implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False
    if not 2 <= len(s) <= 6:
        return False
    any_numbers = False
    for c in s:
        if c.isdigit():
            if c == "0" and not any_numbers:
                return False
            any_numbers = True
        elif c.isalpha():
            if any_numbers:
                return False
        else:
            return False
    else:
        return True

main()
