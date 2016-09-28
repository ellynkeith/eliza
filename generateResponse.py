import random 

posFeelings = ["happy", "great", "good", "super"]
neutFeelings = ["okay", "ok", "meh", "alright"]
negFeelings = ["bad", "sad", "terrible", "blegh", "blah", "eh"]

def taciturn(howAreYou):
    howAreYou = howAreYou.lower()
    if " " not in howAreYou:
        return howAreYou
    else:
        return howAreYou.split()

def greeting(howAreYou):
    if " " not in howAreYou:
        if howAreYou in posFeelings:
            return whichResp(howAreYou, posFeelings)
        elif howAreYou in neutFeelings:
            return whichResp(howAreYou, neutFeelings)
        elif howAreYou in negFeelings:
            return whichResp(howAreYou, negFeelings)
        else: 
            return randResp()

    else:
        for word in howAreYou:
            if word in posFeelings:
                return whichResp(word, posFeelings)
            elif word in neutFeelings:
                return whichResp(word, neutFeelings)
            elif word in negFeelings:
                return whichResp(word, negFeelings)
            else: 
                return randResp()
                
def whichResp(getFeels, listFeels):
    if listFeels == posFeelings:
        return "That's good to hear. What's made you feel %s? " %(getFeels)
    elif listFeels == neutFeelings:
        return "What's made you feel %s? " %(getFeels)
    elif listFeels == negFeelings:
        return "I'm sorry to hear that. What's made you feel %s? " %(getFeels)

def fillerResp(getResp):
    return "You seem hesitant. Can you tell me more about that? "


def randResp():
    resp = ["Can you elaborate on that? ", "What does that suggest to you? ", "Tell me more about that. ", "Look at where you are. Look at where you started. The fact that you're alive is a miracle. ", "Look around, look around, at how lucky we are to be alive right now. ", "Just stay alive. That would be enough. "]
    return random.choice(resp)







