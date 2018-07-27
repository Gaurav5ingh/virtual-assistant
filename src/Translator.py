from googletrans import LANGUAGES, Translator
from Voice import talk

def translate():

    trans = Translator()

    talk("Enter some string :")
    in_str = input()

    out_str = trans.translate(in_str)
    print ("The input language is "+LANGUAGES[out_str.src] + "\nIts translation in English is: " + out_str.text)
