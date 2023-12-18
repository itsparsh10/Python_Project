import json
from difflib import get_close_matches
from googletrans import Translator

dictionary_data = json.load(open("dictionary_data.json"))
translator = Translator()

def translate(word, target_language='en'):
    word = word.lower()
    if word in dictionary_data:
        return dictionary_data[word]
    elif word.title() in dictionary_data:
        return dictionary_data[word.title()] 
    elif word.upper() in dictionary_data:
        return dictionary_data[word.upper()]
    elif len(get_close_matches(word, dictionary_data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word, dictionary_data.keys())[0])
        decide = input("Press y for yes or n for no: ")
        if decide == "y":
            return dictionary_data[get_close_matches(word, dictionary_data.keys())[0]]
        elif decide == "n":
            return "Pugger, your paw steps on working keys."
        else:
            return "You have entered the wrong input. Please enter just y or n."    
    else:
        print("You have entered wrong keys. Try again.")
        

word = input("Enter the word you want to search: ")
target_language = input("Enter the target language (e.g., 'fr' for French, 'es' for Spanish): ")

output = translate(word)

if type(output) == list:
    for item in output:
        translated_item = translator.translate(item, dest=target_language).text
        print(translated_item)
else:
    translated_output = translator.translate(output, dest=target_language).text
    print(translated_output)
