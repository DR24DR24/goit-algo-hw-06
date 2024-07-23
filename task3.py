import task1
import math

def dijkstra(graph, start):
    nodes_table={node:[float("inf"), False,start] for node in graph.nodes()}
    current_nodes_table=nodes_table
    nodes_table[start][0]=0
    while True:
        min_key,min_value=min(nodes_table.items(),\
                            key= lambda item: item[1][0] if  not item[1][1] else float("inf"))
        if nodes_table[min_key][1]==True:
            break
        nodes_table[min_key][1]=True
        for neighbour in graph[min_key]:
            new_weight=nodes_table[min_key][0]+\
                graph.get_edge_data(neighbour,min_key)["time"]
            if nodes_table[neighbour][0]>new_weight:
                nodes_table[neighbour][0]=new_weight
                nodes_table[neighbour][2]=min_key
                    
    return nodes_table

#table = dijkstra(task1.G, "A")
nodes_list=list(task1.G.nodes())
dinstance_table=[]
for i,k in enumerate(nodes_list):
    table = dijkstra(task1.G, k)
    dinstance_table.append([])
    for j,l in enumerate(nodes_list):
        dinstance_table[i].append(table[l][0])

print(" ",nodes_list)
for i,k in enumerate(nodes_list):
    print(k,dinstance_table[i])

