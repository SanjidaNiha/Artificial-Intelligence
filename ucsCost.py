import heapq

def ucs(graph, start, goal):
    explored = set()
    priority = [(0, [start])]

    while priority:
        cost, path = heapq.heappop(priority)
        node = path[-1]

        if node in explored:
            continue

        explored.add(node)

        if node == goal:
            path_cost = cost  # The path cost is the cumulative cost
            return path, path_cost

        for neighbor, step_cost in graph.get(node, {}).items():
            if neighbor not in explored:
                new_cost = cost + step_cost
                new_path = path + [neighbor]
                heapq.heappush(priority, (new_cost, new_path))

    return 'No path found.', 0

# Define the graph
graph = {
    'S': {'A': 5, 'B': 2, 'C': 4},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1},
}

# Take user inputs for start and goal nodes
start_node = input("Enter the start node: ").strip()
goal_node = input("Enter the goal node: ").strip()

result, path_cost = ucs(graph, start_node, goal_node)

if result != 'No path found.':
    print(f'Shortest path from {start_node} to {goal_node}:')
    print(' -> '.join(result))  # Join path elements for readability
    print(f'Path Cost: {path_cost}')
else:
    print('No path found.')
