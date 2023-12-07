a = int(input("Enter century of year: "))

def century():
    if a > 1801 and a < 1900:
        print("19th century")

    elif a > 1901 and a < 2000:
        print("20 century")

    elif a > 2001 or a > 2024:
        print("21th century")


century()
