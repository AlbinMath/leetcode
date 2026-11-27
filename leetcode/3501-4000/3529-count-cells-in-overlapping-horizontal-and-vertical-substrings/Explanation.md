# LeetCode 3529: Count Cells in Overlapping Horizontal and Vertical Substrings

**LeetCode Problem #3529 — Count Cells in Overlapping Horizontal and Vertical Substrings**
Solve LeetCode Count Cells in Overlapping Horizontal and Vertical Substrings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Cells in Overlapping Horizontal and Vertical Substrings |
| LeetCode | #3529 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an `m x n` matrix `grid` consisting of characters and a string `pattern`.

A horizontal substring is a contiguous sequence of characters read from left to right. If the end of a row is reached before the substring is complete, it wraps to the first column of the next row and continues as needed. You do **not** wrap from the bottom row back to the top.

A vertical substring is a contiguous sequence of characters read from top to bottom. If the bottom of a column is reached before the substring is complete, it wraps to the first row of the next column and continues as needed. You do **not** wrap from the last column back to the first.

Count the number of cells in the matrix that satisfy the following condition:

The cell must be part of **at least** one horizontal substring and **at least** one vertical substring, where **both** substrings are equal to the given `pattern`.

Return the count of these cells.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 1000`
- `1 <= m * n <= 10^5`
- `1 <= pattern.length <= m * n`
- `grid` and `pattern` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"`
- **Output:** `1`
- **Explanation:** The pattern `"abaca"` appears once as a horizontal substring (colored blue) and once as a vertical substring (colored red), intersecting at one cell (colored purple).

### Example 2
- **Input:** `grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba"`
- **Output:** `4`
- **Explanation:** The cells colored above are all part of at least one horizontal and one vertical substring matching the pattern `"aba"`.

### Example 3
- **Input:** `grid = [["a"]], pattern = "a"`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Cells in Overlapping Horizontal and Vertical Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The pattern `"abaca"` appears once as a horizontal substring (colored blue) and once as a vertical substring (colored red), intersecting at one cell (colored purple).

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
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        L = len(pattern)
        N = m * n
        if L > N:
            return 0

        def covered(text: str) -> List[bool]:
            s = pattern + '#' + text
            z = [0] * len(s)
            l = r = 0
            for i in range(1, len(s)):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            diff = [0] * (N + 1)
            for start in range(N - L + 1):
                if z[L + 1 + start] >= L:
                    diff[start] += 1
                    diff[start + L] -= 1
            res = [False] * N
            cur = 0
            for i in range(N):
                cur += diff[i]
                res[i] = cur > 0
            return res

        row_text = ''.join(''.join(row) for row in grid)
        col_text = ''.join(grid[i][j] for j in range(n) for i in range(m))

        h = covered(row_text)     # index i*n + j
        v = covered(col_text)     # index j*m + i

        count = 0
        for i in range(m):
            for j in range(n):
                if h[i * n + j] and v[j * m + i]:
                    count += 1
        return count
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
- [1520. Maximum Number of Non-Overlapping Substrings](../../1501-2000/1520-maximum-number-of-non-overlapping-substrings/)
- [2472. Maximum Number of Non-overlapping Palindrome Substrings](../../2001-2500/2472-maximum-number-of-non-overlapping-palindrome-substrings/)
- [2257. Count Unguarded Cells in the Grid](../../2001-2500/2257-count-unguarded-cells-in-the-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/)
