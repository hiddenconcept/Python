filename = input("What is your filename?")
print()
f_extns = filename.split('.')
print("The file extension is:" + repr(f_extns[-1]))
print("And your filename is:" + repr(filename))
print()

