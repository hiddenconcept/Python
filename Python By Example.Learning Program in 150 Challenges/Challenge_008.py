#Ask for the total price of the bill, then ask how many diners there are.
#divide the total bill by the number of diners and show how much each person must pay.


total_bill = int(input("Enter your total bill: "))
patreons = int(input("Enter the number of patreons: "))
split_total = total_bill / patreons

print("Each Person must be pay $",split_total)