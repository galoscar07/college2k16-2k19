"""
For a given puzzle of  n x  n squares with numbers from 1 to ( n x  n-1 ) (one square is empty) in an initial
configuration, find a sequence of movements for the numbers in order to reach a final given configuration, knowing that
a number can move (horizontally or vertically) on an adjacent empty square. In  Figure 7 are presented two examples of
puzzles (with the initial and final configuration).
"""
from src.Ui import UI


def main():
    ui = UI()
    ui.run()


main()



