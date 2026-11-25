# LeetCode 1504: Count Submatrices With All Ones

**LeetCode Problem #1504 — Count Submatrices With All Ones**
Solve LeetCode Count Submatrices With All Ones using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Submatrices With All Ones |
| LeetCode | #1504 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `m x n` binary matrix `mat`, *return the number of **submatrices** that have all ones*.

## Constraints
- `1 <= m, n <= 150`
- `mat[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `mat = [[1,0,1],[1,1,0],[1,1,0]]`
- **Output:** `13`
- **Explanation:** There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

### Example 2
- **Input:** `mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]`
- **Output:** `24`
- **Explanation:** There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Submatrices With All Ones**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,0,1],[1,1,0],[1,1,0]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

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

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                h[j] = h[j] + 1 if mat[i][j] else 0

            cnt = [0] * n
            stack = []
            for j in range(n):
                while stack and h[stack[-1]] >= h[j]:
                    stack.pop()
                if stack:
                    p = stack[-1]
                    cnt[j] = cnt[p] + h[j] * (j - p)
                else:
                    cnt[j] = h[j] * (j + 1)
                stack.append(j)
                total += cnt[j]

        return total
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
- [1277. Count Square Submatrices with All Ones](../../1001-1500/1277-count-square-submatrices-with-all-ones/)
- [3195. Find the Minimum Area to Cover All Ones I](../../3001-3500/3195-find-the-minimum-area-to-cover-all-ones-i/)
- [3197. Find the Minimum Area to Cover All Ones II](../../3001-3500/3197-find-the-minimum-area-to-cover-all-ones-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-submatrices-with-all-ones/)
