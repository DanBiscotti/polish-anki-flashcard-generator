from enum import IntEnum
import random

on = "ą"
en = "ę"
oo = "ó"
ch = "ć"
wu = "ł"
ni = "ń"
sh = "ś"
zi = "ź"
zo = "ż"

class Noun:
    
    # Constructor
    def __init__(self,english,nominative,genetive,dative,accusative,instrumental,locative,vocative,plural,gender):
        self.english=english
        self.nominative=nominative
        self.accusative=accusative
        self.dative=dative
        self.genetive=genetive
        self.instrumental=instrumental
        self.locative=locative
        self.vocative=vocative
        self.plural=plural
        self.gender=gender

    def copula(self):
        if(self.plural):
            return "s"+on+" "
        else:
            return "jest "


class Tense(IntEnum):
    PAST=0
    PRESENT=1
    FUTURE=2

class Gender(IntEnum):
    MALE=0
    FEMALE=1
    NEUTER=2

class Verb:

    # Constructor
    def __init__(self,english,variants):
        self.english=english
        self.variants=variants

    def getVerb(self,tense,gender,plural):
        return self.variants[tense][gender][plural]

class Sentence:

    # Constructor
    def __init__(self,sentenceFunction):
        self.sentenceFunction=sentenceFunction

    def getSentence(self,*args):
        return self.sentenceFunction(*args)

nouns = list()
nouns.append(Noun("kitten","kotek","kotka","kotkowi","kotka","kotkiem","kotku","kotku",False,Gender.MALE))
nouns.append(Noun("book","ksi"+on+zo+"ka","ksi"+on+zo+"ki","ksi"+on+zo+"ce","ksi"+on+zo+"k"+en,"ksi"+on+zo+"k"+on,"ksi"+on+zo+"ce","ksi"+on+zo+"ko",False,Gender.FEMALE))
nouns.append(Noun("egg","jajko","jajka","jajku","jajko","jajkiem","jajku","jajko",False,Gender.NEUTER))
nouns.append(Noun("penises","penisy","penis"+oo+"w","penisom","penisy","penisami","penisach","penisy",True,Gender.MALE))
nouns.append(Noun("pussies","cipki","cipek","cipkom","cipki","cipkami","cipkach","cipki",True,Gender.FEMALE))

verbs = list()
#verbs.appends(Verb("To be","jest","by"+wu,"b"+en+"dzie"))

verb = Verb("",[[["by"+wu,"by"+wu+"y"],["by"+wu+"a","by"+wu+"y"],["by"+wu+"o","by"+wu+"y"]],[["jest","s"+on],["jest","s"+on],["jest","s"+on]],[["b"+en+"dzie","b"+en+"d"+on],["b"+en+"dzie","b"+en+"d"+on],["b"+en+"dzie","b"+en+"d"+on]]])

for noun in nouns:
    print(noun.english.upper()+":")
    print("To "+noun.copula()+noun.nominative)
    print("Nie ma "+noun.genetive)
    print("Przygl"+on+"dam si"+en+" "+noun.dative)
    print("Widz"+en+" "+noun.accusative)
    print("Wychodz"+en+" z "+noun.instrumental)
    print("My"+sh+"l"+en+" o "+noun.locative)
    print("O "+noun.vocative+"!")
    print()

for noun in nouns:
    print("To "+verb.getVerb(int(Tense.PAST),int(noun.gender),int(noun.plural))+" "+noun.nominative)
    print("To "+verb.getVerb(int(Tense.PRESENT),int(noun.gender),int(noun.plural))+" "+noun.nominative)
    print("To "+verb.getVerb(int(Tense.FUTURE),int(noun.gender),int(noun.plural))+" "+noun.nominative)

sentence = Sentence(lambda noun, verb, tense: "To "+verb.getVerb(int(tense),int(noun.gender),int(noun.plural))+" "+noun.nominative)
while True:
    input()
    print(sentence.getSentence(random.choice(nouns),verb,random.choice(tuple(Tense))))
