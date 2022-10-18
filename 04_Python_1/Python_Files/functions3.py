def avg(number):
    sum_number = 0
    for t in number:
        sum_number = sum_number + t     

    avg = sum_number / len(number)
    return avg

x = 128
y = 255
z = avg([x, y])

print("The average of", x, "and", y, "is", z)
