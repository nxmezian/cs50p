#adds groceries to a grocery list
grocery_list = {}

while True:

    try:
        groceries = input().upper()

        if groceries.upper() in grocery_list:
            grocery_list[groceries.upper()] += 1

        else:
            grocery_list[groceries.upper()] = 1


    except EOFError:
        break

for groceries in sorted(grocery_list.keys()):
            print(grocery_list[groceries], groceries)










