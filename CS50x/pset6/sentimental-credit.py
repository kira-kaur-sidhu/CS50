def main():
    number = input("Number: ")

    for elem in number:
        if not elem.isdigit():
            return main()

    if is_valid(number) == True:
        if len(number) == 15:
            if number[0:2] in ["34", "37"]:
                print("AMEX")
                return
        if len(number) == 13 or len(number) == 16:
            if number[0] == "4":
                print("VISA")
                return
        if len(number) == 16:
            if number[0:2] in ["51", "52", "53", "54", "55"]:
                print("MASTERCARD")
                return

    print("INVALID")
    return


def is_valid(number):
    sum = 0
    n = number[::-1]
    for i in range(len(n)):
        if i % 2 == 0:
            sum += int(n[i])
        else:
            if int(n[i]) > 4:
                even = str(int(n[i])*2)
                sum += int(even[0]) + int(even[1])
            else:
                sum += int(n[i])*2

    if sum % 10 == 0:
        return True
    return False


if __name__ == "__main__":
    main()
