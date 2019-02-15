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
        ps = ps.replace(" ", "").split(">")
        self.lhs = ps[0]
        self.rhs = ps[1]
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
        return self.lhs + ">" + self.rhs[:self.crtPos] + "." + self.rhs[self.crtPos:]

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
                if first[prod.rhs[0]] == []:
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
    productions = ["S>AA", "A>aA", "A>b"]
    term = ["a","b"]
    nonterm = ["A","S"]
    pr = []
    pr2 = []
    p = Production()
    p.initFromString("Z>S")
    pr.append(p)

    for prod in productions:
        p = Production()
        p.initFromString(prod)
        pr.append(p)
        pr2.append(p)



    gram = Grammar()
    gram2 = Grammar()

    gram.setNonTerminals(nonterm)
    gram.setProductions(pr)
    gram.setTerminals(term)
    gram.setStartSymbol("S")

    gram2.setNonTerminals(nonterm)
    gram2.setProductions(pr2)
    gram2.setTerminals(term)
    gram2.setStartSymbol("S")

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
    for i in range(0,len(cancol)):
        matrix.append({})

    k=0
    for line in matrix:
        if line == {}:
            if cancol[k].productions[0].lhs == "Z" and cancol[k].productions[0].crtPos == 1:
                matrix[k]["$"] = "acc"
            else:
                prodnumber = 1
                for prod in gram2.productions:
                    if prod.lhs == cancol[k].productions[0].lhs and prod.rhs == cancol[k].productions[0].rhs:
                        for folower in follow[cancol[k].productions[0].lhs]:
                            matrix[k][folower] = "r"+str(prodnumber)
                        break
                    prodnumber += 1
        k += 1

    k = 0
    for tuple in auxTable:
        if(tuple[2] in gram.terminals):
            matrix[tuple[0]][tuple[2]] = "S"+str(tuple[1])
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

    sequence = "aaab"
    sequence +="$"
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
            if str(val)[0].isalpha() and  str(val)[0] == "S":
                stackElems.append(sequence[crtPos])
                stacNumbers.append(int(val[1]))
                crtPos+=1
                topElems += 1
                topNumbers += 1
                el = sequence[crtPos]
            elif str(val)[0].isalpha() and  str(val)[0] == "r":
                val = int(val[1])
                nr = len(gram2.productions[val-1].rhs)
                for i in range(0,nr):
                    if len(stackElems) <= 0:
                        finished = True
                        error = True
                        break
                    stackElems.pop()
                    stacNumbers.pop()
                    topElems -= 1
                    topNumbers -= 1
                if error == False:
                    stackElems.append(gram2.productions[val-1].lhs)
                    for chestieDePrintat in stackElems:
                        print(chestieDePrintat,end="")
                    print(sequence[crtPos:])
                    topElems+=1
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