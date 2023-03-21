import heapq

#here's an example of how to implement a uniform-cost search algorithm in Python using the heapq module

# define a function to perform uniform-cost search
def ucs(graph, start, goal):
    visited = set()  # create an empty set to keep track of visited nodes
    queue = [(0, start, [])]  # create a priority queue to keep track of nodes to be explored, along with their cost and path
    
    while queue:  # loop until the queue is empty
        cost, node, path = heapq.heappop(queue)  # get the next node, its cost, and its path from the queue
        if node not in visited:
            visited.add(node)  # mark the node as visited
            path = path + [node]  # add the node to the path
            if node == goal:
                return (cost, path)  # if the goal node is found, return its cost and path
            neighbors = graph[node]  # get the neighbors of the node
            for neighbor, neighbor_cost in neighbors.items():
                if neighbor not in visited:
                    total_cost = cost + neighbor_cost  # calculate the total cost of the neighbor node
                    heapq.heappush(queue, (total_cost, neighbor, path))  # add the neighbor to the queue, along with its cost and path
    
    return None  # if the goal node is not found, return None

#In this example, we define a function called ucs that takes three arguments: graph, which is a dictionary representing the graph we want to search, start, which is the starting node for the search, and goal, which is the goal node we want to find.
#The function uses a priority queue to keep track of nodes to be explored, along with their cost and path. The cost is used as the priority, so the priority queue always returns the node with the lowest cost. The heapq module is used to create and manipulate the priority queue.
#The while loop runs until the queue is empty. In each iteration of the loop, the function gets the next node, its cost, and its path from the priority queue using the heappop method, checks if the node has been visited before, adds the node to the visited set if it hasn't been visited before, adds the node to the path, checks if the node is the goal node, and gets the neighbors of the node using the graph dictionary. For each neighbor, the function calculates the total cost of the neighbor node, adds the neighbor to the priority queue, along with its cost and path.

#If the goal node is found, the function returns its cost and path. If the goal node is not found, the function returns None.
