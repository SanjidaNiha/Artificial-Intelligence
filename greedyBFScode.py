import heapq

def greedy_search(graph, start, goal):
    queue = [(0, start)] 
    visited = {} 
    cumulative_cost = {start: 0} 

    while queue:
        _, current_node = heapq.heappop(queue)   #"throwaway" variable 

        if current_node == goal:
            return new_path(visited, start, goal), cumulative_cost[goal]

        for neighbor, cost in graph[current_node]['neighbors']:
            if neighbor not in visited:
                new_cost = cumulative_cost[current_node] + cost  
                priority = graph[neighbor]['heuristic'] 
                heapq.heappush(queue, (priority, neighbor)) 
                visited[neighbor] = current_node 
                cumulative_cost[neighbor] = new_cost  

    return None,  float('inf')

def new_path(visited, start, goal):
    path = []
    current_node = goal

    while current_node != start:
        path.insert(0, current_node)  
        current_node = visited[current_node]  # predecessor (parent) of the current_node

    path.insert(0, start) 
    return path

graph = {
    'S': {'heuristic': 8, 'neighbors': [('A', 1), ('B', 5), ('C', 8)]},
    'A': {'heuristic': 8, 'neighbors': [('D', 3), ('E', 7), ('G', 9)]},
    'B': {'heuristic': 4, 'neighbors': [('G', 4)]},
    'C': {'heuristic': 3, 'neighbors': [('G', 5)]},
    'D': {'heuristic': float('inf'), 'neighbors': []},
    'E': {'heuristic': float('inf'), 'neighbors': []},
    'G': {'heuristic': 0, 'neighbors': []}
}

start_node = input('Enter the start node: ')
goal_node = input('Enter the goal node: ')

path, cost = greedy_search(graph, start_node, goal_node)

if path:
    print(f'Path from {start_node} to {goal_node}: {path}')
    print(f'Path cost: {cost}')
else:
    print('No path found')
    print(f'Path cost: {cost}')
