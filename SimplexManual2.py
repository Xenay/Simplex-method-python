import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

obj_func = [-6, -7, 0, 0, 0, 1, 0]

lhs = [[7, 6, 1, 0, 0, 0],
       [5, 9, 0, 1, 0, 0],
       [1, -1, 0, 0, 1, 0]]

rhs = [42, 45, 4]

bounds = [(-np.inf, np.inf), (-np.inf, np.inf)]


def plot_constraints(x_values):
    x = np.linspace(-10, 10, 400)
    y1 = (42 - 7 * x) / 6
    y2 = (45 - 5 * x) / 9
    y3 = x - 4

    plt.plot(x, y1, label='7x + 6y ≤ 42')
    plt.plot(x, y2, label='5x + 9y ≤ 45')
    plt.plot(x, y3, label='x − y ≤ 4')

    plt.plot([0, 5], [0, 0], 'r--', alpha=0.1)
    plt.plot([0, 0], [0, 4], 'r--', alpha=0.1)

    plt.fill_between(x, y1, where=(y1 <= y2) & (y1 >= y3), color='gray', alpha=0.5)
    plt.fill_between(x, y2, where=(y2 <= y1) & (y2 >= y3), color='gray', alpha=0.5)
    plt.fill_between(x, y3, where=(y3 < y1), color='gray', alpha=0.5)

    plt.plot(x_values[0], x_values[1], 'ro', label='Optimized x', markersize=5)

    plt.xlim((-10, 10))
    plt.ylim((-10, 10))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Simplex plot')
    plt.legend()
    plt.grid(True)
    plt.show()


def Calculate(obj_func, lhs, rhs):
    nit = 1
    np.set_printoptions(precision=2, suppress=True)
    table = np.column_stack((lhs, rhs)).astype(float)
    # print
    print("Table Start: ----------------------------")
    print(table)
    print(obj_func)

    while True:
        ratios = []
        pivot_col = np.argmin(obj_func)
        ratios = table[:, -1] / table[:, pivot_col]
        ratios[ratios < 0] = np.inf
        pivot_row = np.argmin(ratios)

        if all(x >= 0 for x in obj_func[:-2]):
            break

        pivot = table[pivot_row, pivot_col]
        print("pivot je: ", table[pivot_row, pivot_col])
        table[pivot_row, :] /= pivot

        for i in range(table.shape[0]):
            if i == pivot_row:
                continue
            ratio = table[i, pivot_col]
            table[i, :] -= ratio * table[pivot_col, :]
            ratio_obj = obj_func[pivot_col]
            obj_func -= ratio_obj * table[pivot_col, :]
        # print
        print("Iteration num: " + str(nit) + "---------------------------------------------")
        print(table)
        print(obj_func)
        nit = nit + 1

    # Extract the optimal value and decision variables
    fun = obj_func[-1]
    x = table[:-1, -1]

    # Print the additional information

    print("Optimal solution:")
    print("fun =", fun)
    print("x =", x)
    print("nit =", nit)
    print(table)
    print(obj_func)
    plot_constraints([x[0], x[1]])


Calculate(obj_func, lhs, rhs)
