# Emojize - plement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

import emoji

text = input("Input: ").strip()

print("Output:", emoji.emojize(text, language='alias'))
