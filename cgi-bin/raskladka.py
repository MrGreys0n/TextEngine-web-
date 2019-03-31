#!/usr/bin/env python3
import cgi
import html
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text1 = html.escape(text1)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
            <style>
            h1 {
                font-family: 'Times New Roman', Times, serif; /* Гарнитура текста */ 
                font-size: 250%;
               } 
            p {
                font-family: Verdana, Arial, Helvetica, sans-serif; 
                font-size: 16pt;
               }
           </style>
        </head>
        <body bgcolor="BurlyWood">""")

print("<h1>Обработка данных форм!</h1>")
text = text1
d = {"q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н",
     "u": "г", "i": "ш", "o": "щ", "p": "з", "[": "х", "]": "ъ",
     "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р",
     "j": "о", "k": "л", "l": "д", ";": "ж", "'": "э", "z": "я",
     "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь",
     ",": "б", ".": "ю", "`": "ё",
     "Q": "Й", "W": "Ц", "E": "У", "R": "К", "T": "Е", "Y": "Н",
     "U": "Г", "I": "Ш", "O": "Щ", "P": "З", "{": "Х", '}': 'Ъ',
     "A": "Ф", "S": "Ы", "D": "В", "F": "А", "G": "П", "H": "Р",
     "J": "О", "K": "Л", "L": "Д", ":": "Ж", '"': 'Э', "Z": "Я",
     "X": "Ч", "C": "С", "V": "М", "B": "И", "N": "Т",
     "<": "Б", ">": "Ю", "~": "Ё", 'M': 'Ь', '/': '.', '?': ','}
data = []
for symbol in text:
    if symbol in d:
        data.append(d[symbol])
    else:
        data.append(symbol)
data = ''.join(data)

print("<p>Результат: {}</p>".format(data))

print("""</body>
        </html>""")
