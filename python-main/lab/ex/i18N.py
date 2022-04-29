
greet = {"de" : "Guten morgen",
         "fr": "Bonjour",
         "it": "Buongiorno", 
         "en": "Good morning"
}

nom = input("Votre nom : ")
# lang = input("Votre langue {} : ".format(list(greet.keys())))
lang = input("Votre langue {} : ".format(list(greet.keys())))

print(greet.get(lang, greet["en"]), 
      "\n",nom)