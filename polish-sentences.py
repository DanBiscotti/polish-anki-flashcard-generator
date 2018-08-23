class Noun:
    def __init__(self,english,nominative,genetive,dative,accusative,instrumental,locative,vocative,plural):
        self.english=english
        self.nominative=nominative
        self.accusative=accusative
        self.dative=dative
        self.genetive=genetive
        self.instrumental=instrumental
        self.locative=locative
        self.vocative=vocative
        self.plural=plural

on = "ą"
en = "ę"
oo = "ó"
ch = "ć"
wu = "ł"
ni = "ń"
sh = "ś"
zi = "ź"
zo = "ż"

nouns = list()
nouns.append(Noun("kitten","kotek","kotka","kotkowi","kotka","kotkiem","kotku","kotku",False))
nouns.append(Noun("book","ksi"+on+zo+"ka","ksi"+on+zo+"ki","ksi"+on+zo+"ce","ksi"+on+zo+"k"+en,"ksi"+on+zo+"k"+on,"ksi"+on+zo+"ce","ksi"+on+zo+"ko",False))
nouns.append(Noun("egg","jajko","jajka","jajku","jajko","jajkiem","jajku","jajko",False))
nouns.append(Noun("penises","penisy","penis"+oo+"w","penisom","penisy","penisami","penisach","penisy",True))
nouns.append(Noun("pussies","cipki","cipek","cipkom","cipki","cipkami","cipkach","cipki",True))

for noun in nouns:
    print(noun.english.upper()+":")
    print("To "+("jest " if not noun.plural else "s"+on+" ")+noun.nominative)
    print("Nie ma "+noun.genetive)
    print("Przygl"+on+"dam si"+en+" "+noun.dative)
    print("Widz"+en+" "+noun.accusative)
    print("Wychodz"+en+" z "+noun.instrumental)
    print("My"+sh+"l"+en+" o "+noun.locative)
    print("O "+noun.vocative+"!")
    print()
