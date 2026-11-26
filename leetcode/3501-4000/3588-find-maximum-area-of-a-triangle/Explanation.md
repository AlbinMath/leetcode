# LeetCode 3588: Find Maximum Area of a Triangle

**LeetCode Problem #3588 — Find Maximum Area of a Triangle**
Solve LeetCode Find Maximum Area of a Triangle using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Area of a Triangle |
| LeetCode | #3588 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D array `coords` of size `n x 2`, representing the coordinates of `n` points in an infinite Cartesian plane.

Find **twice** the **maximum** area of a triangle with its corners at *any* three elements from `coords`, such that at least one side of this triangle is **parallel** to the x-axis or y-axis. Formally, if the maximum area of such a triangle is `A`, return `2 * A`.

If no such triangle exists, return -1.

**Note** that a triangle *cannot* have zero area.

## Constraints
- `1 <= n == coords.length <= 10^5`
- `1 <= coords[i][0], coords[i][1] <= 10^6`
- All `coords[i]` are **unique**.

## Examples
### Example 1
- **Input:** `coords = [[1,1],[1,2],[3,2],[3,3]]`
- **Output:** `2`
- **Explanation:** The triangle shown in the image has a base 1 and height 2. Hence its area is `1/2 * base * height = 1`.

### Example 2
- **Input:** `coords = [[1,1],[2,2],[3,3]]`
- **Output:** `-1`
- **Explanation:** The only possible triangle has corners `(1, 1)`, `(2, 2)`, and `(3, 3)`. None of its sides are parallel to the x-axis or the y-axis.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Maximum Area of a Triangle**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coords = [[1,1],[1,2],[3,2],[3,3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The triangle shown in the image has a base 1 and height 2. Hence its area is `1/2 * base * height = 1`.

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
    def maxArea(self, coords: List[List[int]]) -> int:
        def solve(pts):
            lo, hi = {}, {}
            for x, y in pts:
                if x not in lo:
                    lo[x] = hi[x] = y
                else:
                    if y < lo[x]: lo[x] = y
                    if y > hi[x]: hi[x] = y
            min_x, max_x = min(lo), max(lo)
            best = 0
            for x in lo:
                base = hi[x] - lo[x]
                height = max(x - min_x, max_x - x)
                best = max(best, base * height)
            return best

        ans = max(solve(coords), solve([[y, x] for x, y in coords]))
        return ans if ans > 0 else -1
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
- [812. Largest Triangle Area](../../0501-1000/0812-largest-triangle-area/)
- [3200. Maximum Height of a Triangle](../../3001-3500/3200-maximum-height-of-a-triangle/)
- [2975. Maximum Square Area by Removing Fences From a Field](../../2501-3000/2975-maximum-square-area-by-removing-fences-from-a-field/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-area-of-a-triangle/)
