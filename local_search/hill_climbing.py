import numpy as np

def hill_climbing_search(problem, max_iterations=1000):
    """
    This function performs hill climbing search on a given problem.
    The problem is defined as a function that takes a state as input and returns its value.
    The function returns the best state found after a certain number of iterations.
    """
    current_state = problem.get_initial_state()
    for i in range(max_iterations):
        neighbors = problem.get_neighbors(current_state)
        neighbor_values = [problem.evaluate(state) for state in neighbors]
        best_neighbor_index = np.argmax(neighbor_values)
        if neighbor_values[best_neighbor_index] > problem.evaluate(current_state):
            current_state = neighbors[best_neighbor_index]
        else:
            break
    return current_state

# example usage
class Problem:
    def __init__(self):
        self.initial_state = np.array([0, 0])
    
    def get_initial_state(self):
        return self.initial_state
    
    def evaluate(self, state):
        x, y = state
        return -((x-2)**2 + (y-2)**2)
    
    def get_neighbors(self, state):
        x, y = state
        neighbors = [
            np.array([x+1, y]),
            np.array([x-1, y]),
            np.array([x, y+1]),
            np.array([x, y-1])
        ]
        return neighbors

problem = Problem()
best_state = hill_climbing_search(problem)
print("Best state found:", best_state)
