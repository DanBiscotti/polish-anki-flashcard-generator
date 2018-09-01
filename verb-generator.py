import json
import _pickle as pickle
from wordclasses import Verb
from grammarconstants import PAST,PRESENT,FUTURE,MALE,FEMALE,NEUTER,SINGULAR,PLURAL,FIRST,SECOND,THIRD,PERFECT,IMPERFECT

def inputS(s):
    st = input(s)
    if st == 'x':
        sys.exit()

with  open('verbs.pkl','rb+') as f:
    obj = pickle.load(f)
verbs=obj['verbs']
transitives=obj['transitives']
intransitives=obj['intransitives']
ditransitives=obj['ditransitives']
linkings=obj['linkings']
auxiliaries=obj['auxiliaries']
f.close()

print("Adding new verb")
print()

# Generate english variations of the verb
engInfinitive=input("english infinitive: ")
engPastTensePerfect=input("english past tense perfect: ")
engPastTenseImperfectSingular=input("english past tense imperfect singular: ")
engPastTenseImperfectPlural=input("english past tense imperfect plural: ")
engPresentTenseSingularFirst= input("english present tense singular first: ")
engPresentTenseSingular=input("english present tense singular third: ")
engPresentTensePlural=input("english present tense plural: ")
engFutureTensePerfect=input("english future tense perfect: ")
engFutureTenseImperfect=input("english future tense imperfect: ")

# Set english variations on the verb
engVerbVariants = Verb.initVerbVariants()
for i in range(3):
    for j in range(2):
        for k in range(3):
            if j == PLURAL or k == SECOND:
                engVerbVariants[PAST][i][j][k][IMPERFECT]=engPastTenseImperfectPlural
                engVerbVariants[PRESENT][i][j][k][PERFECT]=engPresentTensePlural
                engVerbVariants[PRESENT][i][j][k][IMPERFECT]=engPresentTensePlural
            else:
                engVerbVariants[PAST][i][j][k][IMPERFECT]=engPastTenseImperfectSingular
                if k == FIRST:
                    engVerbVariants[PRESENT][i][j][k][IMPERFECT]=engPresentTenseSingularFirst
                else:
                    engVerbVariants[PRESENT][i][j][k][IMPERFECT]=engPresentTenseSingular
                engVerbVariants[PRESENT][i][j][k][PERFECT]=engPresentTenseSingular
            engVerbVariants[PAST][i][j][k][PERFECT]=engPastTensePerfect
            engVerbVariants[FUTURE][i][j][k][PERFECT]=engFutureTensePerfect
            engVerbVariants[FUTURE][i][j][k][IMPERFECT]=engFutureTenseImperfect
       
# Get type of verb (which verb groups to add it to)
if input("transitive? (he "+engPresentTenseSingular+" the ball)")=="y":
    transitives.append(len(verbs))
else:
    pass
if input("intransitive? (he "+engPresentTenseSingular+")")=="y":
    intransitives.append(len(verbs)) 
else:
    pass
if input("ditransitive (uses an indirect object)") == "y":
    ditransitives.append(len(verbs))
else:
    pass
if input("linking? (links the subject to a noun or an adjective)") == "y":
    linkings.append(len(verbs))  
else:
    pass
if input("auxiliary? (be, do, have) comes before another verb to provide extra information") == "y":
    auxiliaries.append(len(verbs))
else:
    pass

# Init nouns to make interface easier to handle (so user can see which variation of the verb to input)
nouns = Verb.initVerbVariants()
pnouns = Verb.initVerbVariants()
for i in range(3):
    for j in range(2):

        # Initialise English nouns
        nouns[i][MALE][SINGULAR][FIRST][j]="I (male)"
        nouns[i][MALE][SINGULAR][SECOND][j]="you (male)"
        nouns[i][MALE][SINGULAR][THIRD][j]="the kitten"
        nouns[i][MALE][PLURAL][FIRST][j]="we (male)"
        nouns[i][MALE][PLURAL][SECOND][j]="you (plural,male)"
        nouns[i][MALE][PLURAL][THIRD][j]="the penises"
        nouns[i][FEMALE][SINGULAR][FIRST][j]="I (female)"
        nouns[i][FEMALE][SINGULAR][SECOND][j]="you (female)"
        nouns[i][FEMALE][SINGULAR][THIRD][j]="the book"
        nouns[i][FEMALE][PLURAL][FIRST][j]="we (female)"
        nouns[i][FEMALE][PLURAL][SECOND][j]="you (plural,female)"
        nouns[i][FEMALE][PLURAL][THIRD][j]="the pussies"
        nouns[i][NEUTER][SINGULAR][THIRD][j]="the egg"
        nouns[i][NEUTER][PLURAL][THIRD][j]="jajka"

        # Init Polish nouns
        pnouns[i][MALE][SINGULAR][FIRST][j]="ja"
        pnouns[i][MALE][SINGULAR][SECOND][j]="ty"
        pnouns[i][MALE][SINGULAR][THIRD][j]="kotek"
        pnouns[i][MALE][PLURAL][FIRST][j]="my"
        pnouns[i][MALE][PLURAL][SECOND][j]="wy"
        pnouns[i][MALE][PLURAL][THIRD][j]="penisy"
        pnouns[i][FEMALE][SINGULAR][FIRST][j]="ja"
        pnouns[i][FEMALE][SINGULAR][SECOND][j]="ty"
        pnouns[i][FEMALE][SINGULAR][THIRD][j]="książka"
        pnouns[i][FEMALE][PLURAL][FIRST][j]="my"
        pnouns[i][FEMALE][PLURAL][SECOND][j]="wy"
        pnouns[i][FEMALE][PLURAL][THIRD][j]="cipki"
        pnouns[i][NEUTER][SINGULAR][THIRD][j]="jajko"

polishInfinitive = input("polish infinitive: ")


# Collect input from user on polish variation on the verb
verbVariants = Verb.initVerbVariants()
for i in range(3):
    for j in range(3):
        for k in range(2):
            for l in range(3):
                for m in range(2):
                    # TODO future imperfect will be + infinitive
                    if i == PRESENT and j == FEMALE:
                        verbVariants[i][j][k][l][m]=verbVariants[i][MALE][k][l][m]
                    elif (j == NEUTER and l == FIRST) or (j == NEUTER and l == SECOND):
                        pass
                    elif j == NEUTER and k == PLURAL:
                        verbVariants[i][j][k][l][m]=verbVariants[i][FEMALE][k][l][m]
                    elif i == PRESENT and m == PERFECT:
                        pass
                    elif i == FUTURE and m == IMPERFECT:
                        verbVariants[i][j][k][l][m] verbs[0].variants[i][j][k][l][m]+" "+polishInfinitive
                    else: 
                        verbVariants[i][j][k][l][m] = input(nouns[i][j][k][l][m]+" "+engVerbVariants[i][j][k][l][m]+": "+pnouns[i][j][k][l][m]+" ")

verbs.append(Verb(engInfinitive,polishInfinitive,verbVariants))

with  open('verbs.json','wb+') as f:
    pickle.dump(obj,f)
    f.close()
