# Testing my Twitter - In a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

def main():
    word = input("Input: ").strip()
    print("Output:", shorten(word))


def shorten(word):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    for letter in word:
        if letter in vowels:
            changed_word = word.replace(letter, "")
            word = changed_word

    return word


if __name__ == "__main__":
    main()
