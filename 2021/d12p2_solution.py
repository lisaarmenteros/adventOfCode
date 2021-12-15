# Advent of Code - Day 12 Problem 2
from collections import defaultdict

class Graph:
    def __init__ (self): 
        self.graph = defaultdict(list)

    def addEdge(self, n, e):
        self.graph[n].append(e)
        self.graph[e].append(n)
    
    # Recursive function to work in combo with printAllPaths(). Prints all paths from n to d
    # Vistied[] will keep track of all lowercase vertices visited 
    # Path will store all the vertices visited
    def printAllPaths(self, n, d, visited = set(), doubled = False):    
        # If the current node is our destination increment the number of paths
        if n == d:
            return 1
        total = 0
        for next in self.graph[n]:
            if next == "start": continue
            if next in visited and doubled: continue
            if next in visited: 
                total += self.printAllPaths(next, d, visited | {n} if n == n.lower() else visited, True)
            else:
                total += self.printAllPaths(next, d, visited | {n} if n == n.lower() else visited, doubled)

        return total

# Read file and store into a 2D array containing the edges
def main():
    inputFile = open('input/d12_input.txt')
    edges = list(inputFile.readlines())

    for i in range(len(edges)):
        edges[i] = edges[i].strip().split("-")
    
    # Create the graph
    graph = Graph()

    # Add all the edges into our graph
    for i in range(len(edges)):
        graph.addEdge(edges[i][0],edges[i][1])

    print(graph.printAllPaths("start", "end"))
    
main()