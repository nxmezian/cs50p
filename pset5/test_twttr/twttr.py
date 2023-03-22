def main():
    tweet = input("What's on your mind? ")
    newtweet = shorten(tweet)
    print(newtweet)


def shorten(word):

    return word.translate({ord(i): None for i in "aeiouAEIOU"})

if __name__ == "__main__":
    main()