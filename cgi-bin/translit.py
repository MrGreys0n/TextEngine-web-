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
            <title>Транслит</title>
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
        <body bgcolor="BurlyWood">
        <center>""")

print("<h1>Обработка введённого текста!</h1>")
d = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
             "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
             "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
             "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
             "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
             "б": "b", "ю": "ju", "ё": "jo",
             "Й": "J", "Ц": "C", "У": "U", "К": "K", "Е": "E", "Н": "N",
             "Г": "G", "Ш": "Sh", "Щ": "Shh", "З": "Z", "Х": "H",
             "Ф": "F", "Ы": "Y", "В": "V", "А": "A", "П": "P", "Р": "R",
             "О": "O", "Л": "L", "Д": "D", "Ж": "Zh", "Э": "Je", "Я": "Ya",
             "Ч": "Ch", "С": "S", "М": "M", "И": "I", "Т": "T",
             "Б": "B", "Ю": "Ju", "Ё": "Jo"}
text = text1
translit = []

for symbol in text:
    if symbol in d:
        translit.append(d[symbol])
    else:
        translit.append(symbol)
        
translit = ''.join(translit)

if text == text.upper():
    translit = translit.upper()
    
print("<p>Ввод: {}</p>".format(text1))
print("<p>Результат: {}</p>".format(translit))

print("""</center>
         </body>
         </html>""")
