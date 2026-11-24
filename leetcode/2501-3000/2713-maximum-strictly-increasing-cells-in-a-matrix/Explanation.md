# LeetCode 2713: Maximum Strictly Increasing Cells in a Matrix

**LeetCode Problem #2713 — Maximum Strictly Increasing Cells in a Matrix**
Solve LeetCode Maximum Strictly Increasing Cells in a Matrix using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Strictly Increasing Cells in a Matrix |
| LeetCode | #2713 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **1-indexed** `m x n` integer matrix `mat`, you can select any cell in the matrix as your **starting cell**.

From the starting cell, you can move to any other cell **in the** **same row or column**, but only if the value of the destination cell is **strictly greater** than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the **maximum number of cells** that you can visit in the matrix by starting from some cell.

Return *an integer denoting the maximum number of cells that can be visited.*

## Constraints
- `m == mat.length `
- `n == mat[i].length `
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `-10^5 <= mat[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `mat = [[3,1],[3,4]]`
- **Output:** `2`
- **Explanation:** The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2.

### Example 2
- **Input:** `mat = [[1,1],[1,1]]`
- **Output:** `1`
- **Explanation:** Since the cells must be strictly increasing, we can only visit one cell in this example.

### Example 3
- **Input:** `mat = [[3,1,6],[-9,5,7]]`
- **Output:** `4`
- **Explanation:** The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Strictly Increasing Cells in a Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[3,1],[3,4]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from collections import defaultdict

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[mat[i][j]].append((i, j))

        row = [0] * m
        col = [0] * n
        ans = 0

        for v in sorted(groups, reverse=True):
            cells = groups[v]
            vals = [1 + max(row[i], col[j]) for i, j in cells]
            for (i, j), d in zip(cells, vals):
                if d > row[i]:
                    row[i] = d
                if d > col[j]:
                    col[j] = d
                if d > ans:
                    ans = d
        return ans
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)
- [1030. Matrix Cells in Distance Order](../../1001-1500/1030-matrix-cells-in-distance-order/)
- [1252. Cells with Odd Values in a Matrix](../../1001-1500/1252-cells-with-odd-values-in-a-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/)
