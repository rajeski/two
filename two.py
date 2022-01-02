#1. Two digit input.
two_digit_number = input("Type a two digit number: ")
#2. Add the two numbers together.
try:
    sum = int(two_digit_number[0])+int(two_digit_number[1])
    print(f"Sum of digits of {two_digit_number} is {sum}.")
except ValueError:
    print("Please enter an integer.")