# LeetCode 3482: Analyze Organization Hierarchy

**LeetCode Problem #3482 — Analyze Organization Hierarchy**
Solve LeetCode Analyze Organization Hierarchy using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Analyze Organization Hierarchy |
| LeetCode | #3482 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Table: `Employees`

+----------------+---------+
| Column Name | Type | 
+----------------+---------+
| employee_id | int |
| employee_name | varchar |
| manager_id | int |
| salary | int |
| department | varchar |
+----------------+----------+
employee_id is the unique key for this table.
Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department.
manager_id is null for the top-level manager (CEO).

Write a solution to analyze the organizational hierarchy and answer the following:

**Hierarchy Levels:** For each employee, determine their level in the organization (CEO is level `1`, employees reporting directly to the CEO are level `2`, and so on). 
 **Team Size:** For each employee who is a manager, count the total number of employees under them (direct and indirect reports). 
 **Salary Budget:** For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).

Return *the result table ordered by the result ordered by **level** in **ascending** order, then by **budget** in **descending** order, and finally by **employee_name** in **ascending** order*.

*The result format is in the following example.*

## Examples
Consider the standard input for **Analyze Organization Hierarchy**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Analyze Organization Hierarchy**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Complement Lookup / Hash Table Frequency** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [3497. Analyze Subscription Conversion ](../../3001-3500/3497-analyze-subscription-conversion/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/analyze-organization-hierarchy/)
