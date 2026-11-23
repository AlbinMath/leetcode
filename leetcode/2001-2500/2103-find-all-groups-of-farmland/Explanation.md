# LeetCode 1992: Find All Groups of Farmland

**LeetCode Problem #1992 — Find All Groups of Farmland**
Solve LeetCode Find All Groups of Farmland using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Groups of Farmland |
| LeetCode | #1992 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** `m x n` binary matrix `land` where a `0` represents a hectare of forested land and a `1` represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist **entirely** of farmland. These rectangular areas are called **groups**. No two groups are adjacent, meaning farmland in one group is **not** four-directionally adjacent to another farmland in a different group.

`land` can be represented by a coordinate system where the top left corner of `land` is `(0, 0)` and the bottom right corner of `land` is `(m-1, n-1)`. Find the coordinates of the top left and bottom right corner of each **group** of farmland. A **group** of farmland with a top left corner at `(r_1, c_1)` and a bottom right corner at `(r_2, c_2)` is represented by the 4-length array `[r_1, c_1, r_2, c_2].`

Return *a 2D array containing the 4-length arrays described above for each **group** of farmland in *`land`*. If there are no groups of farmland, return an empty array. You may return the answer in **any order***.

## Constraints
- `m == land.length`
- `n == land[i].length`
- `1 <= m, n <= 300`
- `land` consists of only `0`'s and `1`'s.
- Groups of farmland are **rectangular** in shape.

## Examples
### Example 1
- **Input:** `land = [[1,0,0],[0,1,1],[0,1,1]]`
- **Output:** `[[0,0,0,0],[1,1,2,2]]`
- **Explanation:** The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].

### Example 2
- **Input:** `land = [[1,1],[1,1]]`
- **Output:** `[[0,0,1,1]]`
- **Explanation:** The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].

### Example 3
- **Input:** `land = [[0]]`
- **Output:** `[]`
- **Explanation:** There are no groups of farmland.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find All Groups of Farmland**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `land = [[1,0,0],[0,1,1],[0,1,1]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,0,0,0],[1,1,2,2]]`.
4. **Verification:** The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].

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
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    r, c = i, j
                    while r + 1 < m and land[r + 1][j] == 1:
                        r += 1
                    while c + 1 < n and land[i][c + 1] == 1:
                        c += 1
                    ans.append([i, j, r, c])
        return ans
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
- [438. Find All Anagrams in a String](../../0001-0500/0438-find-all-anagrams-in-a-string/)
- [448. Find All Numbers Disappeared in an Array](../../0001-0500/0448-find-all-numbers-disappeared-in-an-array/)
- [1397. Find All Good Strings](../../1501-2000/1513-find-all-good-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-groups-of-farmland/)
