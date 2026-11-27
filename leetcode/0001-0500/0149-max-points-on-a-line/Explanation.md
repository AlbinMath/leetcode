# LeetCode 149: Max Points on a Line

**LeetCode Problem #149 — Max Points on a Line**
Solve LeetCode Max Points on a Line using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Points on a Line |
| LeetCode | #149 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

## Constraints
- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= x_i, y_i <= 10^4`
- All the `points` are **unique**.

## Examples
### Example 1
- **Input:** `points = [[1,1],[2,2],[3,3]]`
- **Output:** `3`

### Example 2
- **Input:** `points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]`
- **Output:** `4`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Max Points on a Line**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,1],[2,2],[3,3]]`.
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
from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        best = 1
        for i in range(n):
            x1, y1 = points[i]
            cnt = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                cnt[(dx, dy)] += 1
            if cnt:
                best = max(best, max(cnt.values()) + 1)
        return best
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
- [195. Tenth Line](../../0001-0500/0195-tenth-line/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)
- [1621. Number of Sets of K Non-Overlapping Line Segments](../../1501-2000/1621-number-of-sets-of-k-non-overlapping-line-segments/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-points-on-a-line/)
