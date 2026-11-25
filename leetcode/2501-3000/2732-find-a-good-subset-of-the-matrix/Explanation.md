# LeetCode 2732: Find a Good Subset of the Matrix

**LeetCode Problem #2732 — Find a Good Subset of the Matrix**
Solve LeetCode Find a Good Subset of the Matrix using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find a Good Subset of the Matrix |
| LeetCode | #2732 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** `m x n` binary matrix `grid`.

Let us call a **non-empty** subset of rows **good** if the sum of each column of the subset is at most half of the length of the subset.

More formally, if the length of the chosen subset of rows is `k`, then the sum of each column should be at most `floor(k / 2)`.

Return *an integer array that contains row indices of a good subset sorted in **ascending** order.*

If there are multiple good subsets, you can return any of them. If there are no good subsets, return an empty array.

A **subset** of rows of the matrix `grid` is any matrix that can be obtained by deleting some (possibly none or all) rows from `grid`.

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m <= 10^4`
- `1 <= n <= 5`
- `grid[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]`
- **Output:** `[0,1]`
- **Explanation:** We can choose the 0^th and 1^st rows to create a good subset of rows.
The length of the chosen subset is 2.
- The sum of the 0^th column is 0 + 0 = 0, which is at most half of the length of the subset.
- The sum of the 1^st column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 2^nd column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 3^rd column is 0 + 1 = 1, which is at most half of the length of the subset.

### Example 2
- **Input:** `grid = [[0]]`
- **Output:** `[0]`
- **Explanation:** We can choose the 0^th row to create a good subset of rows.
The length of the chosen subset is 1.
- The sum of the 0^th column is 0, which is at most half of the length of the subset.

### Example 3
- **Input:** `grid = [[1,1,1],[1,1,1]]`
- **Output:** `[]`
- **Explanation:** It is impossible to choose any subset of rows to create a good subset.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find a Good Subset of the Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1]`.
4. **Verification:** We can choose the 0^th and 1^st rows to create a good subset of rows.
The length of the chosen subset is 2.
- The sum of the 0^th column is 0 + 0 = 0, which is at most half of the length of the subset.
- The sum of the 1^st column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 2^nd column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 3^rd column is 0 + 1 = 1, which is at most half of the length of the subset.

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
class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        first = {}
        for i, row in enumerate(grid):
            mask = 0
            for j, v in enumerate(row):
                if v:
                    mask |= 1 << j
            if mask == 0:
                return [i]
            if mask not in first:
                first[mask] = i

        masks = list(first.items())
        for a, i in masks:
            for b, j in masks:
                if a & b == 0 and i != j:
                    return sorted([i, j])
        return []
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
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1001-1500/1439-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
- [1397. Find All Good Strings](../../1001-1500/1397-find-all-good-strings/)
- [1982. Find Array Given Subset Sums](../../1501-2000/1982-find-array-given-subset-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/)
