# LeetCode 59: Spiral Matrix II

**LeetCode Problem #59 — Spiral Matrix II**
Solve LeetCode Spiral Matrix II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Spiral Matrix II |
| LeetCode | #59 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer `n`, generate an `n x n` `matrix` filled with elements from `1` to `n^2` in spiral order.

## Constraints
- `1 <= n <= 20`

## Examples
### Example 1
- **Input:** `n = 3`
- **Output:** `[[1,2,3],[8,9,4],[7,6,5]]`

### Example 2
- **Input:** `n = 1`
- **Output:** `[[1]]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Spiral Matrix II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,3],[8,9,4],[7,6,5]]`.

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
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        num = 1

        while top <= bottom and left <= right:

            # 1. Left -> Right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1

            top += 1

            # 2. Top -> Bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1

            right -= 1

            # 3. Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1

                bottom -= 1

            # 4. Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1

                left += 1

        return matrix
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
- [54. Spiral Matrix](../../0001-0500/0054-spiral-matrix/)
- [885. Spiral Matrix III](../../0501-1000/0885-spiral-matrix-iii/)
- [2326. Spiral Matrix IV](../../2001-2500/2326-spiral-matrix-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/spiral-matrix-ii/)
