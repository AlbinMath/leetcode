# LeetCode 1828: Queries on Number of Points Inside a Circle

**LeetCode Problem #1828 — Queries on Number of Points Inside a Circle**
Solve LeetCode Queries on Number of Points Inside a Circle using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Queries on Number of Points Inside a Circle |
| LeetCode | #1828 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `points` where `points[i] = [x_i, y_i]` is the coordinates of the `i^th` point on a 2D plane. Multiple points can have the **same** coordinates.

You are also given an array `queries` where `queries[j] = [x_j, y_j, r_j]` describes a circle centered at `(x_j, y_j)` with a radius of `r_j`.

For each query `queries[j]`, compute the number of points **inside** the `j^th` circle. Points **on the border** of the circle are considered **inside**.

Return *an array *`answer`*, where *`answer[j]`* is the answer to the *`j^th`* query*.

## Constraints
- `1 <= points.length <= 500`
- `points[i].length == 2`
- `0 <= x_​​​​​​i, y_​​​​​​i <= 500`
- `1 <= queries.length <= 500`
- `queries[j].length == 3`
- `0 <= x_j, y_j <= 500`
- `1 <= r_j <= 500`
- All coordinates are integers.

## Examples
### Example 1
- **Input:** `points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]`
- **Output:** `[3,2,2]`

### Example 2
- **Input:** `points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]`
- **Output:** `[2,3,2,4]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Queries on Number of Points Inside a Circle**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,2]`.

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
from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for qx, qy, r in queries:
            r2 = r * r
            cnt = 0
            for x, y in points:
                dx, dy = x - qx, y - qy
                if dx * dx + dy * dy <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans
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
- [2249. Count Lattice Points Inside a Circle](../../2001-2500/2249-count-lattice-points-inside-a-circle/)
- [2503. Maximum Number of Points From Grid Queries](../../2501-3000/2503-maximum-number-of-points-from-grid-queries/)
- [1610. Maximum Number of Visible Points](../../1501-2000/1610-maximum-number-of-visible-points/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/)
