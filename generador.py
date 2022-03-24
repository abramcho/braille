import json

txt = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z á é í ó ú # '"

data = {"title": "Zoogotá",
        "author": "Manuel Espitia Benavides",
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

data["chapters"][0]["content"] += "La única ciudad en la que los gatos son cualquiera, los perros juegan micro, los" \
                                  " micos se montan en las espaldas de los ejecutivos, las abejas cobran de más, los" \
                                  " chulos piden limosna, las moscas no se dejan robar de las ratas que chalequean," \
                                  " a las que los sapos echan al agua para que los cerdos que andan en moto los " \
                                  " atrapen como peces"

with open("braille.json", "w") as file:
    json.dump(data, file)
print(data)
