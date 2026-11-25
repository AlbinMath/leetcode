# LeetCode 3453: Separate Squares I

**LeetCode Problem #3453 — Separate Squares I**
Solve LeetCode Separate Squares I using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Separate Squares I |
| LeetCode | #3453 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a 2D integer array `squares`. Each `squares[i] = [x_i, y_i, l_i]` represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum** y-coordinate value of a horizontal line such that the total area of the squares above the line *equals* the total area of the squares below the line.

Answers within `10^-5` of the actual answer will be accepted.

**Note**: Squares **may** overlap. Overlapping areas should be counted **multiple times**.

## Constraints
- `1 <= squares.length <= 5 * 10^4`
- `squares[i] = [x_i, y_i, l_i]`
- `squares[i].length == 3`
- `0 <= x_i, y_i <= 10^9`
- `1 <= l_i <= 10^9`
- The total area of all the squares will not exceed `10^12`.

## Examples
### Example 1
- **Input:** `squares = [[0,0,1],[2,2,1]]`
- **Output:** `1.00000`
- **Explanation:** Any horizontal line between `y = 1` and `y = 2` will have 1 square unit above it and 1 square unit below it. The lowest option is 1.

### Example 2
- **Input:** `squares = [[0,0,2],[1,1,1]]`
- **Output:** `1.16667`
- **Explanation:** The areas are: 

 
 Below the line: `7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5`. 
 Above the line: `5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5`. 
 

 Since the areas above and below the line are equal, the output is `7/6 = 1.16667`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Separate Squares I**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `squares = [[0,0,1],[2,2,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1.00000`.
4. **Verification:** Any horizontal line between `y = 1` and `y = 2` will have 1 square unit above it and 1 square unit below it. The lowest option is 1.

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
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = sum(l * l for _, _, l in squares)
        half = total / 2

        def below(y: float) -> float:
            s = 0.0
            for _, yi, l in squares:
                h = y - yi
                if h > 0:
                    s += l * (h if h < l else l)
            return s

        lo, hi = 0.0, float(max(yi + l for _, yi, l in squares))
        for _ in range(100):
            mid = (lo + hi) / 2
            if below(mid) >= half:
                hi = mid
            else:
                lo = mid
        return hi
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
- [3454. Separate Squares II](../../3001-3500/3454-separate-squares-ii/)
- [279. Perfect Squares](../../0001-0500/0279-perfect-squares/)
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/separate-squares-i/)
