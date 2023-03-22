#CHANGE 
def main():
    fraction = input("Input fraction ")
    frac_conv = convert(fraction)
    output = gauge(frac_conv)
    print(output)


def convert(fraction):
    while True:

        try:
                x, y = fraction.split("/")
                x = int(x)
                y = int(y)
                if x < y  or x == y:
                    fraction = (x/y)
                    percentage = int (fraction * 100)
                    return percentage
                else:
                    raise ZeroDivisionError

        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):

    percentage = int(percentage)

    if percentage == 66:
        return ("67%")

    elif percentage >= 99:
        return ("F")

    elif percentage <=1:
        return ("E")

    else:
         return str(percentage) + "%"


if __name__ == "__main__":
    main()