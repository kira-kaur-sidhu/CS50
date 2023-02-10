# Re-requesting a vanity plate-  in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests.


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if not plate[:2].isalpha():
        return False
    if not 1 < len(plate) < 7:
        return False

    any_numbers = False
    for c in plate:
        if c.isdigit():
            if c == "0" and not any_numbers:
                return False
            any_numbers = True
        elif c.isalpha():
            if any_numbers:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    main()
