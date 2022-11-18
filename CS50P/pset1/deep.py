# Deep

def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

    if x == "42":
        print ("Yes")
    elif x == "forty two":
        print("Yes")
    elif x == "forty-two":
        print("Yes")
    else:
        print ("No")

main()
