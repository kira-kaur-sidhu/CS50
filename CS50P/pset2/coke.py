# Coke Machine - mplement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

# Coke machine

def main():

    change = 0
    amount = 0

    while change < 50:

        change = int(input("Insert Coin: "))

        if change == 25 or change == 10 or change == 5:
            amount += change
            if amount < 50:
                print("Amount due: ", 50 - amount)
            else:
                break
        else:
            print("Amount due: ", 50)

    while amount > 50 or amount == 50:
        print("Changed owed: ", amount - 50)
        break

main()
