# Little Professor - implement a program that:
# Prompts the user for a level, n, if the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.

import random


def main():
    level = get_level()
    score = 0
    total_equations = 0

    while total_equations < 10:
        incorrect_guesses = 0
        x, y = generate_integer(level), generate_integer(level)

        while True:
            answer = int(input(f"{x} + {y} = "))

            if answer == x + y:
                score += 1
                total_equations += 1
                incorrect_guesses = 0
                break

            else:
                if incorrect_guesses < 2:
                    print("EEE")
                    incorrect_guesses += 1

                else:
                    print("EEE")
                    print(f"{x} + {y} = {x+y}")
                    incorrect_guesses = 0
                    total_equations += 1
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1,4):
                break
        except ValueError:
            pass

    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)

    elif level == 2:
        return random.randint(10,99)

    elif level == 3:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
