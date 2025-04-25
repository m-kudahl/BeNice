import pandas
from pynput import keyboard

words = pandas.read_csv('words.csv')


replacements = dict(zip(words['badword'],words['goodword']))


test_string = "fuck this shit"

def replace_words(input):
        new_text = input.lower()
        for badword, goodword in replacements.items():
                new_text = new_text.replace(badword,goodword)
        print(new_text)

replace_words(test_string)