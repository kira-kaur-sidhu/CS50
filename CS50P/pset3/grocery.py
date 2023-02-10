# Grocery - mplement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. 

grocery = []
freq = []
while True:
    try:
        item = input("").upper()
        grocery.append(item)

    except EOFError:
        for item in sorted(grocery):
            if item not in freq:
                print(grocery.count(item), item, sep = " ")
                freq.append(item)
            else:
                pass
        break
