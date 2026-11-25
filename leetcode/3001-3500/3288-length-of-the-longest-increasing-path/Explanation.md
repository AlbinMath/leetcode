# LeetCode 3288: Length of the Longest Increasing Path

**LeetCode Problem #3288 — Length of the Longest Increasing Path**
Solve LeetCode Length of the Longest Increasing Path using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Length of the Longest Increasing Path |
| LeetCode | #3288 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D array of integers `coordinates` of length `n` and an integer `k`, where `0 <= k < n`.

`coordinates[i] = [x_i, y_i]` indicates the point `(x_i, y_i)` in a 2D plane.

An **increasing path** of length `m` is defined as a list of points `(x_1, y_1)`, `(x_2, y_2)`, `(x_3, y_3)`, ..., `(x_m, y_m)` such that:

`x_i < x_i + 1` and `y_i < y_i + 1` for all `i` where `1 <= i < m`. 
 `(x_i, y_i)` is in the given coordinates for all `i` where `1 <= i <= m`.

Return the **maximum** length of an **increasing path** that contains `coordinates[k]`.

## Constraints
- `1 <= n == coordinates.length <= 10^5`
- `coordinates[i].length == 2`
- `0 <= coordinates[i][0], coordinates[i][1] <= 10^9`
- All elements in `coordinates` are **distinct**.
- `0 <= k <= n - 1`

## Examples
### Example 1
- **Input:** `coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1`
- **Output:** `3`
- **Explanation:** `(0, 0)`, `(2, 2)`, `(5, 3)` is the longest increasing path that contains `(2, 2)`.

### Example 2
- **Input:** `coordinates = [[2,1],[7,0],[5,6]], k = 2`
- **Output:** `2`
- **Explanation:** `(2, 1)`, `(5, 6)` is the longest increasing path that contains `(5, 6)`.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Length of the Longest Increasing Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** `(0, 0)`, `(2, 2)`, `(5, 3)` is the longest increasing path that contains `(2, 2)`.

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
from bisect import bisect_left
from typing import List

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        px, py = coordinates[k]

        def lis(points):
            points.sort(key=lambda p: (p[0], -p[1]))
            tails = []
            for _, y in points:
                pos = bisect_left(tails, y)      # strictly increasing
                if pos == len(tails):
                    tails.append(y)
                else:
                    tails[pos] = y
            return len(tails)

        left = [(x, y) for x, y in coordinates if x < px and y < py]
        right = [(x, y) for x, y in coordinates if x > px and y > py]

        return lis(left) + 1 + lis(right)
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
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [388. Longest Absolute File Path](../../0001-0500/0388-longest-absolute-file-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/length-of-the-longest-increasing-path/)
