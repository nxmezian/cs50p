#takes str input and counts how many times um is used
import re

#takes input from user
def main():
    s = []
    s = input("test: ").lower()
    count(s)

#splits user input, iterates over each word and counts if and how many times the word "um" has been used
def count(s):
    splits =str.split(s)
    count = 0
    for words in splits:
        if re.search(r"^um[\W]*$", words, re.IGNORECASE):
            count +=1
    return(count)

if __name__ == "__main__":
    main()


