from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpConstraint


def main():
    # Create the model
    model = LpProblem(name="small-problem", sense=LpMaximize)

    # Initialize the decision variables
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)
    print(f"Type of x variable = {type(x)}")

    expression = 2 * x + 4 * y
    print(f"Type of expression = {type(expression)}")

    constraint = 2 * x + 4 * y >= 8
    print(f"Type of constraint = {type(constraint)}")

    # Add the constraints to the model
    model += (2 * x + y <= 20, "red_constraint")
    model += (4 * x - 5 * y >= -10, "blue_constraint")
    model += (-x + 2 * y >= -2, "yellow_constraint")
    model += (-x + 5 * y == 15, "green_constraint")

    # Add the objective function to the model
    obj_func = x + 2 * y
    model += obj_func
    # Alternatives
    # model += x + 2 * y
    # model += lpSum([x, 2 * y])

    print(model)

    model: LpProblem
    # Solve the problem with default solver CBC
    status = model.solve()
    # status is 1 if the optimal solution is found

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
