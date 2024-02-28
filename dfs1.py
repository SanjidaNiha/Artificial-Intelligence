graph = {}
costs = {}

# Function to add an edge to the graph
def add_edge(u, v, cost):
    if u not in graph:
        graph[u] = []
    graph[u].append(v)
    costs[(u, v)] = cost

# Function for DFS path finding
def dfs_path(start, end, visited, path, total_cost):
    visited.add(start)
    path.append(start)

    if start == end:
        return path, total_cost

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                new_total_cost = total_cost + costs[(start, neighbor)]
                result, result_cost = dfs_path(neighbor, end, visited, path.copy(), new_total_cost)
                if result:
                    return result, result_cost
    
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

# Initialize variables
visited_nodes = set()
start_path = []
start_cost = 0

# Find and print path using DFS
path_result, total_cost = dfs_path(source_node, destination_node, visited_nodes, start_path, start_cost)
if path_result:
    print("Path:", "->".join(path_result))
    print("Total path cost:", total_cost)
else:
    print("No path found.")
