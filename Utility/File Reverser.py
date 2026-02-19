#file must bne in the same folder as the script for it to run properly or it will get an error. change the name to the text file you wish
with open('example.txt') as file:
    text = file.read()

#if you run the code twice it will change it back to normal
words = text.split()
reversed_words = []
for word in words:
    word = word[::-1]
    reversed_words.append(word)

    reversed_text = ' '.join(reversed_words)


    with open('example.txt', 'w') as file:
        file.write(reversed_text)
