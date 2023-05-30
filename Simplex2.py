from scipy.optimize import linprog
import numpy as np

# Min to max = obj_func * -1
obj_func = [-6, -7]

lhs = [[7, 6],
       [5, 9],
       [1, -1]]

rhs = [42, 45, 4]

# bounds = [(0, None), (0, None)]
bounds = [(-np.inf, np.inf), (-np.inf, np.inf)]

result = linprog(c=obj_func, A_ub=lhs, b_ub=rhs, bounds=bounds, method='simplex')

print(result)

