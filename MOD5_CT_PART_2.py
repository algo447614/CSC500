# ask user for quantity of books purchased
books = int(input("Enter the number of books purchased this month: "))

# calculate points
if books >= 8:
    points = 60
elif books >= 6:
    points = 30
elif books >= 4:
    points = 15
elif books >= 2:
    points = 5
else:
    points = 0

# display result
print(f"You earned {points} points.")
