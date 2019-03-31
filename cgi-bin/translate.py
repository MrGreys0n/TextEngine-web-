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
text = html.escape(text)
LANGUAGE1 = form.getfirst("LANGUAGE1")
LANGUAGE2 = form.getfirst("LANGUAGE2")
err = 0
if LANGUAGE1 == None:
    LANGUAGE1 = 'Русский'
    err = 1
if LANGUAGE2 == None:
    LANGUAGE2 = 'Русский'
    err = 1
if LANGUAGE1 == 'Язык исходного текста':
    LANGUAGE1 = 'Русский'
    err = 1
if LANGUAGE2 == 'Язык перевода':
    LANGUAGE2 = 'Русский'
    err = 1

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Перевод</title>
            <style>
            h1 {
                font-family: 'Times New Roman', Times, serif; /* Гарнитура текста */ 
                font-size: 48pt;
                color: DarkRed;
                } 
            p {
                font-family: Verdana, Arial, Helvetica, sans-serif; 
                font-size: 16pt;
               }
           </style>
        </head>
        <body bgcolor="BurlyWood">
        <center>
        <h1>----------------TextEngine by ev1n----------------</h1>""")

LANGUAGE1 = DICT_WITH_LANGS[LANGUAGE1]
LANGUAGE2 = DICT_WITH_LANGS[LANGUAGE2]
lang = LANGUAGE1 + '-' + LANGUAGE2
if err == 0:
    r = requests.post(URL, data={'key': KEY, 'text': text, 'lang': lang})
    data = r.text[r.text.find('['):-1][2:-2]
    print("<p>Перевод введённого текста: {}</p>".format(data))
else:
    print("<p>Не выбран язык</p>")

print("""</body>
        </html>""")
