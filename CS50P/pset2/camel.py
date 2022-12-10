# Camel Case - plement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

def main():

    camelCase = input("camelCase: ").replace(" ", "_")

    for c in camelCase:
        if c.isupper():
            camelCase = camelCase.replace(c, "_" + c)
        if camelCase[0] == "_":
            camelCase = camelCase[1:]

    snake_case = camelCase.lower()

    print("snake_case: ", snake_case)

main()
