import random

#DATA 
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},./?-=+*!@#$%^&_<>:`~ "

#variables (allow = True    not allowed = False)
upper, lower, nums, syms = True, True, True, True

full_content = ""

if upper:
    full_content += uppercase_letters
if lower:
    full_content += lowercase_letters
if nums:
    full_content += digits
if syms:
    full_content += symbols



length = int(input("Type the length of your password: "))  #password length
amount = int(input("How many passwords you want to generate: ")) #how many password will generate the program 

#Generator 
for x in range(amount):
    password = "".join(random.sample(full_content,length))
    print("Password: " + password)

