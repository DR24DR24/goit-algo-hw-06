import networkx as nx
#import matplotlib.pyplot as plt
import task1

def dfs(graph,start):
    stack=[start]
    visited=set()
    path={start:start}
    print("dfs")
    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
            for neighbour in set(graph[vertex])-visited:
                # print(type(neighbour))
                # print(type(graph[vertex]))
                # print(list(graph[vertex]))
                path[neighbour]=vertex

                stack.append(neighbour)
    print()
    return path

path=dfs(task1.G,"A")
print(f"dfs path dictionary: {path} \n")

 

def bfs(graph,start):
    queue=[start]
    visited=set()
    path={start:start}
    print("bfs")
    while queue:
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end= " ")
            for neighbour in set(graph[vertex])-visited:
                # print(type(neighbour))
                # print(type(graph[vertex]))
                # print(list(graph[vertex]))
                path[neighbour]=vertex
                queue.append(neighbour)
    print()
    return path

path=bfs(task1.G,"A")
print(f"bfs path dictionary: {path} \n")



def biuld_path(graph,start,finish,f ):
    path=f(graph,"A")
    position=finish
    print(f"build path between {start} and {finish}, {f.__name__} ")
    print(finish, end=" ")
    while path[position]!= start:
        print(path[position], end= " ")
        position=path[position]
    print(start,"\n")    
    
biuld_path(task1.G,"A","I",dfs)   
biuld_path(task1.G,"A","I",bfs)  