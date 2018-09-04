import random as rand
from grammarconstants import *

# Sentence class
class Sentence:

    # Constructor
    def __init__(self,sentenceFunction):
        self.sentenceFunction=sentenceFunction

    def get(self):
        return self.sentenceFunction()

class Rand:

    @staticmethod
    def tense():
        return rand.choice(TENSE)

    @staticmethod
    def gender():
        return rand.choice(GENDER)

    @staticmethod
    def mult():
        return rand.choice(MULT)

    @staticmethod
    def person():
        return rand.choice(PERSON)

    @staticmethod
    def verbstate():
        return rand.choice(verbstate)

    # randVerb will randomize any verb variables that are not provided
    @classmethod
    def randVerb(cls,tense=None,gender=None,mult=None,person=None,verbstate=None,personable=False):
        nTense=None 
        nGender=None
        nMult=None
        nPerson=None
        nVerbstate=None
        while not Rand.validateVerb(nTense,nGender,nMult,nPerson,nVerbstate,personable):
            if tense == None:
                nTense = rand.choice(TENSE)
            else:
                nTense = tense
            if gender == None:
                nGender = rand.choice(GENDER)
            else:
                nGender = gender
            if mult == None:
                nMult = rand.choice(MULT)
            else:
                nMult = mult
            if person == None:
                nPerson = rand.choice(PERSON)
            else:
                nPerson = person
            if verbstate == None:
                nVerbstate = rand.choice(VERBSTATE)
            else:
                nVerbstate = verbstate
        return { "tense":nTense,"gender":nGender,"mult":nMult,"person":nPerson,"verbstate":nVerbstate}

    # validateVerb ensures no incorrect combinations of variables are used
    @staticmethod
    def validateVerb(tense,gender,mult,person,verbstate,personable):
        if tense == None or gender == None or mult == None or person == None or verbstate == None:
            return False
        if tense == PRESENT and verbstate == PERFECT:
            return False
        if (person == FIRST or person == SECOND) and gender == NEUTER:
            return False
        return True

