# For single Source Shortest Path Algorithm
# Define the Greedy search algorithm for the Single-Source Shortest Path Problem
def greedy_shortest_path(graph, start):
    # Initialize the distances dictionary with the starting vertex and its distance
    distances = {start: 0}
    
    # Initialize the visited set with the starting vertex
    visited = set([start])
    
    # Initialize the priority queue with the starting vertex and its distance
    queue = [(start, 0)]
    
    while queue:
        # Get the vertex with the smallest distance from the priority queue
        current, distance = min(queue, key=lambda x: x[1])
        
        # Add the current vertex to the visited set
        visited.add(current)
        
        # Update the distances dictionary with the current vertex and its distance
        distances[current] = distance
        
        # Add the neighbors of the current vertex to the priority queue
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                queue.append((neighbor, distance + weight))
        
        # Remove the current vertex from the priority queue
        queue.remove((current, distance))
    
    # Return the distances dictionary
    return distances
