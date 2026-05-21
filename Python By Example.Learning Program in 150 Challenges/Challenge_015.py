#Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”,
# otherwise display the message “I don’t like [colour], I prefer red”.

colour = input("Enter your favourite colour: ")

if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too")
else:
    print("I don't like", colour + ", I prefer red")