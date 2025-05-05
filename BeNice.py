import pandas
import keyboard

# read csv into DataFrame
words = pandas.read_csv('words.csv')

# create dictionary with columns from seperate dataframes to match the values
replacements = dict(zip(words['badword'], words['goodword']))

def auto_replace():
    for badword, goodword in replacements.items():

        # define callback, needed for keyboard word listener
        # make sure badword and goodword capture the current values
        def callback(x=badword, y=goodword):
                for i in range(len(x)+1):
                     keyboard.send('backspace')
                keyboard.write(f"{y} ")

        # call add_word_listener and use the defined callback on 'badword' trigger
        keyboard.add_word_listener(
            badword,
            callback,
            triggers=['space','enter'],
            match_suffix=False,
            timeout=0
        )
    # wait forever, infinite runtime
    keyboard.wait()

auto_replace()