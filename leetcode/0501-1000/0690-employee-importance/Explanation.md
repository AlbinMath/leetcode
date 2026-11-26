# LeetCode 690: Employee Importance

**LeetCode Problem #690 — Employee Importance**
Solve LeetCode Employee Importance using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Employee Importance |
| LeetCode | #690 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees `employees` where:

`employees[i].id` is the ID of the `i^th` employee. 
 `employees[i].importance` is the importance value of the `i^th` employee. 
 `employees[i].subordinates` is a list of the IDs of the direct subordinates of the `i^th` employee.

Given an integer `id` that represents an employee's ID, return *the **total** importance value of this employee and all their direct and indirect subordinates*.

## Constraints
- `1 <= employees.length <= 2000`
- `1 <= employees[i].id <= 2000`
- All `employees[i].id` are **unique**.
- `-100 <= employees[i].importance <= 100`
- One employee has at most one direct leader and may have several subordinates.
- The IDs in `employees[i].subordinates` are valid IDs.

## Examples
### Example 1
- **Input:** `employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1`
- **Output:** `11`
- **Explanation:** Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

### Example 2
- **Input:** `employees = [[1,2,[5]],[5,-3,[]]], id = 5`
- **Output:** `-3`
- **Explanation:** Employee 5 has an importance value of -3 and has no direct subordinates.
Thus, the total importance value of employee 5 is -3.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Employee Importance**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def getImportance(self, employees, id):
        emp = {e.id: e for e in employees}

        def dfs(i):
            e = emp[i]
            return e.importance + sum(dfs(s) for s in e.subordinates)

        return dfs(id)
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2285. Maximum Total Importance of Roads](../../2001-2500/2285-maximum-total-importance-of-roads/)
- [577. Employee Bonus](../../0501-1000/0577-employee-bonus/)
- [1378. Replace Employee ID With The Unique Identifier](../../1001-1500/1378-replace-employee-id-with-the-unique-identifier/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/employee-importance/)
