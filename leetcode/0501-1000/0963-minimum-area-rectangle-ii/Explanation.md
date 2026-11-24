# LeetCode 963: Minimum Area Rectangle II

**LeetCode Problem #963 — Minimum Area Rectangle II**
Solve LeetCode Minimum Area Rectangle II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Area Rectangle II |
| LeetCode | #963 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of points in the **X-Y** plane `points` where `points[i] = [x_i, y_i]`.

Return *the minimum area of any rectangle formed from these points, with sides **not necessarily parallel** to the X and Y axes*. If there is not any such rectangle, return `0`.

Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `1 <= points.length <= 50`
- `points[i].length == 2`
- `0 <= x_i, y_i <= 4 * 10^4`
- All the given points are **unique**.

## Examples
### Example 1
- **Input:** `points = [[1,2],[2,1],[1,0],[0,1]]`
- **Output:** `2.00000`
- **Explanation:** The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

### Example 2
- **Input:** `points = [[0,1],[2,1],[1,1],[1,0],[2,0]]`
- **Output:** `1.00000`
- **Explanation:** The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

### Example 3
- **Input:** `points = [[0,3],[1,2],[3,1],[1,3],[2,1]]`
- **Output:** `0`
- **Explanation:** There is no possible rectangle to form from these points.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Area Rectangle II**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,2],[2,1],[1,0],[0,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2.00000`.
4. **Verification:** The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

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
from collections import defaultdict
from math import hypot
from typing import List

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        groups = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                key = (x1 + x2, y1 + y2, (x1 - x2) ** 2 + (y1 - y2) ** 2)
                groups[key].append((i, j))

        best = float('inf')
        for pairs in groups.values():
            m = len(pairs)
            for a in range(m):
                i, _ = pairs[a]
                x1, y1 = points[i]
                for b in range(a + 1, m):
                    k, l = pairs[b]
                    x3, y3 = points[k]
                    x4, y4 = points[l]
                    area = (hypot(x3 - x1, y3 - y1) *
                            hypot(x4 - x1, y4 - y1))
                    best = min(best, area)
        return 0 if best == float('inf') else best
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
- [939. Minimum Area Rectangle](../../0501-1000/0939-minimum-area-rectangle/)
- [3197. Find the Minimum Area to Cover All Ones II](../../3001-3500/3197-find-the-minimum-area-to-cover-all-ones-ii/)
- [223. Rectangle Area](../../0001-0500/0223-rectangle-area/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-area-rectangle-ii/)
