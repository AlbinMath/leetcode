# LeetCode 3625: Count Number of Trapezoids II

**LeetCode Problem #3625 — Count Number of Trapezoids II**
Solve LeetCode Count Number of Trapezoids II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Trapezoids II |
| LeetCode | #3625 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `points` where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point on the Cartesian plane.

Return the number of unique *trapezoids* that can be formed by choosing any four distinct points from `points`.

A **trapezoid** is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

## Constraints
- `4 <= points.length <= 500`
- `&ndash;1000 <= x_i, y_i <= 1000`
- All points are pairwise distinct.

## Examples
### Example 1
- **Input:** `points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]`
- **Output:** `2`
- **Explanation:** There are two distinct ways to pick four points that form a trapezoid: 

 
 The points `[-3,2], [2,3], [3,2], [2,-3]` form one trapezoid. 
 The points `[2,3], [3,2], [3,0], [2,-3]` form another trapezoid.

### Example 2
- **Input:** `points = [[0,0],[1,0],[0,1],[2,1]]`
- **Output:** `1`
- **Explanation:** There is only one trapezoid which can be formed.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Number of Trapezoids II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** There are two distinct ways to pick four points that form a trapezoid: 

 
 The points `[-3,2], [2,3], [3,2], [2,-3]` form one trapezoid. 
 The points `[2,3], [3,2], [3,0], [2,-3]` form another trapezoid.

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
from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        slopes = defaultdict(lambda: defaultdict(int))   # (dx,dy) -> {c: count}
        mids = defaultdict(int)                          # (sx,sy) -> count
        mids_slope = defaultdict(int)                    # (sx,sy,dx,dy) -> count

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx, dy = xj - xi, yj - yi
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                c = dx * yi - dy * xi
                slopes[(dx, dy)][c] += 1
                sx, sy = xi + xj, yi + yj
                mids[(sx, sy)] += 1
                mids_slope[(sx, sy, dx, dy)] += 1

        pairs = 0
        for lines in slopes.values():
            total = sum(lines.values())
            sq = sum(v * v for v in lines.values())
            pairs += (total * total - sq) // 2

        para = sum(m * (m - 1) // 2 for m in mids.values())
        para -= sum(m * (m - 1) // 2 for m in mids_slope.values())

        return pairs - para
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
- [3623. Count Number of Trapezoids I](../../3501-4000/3886-count-number-of-trapezoids-i/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1501-2000/1511-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-trapezoids-ii/)
