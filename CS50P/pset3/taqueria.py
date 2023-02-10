# Felipe's Taqueria - mplement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            total += float(menu[item])
            format_total = "{:.2f}".format(total)
            print("Total: ", "$", format_total, sep="")
        else:
            pass

    except EOFError:
        break
