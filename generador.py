import json

txt = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z á é í ó ú # '"

data = {"title": "Le petit prince",
        "author": "Antoine de Saint-Exupéry",
        "chapters": [
            {
                "number": 1,
                "title": "",
                "content": ""
            }
        ]
        }

txt = txt.split(' ')

# for i in txt:
#     data["chapters"][0]["content"] += f"{i * 10} {' '.join([i]*10)}\n"

data["chapters"][0]["content"] += '-No -dijo el principito-. Busco amigos. ¿Qué significa "domesticar"? ' \
                                  '-volvió a preguntar el principito.\n\n' \
                                  '-Es una cosa ya olvidada -dijo el zorro-, ' \
                                  'significa "crear vínculos...\n\n-¿Crear vínculos?\n\n-Efectivamente, ' \
                                  'verás -dijo el zorro-. Tú no eres para mí todavía más que un muchachito ' \
                                  'igual a otros cien mil muchachitos y no te necesito para nada. Tampoco tú ' \
                                  'tines necesidad de mí y no soy para ti más que un zorro entre otros cien mil ' \
                                  'zorros semejantes. Pero si tú me domesticas, entonces tendremos necesidad el ' \
                                  'uno del otro. Tú serás para mí único en el mundo, yo seré para ti único en el ' \
                                  'mundo...'

with open("braille.json", "w") as file:
    json.dump(data, file)
print(data)
