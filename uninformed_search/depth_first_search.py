# define a function to perform depth-first search
def dfs(graph, start):
    visited = set()  # create an empty set to keep track of visited nodes
    stack = [start]  # create a stack to keep track of nodes to be explored
    
    while stack:  # loop until the stack is empty
        node = stack.pop()  # get the next node from the stack
        if node not in visited:
            visited.add(node)  # mark the node as visited
            neighbors = graph[node]  # get the neighbors of the node
            stack.extend(neighbors)  # add the neighbors to the stack
    
    return visited

#In this example, i define a function called dfs that takes two arguments: graph, which is a dictionary representing the graph we want to search, and start, which is the starting node for the search.
#The function creates an empty set called visited to keep track of visited nodes, and a stack called stack to keep track of nodes to be explored. The while loop runs until the stack is empty. In each iteration of the loop, the function gets the next node from the stack using the pop method, checks if the node has been visited before using the visited set, adds the node to the visited set if it hasn't been visited before, gets the neighbors of the node using the graph dictionary, and adds the neighbors to the stack using the extend method.
#Finally, the function returns the visited set, which contains all the nodes that were visited during the search.

#Run function
from dataset import graph
print(dfs(graph,'A'))