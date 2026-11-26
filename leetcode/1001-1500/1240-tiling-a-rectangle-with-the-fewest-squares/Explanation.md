# LeetCode 1240: Tiling a Rectangle with the Fewest Squares

**LeetCode Problem #1240 — Tiling a Rectangle with the Fewest Squares**
Solve LeetCode Tiling a Rectangle with the Fewest Squares using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tiling a Rectangle with the Fewest Squares |
| LeetCode | #1240 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a rectangle of size `n` x `m`, return *the minimum number of integer-sided squares that tile the rectangle*.

## Constraints
- `1 <= n, m <= 13`

## Examples
### Example 1
- **Input:** `n = 2, m = 3`
- **Output:** `3`
- **Explanation:** `3` squares are necessary to cover the rectangle.
`2` (squares of `1x1`)
`1` (square of `2x2`)

### Example 2
- **Input:** `n = 5, m = 8`
- **Output:** `5`

### Example 3
- **Input:** `n = 11, m = 13`
- **Output:** `6`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Tiling a Rectangle with the Fewest Squares**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, m = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** `3` squares are necessary to cover the rectangle.
`2` (squares of `1x1`)
`1` (square of `2x2`)

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
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # n rows, m columns; heights[c] = filled height of column c
        best = n * m
        heights = [0] * m

        def dfs(count: int) -> None:
            nonlocal best
            if count >= best:
                return
            # find the lowest column (leftmost on ties)
            low = min(heights)
            if low == n:
                best = count
                return
            start = heights.index(low)

            # width of the flat segment starting at `start`
            end = start
            while end < m and heights[end] == low:
                end += 1
            max_side = min(end - start, n - low)

            for side in range(max_side, 0, -1):
                for c in range(start, start + side):
                    heights[c] += side
                dfs(count + 1)
                for c in range(start, start + side):
                    heights[c] -= side

        dfs(0)
        return best
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
- [279. Perfect Squares](../../0001-0500/0279-perfect-squares/)
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [977. Squares of a Sorted Array](../../0501-1000/0977-squares-of-a-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)
