# LeetCode 1491: Average Salary Excluding the Minimum and Maximum Salary

**LeetCode Problem #1491 — Average Salary Excluding the Minimum and Maximum Salary**
Solve LeetCode Average Salary Excluding the Minimum and Maximum Salary using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Average Salary Excluding the Minimum and Maximum Salary |
| LeetCode | #1491 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of **unique** integers `salary` where `salary[i]` is the salary of the `i^th` employee.

Return *the average salary of employees excluding the minimum and maximum salary*. Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `3 <= salary.length <= 100`
- `1000 <= salary[i] <= 10^6`
- All the integers of `salary` are **unique**.

## Examples
### Example 1
- **Input:** `salary = [4000,3000,1000,2000]`
- **Output:** `2500.00000`
- **Explanation:** Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

### Example 2
- **Input:** `salary = [1000,2000,3000]`
- **Output:** `2000.00000`
- **Explanation:** Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Average Salary Excluding the Minimum and Maximum Salary**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `salary = [4000,3000,1000,2000]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2500.00000`.
4. **Verification:** Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def average(self, salary: list[int]) -> float:
        total = sum(salary)
        minimum = min(salary)
        maximum = max(salary)

        return (total - minimum - maximum) / (len(salary) - 2)
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2058. Find the Minimum and Maximum Number of Nodes Between Critical Points](../../2001-2500/2058-find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2091-removing-minimum-and-maximum-from-array/)
- [3428. Maximum and Minimum Sums of at Most Size K Subsequences](../../3001-3500/3428-maximum-and-minimum-sums-of-at-most-size-k-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)
