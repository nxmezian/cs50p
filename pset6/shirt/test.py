import sys
from PIL import Image, ImageOps

try:

    if len(sys.argv) >3:
        print("Too many command-line arguments")
        sys.exit(1)

    else:

        shirt = Image.open("shirt.png")
        size = shirt.size

        muppet = Image.open(sys.argv[1])
        muppet = ImageOps.fit(shirt,size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])

except IndexError:
    print("Too few command-line arguments")
    sys.exit(1)