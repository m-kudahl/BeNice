import keyboard
import pandas

words = pandas.read_csv("words.csv")

# use badword column as index and read the goodword column
replacements = words.set_index("badword")["goodword"].to_dict()

# define a letter buffer
buffer = ""


def keypress(key):
    # declare buffer as global variable
    global buffer

    # switch (match case) statement for the key being pressed
    match key.name:

        # reset buffer on space or enter key
        case "space" | "enter":
            buffer = ""
            return

        # delete last letter in buffer on backspace
        case "backspace":
            buffer = buffer[:-1]
            return

        # prevent buttons that are not letters from being added to the buffer
        case "skift" | "shift" | "return" | "ctrl":
            return

        # else, add the keypress to the buffer
        case _:
            buffer += key.name

    # Now check the buffer for matches
    for badword, goodword in replacements.items():

        # force buffer to lowercase to capture uppercase
        # probably not the best way to do this
        if buffer.lower() == badword.lower():

            # Delete letters from badword
            for letters in badword:
                keyboard.send("backspace")

            # write goodword
            keyboard.write(goodword)

            # Reset buffer
            buffer = ""


keyboard.on_press(keypress)
# let's wait (forever!)
keyboard.wait()
