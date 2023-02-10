# NUMB3ERS  - implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

import re
import sys


def main():

    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
