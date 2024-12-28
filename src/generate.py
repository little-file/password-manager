import random
import string
def main():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_character = "!'^+%&/()=?_>£<#$½¾{[]} |*-"
    leght = int(input("enter the leght: "))
    all_character= lowercase_letters + uppercase_letters + numbers + special_character
    password = "".join(random.choices(all_character , k= leght))

