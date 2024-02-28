import heapq

# Greedy Best-First Search function
def greedy_search(graph, start, goal):
    # Initialize the priority queue (heap) for nodes to explore,
    # the visited dictionary, and the cumulative cost dictionary.
    queue = [(0, start)]  # Priority queue (heap) to store nodes to explore
    visited = {}  # To keep track of visited nodes
    cumulative_cost = {start: 0}  # To keep track of cumulative cost to reach each node

    # Start exploring nodes
    while queue:
        # Get the node with the highest priority (lowest heuristic value)
        #priority value is not needed
        _, current_node = heapq.heappop(queue)

        # Check if we've reached the goal node
        if current_node == goal:
            # Return the reconstructed path and the cost
            return reconstruct_path(visited, start, goal), cumulative_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current_node]['neighbors']:
            if neighbor not in visited:
                # Calculate the new cumulative cost
                new_cost = cumulative_cost[current_node] + cost
                # Use the heuristic value as the priority
                priority = graph[neighbor]['heuristic']
                # Add the neighbor to the queue
                heapq.heappush(queue, (priority, neighbor))
                # Mark the neighbor as visited and update its cumulative cost
                visited[neighbor] = current_node
                cumulative_cost[neighbor] = new_cost

    # If no path is found, return None and set cost to infinity
    return None, float('inf')

# Reconstruct the path from start to goal
def reconstruct_path(visited, start, goal):
    path = []
    current_node = goal

    while current_node != start:
        path.insert(0, current_node)
        current_node = visited[current_node]     # predecessor (parent) of the current_node

    path.insert(0, start)
    return path

# Example graph structure (you can customize this for your problem):
graph = {
    'S': {'heuristic': 8, 'neighbors': [('A', 1), ('B', 5), ('C', 8)]},
    'A': {'heuristic': 8, 'neighbors': [('D', 3), ('E', 7), ('G', 9)]},
    'B': {'heuristic': 4, 'neighbors': [('G', 4)]},
    'C': {'heuristic': 3, 'neighbors': [('G', 5)]},
    'D': {'heuristic': float('inf'), 'neighbors': []},
    'E': {'heuristic': float('inf'), 'neighbors': []},
    'G': {'heuristic': 0, 'neighbors': []}
}

# Take user inputs for start and goal nodes
start_node = input('Enter the start node: ')
goal_node = input('Enter the goal node: ')

# Perform the search and display the result
path, cost = greedy_search(graph, start_node, goal_node)

if path:
    print(f'Path from {start_node} to {goal_node}: {path}')
    print(f'Path cost: {cost}')
else:
    print('No path found')
