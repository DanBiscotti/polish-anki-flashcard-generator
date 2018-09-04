from grammarconstants import *
import random

# wordclasses - Holds classes for different types of words


# Noun class
class Noun:
    
    # Constructor
    def __init__(self,english,cases,mult,gender):
        self.english=english
        self.cases=cases
        self.mult=mult
        self.gender=gender
        self.person=THIRD

    def get(self,case):
        return self.cases[case]


# Pronoun class
class Pronoun(Noun):

    pronouns = list()

    # Constructor
    def __init__(self,english,cases,mult,gender,person):
        Noun.__init__(self,english,cases,mult,gender)
        self.english=english
        self.cases=cases
        self.mult=mult
        self.gender=gender
        self.person=person

        
    def get(self,case):
        if(self.gender==NEUTER):
            self.gender=random.choice(tuple([MALE,FEMALE,NEUTER]))
        return self.cases[case]

    def getGendered(self,gender):
        self.gender=gender
        return self
    
    @classmethod
    def getNonPersonalPronoun(cls, singular):
        if singular == SINGULAR:
            return Pronoun.pronouns[5]
        else:
            return Pronoun.pronouns[8]

    @classmethod
    def getPronoun(cls,gender,singular,person,personal=False):
        if singular == SINGULAR:
            if person == FIRST:
                return Pronoun.pronouns[0]
            elif person == SECOND:
                return Pronoun.pronouns[1]
            else:
                if personal:
                    if gender == MALE:
                        return Pronoun.pronouns[2]
                    elif gender == FEMALE:
                        return Pronoun.pronouns[3]
                else:
                    return Pronoun.pronouns[4]
        else:
            if person == FIRST:
                return Pronoun.pronouns[5]
            elif person == SECOND:
                return Pronoun.pronouns[6]
            else:
                if gender == MALE:
                    return Pronoun.pronouns[7]
                elif gender == FEMALE:
                    return Pronoun.pronouns[8]
                else:
                    return Pronoun.pronouns[9]

Pronoun.pronouns.append(Pronoun("I",["ja","","","","","",""],SINGULAR,NEUTER,FIRST))
Pronoun.pronouns.append(Pronoun("you",["ty","","","","","",""],SINGULAR,NEUTER,SECOND))
Pronoun.pronouns.append(Pronoun("he",["on","","","","","",""],SINGULAR,MALE,THIRD))
Pronoun.pronouns.append(Pronoun("she",["ona","","","","","",""],SINGULAR,FEMALE,THIRD))
Pronoun.pronouns.append(Pronoun("it",["to","","","","","",""],SINGULAR,NEUTER,THIRD))
Pronoun.pronouns.append(Pronoun("we",["my","","","","","",""],PLURAL,NEUTER,FIRST))
Pronoun.pronouns.append(Pronoun("you (plural)",["wy","","","","","",""],PLURAL,NEUTER,SECOND))
Pronoun.pronouns.append(Pronoun("they (male)",["oni","","","","","",""],PLURAL,MALE,THIRD))
Pronoun.pronouns.append(Pronoun("they (female)",["one","","","","","",""],PLURAL,FEMALE,THIRD))
Pronoun.pronouns.append(Pronoun("they (neuter)",["ono","","","","","",""],PLURAL,NEUTER,THIRD))

# Verb Class
class Verb:

    # Constructor
    def __init__(self,english,infinitive,variants):
        self.english=english
        self.infinitive=infinitive
        self.variants=variants

    def get(self,tense,gender,plural,person,perfect):
        return self.variants[tense][gender][plural][person][perfect]

    # Method that returns an empty 5d array for holding verb conjugations
    @staticmethod
    def initVerbVariants():
        result = list()
        for i in range(3):
            result.append(list())
            for j in range(3):
                result[i].append(list())
                for k in range(2):
                    result[i][j].append(list())
                    for l in range(3):
                        result[i][j][k].append(list())
                        for m in range(2):
                            result[i][j][k][l].append(list())
        return result


# Adjective class
class Adjective:

    #Constructor
    def __init__(self,cases,plural,gender):
            this.cases=cases
            this.plural=plural
            this.gender=gender


# Demonstrative class
class Demonstrative:

    # Constructor
    def __init__(self):
        demMat = list()
        for i in range(7):
            demMat.append(list())
            for j in range(3):
                demMat[i].append(list())
                for k in range(2):
                    demMat[j].append(list())

    def get(cls,proximity,case,gender,plural):
        return ("tam" if bool(proximity) else "") + demMat[case][gender][plural]
