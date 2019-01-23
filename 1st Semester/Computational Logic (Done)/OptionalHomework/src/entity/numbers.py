from src.entity.validators import StoreException


def returnNumberAndBase(number):
    try:
        di = {"b":2, "t":3, "f":4, "p":5, "s":6, "v":7, "e":8, "n":9, "h":16}
        b = number[len(number)-1]
        number = number[:len(number)-1]
        base = di[b]
        if base != 16:
            li = []
            for i in number:
                li.append(i)
            for i in li:
                if int(i) >= base:
                    raise Exception('Invalid input')
            return(li,base)
        elif base == 16:
            li = []
            for i in number:
                li.append(i)
            for i in li:
                if i not in ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]:
                    raise Exception("Invalid Input")
            return(li,base)
    except Exception as e:
        print(e)

c = input("Number=")
while c != "nu":
    print(returnNumberAndBase(c))
    c = input("Number=")