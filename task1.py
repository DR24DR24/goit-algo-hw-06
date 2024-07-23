import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (станцій/зупинок)
stations = [
    "Station A", "Station B", "Station C", "Station D", "Station E",
    "Station F", "Station G", "Station H", "Station I", "Station J"
]
G.add_nodes_from(stations)

# Додавання рёбер (маршрутів) з атрибутами (відстань, час у дорозі)
routes = [
    ("Station A", "Station B", {"distance": 5, "time": 10}),
    ("Station A", "Station C", {"distance": 7, "time": 15}),
    ("Station B", "Station D", {"distance": 3, "time": 7}),
    ("Station B", "Station E", {"distance": 4, "time": 8}),
    ("Station C", "Station F", {"distance": 6, "time": 12}),
    ("Station D", "Station G", {"distance": 5, "time": 10}),
    ("Station E", "Station H", {"distance": 2, "time": 5}),
    ("Station F", "Station I", {"distance": 8, "time": 16}),
    ("Station G", "Station J", {"distance": 4, "time": 9}),
    ("Station H", "Station I", {"distance": 3, "time": 7}),
    ("Station I", "Station J", {"distance": 6, "time": 13}),
]

G.add_edges_from(routes)

if "__main__"==__name__:
    # Візуалізація графа
    pos = nx.spring_layout(G)  # Визначення позицій вершин
    #pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")

    # Додавання міток для атрибутів рёбер (відстань, час у дорозі)
    edge_labels = {(u, v): f"{d['distance']} km, {d['time']} min" for u, v, d in G.edges(data=True)}

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Transport Network of a City")
    plt.show()

    num_of_nodes=G.number_of_nodes()
    num_of_edges=G.number_of_edges()
    is_connected=nx.is_connected(G)
    print(f"num_of_nodes: {num_of_nodes} num_of_edges: {num_of_edges} is_connected: {is_connected} ")
    degree_centrality=nx.degree_centrality(G)
    closeness_centrality=nx.closeness_centrality(G)
    betweenness_centrality=nx.betweenness_centrality(G)
    print(f"degree_centrality: {degree_centrality}")
    print(f"closeness_centrality: {closeness_centrality}")
    print(f"betweenness_centrality: {betweenness_centrality}")
    degree=dict(G.degree())
    print(f"degree : {degree}")