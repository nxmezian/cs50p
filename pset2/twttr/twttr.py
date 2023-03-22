#takes a "tweet" as input and removes all vowels
tweet = input("What's on your mind? ")

newtweet = tweet.translate({ord(i): None for i in "aeiouAEIOU"})

print(newtweet)




