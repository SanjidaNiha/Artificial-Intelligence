graph = {
    'S': {'A': 1, 'B': 5, 'C': 8},
    'A': {'D': 3, 'E': 7, 'G': 9},
    'B': {'G': 4},
    'C': {'G': 5},
    'D': {},
    'E': {},
    'G': {}
}

heuristic = {
    'S': 8,
    'A': 8,
    'B': 4,
    'C': 3,
    'D': float('inf'),
    'E': float('inf'),
    'G': 0
}

def is_heuristic_valid(graph, heuristic):
    for node in graph:
        for neighbor, weight in graph[node].items():
            if heuristic[node] > weight + heuristic[neighbor]:
                #heuristic function overestimates the true cost
                #for at least one node, violating the admissibility property
                return False
    return True


# A* Algorithm
def astar(start, goal):
   

    if not is_heuristic_valid(graph, heuristic):
        print("Heuristic function is not valid for A* implementation.")
        return None, 0

    visited = [start]
    parent = {}
    c_cost = {node: float('inf') for node in graph}
    c_cost[start] = 0

    while visited:
        #Node Selection
        current = min(visited, key=lambda node: c_cost[node])  #custom criterion for sorting or evaluating elements
        visited.remove(current)

        if current == goal:
            path = [current]
            total_cost = 0
            #Path Construction 
            while current in parent:
                previous_node = parent[current]
                total_cost += graph[previous_node][current]
                current = previous_node
                path.insert(0, current)
            return path, total_cost

        for neighbor, weight in graph[current].items():
            tot_cost = c_cost[current] + weight

            if tot_cost < c_cost[neighbor]:
                parent[neighbor] = current
                c_cost[neighbor] = tot_cost
                if neighbor not in visited:
                    visited.append(neighbor)

    return None, 0

start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

if start_node in graph and goal_node in graph:
    path, path_cost = astar(start_node, goal_node)
    if path:
        print("Shortest path:", path)
        print("Path cost:", path_cost)
    else:
        print("No path found.")
else:
    print("Invalid starting or goal node. Please use valid node names from the graph.")