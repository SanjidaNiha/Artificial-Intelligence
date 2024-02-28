import heapq

class Node:
    def __init__(self, state, cost, parent):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def ucs(graph, start, goal):
    explored = set()
    frontier = []
    counter = 0  # Counter for unique priorities
    
    start_node = Node(start, 0, None)
    heapq.heappush(frontier, (start_node.cost, counter, start_node))
    
    while frontier:
        _, _, node = heapq.heappop(frontier)
        
        if node.state in explored:
            continue

        explored.add(node.state)

        if node.state == goal:
            return construct_path(node)

        for neighbor, step_cost in graph[node.state].items():
            if neighbor not in explored:
                new_cost = node.cost + step_cost
                new_node = Node(neighbor, new_cost, node)
                counter += 1  # Increment counter for unique priorities
                heapq.heappush(frontier, (new_node.cost, counter, new_node))

    return None  # Goal state is not reachable

def construct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

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
path = ucs(graph, start_node, goal_node)

if path:
    print("Shortest path from {} to {}:".format(start_node, goal_node))
    print(path)
else:
    print("No path found from {} to {}.".format(start_node, goal_node))
