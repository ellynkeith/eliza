import random 
    
    def greeting():
        howAreYou = raw_input("Hi, how are you today? ").lower()
        posFeelings = ["happy", "great", "good", "super"]
        neutFeelings = ["okay", "ok", "meh"]
        negFeelings = ["bad", "sad", "terrible", "blegh", "blah", "eh"]

        if len(howAreYou.split()) == 1:
            print gs.whichResp(howAreYou, posFeelings, neutFeelings,negFeelings)
    
    else:
        howAreYou = howAreYou.split(" ")
        for word in howAreYou:
            if word in posFeelings:
                print gs.genResp("That's good to hear. Do you want to talk about anything in particular today? ")
            elif word in neutFeelings:
                print gs.genResp("How are you feeling? ")
            elif word in negFeelings:
                print gs.genResp("I'm sorry to hear that. Is anything in particular bothering you? ")

def genResp(getResp):
    resp = raw_input(getResp)
    return resp

def whichResp(getResp, getPosFeels, getNeutFeels, getNegFeels):
    if getResp in getPosFeels:
        resp = genResp("That's good to hear. Do you want to talk about anything in particular today? ")
    elif getResp in getNeutFeels:
        resp = genResp("How are you feeling? ")
    elif getResp in getNegFeels:
        resp = genResp("I'm sorry to hear that. Is anything in particular bothering you? ")
    return resp

def randResp():
    resp = ["Can you elaborate on that? ", "What does that suggest to you? ", "Tell me more about that. "]
    return random.choice(genResp(resp))