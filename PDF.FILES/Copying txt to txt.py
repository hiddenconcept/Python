
#'R' categories as reads ,'W' writes
with open("input.txt","r") as source_file:
    with open("output.txt","w") as destination_file:
        for line in source_file:
            destination_file.write(line)
    print("✅output.txt done✅")


#source_file parameter and destination help define the values