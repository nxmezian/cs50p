#takes coins as input and informs user of any change due
total = 50



while True:
    print("Amount due:", total)

    change = int(input("How many cents? "))

    if change != 5 and change != 10 and change !=25:
            change = 0
    total = total - change


    newtotal = total
    if newtotal <=0:
                print("Change owed", ((newtotal - newtotal)-newtotal))
                break





