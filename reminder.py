# Asking the user to input two integers
dividend = int(input("Please enter an integer to be divided: "))
divisor = int(input("Please enter an integer to divide by: "))

# Performing the division and calculating the remainder
quotient = dividend // divisor
remainder = dividend % divisor

# Printing the result
print(f"The result of this division is {quotient} with a remainder of {remainder}")
