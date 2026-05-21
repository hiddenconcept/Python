#Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number,
# otherwise show the first number first and then the second.

# Ask for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compare and display in order
if num1 > num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)