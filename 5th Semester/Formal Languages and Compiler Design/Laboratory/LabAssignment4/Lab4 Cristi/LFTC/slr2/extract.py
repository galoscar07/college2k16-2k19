class Grammar:
    def __init__(self):
        self.terminals = []
        self.nonTerminals = []
        self.productions = []
        self.startSymbol = ""
    def setTerminals(self, listTerminals):
        self.terminals = listTerminals
    def setStartSymbol(self, startsymbol):
        self.startSymbol = startsymbol
    def setNonTerminals(self, listNonTerminals):
        self.nonTerminals = listNonTerminals
    def setProductions(self, listProductions):
        self.productions = listProductions


class Production:
    def __init__(self):
        self.rhs = ""
        self.lhs = ""
        self.crtPos = 0

    def initFromString(self, productionString):
        ps = str(productionString)
        ps = ps.split(">")
        self.lhs = int(ps[0].replace(" ", ""))
        self.rhs = ps[1].strip()
        self.rhs = " ".join(self.rhs.split())
        self.rhs = self.rhs.split(" ")
        res = []
        for el in self.rhs:
            res.append(int(el))
        self.rhs = res
        self.crtPos = 0

    def initFromProduction(self, production):
        self.rhs = production.rhs
        self.lhs = production.lhs
        self.crtPos = production.crtPos + 1

    def goto(self):
        if self.crtPos >= len(self.rhs):
            return None
        p = Production()
        p.initFromProduction(self)
        return p

    def getCurrentAtom(self):
        if self.crtPos == len(self.rhs):
            return None
        return self.rhs[self.crtPos]

    def isProdChecked(self):
        return self.crtPos == len(self.rhs)

    def __str__(self):
        str1 = ""
        str2 = ""

        for el in self.rhs[:self.crtPos]:
            str1+=str(el)

        for el in self.rhs[self.crtPos:]:
            str2+=str(el)

        return str(self.lhs) + ">" + str1 + "." + str2

    def __eq__(self, other):
        return (self.rhs == other.rhs) and (self.lhs == other.lhs) and (self.crtPos == other.crtPos)

    def __hash__(self):
        return hash(str(self))

class setOfProductions:
    def __init__(self, listOfProductions, id):
        self.productions = listOfProductions
        self.id = id
    def setProductions(self, listOfProductions):
        self.productions = listOfProductions
    def setId(self, newid):
        self.id = newid
    def __eq__(self, other):
        for el in self.productions:
            if el not in other.productions:
                return False
        return True
    def __str__(self):
        string = "s"+str(self.id)+"={\n"
        for el in self.productions:
            string+=" "+str(el)+"\n"
        string+="}\n"
        return string

def Closure(element, grammar):
    closure = [element]
    foundNew = True
    while foundNew:
        foundNew = False
        for curentClosureElement in closure:
            for newProduction in grammar.productions:
                if (newProduction.lhs == curentClosureElement.getCurrentAtom()) and (newProduction not in closure):
                    closure.append(newProduction)
                    foundNew = True
    return closure



def ColCan_LR0(grammar):
    auxTable = []
    crtNumber = 0
    canonicalColection = []
    s0 = Closure(grammar.productions[0],grammar)
    canonicalColection.append(setOfProductions(s0,0))
    changed = True
    while changed:
        changed = False
        for state in canonicalColection:
            for prod in state.productions:
                if prod.goto() is None:
                    continue
                sn = setOfProductions(Closure(prod.goto(),grammar),0)
                if sn not in canonicalColection:
                    crtNumber += 1
                    sn.setId(crtNumber)
                    canonicalColection.append(sn)
                    changed = True
                for i in range(0,len(canonicalColection)):
                    if canonicalColection[i] == sn:
                        tupCrt = (state.id, canonicalColection[i].id, prod.getCurrentAtom())
                        exist = False
                        for tuple in auxTable:
                            if (tuple[0] == tupCrt[0]) and (tuple[1] == tupCrt[1]) and (tuple[2] == tupCrt[2]):
                                exist = True
                        if not exist:
                            auxTable.append(tupCrt)
                        break
    return (canonicalColection, auxTable)

def First(grammar):
    first = {}
    for el in grammar.terminals:
        first[el] = [el]
    for el in grammar.nonTerminals:
        first[el] = []
    change = True
    while change:
        change = False
        for prod in grammar.productions:
            if prod.rhs[0] in grammar.terminals:
                if prod.rhs[0] not in first[prod.lhs]:
                    first[prod.lhs].append(prod.rhs[0])
                    change = True
            elif prod.rhs[0] in grammar.nonTerminals:
                if first[prod.lhs] == []:
                    first[prod.lhs] = first[prod.rhs[0]]
                    change = True
    return first

def Follow(grammar, first):
    follow = {}
    for el in grammar.nonTerminals:
        follow[el] = []
    follow[grammar.startSymbol].append("$")
    change = True
    while change:
        change = False
        for prod in grammar.productions:
            for i in range(0,len(prod.rhs)):
                atom = prod.rhs[i]
                if atom in grammar.nonTerminals and i<len(prod.rhs)-1:
                    for newElement in first[prod.rhs[i+1]]:
                        if newElement not in follow[atom]:
                            follow[atom].append(newElement)
                            change = True
                elif atom in grammar.nonTerminals and i>=len(prod.rhs) - 1:
                    if follow[prod.lhs] != []:
                        for newElement in follow[prod.lhs]:
                            if newElement not in follow[atom]:
                                follow[atom].append(newElement)
    return follow





if __name__ == "__main__":

    file = open("terminals","r")
    terminalsDict = {}
    k = 0
    for el in file:
        el = el.replace("\n","").replace(" ","")
        terminalsDict[el] = k
        #print(el +" "+str(k))
        k += 1
    file.close()
    file = open("productions","r")

    prod = []
    nonterminals = []

    for el in file:
        el = el.replace("\n","")
        lhs, rhs = el.split("::=")
        rhs = rhs.replace('"','').split(" ")
        newRhs = ""
        for atom in rhs:
            atom = atom.replace(" ","")
            if atom in terminalsDict.keys():
                newRhs+=" "+str(terminalsDict[atom])+" "
            else:
                newRhs += " "+str(atom)+" "
        rhs = newRhs
        listel = rhs.split("|")
        for comp in listel:
            tmp = ""+str(lhs)+" > "+str(comp)
            tmp = " ".join(tmp.split())
            prod.append(tmp)
            if lhs not in nonterminals:
                nonterminals.append(lhs)
    firstNonterm = k
    nonterminalDict = {}
    for val in nonterminals:
        val = val.replace(" ","")
        nonterminalDict[val] = k
        k += 1

    finalProductions = []
    for el in prod:
        rhs = el.split(" ")
        newRhs = ""
        for atom in rhs:
            atom = atom.replace(" ", "")
            if atom in nonterminalDict.keys():
                newRhs += " " + str(nonterminalDict[atom]) + " "
            else:
                newRhs += " " + str(atom) + " "
        #newRhs = " ".join(newRhs.split())
        finalProductions.append(newRhs)
    print(finalProductions)
    print(nonterminalDict)
    print(terminalsDict)

    productions1 = []
    p = Production()
    p.initFromString(str(k+1)+">"+str(firstNonterm))
    productions1.append(p)
    productions2 = []
    for pr in finalProductions:
        p = Production()
        p.initFromString(pr)
        productions1.append(p)
        productions2.append(p)

    gram = Grammar()
    gram2 = Grammar()

    gram.setNonTerminals(nonterminalDict.values())
    gram.setTerminals(terminalsDict.values())
    gram.setStartSymbol(firstNonterm)
    gram.setProductions(productions1)

    gram2.setNonTerminals(nonterminalDict.values())
    gram2.setTerminals(terminalsDict.values())
    gram2.setStartSymbol(firstNonterm)
    gram2.setProductions(productions2)

    follow = Follow(gram2, First(gram2))

    cancol, auxTable = ColCan_LR0(gram)

    for stuf in cancol:
        print(stuf)

    for tuple in auxTable:
        print(str(tuple[0]), str(tuple[1]), str(tuple[2]))

    auxTable.sort(key=lambda x: x[0])
    print("")
    print("")

    matrix = []
    for i in range(0, len(cancol)):
        matrix.append({})
    ff = k
    k = 0
    for line in matrix:
        if line == {}:
            if k == 1:
                matrix[k]["$"] = "acc"
            else:
                prodnumber = 1
                for prod in gram2.productions:
                    if prod.lhs == cancol[k].productions[0].lhs and prod.rhs == cancol[k].productions[0].rhs:
                        for folower in follow[cancol[k].productions[0].lhs]:
                            matrix[k][folower] = "r" + str(prodnumber)
                        break
                    prodnumber += 1
        k += 1

    k = 0
    for tuple in auxTable:
        if (tuple[2] in gram.terminals):
            matrix[tuple[0]][tuple[2]] = "S" + str(tuple[1])
        else:
            matrix[tuple[0]][tuple[2]] = str(tuple[1])

    for line in matrix:
        print(str(k), end=" ")
        k += 1
        for el in line.keys():
            print(str(el) + "/" + str(line[el]), end=" ")
        print("")

    print("")
    print("")

    inp = "7 0 2 20 21 24 0 29 0 25"
    sequence = inp.split(" ")
    newseq = []
    for el in sequence:
        newseq.append(int(el))
    sequence = newseq
    sequence += "$"
    stackElems = []
    stacNumbers = [0]
    topElems = -1
    topNumbers = 0
    crtPos = 0
    el = sequence[crtPos]
    finished = False
    error = False
    print(sequence)
    while crtPos < len(sequence) and finished == False:
        if el in matrix[stacNumbers[topNumbers]].keys():
            val = matrix[stacNumbers[topNumbers]][el]
            if str(val)[0].isalpha() and str(val)[0] == "S":
                stackElems.append(sequence[crtPos])
                stacNumbers.append(int(val[1:]))
                crtPos += 1
                topElems += 1
                topNumbers += 1
                el = sequence[crtPos]
            elif str(val)[0].isalpha() and str(val)[0] == "r":
                val = int(val[1])
                nr = len(gram2.productions[val - 1].rhs)
                for i in range(0, nr):
                    if len(stackElems) <= 0:
                        finished = True
                        error = True
                        break
                    stackElems.pop()
                    stacNumbers.pop()
                    topElems -= 1
                    topNumbers -= 1
                if error == False:
                    stackElems.append(gram2.productions[val - 1].lhs)
                    for chestieDePrintat in stackElems:
                        print(chestieDePrintat, end="")
                    print(sequence[crtPos:])
                    topElems += 1
                    el = stackElems[topElems]
            elif str(val)[0].isalpha() and str(val) == "acc":
                finished = True
            elif str(val)[0].isdigit():
                stacNumbers.append(int(val))
                topNumbers += 1
                el = sequence[crtPos]
        else:
            error = True
            finished = True
    if error:
        print("Error!")
    else:
        print("Ok!")