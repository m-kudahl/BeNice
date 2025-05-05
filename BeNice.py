import keyboard
import pandas

words = pandas.read_csv('words.csv')

# create dictionary with columns from seperate dataframes to match the values
replacements = dict(zip(words['badword'], words['goodword']))

# define a letter buffer
buffer = ''

def keypress(key):
    global buffer

    # reset the buffer on space and enter
    if key.name == 'space' or key.name == 'enter':
        buffer = ''  
        return
    
    # delete last character from buffer on backspace
    elif key.name == 'backspace':
        buffer = buffer[:-1]
        return
    
    # ugly elif check for combination keys
    # this can be done better
    elif key.name == 'skift' or key.name == 'shift' or key.name == 'return' or key.name == 'ctrl':
        return

    # else add letter to buffer
    else:
        buffer += key.name

    # Now check the buffer for matches
    for badword, goodword in replacements.items():

        # force buffer to lowercase to capture uppercase
        # probably not the best way to do this
        if buffer.lower() == badword.lower():
            
            # Delete letters from badword
            for letters in badword:
                keyboard.send('backspace')

            # write goodword
            keyboard.write(goodword)

            # Reset buffer
            buffer = ''

keyboard.on_press(keypress)
    # let's wait! (forever)
keyboard.wait()
