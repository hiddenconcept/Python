#Ask how many slices of pizza the user started with and ask how many slices they have eaten.
#Work out how many slices they have left and display the answer in a user-friendly format

startnum = int(input("Enter the number of slices of pizza you started with: "))
endnum = int(input("Enter the number of slices of pizza have eaten? "))
slicesleft = startnum - endnum
print("You have:",slicesleft, "slices remaining ")