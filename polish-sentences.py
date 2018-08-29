from enum import IntEnum
import random
import wordclasses

# NOUNS
nouns = list()
nouns.append(Noun("kitten",["kotek","kotka","kotkowi","kotka","kotkiem","kotku","kotku"],SINGULAR,MALE))
nouns.append(Noun("book",["książka","książki","książce","książkę","książką","książce","książko"],SINGULAR,FEMALE,THIRD))
nouns.append(Noun("egg",["jajko","jajka","jajku","jajko","jajkiem","jajku","jajko"],SINGULAR,NEUTER))
nouns.append(Noun("penises",["penisy","penis"+oo+"w","penisom","penisy","penisami","penisach","penisy"],PLURAL,MALE))
nouns.append(Noun("pussies",["cipki","cipek","cipkom","cipki","cipkami","cipkach","cipki"],PLURAL,FEMALE))

# PRONOUNS
pronouns = list()
pronouns.append(Pronoun("I",["ja","","","","","",""],SINGULAR,NEUTER,FIRST))
pronouns.append(Pronoun("you",["ty","","","","","",""],SINGULAR,NEUTER,SECOND))
pronouns.append(Pronoun("he",["on","","","","","",""],SINGULAR,MALE,THIRD))
pronouns.append(Pronoun("she",["ona","","","","","",""],SINGULAR,FEMALE,THIRD))
pronouns.append(Pronoun("it",["to","","","","","",""],SINGULAR,NEUTER,THIRD))
pronouns.append(Pronoun("we",["my","","","","","",""],PLURAL,NEUTER,FIRST))
pronouns.append(Pronoun("you (plural)",["wy","","","","","",""],PLURAL,NEUTER,SECOND))
pronouns.append(Pronoun("they (male)",["oni","","","","","",""],PLURAL,MALE,THIRD))
pronouns.append(Pronoun("they (female)",["ona","","","","","",""],PLURAL,FEMALE,THIRD))

with open(verbs.json) as f:
    verbs = json.load(f)['verbs']

sentences = list()

def sentence1():
    subject = random.choice(nouns)
    tense = random.choice(tuple(Tense))
    return "To "+toBe.getVerb(int(tense),int(subject.gender),int(subject.plural))+" "+subject.nominative

def sentence2():
    verb = random.choice(verbs)
    return "Lubi"+en+" "+verb.infinitive

def sentence3():
    subject = random.choice(nouns)
    verb = random.choice(verbs)
    return subject.nominative+" lubi "+verb.infinitive

def sentence4():

sentences.append(Sentence(sentence1))
sentences.append(Sentence(sentence2))

while True:
    print(random.choice(sentences).getSentence())
    s = input()
    if(s=="x"):
        sys.exit()
