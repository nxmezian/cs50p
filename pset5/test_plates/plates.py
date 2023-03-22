#evaluates if given car plate is legal or not
import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <2 or len(s) >6:
        return 0

    if  s[0] not in string.ascii_letters:
        return 0
    if  s[1] not in string.ascii_letters:
        return 0

    if len(s) > 3:
        if s[2] in string.digits and s[3] in string.ascii_letters:
            return 0

    if len(s) > 4:
        if s[3] in string.digits and s[4] in string.ascii_letters:
            return 0

    if len(s) > 5:
        if s[4] in string.digits and s[5] in string.ascii_letters:
            return 0

    for i in s:
        if i in (".","?", " ", "?", "!", ";", ":"):
            return 0

    else:
        return 1

if __name__ == "__main__":
    main()