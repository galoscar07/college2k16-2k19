from src.graph import Graph, loadFromFile
from src.ui import UI


if __name__ == '__main__':
    graph = loadFromFile(
            "/Users/galoscar/Documents/College/Semester 2/Graph Algorithmics/Laboratory/Graph_Algorithms/src/text")
    ui = UI(graph)
    ui.menu()