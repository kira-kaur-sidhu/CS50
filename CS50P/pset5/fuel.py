# Refueling - in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests.


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(f"{gauge(percentage)}%")


def convert(fraction):
    (x,y) = fraction.split("/")
    percentage = (int(x) / int(y)) * 100
    return round(percentage)



def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
