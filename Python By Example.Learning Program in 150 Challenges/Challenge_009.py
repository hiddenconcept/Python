#write a program that will ask for the number of days and then will show how many hours,minutes and seconds in that number of days.


days = int(input("Enter how many days: "))
hours = days*24
minutes = hours*60
seconds = minutes*60
print("In",days,"days there are...")
print(hours,"hours, there are...")
print(minutes,"minutes, there are...")
print(seconds,"seconds")