def Translate(phrase) :
    Translated_Phrase =""
    for letter in phrase :
        if letter.lower() in "aeiou":
            Translated_Phrase += "V"
        else :
            Translated_Phrase += letter.lower()
    return Translated_Phrase
phrase = input("\nPlease enter a phrase you want to translate : ")
phrase = Translate(phrase)
print("The translated phrase is " + phrase)