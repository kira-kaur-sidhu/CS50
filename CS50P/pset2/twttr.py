# Just Setting Up my Twitter - plement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():

    tweet = input("Input: ").strip()
    changed_tweet = ""

    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    for letter in tweet:
        if letter in vowels:
            changed_tweet = tweet.replace(letter, "")
            tweet = changed_tweet

    print("Output: ", tweet)


main()
