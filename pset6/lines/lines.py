#counts the number of lines in a file, excluding blank lines beginning with #
import sys

if len(sys.argv) >=3:
    print("Too many command-line arguments")
    raise 1

try:

    if (".py") in sys.argv[1]:

        with open (sys.argv[1]) as file:
                lines = file.readlines()

        count = 0

        for line in lines:
            if line.strip().startswith("#"):
                count +=0
            elif line.isspace():
                count +=0
            else:
                count +=1

        print(count)


    else:
        print("Not a Python file")
        raise 1


except IndexError:
    if len(sys.argv) <= 1:
        print("Too few command-line arguments")
        raise 1

except FileNotFoundError:
    print("File does not exist")
    raise 1









