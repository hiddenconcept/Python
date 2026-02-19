import os
from datetime import datetime

directory = 'files'

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(word_count)
    #current date and time
    day = datetime.now().strftime("%Y-%m-%d")

    new_filename = f'{filename[:-4]}-{word_count}-{day}.txt'

    new_filepath = os.path.join(directory, new_filename)
    #this rename changes it and makes it offical
    os.rename(filepath, new_filepath)
