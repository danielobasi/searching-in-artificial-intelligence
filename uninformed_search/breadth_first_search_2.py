from collections import deque
from dataset import graph

# define a function to perform breadth-first search
def bfs(graph, start):
    visited = set()  # create an empty set to keep track of visited nodes
    queue = deque([start])  # create a deque to keep track of nodes to be explored
    
    while queue:  # loop until the queue is empty
        node = queue.popleft()  # get the next node from the queue
        if node not in visited:
            visited.add(node)  # mark the node as visited
            neighbors = graph[node]  # get the neighbors of the node
            queue.extend(neighbors)  # add the neighbors to the queue
    
    return visited
#In this example, I define a function called bfs that takes two arguments: graph, which is a dictionary representing the graph we want to search, and start, which is the starting node for the search.
#The function creates an empty set called visited to keep track of visited nodes, and a deque called queue to keep track of nodes to be explored. The while loop runs until the queue is empty. In each iteration of the loop, the function gets the next node from the queue using the popleft method, checks if the node has been visited before using the visited set, adds the node to the visited set if it hasn't been visited before, gets the neighbors of the node using the graph dictionary, and adds the neighbors to the queue using the extend method.
#Finally, the function returns the visited set, which contains all the nodes that were visited during the search
print(bfs(graph,'A'))