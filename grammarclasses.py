# Sentence class
class Sentence:

    # Constructor
    def __init__(self,sentenceFunction):
        self.sentenceFunction=sentenceFunction

    def get(self):
        return self.sentenceFunction()
