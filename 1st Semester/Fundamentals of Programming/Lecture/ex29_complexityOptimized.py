'''
Created on Dec 6, 2016

@author: Arthur
'''
from examples.ex27_complexity import fibonacciIterative, fibonacciRecursive, toMiliseconds
from datetime import datetime
from texttable import Texttable

'''
    4. To speed up the recursive implementation, we use memoization to store interim results
'''
results = { 0:0, 1:1 }

def fibonacciMemoization(n):
    if n not in results:
        results[n] = fibonacciMemoization(n - 1) + fibonacciMemoization(n - 2)
    return results[n]

dataList = []

def speedTestFibonacci(term):
        t1 = datetime.now()
        fibonacciIterative(term)
        t2 = datetime.now()
        fibonacciRecursive(term)
        t3 = datetime.now()
        fibonacciMemoization(term)
        t4 = datetime.now()
        return (toMiliseconds(t1 , t2), toMiliseconds(t2, t3), toMiliseconds(t3, t4))

'''
    NB!
    To run the function below, you must have installed the texttable component from:
    https://github.com/foutaise/texttable
'''
def buildResultTable():
    table = Texttable()
    table.add_row(['Term', 'Iterative', 'Recursive', 'Memoization'])
    for term in [10, 20, 30, 32, 34, 36]:
        row = speedTestFibonacci(term)
        table.add_row([term, row[0], row[1], row[2]])
    return table     

if __name__ == "__main__":  
    print(buildResultTable().draw())
        
'''
    In case you cannot run the example, this is what it is supposed to look like:
    
    +------+-----------+-----------+-------------+
    | Term | Iterative | Recursive | Memoization |
    +------+-----------+-----------+-------------+
    | 10   | 0         | 0         | 0           |
    +------+-----------+-----------+-------------+
    | 20   | 0         | 3         | 0           |
    +------+-----------+-----------+-------------+
    | 30   | 0         | 345       | 0           |
    +------+-----------+-----------+-------------+
    | 32   | 0         | 912       | 0           |
    +------+-----------+-----------+-------------+
    | 34   | 0         | 2381      | 0           |
    +------+-----------+-----------+-------------+
    | 36   | 0         | 6215      | 0           |
    +------+-----------+-----------+-------------+

    NB!
    0 miliseconds is not really 0, it's just too short to measure accurately
'''