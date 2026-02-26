#The 'W' is indicating the script is going to write

with open("output.txt","w") as f:
    f.write("Hello, World!\n")
    f.write("& Welcome to Jackass\n")
print("✅output.txt created✅")