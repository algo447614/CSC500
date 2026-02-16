while True:
    try:
        num1 = int(input("Please enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        num2 = int(input("Please enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

sum_result = num1 + num2
difference_result = num1 - num2

print("Sum of numbers:", sum_result)
print("Difference of numbers:", difference_result)
