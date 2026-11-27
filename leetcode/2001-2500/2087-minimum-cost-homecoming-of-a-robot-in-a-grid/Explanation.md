# LeetCode 2087: Minimum Cost Homecoming of a Robot in a Grid

**LeetCode Problem #2087 — Minimum Cost Homecoming of a Robot in a Grid**
Solve LeetCode Minimum Cost Homecoming of a Robot in a Grid using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost Homecoming of a Robot in a Grid |
| LeetCode | #2087 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an `m x n` grid, where `(0, 0)` is the top-left cell and `(m - 1, n - 1)` is the bottom-right cell. You are given an integer array `startPos` where `startPos = [start_row, start_col]` indicates that **initially**, a **robot** is at the cell `(start_row, start_col)`. You are also given an integer array `homePos` where `homePos = [home_row, home_col]` indicates that its **home** is at the cell `(home_row, home_col)`.

The robot needs to go to its home. It can move one cell in four directions: **left**, **right**, **up**, or **down**, and it can not move outside the boundary. Every move incurs some cost. You are further given two **0-indexed** integer arrays: `rowCosts` of length `m` and `colCosts` of length `n`.

If the robot moves **up** or **down** into a cell whose **row** is `r`, then this move costs `rowCosts[r]`. 
 If the robot moves **left** or **right** into a cell whose **column** is `c`, then this move costs `colCosts[c]`.

Return *the **minimum total cost** for this robot to return home*.

## Constraints
- `m == rowCosts.length`
- `n == colCosts.length`
- `1 <= m, n <= 10^5`
- `0 <= rowCosts[r], colCosts[c] <= 10^4`
- `startPos.length == 2`
- `homePos.length == 2`
- `0 <= start_row, home_row < m`
- `0 <= start_col, home_col < n`

## Examples
### Example 1
- **Input:** `startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]`
- **Output:** `18`
- **Explanation:** One optimal path is that:
Starting from (1, 0)
-> It goes down to (

### Example 2
- **Input:** `startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]`
- **Output:** `0`
- **Explanation:** The robot is already at its home. Since no moves occur, the total cost is 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Cost Homecoming of a Robot in a Grid**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** One optimal path is that:
Starting from (1, 0)
-> It goes down to (

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
    def minCost(self, startPos: List[int], homePos: List[int],
                rowCosts: List[int], colCosts: List[int]) -> int:
        sr, sc = startPos
        hr, hc = homePos
        total = 0
        if hr > sr:
            total += sum(rowCosts[sr + 1:hr + 1])
        elif hr < sr:
            total += sum(rowCosts[hr:sr])
        if hc > sc:
            total += sum(colCosts[sc + 1:hc + 1])
        elif hc < sc:
            total += sum(colCosts[hc:sc])
        return total
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
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)
- [2304. Minimum Path Cost in a Grid](../../2001-2500/2304-minimum-path-cost-in-a-grid/)
- [1536. Minimum Swaps to Arrange a Binary Grid](../../1501-2000/1536-minimum-swaps-to-arrange-a-binary-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/)
