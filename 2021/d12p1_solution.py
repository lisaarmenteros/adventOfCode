# Advent of Code - Day 12 Problem 1
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
    def printAllPathsUtil(self, n, d, visited, path, numberOfPaths):

        # Append the node to the path
        path.append(n)

        # Mark current node as visited if it is a lower case set of letters. Capital lettered nodes can be 
        # visited any number of times so we do not have to worry about marking them for visits
        if n.islower():
            visited[n] = True
        
        # If the current node is our destination increment the number of paths
        if n == d:
            #print(path)
            numberOfPaths[0] += 1
        else:
            # Current node is not our destination so we must continue recurively through all the edges
            for i in self.graph[n]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path, numberOfPaths)
        
        # Remove current node from path and mark it as unvisited
        path.pop()
        visited[n] = False

    # Prints all possible paths from start (s) to end (e)
    def printAllPaths(self, s, e):

        visited = {}
        # Mark all nodes as not visited:
        for i in self.graph:
            visited[i] = False

        # Create array to store paths
        path = []

        # Counter for number of paths
        numberOfPaths = [0]

        self.printAllPathsUtil(s, e, visited, path, numberOfPaths)

        print(numberOfPaths)

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
    
    graph.printAllPaths("start", "end")
    
main()