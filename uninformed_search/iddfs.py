# define a function to perform iterative deepening depth-first search
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()  # create an empty set to keep track of visited nodes
        stack = [(start, 0)]  # create a stack to keep track of nodes to be explored, along with their depth
        
        while stack:  # loop until the stack is empty
            node, node_depth = stack.pop()  # get the next node and its depth from the stack
            if node not in visited and node_depth <= depth:
                visited.add(node)  # mark the node as visited
                if node == goal:
                    return True  # if the goal node is found, return True
                neighbors = graph[node]  # get the neighbors of the node
                for neighbor in neighbors:
                    stack.append((neighbor, node_depth + 1))  # add the neighbors to the stack, along with their depth
        
    return False  # if the goal node is not found within the max depth, return False

#In this example, we define a function called iddfs that takes four arguments: graph, which is a dictionary representing the graph we want to search, start, which is the starting node for the search, goal, which is the goal node we want to find, and max_depth, which is the maximum depth to explore.
#The function uses a loop to gradually increase the depth of the search until the maximum depth is reached. For each depth, the function creates an empty set called visited to keep track of visited nodes, and a stack called stack to keep track of nodes to be explored, along with their depth.

#The while loop runs until the stack is empty. In each iteration of the loop, the function gets the next node and its depth from the stack using the pop method, checks if the node has been visited before and whether its depth is within the current maximum depth, adds the node to the visited set if it hasn't been visited before, checks if the node is the goal node, and gets the neighbors of the node using the graph dictionary. If the goal node is found, the function returns True. If the goal node is not found within the current maximum depth, the function increases the depth and starts again with a new visited set and stack.
#Finally, if the goal node is not found within the maximum depth, the function returns False.