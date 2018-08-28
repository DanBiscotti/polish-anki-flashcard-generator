from grammarconstants import PAST,PRESENT,FUTURE,MALE,FEMALE,NEUTER,SINGULAR,PLURAL,FIRST,SECOND,THIRD,PERFECT,IMPERFECT,NEAR,FAR
# Noun class
class Noun:
    
    # Constructor
    def __init__(self,english,cases,singular,gender):
        self.english=english
        self.cases=cases
        self.singular=singular
        self.gender=gender
        self.person=THIRD

    def getNoun(case):
        return cases[case]

    def copula(self):
        if(bool(self.singular)):
            return "jest "
        else:
            return "s"+on+" "

# Pronoun class
class Pronoun(Noun):

    # Constructor
    def __init__(self,english,cases,plural,gender,person):
        Noun.__init__(self,english,cases,plural,gender)
        self.person=person

    def get(case):
        if(self.gender==NEUTER):
            self.gender=random.choice(tuple(MALE,FEMALE,NEUTER))
        return cases[case]

    def get(case,gender):
        self.gender=gender
        return cases[case]

# Verb Class
class Verb:

    # Constructor
    def __init__(self,english,infinitive,variants):
        self.english=english
        self.infinitive=infinitive
        self.variants=variants

    def get(self,tense,gender,plural,person):
        return self.variants[tense][gender][plural][person]

# Adjective class
class Adjective:

    #Constructor
    def __init__(self,cases,plural,gender):
            this.cases=cases
            this.plural=plural
            this.gender=gender

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



