
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lower + upper + numbers + symbols
length = int(input("Enter password length of password"))
password = "".join(random.sample(string,length))

print("Your new password is:",password)