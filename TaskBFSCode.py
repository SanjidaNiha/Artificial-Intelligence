# Create an empty graph
graph = {}
costs = {}

# Function to add an edge to the graph
def add_edge(u, v, cost):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    costs[(u, v)] = cost

# Function for BFS shortest path
def bfs_shortest_path(start, end):
    queue = [(start, [start], 0)]
    
    while queue:
        node, path, total_cost = queue.pop(0)
        
        if node == end:
            return path, total_cost
        
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in path:
                    new_path = path + [neighbor]
                    new_total_cost = total_cost + costs[(node, neighbor)]
                    queue.append((neighbor, new_path, new_total_cost))
    
    return None, None

# Add edges to the graph

add_edge('S', 'A', 5)
add_edge('S', 'B', 2)
add_edge('S', 'C', 4)
add_edge('A', 'D', 9)
add_edge('A', 'E', 4)
add_edge('E', 'G', 6)
add_edge('D', 'H', 7)
add_edge('B', 'G', 6)
add_edge('F', 'G', 1)
add_edge('C', 'F', 2)


# Get user input
source_node = input("Enter the source node: ")
destination_node = input("Enter the destination node: ")

# Find and print with path
path, total_cost = bfs_shortest_path(source_node, destination_node)
if path:
    print("The respective path:", "->".join(path))
    print("Total path cost:", total_cost)
else:
    print("No path found.")
