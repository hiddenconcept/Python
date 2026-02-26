#Notice 'A' it is referring to append command in the script

with open("output.txt", "a") as f:
    f.write("Welcome back to the slim shady show\n")
print("✅output.txt appended✅")