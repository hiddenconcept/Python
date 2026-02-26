#Setting up the parameters
lines = ["Apple\n","Banana\n","Cherry\n"]

#locaitng the file and using the 'W' to run the write script
with open("output.txt","w") as f:
    f.writelines(lines)
    f.write("\n")
print("✅output.txt multiple lines✅")

#This way still uses the variable, but it helps create a space between the list when it writes the script
#Notice the 2 \n
with open("output.txt","a") as f:
    for line in lines:
        f.write(line + "\n")