import random
import math

rangestart = int(1)
range_end = int(100)
 
x = random.randint(rangestart, range_end)
print("You've only got",
       round(math.log(range_end - rangestart + 1, 2)),
      "chances to guess the integer!")
 
count = 0
 
while count < math.log(range_end - rangestart + 1, 2):
    count += 1
 
    guess = int(input("Guess a number: "))
 
    if x == guess:
        print("Congratulations you did it in ",
              count, " tries")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")
 
if count >= math.log(range_end - rangestart + 1, 2):
    print("Mission failed!")
    print("The number was %d" % x)