import random
import string
from datetime import datetime

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty. Please try again.")
        else:
            return value

def get_valid_dob(prompt):
    while True:
        dob = input(prompt).strip()
        try:
            # Check exact format DD/MM/YYYY
            valid_date = datetime.strptime(dob, "%d/%m/%Y")
            return dob
        except ValueError:
            print("Invalid format! Please enter DOB in DD/MM/YYYY format.")

def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["yes", "no"]:
            return value
        else:
            print("Please enter 'yes' or 'no' only.")

def get_valid_length(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print("Please enter a valid positive number.")

# User Inputs
name = get_non_empty_input("Enter your name: ")
dob = get_valid_dob("Enter your Date of Birth (DD/MM/YYYY): ")
word = get_non_empty_input("Enter a random word you like: ")
length = get_valid_length("Enter the password length: ")
special = get_yes_no("Do you want to add special characters? (yes/no): ")
digits = get_yes_no("Do you want to add numbers? (yes/no): ")

def gen_pswd():
    characters = string.ascii_letters

    if digits == "yes":
        characters += string.digits

    if special == "yes":
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password = gen_pswd()
    print("Generated Password:", password)

