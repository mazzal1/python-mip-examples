from enum import Enum
from scipy.optimize import linprog
from numpy import inf


class PulpMethod(Enum):
    SIMPLEX = "simplex"
    REVISED_SIMPLEX = "revised simplex"
    INTERIOR_POINT = "interior-point"


def main():
    objective_function = [-1, -2]

    left_hand_side_inequalities = [
        [2, 1],
        [-4, 5],
        [1, -2]
    ]
    right_hand_side_inequalities = [
        20,
        10,
        2
    ]

    left_hand_side_equalities = [
        [-1, 5]
    ]
    right_hand_side_equalities = [15]

    bounds = [
        (0, inf),  # 0 <= x < +inf
        (0, inf)
    ]  # (default bounds)

    optimization_result = linprog(c=objective_function,
                                  A_ub=left_hand_side_inequalities,
                                  b_ub=right_hand_side_inequalities,
                                  A_eq=left_hand_side_equalities,
                                  b_eq=right_hand_side_equalities,
                                  bounds=bounds,
                                  method=PulpMethod.REVISED_SIMPLEX.value)

    print(optimization_result)


if __name__ == '__main__':
    main()
