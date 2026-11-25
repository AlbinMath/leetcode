# LeetCode 2643: Row With Maximum Ones

**LeetCode Problem #2643 — Row With Maximum Ones**
Solve LeetCode Row With Maximum Ones using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Row With Maximum Ones |
| LeetCode | #2643 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a `m x n` binary matrix `mat`, find the **0-indexed** position of the row that contains the **maximum** count of **ones,** and the number of ones in that row.

In case there are multiple rows that have the maximum count of ones, the row with the **smallest row number** should be selected.

Return* an array containing the index of the row, and the number of ones in it.*

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `mat[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `mat = [[0,1],[1,0]]`
- **Output:** `[0,1]`
- **Explanation:** Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1`)`. So, the answer is [0,1].

### Example 2
- **Input:** `mat = [[0,0,0],[0,1,1]]`
- **Output:** `[1,2]`
- **Explanation:** The row indexed 1 has the maximum count of ones `(2)`. So we return its index, `1`, and the count. So, the answer is [1,2].

### Example 3
- **Input:** `mat = [[0,0],[1,1],[0,0]]`
- **Output:** `[1,2]`
- **Explanation:** The row indexed 1 has the maximum count of ones (2). So the answer is [1,2].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Row With Maximum Ones**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[0,1],[1,0]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1]`.
4. **Verification:** Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1`)`. So, the answer is [0,1].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        counts = [sum(row) for row in mat]
        best = max(counts)
        return [counts.index(best), best]
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3228. Maximum Number of Operations to Move Ones to the End](../../3001-3500/3228-maximum-number-of-operations-to-move-ones-to-the-end/)
- [2482. Difference Between Ones and Zeros in Row and Column](../../2001-2500/2482-difference-between-ones-and-zeros-in-row-and-column/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/row-with-maximum-ones/)
