#!/usr/bin/env python3
import cgi
import html
import sys
import codecs
import requests

DICT_WITH_LANGS = {'Русский': 'ru', 'Испанский': 'es', 'Английский': 'en',
                   'Итальянский': 'it', 'Французский': 'fr', 'Немецкий': 'de',
                   'Нидерландский': 'nl', 'Украинский': 'uk',
                   'Словенский': 'sl', 'Норвежский': 'no', 'Литовский': 'lt',
                   'Латинский': 'la', 'Белорусский': 'be'}
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
a = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961'
b = '.08d0c5ada49017ed764c042723895ffab867be7a'
KEY = a + b

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
text = form.getfirst("TEXT_1", "не задано")
text = html.escape(text1)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Перевод</title>
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
LANGUAGE1 = DICT_WITH_LANGS[text]
LANGUAGE2 = DICT_WITH_LANGS[text]
lang = LANGUAGE1 + '-' + LANGUAGE2
r = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
data = r.find('['):-1][2:-2])

print("<p>Результат: {}</p>".format(data))

print("""</body>
        </html>""")
