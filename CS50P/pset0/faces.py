# Faces - implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂  and any :( converted to 🙁

def main():

    # Input phrase and replace emoticons with emojis
    faces = input().replace(":)", "🙂").replace(":(","🙁")

    # Print phrase
    print(faces)

main()
