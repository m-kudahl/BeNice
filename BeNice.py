import pandas
import keyboard

words = pandas.read_csv('words.csv')
replacements = dict(zip(words['badword'], words['goodword']))

def auto_replace():
    for badword, goodword in replacements.items():
        def callback(x=badword, y=goodword):
                for i in range(len(x)+1):
                     keyboard.send('backspace')
                keyboard.write(f"{y} ")

        keyboard.add_word_listener(
            badword,
            callback,
            triggers=['space','enter'],
            match_suffix=False,
            timeout=0
        )
    keyboard.wait()

auto_replace()