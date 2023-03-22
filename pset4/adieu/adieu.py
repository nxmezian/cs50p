#concatenates a number of names with the text of a song, includes the correct syntax and grammar based on the number of names inputted
import inflect
import sys

p = inflect.engine()

#creates dictionary for names to be appended to it
list_of_names =[]

#prompts for names and appends them to the list until users inputs ctrl+D
while True:
    try:
        added_names = input("Add a name: ")
        list_of_names.append(added_names)

#EOF prompts for song containing the inputted names
    except EOFError:
        inflected_names = p.join(list_of_names)
        song = ("Adieu, adieu, to")
        print(song, inflected_names)
        sys.exit(0)










