# LeetCode 3623: Count Number of Trapezoids I

**LeetCode Problem #3623 — Count Number of Trapezoids I**
Solve LeetCode Count Number of Trapezoids I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Trapezoids I |
| LeetCode | #3623 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]` represents the coordinates of the `i^th` point on the Cartesian plane.

A **horizontal** **trapezoid** is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique ***horizontal* *trapezoids*** that can be formed by choosing any four distinct points from `points`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `4 <= points.length <= 10^5`
- `&ndash;10^8 <= x_i, y_i <= 10^8`
- All points are pairwise distinct.

## Examples
### Example 1
- **Input:** `points = [[1,0],[2,0],[3,0],[2,2],[3,2]]`
- **Output:** `3`
- **Explanation:** There are three distinct ways to pick four points that form a horizontal trapezoid: 

 
 Using points [1,0] , [2,0] , [3,2] , and [2,2] . 
 Using points [2,0] , [3,0] , [3,2] , and [2,2] . 
 Using points [1,0] , [3,0] , [3,2] , and [2,2] .

### Example 2
- **Input:** `points = [[0,0],[1,0],[0,1],[2,1]]`
- **Output:** `1`
- **Explanation:** There is only one horizontal trapezoid that can be formed.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Number of Trapezoids I**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,0],[2,0],[3,0],[2,2],[3,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are three distinct ways to pick four points that form a horizontal trapezoid: 

 
 Using points [1,0] , [2,0] , [3,2] , and [2,2] . 
 Using points [2,0] , [3,0] , [3,2] , and [2,2] . 
 Using points [1,0] , [3,0] , [3,2] , and [2,2] .

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
from collections import Counter
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows = Counter(y for _, y in points)
        total = 0   # sum of segments over earlier rows
        ans = 0
        for c in rows.values():
            seg = c * (c - 1) // 2
            ans = (ans + seg * total) % MOD
            total = (total + seg) % MOD
        return ans
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
- [3625. Count Number of Trapezoids II](../../3501-4000/3625-count-number-of-trapezoids-ii/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1001-1500/1395-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-trapezoids-i/)
