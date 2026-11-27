# LeetCode 1901: Find a Peak Element II

**LeetCode Problem #1901 — Find a Peak Element II**
Solve LeetCode Find a Peak Element II using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find a Peak Element II |
| LeetCode | #1901 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **peak** element in a 2D grid is an element that is **strictly greater** than all of its **adjacent **neighbors to the left, right, top, and bottom.

Given a **0-indexed** `m x n` matrix `mat` where **no two adjacent cells are equal**, find **any** peak element `mat[i][j]` and return *the length 2 array *`[i,j]`.

You may assume that the entire matrix is surrounded by an **outer perimeter** with the value `-1` in each cell.

You must write an algorithm that runs in `O(m log(n))` or `O(n log(m))` time.

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 500`
- `1 <= mat[i][j] <= 10^5`
- No two adjacent cells are equal.

## Examples
### Example 1
- **Input:** `mat = [[1,4],[3,2]]`
- **Output:** `[0,1]`
- **Explanation:** Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

### Example 2
- **Input:** `mat = [[10,20,15],[21,30,14],[7,16,32]]`
- **Output:** `[1,1]`
- **Explanation:** Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Find a Peak Element II**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,4],[3,2]]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,1]`.
4. **Verification:** Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            # row of the maximum in column mid
            r = max(range(m), key=lambda i: mat[i][mid])
            val = mat[r][mid]

            left = mat[r][mid - 1] if mid > 0 else -1
            right = mat[r][mid + 1] if mid < n - 1 else -1

            if val > left and val > right:
                return [r, mid]
            if left > val:
                hi = mid - 1
            else:
                lo = mid + 1

        return [-1, -1]  # unreachable given the problem guarantees
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [162. Find Peak Element](../../0001-0500/0162-find-peak-element/)
- [34. Find First and Last Position of Element in Sorted Array](../../0001-0500/0034-find-first-and-last-position-of-element-in-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-a-peak-element-ii/)
