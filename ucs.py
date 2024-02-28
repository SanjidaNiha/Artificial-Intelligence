import heapq

def ucs(graph, start, goal):
    explored = set()
    frontier = [(0, [start])]  # Use a list to track the path

    while frontier:
        cost, path = heapq.heappop(frontier)
        node = path[-1]

        if node in explored:
            continue

        explored.add(node)

        if node == goal:
            return ' -> '.join(path)

        for neighbor, step_cost in graph.get(node, {}).items():
            if neighbor not in explored:
                new_cost = cost + step_cost
                new_path = path + [neighbor]
                heapq.heappush(frontier, (new_cost, new_path))

    return 'No path found.'

# Example usage:
graph = {
   'S': {'A': 5, 'B': 2, 'C':4},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1},
}

start_node = 'S'
goal_node = 'G'
result = ucs(graph, start_node, goal_node)

if result:
    print(f'Shortest path from {start_node} to {goal_node}:')
    print(result)
else:
    print('No path found.')
