from queue import PriorityQueue

def a_star(start, goal, graph, heuristic):
    """
    This function performs A* search to find the shortest path from the start node to the goal node in the given graph.
    """
    frontier = PriorityQueue()  # priority queue to store nodes to be explored
    frontier.put(start, 0)  # put the start node in the frontier with a priority of 0
    came_from = {}  # dictionary to store the path from each explored node to its parent
    cost_so_far = {start: 0}  # dictionary to store the cost of the path from the start node to each explored node

    while not frontier.empty():
        current = frontier.get()  # get the node with the lowest priority from the frontier
        if current == goal:
            break  # we have found the goal node, so exit the loop

        # loop through the neighbors of the current node
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)  # calculate the priority of the neighbor node
                frontier.put(neighbor, priority)  # add the neighbor node to the frontier with its priority
                came_from[neighbor] = current  # set the parent of the neighbor node to the current node

    # reconstruct the path from the start node to the goal node
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

# example usage
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'D': 3, 'E': 5},
    'C': {'A': 3, 'E': 2},
    'D': {'B': 3},
    'E': {'B': 5, 'C': 2, 'F': 4},
    'F': {'E': 4}
}

start = 'A'
goal = 'F'
heuristic = lambda a, b: 0  # zero heuristic (equivalent to Dijkstra's algorithm)
path = a_star(start, goal, graph, heuristic)
print("Shortest path from", start, "to", goal, ":", path)
