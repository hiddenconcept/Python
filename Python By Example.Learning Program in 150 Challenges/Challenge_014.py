#Ask the user to enter a number between 10 and 20 (inclusive).
# If they enter a number within this range, display the message “Thank you”,
# otherwise display the message “Incorrect answer”.

# Ask the user to enter a number
number = int(input("Enter a number between 10 and 20: "))

# Check if the number is within the range
if 10 <= number <= 20:
    print("Thank you")
else:
    print("Incorrect answer")
