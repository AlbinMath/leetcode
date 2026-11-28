# LeetCode 826: Most Profit Assigning Work

**LeetCode Problem #826 — Most Profit Assigning Work**
Solve LeetCode Most Profit Assigning Work using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Profit Assigning Work |
| LeetCode | #826 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have `n` jobs and `m` workers. You are given three arrays: `difficulty`, `profit`, and `worker` where:

`difficulty[i]` and `profit[i]` are the difficulty and the profit of the `i^th` job, and 
 `worker[j]` is the ability of `j^th` worker (i.e., the `j^th` worker can only complete a job with difficulty at most `worker[j]`).

Every worker can be assigned **at most one job**, but one job can be **completed multiple times**.

For example, if three workers attempt the same job that pays `$1`, then the total profit will be `$3`. If a worker cannot complete any job, their profit is `$0`.

Return the maximum profit we can achieve after assigning the workers to the jobs.

## Constraints
- `n == difficulty.length`
- `n == profit.length`
- `m == worker.length`
- `1 <= n, m <= 10^4`
- `1 <= difficulty[i], profit[i], worker[i] <= 10^5`

## Examples
### Example 1
- **Input:** `difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]`
- **Output:** `100`
- **Explanation:** Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

### Example 2
- **Input:** `difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]`
- **Output:** `0`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Most Profit Assigning Work**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `100`.
4. **Verification:** Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

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
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        i, best, total = 0, 0, 0
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            total += best

        return total
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
- [1953. Maximum Number of Weeks for Which You Can Work](../../1501-2000/1953-maximum-number-of-weeks-for-which-you-can-work/)
- [1986. Minimum Number of Work Sessions to Finish the Tasks](../../1501-2000/1986-minimum-number-of-work-sessions-to-finish-the-tasks/)
- [11. Container With Most Water](../../0001-0500/0011-container-with-most-water/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-profit-assigning-work/)
