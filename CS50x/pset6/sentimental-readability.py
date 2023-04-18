def main():
    text = input("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = letters/words
    S = sentences/words

    index = 0.0588 * (L * 100) - 0.296 * (S * 100) - 15.8

    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {round(index)}")

def count_letters(text):
    count = 0
    for elem in text:
        if elem.isalpha():
            count += 1
    return count

def count_words(text):
    count = 1
    for elem in text:
        if elem == " ":
            count += 1
    return count

def count_sentences(text):
    count = 0
    for elem in text:
        if elem in [".", "?", "!"]:
            count += 1
    return count

if __name__ == '__main__':
    main()
