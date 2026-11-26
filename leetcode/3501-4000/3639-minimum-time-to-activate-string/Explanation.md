# LeetCode 3639: Minimum Time to Activate String

**LeetCode Problem #3639 — Minimum Time to Activate String**
Solve LeetCode Minimum Time to Activate String using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Activate String |
| LeetCode | #3639 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` of length `n` and an integer array `order`, where `order` is a ** permutation ** of the numbers in the range `[0, n - 1]`.

Starting from time `t = 0`, replace the character at index `order[t]` in `s` with `'*'` at each time step.

A ** substring ** is **valid** if it contains **at least** one `'*'`.

A string is **active** if the total number of **valid** substrings is greater than or equal to `k`.

Return the **minimum** time `t` at which the string `s` becomes **active**. If it is impossible, return -1.

## Constraints
- `1 <= n == s.length <= 10^5`
- `order.length == n`
- `0 <= order[i] <= n - 1`
- `s` consists of lowercase English letters.
- `order` is a permutation of integers from 0 to `n - 1`.
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `s = "abc", order = [1,0,2], k = 2`
- **Output:** `0`
- **Explanation:** `t` 
 `order[t]` 
 Modified `s` 
 Valid Substrings 
 Count 
 Active 
 (Count >= k) 
 
 
 
 
 0 
 1 
 `"a*c"` 
 `"*"`, `"a*"`, `"*c"`, `"a*c"` 
 4 
 Yes 
 
 
 

 The string `s` becomes active at `t = 0`. Thus, the answer is 0.

### Example 2
- **Input:** `s = "cat", order = [0,2,1], k = 6`
- **Output:** `2`
- **Explanation:** `t` 
 `order[t]` 
 Modified `s` 
 Valid Substrings 
 Count 
 Active 
 (Count >= k) 
 
 
 
 
 0 
 0 
 `"*at"` 
 `"*"`, `"*a"`, `"*at"` 
 3 
 No 
 
 
 1 
 2 
 `"*a*"` 
 `"*"`, `"*a"`, `" *a*"` , `" a*"` , `"*"` 
 5 
 No 
 
 
 2 
 1 
 `"***"` 
 All substrings (contain `'*'`) 
 6 
 Yes 
 
 
 

 The string `s` becomes active at `t = 2`. Thus, the answer is 2.

### Example 3
- **Input:** `s = "xy", order = [0,1], k = 4`
- **Output:** `-1`
- **Explanation:** Even after all replacements, it is impossible to obtain `k = 4` valid substrings. Thus, the answer is -1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Activate String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc", order = [1,0,2], k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** `t` 
 `order[t]` 
 Modified `s` 
 Valid Substrings 
 Count 
 Active 
 (Count >= k) 
 
 
 
 
 0 
 1 
 `"a*c"` 
 `"*"`, `"a*"`, `"*c"`, `"a*c"` 
 4 
 Yes 
 
 
 

 The string `s` becomes active at `t = 0`. Thus, the answer is 0.

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
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        total = n * (n + 1) // 2
        if total < k:
            return -1

        def ok(t: int) -> bool:
            star = [False] * n
            for i in range(t + 1):
                star[order[i]] = True
            bad = 0
            run = 0
            for i in range(n):
                if star[i]:
                    bad += run * (run + 1) // 2
                    run = 0
                else:
                    run += 1
            bad += run * (run + 1) // 2
            return total - bad >= k

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
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
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-activate-string/)
