# Seasons of Love - mplement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from Rent, without any and between words. 

from datetime import date
import inflect
import sys

def main():
    dob = input("Date of Birth: ")
    print(convert_date(dob))

def convert_date(dob):
    try:
        year, month, day = dob.split("-")
        today = date.today()
        birthday = date(int(year), int(month), int(day))

        new_time = (abs(today - birthday) * 1440).days
        p = inflect.engine()
        correct_string =p.number_to_words(str(new_time)).capitalize().replace("and ", "")

        return f"{correct_string} minutes"

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
