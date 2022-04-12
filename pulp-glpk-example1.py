from enum import Enum
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpConstraint
from pulp import GLPK


class VarCategory(Enum):
    CONTINUOUS = "Continuous"
    INTEGER = "Integer"
    BINARY = "Binary"


def main():
    # Create the model
    model = LpProblem(name="small-problem", sense=LpMaximize)

    # Initialize the decision variables
    x = LpVariable(name="x", lowBound=0, cat=VarCategory.INTEGER.value)
    y = LpVariable(name="y", lowBound=0)

    # Add the constraints to the model
    model += (2 * x + y <= 20, "red_constraint")
    model += (4 * x - 5 * y >= -10, "blue_constraint")
    model += (-x + 2 * y >= -2, "yellow_constraint")
    model += (-x + 5 * y == 15, "green_constraint")

    # Add the objective function to the model
    model += lpSum([x, 2 * y])
    model: LpProblem
    print(model)

    # Solve the problem
    status = model.solve(solver=GLPK(msg=True))

    print(f"status: {model.status}, {LpStatus[model.status]}")

    print(f"objective: {model.objective.value()}")

    for var in model.variables():
        var: LpVariable
        print(f"{var.name}: {var.value()}")

    for name, constraint in model.constraints.items():
        name: str
        constraint: LpConstraint
        print(f"{name}: {constraint.value()}")

    print(f"Sover used: {model.solver}")


if __name__ == '__main__':
    main()
