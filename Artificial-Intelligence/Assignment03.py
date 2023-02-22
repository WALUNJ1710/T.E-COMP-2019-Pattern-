# 1. Define the Greedy search algorithm for the Selection Sort
def greedy_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted part of the array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    # Return the sorted array
    return arr
  
  
# 2. 
# Define the Greedy search algorithm for the Minimum Spanning Tree
def greedy_minimum_spanning_tree(graph):
    # Initialize the set of visited vertices and the set of edges in the minimum spanning tree
    visited = set()
    mst = set()
    
    # Add the first vertex to the visited set
    visited.add(next(iter(graph)))
    
    # Loop until all vertices are visited
    while len(visited) < len(graph):
        # Find the minimum weight edge that connects a visited vertex to an unvisited vertex
        min_edge = None
        for u in visited:
            for v, weight in graph[u].items():
                if v not in visited and (min_edge is None or weight < min_edge[2]):
                    min_edge = (u, v, weight)
        
        # Add the edge to the minimum spanning tree and the visited set
        mst.add(min_edge)
        visited.add(min_edge[1])
    
    # Return the set of edges in the minimum spanning tree
    return mst
  
  
  
  
