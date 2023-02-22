# Define the heuristic function
def heuristic(node, goal):
    # Calculate the Manhattan distance between the current node and the goal node
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Define the A* search algorithm
def astar(start, goal, graph):
    # Initialize the priority queue with the starting node and its priority
    queue = [(start, 0)]
    
    # Initialize the visited set with the starting node
    visited = set([start])
    
    # Initialize the dictionary to store the parent node of each visited node
    parent = {start: None}
    
    while queue:
        # Get the node with the lowest priority from the priority queue
        current, cost = min(queue, key=lambda x: x[1])
        
        # If the current node is the goal node, return the path to it
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        
        # Otherwise, add the neighbors of the current node to the priority queue
        for neighbor in graph[current]:
            # Calculate the cost to move from the current node to the neighbor node
            neighbor_cost = cost + graph[current][neighbor]
            
            # Calculate the heuristic value of the neighbor node
            neighbor_heuristic = heuristic(neighbor, goal)
            
            # Calculate the total cost of the neighbor node
            neighbor_total_cost = neighbor_cost + neighbor_heuristic
            
            # If the neighbor node has not been visited or the new path to the neighbor node is shorter,
            # update the priority queue, visited set, and parent dictionary
            if neighbor not in visited or neighbor_cost < parent[neighbor][0]:
                queue.append((neighbor, neighbor_total_cost))
                visited.add(neighbor)
                parent[neighbor] = (neighbor_cost, current)
        
        # Remove the current node from the priority queue
        queue.remove((current, cost))
    
    # If no path is found, return None
    return None
