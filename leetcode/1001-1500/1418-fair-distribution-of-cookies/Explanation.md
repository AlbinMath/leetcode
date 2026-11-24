# LeetCode 2305: Fair Distribution of Cookies

**LeetCode Problem #2305 — Fair Distribution of Cookies**
Solve LeetCode Fair Distribution of Cookies using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fair Distribution of Cookies |
| LeetCode | #2305 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the `i^th` bag. You are also given an integer `k` that denotes the number of children to distribute **all** the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The **unfairness** of a distribution is defined as the **maximum** **total** cookies obtained by a single child in the distribution.

Return *the **minimum** unfairness of all distributions*.

## Constraints
- `2 <= cookies.length <= 8`
- `1 <= cookies[i] <= 10^5`
- `2 <= k <= cookies.length`

## Examples
### Example 1
- **Input:** `cookies = [8,15,10,20,8], k = 2`
- **Output:** `31`
- **Explanation:** One optimal distribution is [8,15,8] and [10,20]
- The 1^st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2^nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

### Example 2
- **Input:** `cookies = [6,1,3,2,2,4,1,2], k = 3`
- **Output:** `7`
- **Explanation:** One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1^st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2^nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3^rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fair Distribution of Cookies**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cookies = [8,15,10,20,8], k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `31`.
4. **Verification:** One optimal distribution is [8,15,8] and [10,20]
- The 1^st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2^nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.

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
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)  # big bags first prunes faster
        loads = [0] * k
        best = float('inf')

        def dfs(i: int) -> None:
            nonlocal best
            if i == len(cookies):
                best = min(best, max(loads))
                return
            seen = set()
            for c in range(k):
                if loads[c] in seen:
                    continue  # symmetric to an earlier child
                if loads[c] + cookies[i] >= best:
                    continue  # can't improve
                seen.add(loads[c])
                loads[c] += cookies[i]
                dfs(i + 1)
                loads[c] -= cookies[i]

        dfs(0)
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
- [455. Assign Cookies](../../0001-0500/0455-assign-cookies/)
- [888. Fair Candy Swap](../../0501-1000/0924-fair-candy-swap/)
- [1664. Ways to Make a Fair Array](../../1501-2000/1783-ways-to-make-a-fair-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fair-distribution-of-cookies/)
