while True:
    number = int(input("Please enter a number: "))

    if number < 100:
        print("That's low!")
        continue

    if number > 100:
        print("That's high!")
        continue
    if number == 100: 
        print("Good job!")
        break
    