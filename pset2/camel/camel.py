#removes camel case from file name and returns it in snake case
file = input("What is the name of your file? ")
new_file_name = ''

for i in file:
    if ord(i)  >= 65 and ord(i) <= 90:
            i = ("_" + chr(ord(i)+32))
    new_file_name = new_file_name + i


print(new_file_name)