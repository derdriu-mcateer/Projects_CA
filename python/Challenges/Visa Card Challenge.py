# Credit card numbers have a specific structure which varies depending on the vendor (eg. Visa, Mastercard, Amex, etc...)

# The structure of a valid Visa card number is:
# First digit is a 4
# Length is either 13 or 16 digits in total
# Digits 2-6 are the bank number
# The remaining digits (except the last digit) are the account number
# The last digit is a check digit

# Write a program to get a CC number from the user. If it is a Visa card, check the structure and display if it is valid or invalid. If it is valid, extract and display the bank number and account number. If it is not a Visa card, display an appropriate message.


def visa_card_valid():
    card_number = (input("Please enter your credit card number: "))
    card_number = card_number.replace(" ","")
    if card_number[0] == "4" and (len(card_number) == 13 or len(card_number) == 16):
        print("This is a valid Visa card")
        print("The bank number is: " + card_number[1:6] + " The account number is: " + card_number[6:-1])
    else:
        print("This is not a valid Visa card number. Please try again.")

visa_card_valid()