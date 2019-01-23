from Graph import Graph
from Ui import UI

if __name__ == '__main__':
    print("Hello world")
    mat = [[0, 1, 0, 1, 0],
           [1, 0, 1, 1, 1],
           [0, 1, 0, 0, 1],
           [1, 1, 0, 0, 1],
           [0, 1, 1, 1, 0]]
    graph = Graph(mat,5)
    ui = UI(graph)
    ui.menu()
