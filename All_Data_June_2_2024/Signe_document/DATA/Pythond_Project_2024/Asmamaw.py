import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Perform Dijkstra's algorithm
start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

# Create a directed graph from the input graph
G = nx.DiGraph(graph)

# Define positions for nodes to ensure consistent layout
pos = {'A': (0, 0), 'B': (1, 1), 'C': (1, -1), 'D': (2, 0)}

# Plot the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_weight='bold', arrowsize=20)

# Highlight the shortest paths
for node, distance in shortest_distances.items():
    if node != start_node and distance != float('inf'):
        path = nx.shortest_path(G, source=start_node, target=node)
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)

plt.title("Shortest Paths from Node 'A' (Dijkstra's Algorithm)")
plt.show()
