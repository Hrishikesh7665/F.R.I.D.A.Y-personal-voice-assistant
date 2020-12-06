from random import *
import playsound
import os,sys


def resource_path():
    CurrentPath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    spriteFolderPath = os.path.join(CurrentPath, 'Assets/')
    path = os.path.join(spriteFolderPath)
    newPath = path.replace(os.sep, '/')
    return newPath

_path = resource_path()


def isContain_RPS(text, lst):
	for word in lst:
		if word in text:
			return True
	return False


def play(gameName):
	if isContain_RPS(gameName, ['dice','die']):
		playsound.playsound(_path+'Audio/dice.mp3')
		result = "You got " + str(randint(1,6))
		return result

	elif isContain_RPS(gameName, ['coin']):
		playsound.playsound(_path+'Audio/coin.mp3')
		p = randint(-10,10)
		if p>0: return "You got Head"
		else: return "You got Tail"

	else:
		print("Game Not Available")
