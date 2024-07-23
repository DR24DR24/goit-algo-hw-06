import networkx as nx
#import matplotlib.pyplot as plt
import task1

def dfs(graph,start):
    stack=[start]
    visited=set()
    path={start:start}
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbour in set(graph[vertex])-visited:
                # print(type(neighbour))
                # print(type(graph[vertex]))
                # print(list(graph[vertex]))
                path[neighbour]=vertex
                print(path[neighbour])
                stack.append(neighbour)
    return path

path=dfs(task1.G,"Station A")
print(path)

 

def bfs(graph,start):
    queue=[start]
    visited=set()
    path={start:start}
    while queue:
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbour in set(graph[vertex])-visited:
                # print(type(neighbour))
                # print(type(graph[vertex]))
                # print(list(graph[vertex]))
                path[neighbour]=vertex
                print(path[neighbour])
                queue.append(neighbour)
    return path

path=bfs(task1.G,"Station A")
print("bfs: ", path)


def biuld_path(graph,start,finish,f ):
    path=f(graph,"Station A")
    position=finish
    print("\n",finish)
    while path[position]!= start:
        print(path[position])
        position=path[position]
    print(start,"\n")    
    
biuld_path(task1.G,"Station A","Station I",dfs)   
biuld_path(task1.G,"Station A","Station I",bfs)  