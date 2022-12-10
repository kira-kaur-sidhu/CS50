# Math Interpreter - mplement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z

def main():
    theorem = input("Expression: ")

    x, y, z = theorem.split(" ")

    if y == "+":
        exp = int(x )+ int(z)
        print(float(exp))

    elif y == "-":
        exp = int(x) - int(z)
        print(float(exp))

    elif y == "*":
        exp = int(x) * int(z)
        print(float(exp))

    elif y == "/":
        exp = int(x) / int(z)
        print(float(exp))

main()
