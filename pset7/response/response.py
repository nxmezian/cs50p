#takes user input and checks if it is a usable email address

from validator_collection import validators, checkers, errors

email = input("What is your email? ")

try:
    email_address = validators.email(email)
    print("Valid")
except ValueError:
    print("Invalid")