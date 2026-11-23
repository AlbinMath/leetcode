# LeetCode 1380: Lucky Numbers in a Matrix

**LeetCode Problem #1380 — Lucky Numbers in a Matrix**
Solve LeetCode Lucky Numbers in a Matrix using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lucky Numbers in a Matrix |
| LeetCode | #1380 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an `m x n` matrix of **distinct **numbers, return *all **lucky numbers** in the matrix in **any **order*.

A **lucky number** is an element of the matrix such that it is the minimum element in its row and maximum in its column.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= n, m <= 50`
- `1 <= matrix[i][j] <= 10^5`.
- All elements in the matrix are distinct.

## Examples
### Example 1
- **Input:** `matrix = [[3,7,8],[9,11,13],[15,16,17]]`
- **Output:** `[15]`
- **Explanation:** 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

### Example 2
- **Input:** `matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]`
- **Output:** `[12]`
- **Explanation:** 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

### Example 3
- **Input:** `matrix = [[7,8],[1,2]]`
- **Output:** `[7]`
- **Explanation:** 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Lucky Numbers in a Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matrix = [[3,7,8],[9,11,13],[15,16,17]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[15]`.
4. **Verification:** 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

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
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            min_val = min(matrix[i])
            col = matrix[i].index(min_val)

            if all(matrix[r][col] <= min_val for r in range(rows)):
                result.append(min_val)

        return result
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
- [1351. Count Negative Numbers in a Sorted Matrix](../../1001-1500/1476-count-negative-numbers-in-a-sorted-matrix/)
- [1394. Find Lucky Integer in an Array](../../1501-2000/1510-find-lucky-integer-in-an-array/)
- [54. Spiral Matrix](../../0001-0500/0054-spiral-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lucky-numbers-in-a-matrix/)
