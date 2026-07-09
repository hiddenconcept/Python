# Notes for the PCEP Entry Exam as I am going through the CISCO Python course.

# Demonstrating different ways to format output with print()

# By default, print() separates multiple values with a space.
print("The itsy bitsy spider", "climbed up", "the waterspout")

# print() with no arguments prints a blank line.
print()

# The end parameter changes what is printed after the output.
# By default, end="\n" (a new line). Here we use a space instead.
print("Hello, My Name Is:", "Python.", end=" ")
print("Monty Python.")

print()

# The sep parameter changes the separator between multiple values.
print("My", "name", "is", "Monty", "Python.", sep="-")

print()

# You can use both sep and end together.
# sep="_" places underscores between values.
# end="*" replaces the default newline with an asterisk.
print("My", "name", "is", sep="_", end="*")

# This line uses * as the separator and ends with * followed by a newline (\n).
print("Monty", "Python.", sep="*", end="*\n")

print()

# Since end="*" does not include a newline,
# the next print() continues on the same line.
print("My", "name", "is", sep="_", end="*")
print()
print("Monty", "Python.", sep="*", end="*\n")

print()

#sep = separator (goes between multiple values)
print("A", "B", "C", sep="-")
# Output: A-B-C

print()
#end = ending (what gets printed after the output)
print("Hello", end=" ")
print("World")
# Output: Hello World

# Default values
sep = " "
end = "\n"

print("Hello", "World","And","Good","Bye", sep=sep,)

#Data Types print accepts
print("Python")
print(42)
print(3.14)
print(True)
print(False)
