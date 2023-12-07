import random

a = int(input("Boshlanuvchi sonni yozing: "))
b = int(input("qaysi songacha bo'lishini yozing: "))

number = random.randrange(a, b + 1)


while True:

    num = int(input("Enter random number: "))

    if num > number:
        print("pass")

    elif num < number:
        print("baland")

    elif num == number:
        print("Good!!!")


