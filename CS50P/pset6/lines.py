# Lines of Code - implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. 
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

import sys

def main():
    try:
        if len(sys.argv) == 2:
            if ".py" in sys.argv[1]:
                print(count_lines(sys.argv[1]))

            else:
                sys.exit("Not a Python file")

        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        else:
            sys.exit("Too many command-line arguments")

    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(python_file):
    count = 0

    with open(python_file) as file:
        for line in file:
            if not line.lstrip().startswith("#") and line.strip() != "":
                count += 1

    return count

if __name__ == "__main__":
    main()
