# LeetCode 1923: Longest Common Subpath

**LeetCode Problem #1923 — Longest Common Subpath**
Solve LeetCode Longest Common Subpath using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Subpath |
| LeetCode | #1923 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a country of `n` cities numbered from `0` to `n - 1`. In this country, there is a road connecting every pair of cities.

There are `m` friends numbered from `0` to `m - 1` who are traveling through the country. Each one of them will take a path consisting of some cities. Each path is represented by an integer array that contains the visited cities in order. The path may contain a city **more than once**, but the same city will not be listed consecutively.

Given an integer `n` and a 2D integer array `paths` where `paths[i]` is an integer array representing the path of the `i^th` friend, return *the length of the **longest common subpath** that is shared by **every** friend's path, or *`0`* if there is no common subpath at all*.

A **subpath** of a path is a contiguous sequence of cities within that path.

## Constraints
- `1 <= n <= 10^5`
- `m == paths.length`
- `2 <= m <= 10^5`
- `sum(paths[i].length) <= 10^5`
- `0 <= paths[i][j] < n`
- The same city is not listed multiple times consecutively in `paths[i]`.

## Examples
### Example 1
- **Input:** `n = 5, paths = [[0,1, 2,3 ,4],
 [ 2,3 ,4],
 [4,0,1, 2,3 ]]`
- **Output:** `2`
- **Explanation:** The longest common subpath is [2,3].

### Example 2
- **Input:** `n = 3, paths = [[0],[1],[2]]`
- **Output:** `0`
- **Explanation:** There is no common subpath shared by the three paths.

### Example 3
- **Input:** `n = 5, paths = [[ 0 ,1,2,3,4],
 [4,3,2,1, 0 ]]`
- **Output:** `1`
- **Explanation:** The possible longest common subpaths are [0], [1], [2], [3], and [4]. All have a length of 1.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Common Subpath**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5, paths = [[0,1, 2,3 ,4],
 [ 2,3 ,4],
 [4,0,1, 2,3 ]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The longest common subpath is [2,3].

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
import random
from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        MOD = (1 << 61) - 1
        BASE = random.randrange(10**6, MOD - 1)

        def common(L: int) -> bool:
            top = pow(BASE, L, MOD)          # BASE^L, to remove the outgoing element
            cur = None
            for p in paths:
                if len(p) < L:
                    return False
                h = 0
                for i in range(L):
                    h = (h * BASE + p[i] + 1) % MOD
                hashes = {h}
                for i in range(L, len(p)):
                    h = (h * BASE + p[i] + 1 - (p[i - L] + 1) * top) % MOD
                    hashes.add(h)
                cur = hashes if cur is None else (cur & hashes)
                if not cur:
                    return False
            return True

        lo, hi = 0, min(len(p) for p in paths)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if common(mid):
                lo = mid
            else:
                hi = mid - 1
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
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [1143. Longest Common Subsequence](../../1001-1500/1250-longest-common-subsequence/)
- [3043. Find the Length of the Longest Common Prefix](../../3001-3500/3329-find-the-length-of-the-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-subpath/)
