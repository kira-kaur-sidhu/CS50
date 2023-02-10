# Back to the Bank - Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your test.

def main():
    greeting = input("Greeting: ").strip()
    print(value(greeting))


def value(greeting):
    if "hello" in greeting or "Hello" in greeting:
        return 0

    elif greeting[0] == "h" or greeting[0] == "H":
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
