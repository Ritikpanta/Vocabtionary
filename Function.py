import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')
import PyDictionary 

dictionary = PyDictionary.PyDictionary()

def get_meaning(word):
    meaning = dictionary.meaning(word)
    return meaning

def get_synonym(word):
    synonym = dictionary.synonym(word)
    return synonym

def get_antonym(word):
    antonym = dictionary.antonym(word)
    return antonym

def translate(word, code):
    translate = dictionary.translate(word, code)
    return translate