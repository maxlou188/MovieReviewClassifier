import math
import re

class Bayes_Classifier:

    def __init__(self):
        self.words = {}
        self.numPos = 0
        self.numNeg = 0
        self.probPos = 0
        self.probNeg = 0
        #self.stopWords = {"the", "a", "is", "and", "of"}

    def train(self, lines: list):
        for line in lines:
            line = line.replace('\n','')
            fields = line.split('|')
            wordList = (re.sub(r'[^\w\s]', '', fields[2].lower())).split(' ')
            #print(wordList)
            #print(fields)
            if int(fields[0]) == 5:
                self.numPos += 1
                for word in wordList:
                    #if word not in self.stopWords:
                    if word in self.words:
                        self.words[word][0] += 1
                    else:
                        self.words[word] = [2, 1]
            else:
                self.numNeg += 1
                for word in wordList:
                    #if word not in self.stopWords:
                    if word in self.words:
                        self.words[word][1] += 1
                    else:
                        self.words[word] = [1,2]
            #print(self.words)
        self.probPos = math.log(self.numPos / (self.numPos + self.numNeg))
        self.probNeg = math.log(self.numNeg / (self.numPos + self.numNeg))


    def classify(self, lines: list):
        rating = []
        for line in lines:
            line = line.replace('\n','')
            fields = line.split('|')
            fields[2] = re.sub(r'[^\w\s]', '', fields[2].lower())
            wordList = fields[2].split(' ')

            posScore = self.probPos
            negScore = self.probNeg
            for word in wordList:
                if word in self.words:
                    posScore += math.log(self.words[word][0] / self.numPos)
                    negScore += math.log(self.words[word][1] / self.numNeg)
            if posScore > negScore:
                rating.append("5")
            else:
                rating.append("1")
        return rating


