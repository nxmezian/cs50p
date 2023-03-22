#replaces :) and :( with  🙂 and 🙁 respectively

def main():
    convert()

def convert():
    text = input ("Type here...").replace(":)",  "\U0001F642").replace(":(", "\U0001F641")
    print(text)

main()


