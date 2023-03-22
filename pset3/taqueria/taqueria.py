#calculates the price for a meal
def main():
    x = 0.00
    while True:
            try:
                x = x + get_order()
                print ("$"+"{:.2f}".format(x))

            except EOFError:
                break

            except TypeError:
                continue


def get_order():
    menu ={
            "Baja Taco": 4.00,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00}

    order = input("What is your order? ").title()

    if order in menu:
        return(float(menu[order]))


main()

