#2. Given an undirected graph, find a vertex cover of minimum size.
from Graph import Graph, loadFromFile

if __name__ == '__main__':
    graph = loadFromFile(
            "/Users/galoscar/Documents/College/Semester 2/Graph Algorithmics/Laboratory/Practicle Work no. 5/something.txt")
    print('the minimum vertex-cover is:', graph.vertexCover() )