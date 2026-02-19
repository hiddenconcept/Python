#File must be in the same folder as the script, change name for file to open
with open('snowwhite.txt') as file:
    text = file.read()

sentences = text.split()

corrected_sentences =[]

for sentence in sentences:
    sentence = sentence.capitalize()
    corrected_sentences.append(sentence)

corrected_text = ' '.join(corrected_sentences)
#the name of this file is what the new file will be saved under
with open('corrected.txt', 'w') as file:
    file.write(corrected_text)

