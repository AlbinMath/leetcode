# LeetCode 3288: Length of the Longest Increasing Path

**LeetCode Problem #3288 — Length of the Longest Increasing Path**
Solve LeetCode Length of the Longest Increasing Path using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Length of the Longest Increasing Path |
| LeetCode | #3288 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

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
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Length of the Longest Increasing Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** `(0, 0)`, `(2, 2)`, `(5, 3)` is the longest increasing path that contains `(2, 2)`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

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
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)
- [2781. Length of the Longest Valid Substring](../../2501-3000/2781-length-of-the-longest-valid-substring/)
- [2790. Maximum Number of Groups With Increasing Length](../../2501-3000/2790-maximum-number-of-groups-with-increasing-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/length-of-the-longest-increasing-path/)
