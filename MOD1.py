/* 
Part 1:

Write a Python program to find the addition and subtraction of two numbers.
Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output. 
*/

/*
Pseudocode: This program will prompt the user to input one integer, and validate the data type input by user. 
Once verified to be an integer, program will repeat in order to intake a second integer. 
After two integers are input and verified, then the program will produce both the sum and the difference of the two integers. 
*/

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
