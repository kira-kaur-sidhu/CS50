def get_int():
    height = input("Height: ")
    if height == "" or height.isalpha() or int(height) < 1 or int(height) > 8:
        return get_int()
    return int(height)

def block(height):
    for i in range(1, height+1):
        print(" "*(height-i) + "#"*i + "  " + "#"*i)

block(get_int())
