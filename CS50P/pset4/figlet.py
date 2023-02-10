# Frank, Ian and Glen's Letters - mplement a program that:
# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

from pyfiglet import Figlet

import random
import sys

figlet = Figlet()

figlet.getFonts()

try:
    if len(sys.argv) == 1:
        text = input("Input: ").strip()
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font = random_font)

    elif len(sys.argv) > 2 and sys.argv[2] in figlet.getFonts():
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            text = input("Input: ").strip()
            figlet.setFont(font = sys.argv[2])

        else:
            sys.exit("Invalid usage")
except:
    sys.exit("Invalid usage")

print(f"Output: {figlet.renderText(text)}")
