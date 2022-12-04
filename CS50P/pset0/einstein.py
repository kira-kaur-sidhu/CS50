# Einstein - rompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():

    x = int(input("m: "))

    c = 300000000

    z = x * square(c)

    print("E:",z)

def square(c):
    return c * c

main()
