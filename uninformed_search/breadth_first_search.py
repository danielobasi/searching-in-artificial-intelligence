from dataset import graph

visited = [] # List of visisted nodes
queue = []  # Initialize a queue

def bfs(visited,graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end =" ")
       

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    #print(visited)

bfs(visited,graph,'B')