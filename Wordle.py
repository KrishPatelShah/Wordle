import random

class Wordle:
    def __init__(self):
        secretWords = ["royal","squad","stair","scare","foray","comma","natal","shawl","fewer","trope","snout"]
        self.secret = secretWords[random.randint(0,len(secretWords)-1)]
        self.hint = ["grey","grey","grey","grey","grey"]
        self.win = False

    #populates the hint list with grey, yellow or green based on Wordle rules and guess
    def makeHint(self,guess):
        self.hint = ["grey","grey","grey","grey","grey"]
        for i in range(5):
            if guess[i] == self.secret[i]:
                self.hint[i] = "green"
            elif guess[i] in self.secret:
                self.hint[i] = "yellow"
             
            

    #sets win to either true or false based on guess
    def checkWin(self,guess):
        if self.secret == guess:
            self.win = True

    def getSecret(self):
        return self.secret

    def getHint(self):
        return self.hint
        
    def getWin(self):
        return self.win

wordle = Wordle()
numGuesses = 0
print("welcome to wordle!")
while(wordle.getWin() == False and numGuesses < 6):
    guess = input("Please enter a guess:  ")
    numGuesses += 1
    wordle.checkWin(guess)
    if wordle.getWin() == True:
        print("congrats, you won")
    else:
        print("you didn't win yet, guesses remaining = " + str(6 - numGuesses))
        wordle.makeHint(guess)
        print("hint = " + str(wordle.getHint()))
if wordle.getWin() == False:
    print("sorry, you lost, the secret word was: " + wordle.getSecret())
