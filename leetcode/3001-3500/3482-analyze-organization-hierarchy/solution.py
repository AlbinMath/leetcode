import pandas as pd
from collections import defaultdict

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.copy()

    # Build manager -> employees mapping
    children = defaultdict(list)

    for _, row in employees.iterrows():
        children[row["manager_id"]].append(row["employee_id"])

    # Store employee information
    data = employees.set_index("employee_id").to_dict("index")

    result = {}

    def dfs(employee_id, level):
        employee = data[employee_id]

        team_size = 0
        budget = employee["salary"]

        for child_id in children[employee_id]:
            child_size, child_budget = dfs(child_id, level + 1)

            team_size += child_size + 1
            budget += child_budget

        result[employee_id] = {
            "level": level,
            "team_size": team_size,
            "budget": budget
        }

        return team_size, budget

    # Find CEO
    ceo = employees[employees["manager_id"].isna()].iloc[0]["employee_id"]

    # Calculate everything
    dfs(ceo, 1)

    # Create result
    employees["level"] = employees["employee_id"].map(
        lambda x: result[x]["level"]
    )

    employees["team_size"] = employees["employee_id"].map(
        lambda x: result[x]["team_size"]
    )

    employees["budget"] = employees["employee_id"].map(
        lambda x: result[x]["budget"]
    )

    # Required columns and ordering
    return employees[
        ["employee_id", "employee_name", "level", "team_size", "budget"]
    ].sort_values(
        ["level", "budget", "employee_name"],
        ascending=[True, False, True]
    ).reset_index(drop=True)
