##build a tree and make a decision based on some weighting 
##1st make a tree

# import dictionary for graph
import matplotlib.pyplot as plt
from collections import defaultdict

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        } 

def addEdge(graph,u,v):
    graph[u].append(v)

#given knowledge of what node vertices there are
def generate_edges(graph):
    edges = []
 
    # for each node in graph
    for node in graph:
         
        # for each neighbour node of a single node
        for neighbour in graph[node]:
             
            # if edge exists then append
            edges.append((node, neighbour))
    return edges

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
# function to generate all possible paths
def find_all_paths(graph, start, end, path =[]):
  path = path + [start]
  if start == end:
    return [path]
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
    for newpath in newpaths:
      paths.append(newpath)
  return paths
 
def main():
    print("Hello World!")
    addEdge(graph,'a','c')
    addEdge(graph,'b','c')
    addEdge(graph,'b','e')
    addEdge(graph,'c','d')
    addEdge(graph,'c','e')
    addEdge(graph,'c','a')
    addEdge(graph,'c','b')
    addEdge(graph,'e','b')
    addEdge(graph,'d','c')
    addEdge(graph,'e','c')
    print(generate_edges(graph))

if __name__ == "__main__":
    main()
 
