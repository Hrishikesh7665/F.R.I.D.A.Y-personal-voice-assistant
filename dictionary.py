from difflib import get_close_matches
import json
from random import choice
import os,sys


def resource_path():
    CurrentPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # Look for the 'sprites' folder on the path I just gave you:
    spriteFolderPath = os.path.join(CurrentPath, 'Assets/Json/')
    path = os.path.join(spriteFolderPath)
    newPath = path.replace(os.sep, '/')
    return newPath

_path = resource_path()

data = json.load(open(_path+'/dict_data.json', encoding='utf-8'))

def getMeaning(word):
	if word in data:
		return word, data[word], 1
	elif len(get_close_matches(word, data.keys())) > 0:
		word = get_close_matches(word, data.keys())[0]
		return word, data[word], 0
	else:
		return word, ["This word doesn't exists in the dictionary."], -1

def translate(query):
	query = query.replace('dictionary', '')
	if 'meaning' in query:
		ind = query.index('meaning of')
		word = query[ind+10:].strip().lower()
	elif 'definition' in query:
		try:
			ind = query.index('definition of')
			word = query[ind+13:].strip().lower()
		except:
			ind = query.index('definition')
			word = query[ind+10:].strip().lower()
	else: word = query

	word, result, check = getMeaning(word)
	result = choice(result)

	if check==1:
		return ["Here's the definition of \"" +word.capitalize()+ '"', result]
	elif check==0:
		return ["I think you're looking for \"" +word.capitalize()+ '"', "It's definition is,\n" + result]
	else:
		return [result, '']
