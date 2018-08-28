import json
from wordclasses import initVerbVariants, Verb
from grammarconstants import PAST,PRESENT,FUTURE,MALE,FEMALE,NEUTER,SINGULAR,PLURAL,FIRST,SECOND,THIRD,PERFECT,IMPERFECT

def inputS(s):
    st = input(s)
    if st == 'x':
        sys.exit()

with  open('verbs.json') as f:
    obj = json.load(f)
verbs=obj['verbs']
cont=True
while cont:
    print("Adding new verb")
    print()

    # Generate english parts
    engInfinitive=input("english infinitive: ")

    engVerbVariants = initVerbVariants()
    engPastTensePerfect=input("english past tense perfect: ")
    engPastTenseImperfect=input("english past tense imperfect singular: ")
    engPastTenseImperfectPlural=input("english past tense imperfect plural: ")
    engPresentTense=input("english present tense: ")
    engFutureTensePerfect=input("english future tense perfect: ")
    engFutureTenseImperfect=input("english future tense imperfect: ")

    # [Tense][Gender][Plural][Person][Perfect]
    for i in range(3):
        for j in range(2):
            for k in range(3):
                engVerbVariants[PAST][i][j][k][PERFECT]=engPastTensePerfect
                if j == SINGULAR or k == SECOND:
                    engVerbVariants[PAST][i][j][k][IMPERFECT]=engPastTenseImperfect
                else:
                    engVerbVariants[PAST][i][j][k][IMPERFECT]=engPastTenseImperfectPlural
                engVerbVariants[PRESENT][i][j][k][PERFECT]=engPresentTense
                engVerbVariants[PRESENT][i][j][k][IMPERFECT]=engPresentTense
                engVerbVariants[FUTURE][i][j][k][PERFECT]=engFutureTensePerfect
                engVerbVariants[FUTURE][i][j][k][IMPERFECT]=engFutureTensePerfect
                
    # kitten, book, egg, I (male), I (female), You (male), you (female), we (female), we (male), you (plural,male), you (plural, female) 
    nouns = initVerbVariants()
    pnouns = initVerbVariants()
    for i in range(3):
        for j in range(2):
            nouns[i][MALE][SINGULAR][FIRST][j]="I (male)"
            pnouns[i][MALE][SINGULAR][FIRST][j]="ja"
            nouns[i][MALE][SINGULAR][SECOND][j]="you (male)"
            pnouns[i][MALE][SINGULAR][SECOND][j]="ty"
            nouns[i][MALE][SINGULAR][THIRD][j]="the kitten"
            pnouns[i][MALE][SINGULAR][THIRD][j]="kotek"
            nouns[i][MALE][PLURAL][FIRST][j]="we (male)"
            pnouns[i][MALE][PLURAL][FIRST][j]="my"
            nouns[i][MALE][PLURAL][SECOND][j]="you (plural,male)"
            pnouns[i][MALE][PLURAL][SECOND][j]="wy"
            nouns[i][MALE][PLURAL][THIRD][j]="the penises"
            pnouns[i][MALE][PLURAL][THIRD][j]="penisy"
            nouns[i][FEMALE][SINGULAR][FIRST][j]="I (female)"
            pnouns[i][FEMALE][SINGULAR][FIRST][j]="ja"
            nouns[i][FEMALE][SINGULAR][SECOND][j]="you (female)"
            pnouns[i][FEMALE][SINGULAR][SECOND][j]="ty"
            nouns[i][FEMALE][SINGULAR][THIRD][j]="the book"
            pnouns[i][FEMALE][SINGULAR][THIRD][j]="książka"
            nouns[i][FEMALE][PLURAL][FIRST][j]="we (female)"
            pnouns[i][FEMALE][PLURAL][FIRST][j]="my"
            nouns[i][FEMALE][PLURAL][SECOND][j]="you (plural,female)"
            pnouns[i][FEMALE][PLURAL][SECOND][j]="wy"
            nouns[i][FEMALE][PLURAL][THIRD][j]="the pussies"
            pnouns[i][FEMALE][PLURAL][THIRD][j]="cipki"
            nouns[i][NEUTER][SINGULAR][FIRST][j]=""
            nouns[i][NEUTER][SINGULAR][SECOND][j]=""
            nouns[i][NEUTER][SINGULAR][THIRD][j]="the egg"
            pnouns[i][NEUTER][SINGULAR][THIRD][j]="jajko"
            nouns[i][NEUTER][PLURAL][FIRST][j]=""
            nouns[i][NEUTER][PLURAL][SECOND][j]=""
            nouns[i][NEUTER][PLURAL][THIRD][j]="the eggs"
            nouns[i][NEUTER][PLURAL][THIRD][j]="jajka"
    
    polishInfinitive = input("polish infinitive: ")

    verbVariants = initVerbVariants()
    for i in range(3):
        for j in range(3):
            for k in range(2):
                for l in range(3):
                    for m in range(2):
                        if i == PRESENT:
                            if j == FEMALE:
                                verbVariants[i][j][k][l][m]=verbVariants[i][MALE][k][l][m]
                        elif j == NEUTER:
                            if l == FIRST or l == SECOND:
                                pass
                            elif k == PLURAL:
                                verbVariants[i][j][k][l][m]=verbVariants[i][FEMALE][k][l][m]
                        else: 
                            verbVariants[i][j][k][l][m] = input(nouns[i][j][k][l][m]+" "+engVerbVariants[i][j][k][l][m]+": "+pnouns[i][j][k][l][m]+" ")
    verbs.append(Verb(engInfinitive,polishInfinitive,verbVariants))

with  open('verbs.json','w') as f:
    json.dump(obj)
