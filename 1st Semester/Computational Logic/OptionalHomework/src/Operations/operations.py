from src.entity.numbers import returnNumberAndBase


def addition(number1,number2):
    li1,base1 = returnNumberAndBase(number1)
    li2,base2 = returnNumberAndBase(number2)
    if base1 != base2:
        raise Exception("You need to give number in the same base")
    else:
        if len(li2)>len(li1):
            cop = li1
            li1 = li2
            li2 = cop
        if base1 != 16:
            pass