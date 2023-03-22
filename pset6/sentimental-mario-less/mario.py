# creates a pyramid-like structure based on user input
from cs50 import get_int

# prompts user for a height between 1 and 8
while True:
    height = get_int("Enter height ")
    if height > 0 and height < 9:
        break

# prints the pyramid
for i in range(height):
    for j in range(i):
        print("#", end='')
    print("#")
