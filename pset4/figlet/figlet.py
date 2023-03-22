#returns a string in ASCII art
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()


figlet.getFonts()

if len(sys.argv) ==1:
    f = figlet.setFont(font=random.choice(figlet.getFonts()))
    convert_text = input("Input ")
    print (figlet.renderText(convert_text))


elif len(sys.argv) ==3 and sys.argv[1] == ("-f") or sys.argv[1] == ("--format"):
    if sys.argv[2]  not in figlet.getFonts():
        print("Invalid usage")
        sys.exit(1)
    f = Figlet(font=sys.argv[2])
    convert_text = input("Input ")
    print (f.renderText(convert_text))


else:
    print("Invalid usage")
    sys.exit(1)









