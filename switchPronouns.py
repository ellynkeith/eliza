import re 

def switchPron(getUserResp):
	pronouns = {"i":"you", "my":"your", "me":"you"}
	secondPers = [pronouns[n] if n in pronouns.keys() else n for n in getUserResp]

	if secondPers[0] == "you":
		if "don't" in secondPers:
			secondPers.insert(0, "Why don't")
		else:
			secondPers.insert(0, "Why do")
	elif secondPers[0] == "it" or secondPers[0] == "your":
			if "doesn't" in secondPers:
				secondPers.insert(0, "Why doesn't")
			else:
				secondPers.insert(0, "Why does")

	secondPers.append("? ")
	secondPers = " ".join(secondPers)

	return secondPers

def makeQuestion(getUserResp):
	rex = r("i('m|t)?\s\w+(ing|s)?")


#def switchVerbTense(getSent):
	## HOW TO IDENTIFY VERB???

def copVerb(getUserResp):
	getUserResp = getUserResp.split()
	tense = {"am":"are", "i'm": "you're"}
	response = [tense[n] if n in tense.keys() else n for n in getUserResp]
	response.append("? ")
	response = " ".join(response)
	return response




# def main():
# 	getnput = raw_input("test sentence here: ")
# 	print switchPron(getnput)
# 	print copVerb(getnput)

# main()
	
