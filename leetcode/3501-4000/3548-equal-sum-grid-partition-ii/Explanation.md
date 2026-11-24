# LeetCode 3548: Equal Sum Grid Partition II

**LeetCode Problem #3548 — Equal Sum Grid Partition II**
Solve LeetCode Equal Sum Grid Partition II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Equal Sum Grid Partition II |
| LeetCode | #3548 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` matrix `grid` of positive integers. Your task is to determine if it is possible to make **either one horizontal or one vertical cut** on the grid such that:

Each of the two resulting sections formed by the cut is **non-empty**. 
 The sum of elements in both sections is equal , or can be made equal by discounting **at most** one single cell in total (from either section). 
 If a cell is discounted, the rest of the section must **remain connected**.

Return `true` if such a partition exists; otherwise, return `false`.

**Note:** A section is **connected** if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

## Constraints
- `1 <= m == grid.length <= 10^5`
- `1 <= n == grid[i].length <= 10^5`
- `2 <= m * n <= 10^5`
- `1 <= grid[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `grid = [[1,4],[2,3]]`
- **Output:** `true`
- **Explanation:** A horizontal cut after the first row gives sums `1 + 4 = 5` and `2 + 3 = 5`, which are equal. Thus, the answer is `true`.

### Example 2
- **Input:** `grid = [[1,2],[3,4]]`
- **Output:** `true`
- **Explanation:** A vertical cut after the first column gives sums `1 + 3 = 4` and `2 + 4 = 6`. 
 By discounting 2 from the right section (`6 - 2 = 4`), both sections have equal sums and remain connected. Thus, the answer is `true`.

### Example 3
- **Input:** `grid = [[1,2,4],[2,3,5]]`
- **Output:** `false`

### Example 4
- **Input:** `grid = [[4,1,8],[3,2,6]]`
- **Output:** `false`
- **Explanation:** No valid cut exists, so the answer is `false`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Equal Sum Grid Partition II**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,4],[2,3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** A horizontal cut after the first row gives sums `1 + 4 = 5` and `2 + 3 = 5`, which are equal. Thus, the answer is `true`.

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
from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g: List[List[int]]) -> bool:
            m, n = len(g), len(g[0])
            total = sum(map(sum, g))
            top = Counter()
            bot = Counter()
            for row in g:
                bot.update(row)

            acc = 0
            for i in range(m - 1):
                acc += sum(g[i])
                top.update(g[i])
                bot.subtract(g[i])

                A, B = acc, total - acc
                if A == B:
                    return True

                if A > B:
                    diff = A - B
                    rows = i + 1
                    # top section: rows 0..i
                    if rows >= 2 and n >= 2:
                        if top[diff] > 0:
                            return True
                    elif rows == 1:
                        # single row of length n
                        if n >= 2 and (g[0][0] == diff or g[0][n - 1] == diff):
                            return True
                    else:
                        # rows >= 2, n == 1: vertical strip, only ends removable
                        if g[0][0] == diff or g[i][0] == diff:
                            return True
                else:
                    diff = B - A
                    rows = m - i - 1
                    # bottom section: rows i+1..m-1
                    if rows >= 2 and n >= 2:
                        if bot[diff] > 0:
                            return True
                    elif rows == 1:
                        if n >= 2 and (g[m - 1][0] == diff or g[m - 1][n - 1] == diff):
                            return True
                    else:
                        # rows >= 2, n == 1
                        if g[i + 1][0] == diff or g[m - 1][0] == diff:
                            return True
            return False

        if check(grid):
            return True
        transposed = [list(col) for col in zip(*grid)]
        return check(transposed)
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
- [3546. Equal Sum Grid Partition I](../../3501-4000/3546-equal-sum-grid-partition-i/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [698. Partition to K Equal Sum Subsets](../../0501-1000/0698-partition-to-k-equal-sum-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/equal-sum-grid-partition-ii/)
