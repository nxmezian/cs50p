def main():
    greeting = input("Enter greeting: ").lower().strip()
    value(greeting)
    print(f"${value(greeting)}")


def value(greeting):

    if ("hello") in greeting.lower():
        return(0)

    elif greeting[0] == ("h"):
        return(20)

    else:
        return(100)


if __name__ == "__main__":
    main()


