import json
import _pickle as pickle
from wordclasses import Verb
from grammarconstants import PAST,PRESENT,FUTURE,MALE,FEMALE,NEUTER,SINGULAR,PLURAL,FIRST,SECOND,THIRD,PERFECT,IMPERFECT

with  open('verbs.pkl','rb+') as f:
    obj = pickle.load(f)
verbs=obj['verbs']
count=1
for verb in verbs:
    print(str(count)+": "+verb.infinitive)
    count+=1

def getVar(name,options):
    optionString = ""
    for option in options:
        optionString += option+","
    while True:
        var = input(name+" ("+optionString[0:len(optionString)-1]+"): ")
        result = 0
        for option in options:
            if option == var:
                return result
            else:
                result+=1


def changeVariant():
    correct = False
    while not correct:
        tense = getVar("Tense",["PAST","PRESENT","FUTURE"])
        gender = getVar("Gender",["MALE","FEMALE","NEUTER"])
        mult = getVar("Mult",["SINGULAR","PLURAL"])
        person = getVar("Person",["FIRST","SECOND","THIRD"])
        state = getVar("State",["PERFECT","IMPERFECT"])
        print("current: " + verb.get(tense,gender,mult,person,state))
        newVariant = input("Please enter the new variant (x to exit):")
        if newVariant == "x":
            return True
        else:
            Verb.variant[tense][gender][mult][person][state]=newVariant

exit=False
while not exit:
    currentVerb = verbs[int(input("Please select a verb to edit: "))-1]
    print(currentVerb.infinitive)
    done = False
    while not done:
        done = changeVariant()
    exit = (input("Would you like to exit? (y/N)") == "y")


with  open('verbs.pkl','wb+') as f:
    pickle.dump(obj,f)
    f.close()

