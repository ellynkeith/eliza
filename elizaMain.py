import random  
import generateResponse as gs
import switchPronouns as sp
import re


def main():
	## Greet user
	name = raw_input("Hi, my name is Eliza. What's your name? ")
	print "Hello, %s." %(name)
	userResp = raw_input("How are you feeling today? ")

	## in case of fillers
	## problem right now: will only work if filler is only input
	filler = r"u*(h|m)*"
	verbFeels = r"i('m|t)?\s\w+(ing|s)?"

	# if re.search(filler, userResp):
	# 	response = raw_input("You seem hesitant. Can you tell me more about that? ")

	if re.search(verbFeels, userResp):
		print sp.switchPron(userResp.split())
	
	userResp = gs.taciturn(userResp)
	response = raw_input(gs.greeting(userResp))

	response = raw_input("Can you tell me more about that? ")


		


main()
