"""
3. Write a program that, given a graph with costs and two vertices, finds a lowest cost walk between the given vertices,
 or prints a message if there are negative cost cycles accessible from the starting vertex. The program will use a
 matrix defined as d[x,k]=the cost of the lowest cost walk from s to x and of length at most k, where s is the starting
 vertex.
"""
from Graph import Graph, loadFromFile
from Ui import UI

if __name__ == '__main__':
    print("Hello world")
    graph = loadFromFile(
        "/Users/galoscar/Documents/College/Semester 2/Graph Algorithmics/Laboratory/Practicle Work no. 3/graph.txt")
    ui = UI(graph)
    ui.menu()