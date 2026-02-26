with open("output.txt","r") as readfile, open("output2.txt","w") as writefile:
    for line in readfile:
        writefile.write(line)
    print("✅output.txt done✅")
