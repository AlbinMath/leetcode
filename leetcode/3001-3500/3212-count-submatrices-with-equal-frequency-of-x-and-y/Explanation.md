# LeetCode 3212: Count Submatrices With Equal Frequency of X and Y

**LeetCode Problem #3212 — Count Submatrices With Equal Frequency of X and Y**
Solve LeetCode Count Submatrices With Equal Frequency of X and Y using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Submatrices With Equal Frequency of X and Y |
| LeetCode | #3212 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a 2D character matrix `grid`, where `grid[i][j]` is either `'X'`, `'Y'`, or `'.'`, return the number of submatrices that contain:

`grid[0][0]` 
 an **equal** frequency of `'X'` and `'Y'`. 
 **at least** one `'X'`.

## Constraints
- `1 <= grid.length, grid[i].length <= 1000`
- `grid[i][j]` is either `'X'`, `'Y'`, or `'.'`.

## Examples
### Example 1
- **Input:** `grid = [["X","Y","."],["Y",".","."]]`
- **Output:** `3`

### Example 2
- **Input:** `grid = [["X","X"],["X","Y"]]`
- **Output:** `0`
- **Explanation:** No submatrix has an equal frequency of `'X'` and `'Y'`.

### Example 3
- **Input:** `grid = [[".","."],[".","."]]`
- **Output:** `0`
- **Explanation:** No submatrix has at least one `'X'`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Submatrices With Equal Frequency of X and Y**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [["X","Y","."],["Y",".","."]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        px = [[0] * n for _ in range(m)]
        py = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                x = 1 if grid[i][j] == 'X' else 0
                y = 1 if grid[i][j] == 'Y' else 0
                if i > 0:
                    x += px[i - 1][j]
                    y += py[i - 1][j]
                if j > 0:
                    x += px[i][j - 1]
                    y += py[i][j - 1]
                if i > 0 and j > 0:
                    x -= px[i - 1][j - 1]
                    y -= py[i - 1][j - 1]
                px[i][j], py[i][j] = x, y
                if x > 0 and x == y:
                    res += 1

        return res
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
- [2998. Minimum Number of Operations to Make X and Y Equal](../../2501-3000/2998-minimum-number-of-operations-to-make-x-and-y-equal/)
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../../1501-2000/1779-find-nearest-point-that-has-the-same-x-or-y-coordinate/)
- [1224. Maximum Equal Frequency](../../1001-1500/1224-maximum-equal-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/)
