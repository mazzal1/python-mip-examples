from scipy.optimize import linprog
from numpy import inf
from collections import namedtuple


OptimizationMethods = namedtuple(
    "OptimizationMethods", ("simplex", "revised_simplex", "interior_point"))
methods = OptimizationMethods("simplex", "revised simplex", "interior-point")


def main():
    objective_function = [-20, -12, -40, -25]

    left_hand_side_inequalities = [
        [1, 1, 1, 1],  # Manpower
        [3, 2, 1, 0],  # Material A
        [0, 1, 2, 3]  # Material B
    ]

    right_hand_side_inequalities = [
        50,  # Manpower
        100,  # Material A
        90  # Material B
    ]

    optimization_result = linprog(c=objective_function,
                                  A_ub=left_hand_side_inequalities,
                                  b_ub=right_hand_side_inequalities,
                                  method=methods.revised_simplex)

    print(optimization_result)


if __name__ == '__main__':
    main()
