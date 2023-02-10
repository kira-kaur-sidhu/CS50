# CS50 P-Shirt -mplement a program that expects exactly two command-line arguments:
# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.



import sys
from PIL import Image, ImageOps

def main():

    suffixes = (".jpg", ".jpeg", ".png")

    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        if not sys.argv[1].lower().endswith(suffixes):
            sys.exit("Invalid input")

        if not sys.argv[2].lower().endswith(suffixes):
            sys.exit("Invalid input")

        if not sys.argv[1][-4:] == sys.argv[2][-4:]:
            sys.exit("Input and output have different extensions")

        else:
            new_image()


    except FileNotFoundError:
        sys.exit("Input does not exist")

def new_image():

    image = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")

    size = shirt.size

    image_fixed = ImageOps.fit(image, size)

    image_fixed.paste(shirt, shirt)

    image_fixed.save(sys.argv[2])


if __name__ == "__main__":
    main()
