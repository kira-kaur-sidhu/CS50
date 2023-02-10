# Working 9 to 5 - implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
# Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|[0-1][0-2]):?([0-5][0-9])?\s(AM|PM)\sto\s([1-9]|[0-1][0-2]):?([0-5][0-9])?\s(AM|PM)$", s):

        if matches.group(2) == None:
            num2 = 0
        else:
            num2 = int(matches.group(2))


        if matches.group(5) == None:
            num4 = 0
        else:
            num4 = int(matches.group(5))


        if matches.group(3) == "PM" and matches.group(1) != "12":
            num1 = int(matches.group(1)) + 12
        elif matches.group(3) == "AM" and matches.group(1) == "12":
            num1 = 0
        else:
            num1 = int(matches.group(1))


        if matches.group(6) == "PM" and matches.group(4) != "12":
            num3 = int(matches.group(4)) + 12
        elif matches.group(6) == "AM" and matches.group(4) == "12":
            num1 = 0
        else:
            num3 = int(matches.group(4))


        return f"{num1:02}:{num2:02} to {num3:02}:{num4:02}"

    else:
        raise ValueError

if __name__ == "__main__":
    main()
