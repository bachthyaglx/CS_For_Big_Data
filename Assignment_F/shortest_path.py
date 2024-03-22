def dijkstra(graph, start, end):
    # Initialize infinity value
    inf = float('inf')

    # Initialize node data for each node in the graph
    # 'cost': cost of reaching the node from the start
    # 'pred': list of predecessors in the current shortest path
    node_data = {node: {'cost': inf, 'pred': []} for node in graph}

    # Set the cost of the start node to 0
    node_data[start]['cost'] = 0

    # List to keep track of visited nodes
    visited = []

    # Start with the initial node
    temp = start

    # Loop through the graph to find the shortest path
    for i in range(len(graph) - 1):
        # Check if the current node has not been visited
        if temp not in visited:
            # Mark the current node as visited
            visited.append(temp)

            # Initialize a list to store the minimum costs of reaching neighbors
            min_heap = []

            # Iterate through neighbors of the current node
            for j in graph[temp]:
                # Check if the neighbor has not been visited
                if j not in visited:
                    # Calculate the cost of reaching the neighbor
                    cost = node_data[temp]['cost'] + graph[temp][j]

                    # Update the cost and predecessors if a shorter path is found
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + [temp]

                    # Add the cost and the neighbor to the min-heap
                    min_heap.append((node_data[j]['cost'], j))

            # If the min-heap is not empty, update the current node to the one with the minimum cost
            if min_heap:
                min_heap.sort()
                temp = min_heap[0][1]

    # Print shortest path
    path = node_data[end]['pred'] + [end]
    print("Shortest Path:", " -> ".join(path))

    # Print analysis
    analysis = []
    total_distance = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        distance = graph[current_node][next_node]
        analysis.append(f"{current_node}->{next_node}({distance})")
        total_distance += distance

    print("Analysis:")
    for step in analysis:
        print(step)

    print("Shortest Distance:", total_distance)

if __name__ == "__main__":
    
    run_choice = 5
    
    run_choices = {
        4:  "Challenge 4 - Implementing Dijkstra's Shortest Path Algorithm",
        5:  "Challenge 5 - Run for Another Graph",
    }
    
    graph_1 = {
        'S': {'A': 7, 'B': 2, 'C': 3},
        'A': {'S': 7, 'B': 3, 'D': 4},
        'B': {'S': 2, 'A': 3, 'H': 1},
        'C': {'S': 3, 'L': 2},
        'D': {'A': 4, 'B': 4, 'F': 5},
        'E': {'G': 2, 'K': 5},
        'F': {'D': 5, 'H': 3},
        'G': {'H': 2, 'E': 2},
        'H': {'B': 1, 'F': 3, 'G': 2},
        'I': {'J': 6, 'K': 4, 'L': 4},
        'J': {'I': 6, 'K': 4, 'L': 4},
        'K': {'E': 5, 'I': 4, 'J': 4},
        'L': {'C': 2, 'I': 4, 'J': 4}
    }
    start_1, end_1 = 'S', 'E'  
    
    graph_2 = {
        'A': {'B': 2, 'D': 8},
        'B': {'A': 2, 'D': 5, 'E': 6},
        'C': {'E': 9, 'F': 3},
        'D': {'A': 8, 'B': 5, 'E': 3, 'F': 2},
        'E': {'C': 9, 'D': 3, 'F': 1},
        'F': {'D': 2, 'C': 3, 'E': 1}
    }
    start_2, end_2 = 'A', 'C'
        
            
    if run_choice == 4:
        dijkstra(graph_1, start_1, end_1)
    
    if run_choice == 5:
        dijkstra(graph_2, start_2, end_2)
