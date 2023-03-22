#generates math problems
import random
import sys

def main():
    get_level()

def get_level():
    level =int(input("Level: "))
    if level == 1 or level ==2 or level ==3:
        level = generate_integer(level)

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
    else:
        print("wrong")


if __name__ == "__main__":
    main()




