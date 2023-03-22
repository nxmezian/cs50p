#overlays the image of a CS50P t-shirt over another image

import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit (1)

else:
    try:
                shirt = Image.open("shirt.png")
                size = shirt.size

                face = Image.open(sys.argv[1])

                photo_edit = ImageOps.fit(face,size)
                photo_edit.paste(shirt, shirt)

                file_ext1 = os.path.splitext(sys.argv[1])
                file_ext2 = os.path.splitext(sys.argv[2])
                if file_ext1[1] == file_ext2[1]:
                    photo_edit.save(sys.argv[2])
                else:
                    print("Input and output have different extensions")
                    sys.exit (1)

    except IndexError:
        print("Too few command-line arguments")
        sys.exit (1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit (1)
