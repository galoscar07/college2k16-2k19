# Write a program that finds the connected components of an undirected graph using a breadth-first traversal of the graph.
from Ui import UI
from UnDirGraph import loadFromFile

if __name__ == '__main__':
    print("Hallo world")
    graph = loadFromFile(
        "/Users/galoscar/Documents/College/Semester 2/Graph Algorithmics/Laboratory/Practical Work no. 2/Text")
    ui = UI(graph)
    ui.menu()