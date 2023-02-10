# Scourgify - implement a program that:
# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import sys
import csv

def main():
    students = []

    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        else:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].rstrip().split(", ")
                    students.append({"first": first, "last": last, "house": row["house"]})


            with open(sys.argv[2], "w") as file:
                field_names = ["first", "last", "house"]
                writer = csv.DictWriter(file, fieldnames = field_names)
                writer.writeheader()
                writer.writerows(students)


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
