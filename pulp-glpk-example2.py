from enum import Enum
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpConstraint
from pulp import GLPK


class VarCategory(Enum):
    CONTINUOUS = "Continuous"
    INTEGER = "Integer"
    BINARY = "Binary"


def main():
    # Create the model
    model = LpProblem(name="resource-allocation", sense=LpMaximize)

    # Define the decision variables
    x = {i: LpVariable(name=f"x_{i}", lowBound=0) for i in range(1, 5)}
    y = {i: LpVariable(name=f"y{i}", cat=VarCategory.BINARY.value)
         for i in (1, 3)}

    # Add constraints
    model += (lpSum(x.values()) <= 50, "manpower")
    model += (3 * x[1] + 2 * x[2] + x[3] <= 100, "material_a")
    model += (x[2] + 2 * x[3] + 3 * x[4] <= 90, "material_b")

    BIG_M = 100
    model += (x[1] <= y[1] * BIG_M, "x1_constraint")
    model += (x[3] <= y[3] * BIG_M, "x3_constraint")
    model += (y[1] + y[3] <= 1, "y_constraint")

    # Set the objective
    model += 20 * x[1] + 12 * x[2] + 40 * x[3] + 25 * x[4]
    model: LpProblem
    print(model)

    # Solve the optimization problem
    status = model.solve(solver=GLPK())

    # Get the results
    print(f"status: {model.status}, {LpStatus[model.status]}")
    print(f"objective: {model.objective.value()}")

    for var in x.values():
        print(f"{var.name}: {var.value()}")

    for name, constraint in model.constraints.items():
        constraint: LpConstraint
        print(f"{name}: {constraint.value()}")

    print(f"Sover used: {model.solver}")


if __name__ == '__main__':
    main()
