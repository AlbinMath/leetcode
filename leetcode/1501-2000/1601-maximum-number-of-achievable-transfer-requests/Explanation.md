# LeetCode 1601: Maximum Number of Achievable Transfer Requests

**LeetCode Problem #1601 — Maximum Number of Achievable Transfer Requests**
Solve LeetCode Maximum Number of Achievable Transfer Requests using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Achievable Transfer Requests |
| LeetCode | #1601 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We have `n` buildings numbered from `0` to `n - 1`. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array `requests` where `requests[i] = [from_i, to_i]` represents an employee's request to transfer from building `from_i` to building `to_i`.

**All buildings are full**, so a list of requests is achievable only if for each building, the **net change in employee transfers is zero**. This means the number of employees **leaving** is **equal** to the number of employees **moving in**. For example if `n = 3` and two employees are leaving building `0`, one is leaving building `1`, and one is leaving building `2`, there should be two employees moving to building `0`, one employee moving to building `1`, and one employee moving to building `2`.

Return *the maximum number of achievable requests*.

## Constraints
- `1 <= n <= 20`
- `1 <= requests.length <= 16`
- `requests[i].length == 2`
- `0 <= from_i, to_i < n`

## Examples
### Example 1
- **Input:** `n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]`
- **Output:** `5`

### Example 2
- **Input:** `n = 3, requests = [[0,0],[1,2],[2,1]]`
- **Output:** `3`

### Example 3
- **Input:** `n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]`
- **Output:** `4`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Achievable Transfer Requests**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.

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
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        delta = [0] * n
        best = 0

        def dfs(i: int, chosen: int, nonzero: int) -> None:
            nonlocal best
            if chosen + (m - i) <= best:
                return  # even taking every remaining request can't beat best
            if i == m:
                if nonzero == 0:
                    best = chosen
                return

            f, t = requests[i]

            # take request i
            nz = nonzero
            if f != t:
                nz -= delta[f] != 0
                delta[f] -= 1
                nz += delta[f] != 0
                nz -= delta[t] != 0
                delta[t] += 1
                nz += delta[t] != 0
            dfs(i + 1, chosen + 1, nz)
            if f != t:
                delta[f] += 1
                delta[t] -= 1

            # skip request i
            dfs(i + 1, chosen, nonzero)

        dfs(0, 0, 0)
        return best
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
- [1606. Find Servers That Handled Most Number of Requests](../../1501-2000/1606-find-servers-that-handled-most-number-of-requests/)
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/)
