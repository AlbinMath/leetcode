# LeetCode 2661: First Completely Painted Row or Column

**LeetCode Problem #2661 — First Completely Painted Row or Column**
Solve LeetCode First Completely Painted Row or Column using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Completely Painted Row or Column |
| LeetCode | #2661 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `arr`, and an `m x n` integer **matrix** `mat`. `arr` and `mat` both contain **all** the integers in the range `[1, m * n]`.

Go through each index `i` in `arr` starting from index `0` and paint the cell in `mat` containing the integer `arr[i]`.

Return *the smallest index* `i` *at which either a row or a column will be completely painted in* `mat`.

## Constraints
- `m == mat.length`
- `n = mat[i].length`
- `arr.length == m * n`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `1 <= arr[i], mat[r][c] <= m * n`
- All the integers of `arr` are **unique**.
- All the integers of `mat` are **unique**.

## Examples
Consider the standard input for **First Completely Painted Row or Column**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **First Completely Painted Row or Column**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

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
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        pos = [None] * (m * n + 1)
        for i in range(m):
            for j in range(n):
                pos[mat[i][j]] = (i, j)

        row_cnt = [0] * m
        col_cnt = [0] * n

        for idx, v in enumerate(arr):
            r, c = pos[v]
            row_cnt[r] += 1
            col_cnt[c] += 1
            if row_cnt[r] == n or col_cnt[c] == m:
                return idx

        return -1
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
- [3175. Find The First Player to win K Games in a Row](../../3001-3500/3175-find-the-first-player-to-win-k-games-in-a-row/)
- [947. Most Stones Removed with Same Row or Column](../../0501-1000/0947-most-stones-removed-with-same-row-or-column/)
- [1605. Find Valid Matrix Given Row and Column Sums](../../1501-2000/1605-find-valid-matrix-given-row-and-column-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-completely-painted-row-or-column/)
