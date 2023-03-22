#generates randomize math problems

import random
import sys


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level >0 and  level <4:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        print(x,"+", y,"=", end=" ")
        z =int(input())
        if z == x + y:
            print("Correct")
            sys.exit
        else:
            print("EEE")
            sys.exit

    if level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

        print(x,"+", y,"=", end=" ")
        z =int(input())
        if z == x + y:
            print("correct")
            sys.exit
        else:
            print("EEE")
            sys.exit

    if level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

        print(x,"+", y,"=", end=" ")
        z =int(input())
        if z == x + y:
            print("correct")
            sys.exit
        else:
            print("EEE")
            sys.exit

if __name__ == "__main__":
    main()