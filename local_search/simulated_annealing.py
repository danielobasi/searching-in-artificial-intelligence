import numpy as np

def simulated_annealing(start_state, cost_func, neighbor_func, temperature_func, max_iter):
    """
    This function finds the minimum cost state using the simulated annealing algorithm.
    The cost function and neighbor function are used to evaluate the cost of the current state and generate neighbor states.
    The temperature function is used to generate a decreasing sequence of temperatures.
    The max_iter parameter specifies the maximum number of iterations to run.
    """
    current_state = start_state
    current_cost = cost_func(current_state)
    best_state = current_state
    best_cost = current_cost
    t = 1
    while t < max_iter:
        # generate a new state by selecting a random neighbor
        neighbor_state = neighbor_func(current_state)
        neighbor_cost = cost_func(neighbor_state)
        # determine whether to accept the neighbor state based on the current temperature
        delta_cost = neighbor_cost - current_cost
        acceptance_prob = np.exp(-delta_cost / temperature_func(t))
        if acceptance_prob > np.random.rand():
            current_state = neighbor_state
            current_cost = neighbor_cost
        # update the best state if the current state has a lower cost
        if current_cost < best_cost:
            best_state = current_state
            best_cost = current_cost
        # decrease the temperature
        t += 1
    return best_state, best_cost

# example usage
def cost_func(state):
    # example cost function - returns the sum of squared values in the state
    return np.sum(state ** 2)

def neighbor_func(state):
    # example neighbor function - selects a random element in the state and perturbs its value
    neighbor_state = np.copy(state)
    idx = np.random.randint(len(state))
    neighbor_state[idx] += np.random.randn()
    return neighbor_state

def temperature_func(t):
    # example temperature function - returns a decreasing sequence of temperatures
    return 1.0 / np.log(t + 1)

start_state = np.random.randn(5)
best_state, best_cost = simulated_annealing(start_state, cost_func, neighbor_func, temperature_func, 10000)
print("Best state:", best_state)
print("Best cost:", best_cost)
