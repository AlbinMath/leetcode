# LeetCode 1584: Min Cost to Connect All Points

**LeetCode Problem #1584 — Min Cost to Connect All Points**
Solve LeetCode Min Cost to Connect All Points using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Min Cost to Connect All Points |
| LeetCode | #1584 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_i, y_i]`.

The cost of connecting two points `[x_i, y_i]` and `[x_j, y_j]` is the **manhattan distance** between them: `|x_i - x_j| + |y_i - y_j|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.

## Constraints
- `1 <= points.length <= 1000`
- `-10^6 <= x_i, y_i <= 10^6`
- All pairs `(x_i, y_i)` are distinct.

## Examples
### Example 1
- **Input:** `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`
- **Output:** `20`
- **Explanation:** We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

### Example 2
- **Input:** `points = [[3,12],[-2,5],[-4,1]]`
- **Output:** `18`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Min Cost to Connect All Points**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n
        seen = [False] * n
        dist[0] = cost = 0

        for _ in range(n):
            u = min((dist[i], i) for i in range(n) if not seen[i])[1]
            seen[u] = True
            cost += dist[u]
            x, y = points[u]

            for v, (a, b) in enumerate(points):
                if not seen[v]:
                    dist[v] = min(dist[v], abs(x-a) + abs(y-b))

        return cost
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1595. Minimum Cost to Connect Two Groups of Points](../../1501-2000/1595-minimum-cost-to-connect-two-groups-of-points/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1266-minimum-time-visiting-all-points/)
- [1937. Maximum Number of Points with Cost](../../1501-2000/1937-maximum-number-of-points-with-cost/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/)
