# LeetCode 3102: Minimize Manhattan Distances

**LeetCode Problem #3102 — Minimize Manhattan Distances**
Solve LeetCode Minimize Manhattan Distances using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Manhattan Distances |
| LeetCode | #3102 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `points` representing integer coordinates of some points on a 2D plane, where `points[i] = [x_i, y_i]`.

The distance between two points is defined as their Manhattan distance .

Return *the **minimum** possible value for **maximum** distance between any two points by removing exactly one point*.

## Constraints
- `3 <= points.length <= 10^5`
- `points[i].length == 2`
- `1 <= points[i][0], points[i][1] <= 10^8`

## Examples
### Example 1
- **Input:** `points = [[3,10],[5,15],[10,2],[4,4]]`
- **Output:** `12`
- **Explanation:** The maximum distance after removing each point is the following: 

 
 After removing the 0^th point the maximum distance is between points (5, 15) and (10, 2), which is `|5 - 10| + |15 - 2| = 18`. 
 After removing the 1^st point the maximum distance is between points (3, 10) and (10, 2), which is `|3 - 10| + |10 - 2| = 15`. 
 After removing the 2^nd point the maximum distance is between points (5, 15) and (4, 4), which is `|5 - 4| + |15 - 4| = 12`. 
 After removing the 3^rd point the maximum distance is between points (5, 15) and (10, 2), which is `|5 - 10| + |15 - 2| = 18`. 
 

 12 is the minimum possible maximum distance between any two points after removing exactly one point.

### Example 2
- **Input:** `points = [[1,1],[1,1],[1,1]]`
- **Output:** `0`
- **Explanation:** Removing any of the points results in the maximum distance between any two points of 0.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimize Manhattan Distances**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[3,10],[5,15],[10,2],[4,4]]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** The maximum distance after removing each point is the following: 

 
 After removing the 0^th point the maximum distance is between points (5, 15) and (10, 2), which is `|5 - 10| + |15 - 2| = 18`. 
 After removing the 1^st point the maximum distance is between points (3, 10) and (10, 2), which is `|3 - 10| + |10 - 2| = 15`. 
 After removing the 2^nd point the maximum distance is between points (5, 15) and (4, 4), which is `|5 - 4| + |15 - 4| = 12`. 
 After removing the 3^rd point the maximum distance is between points (5, 15) and (10, 2), which is `|5 - 10| + |15 - 2| = 18`. 
 

 12 is the minimum possible maximum distance between any two points after removing exactly one point.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        u = [x + y for x, y in points]
        v = [x - y for x, y in points]

        by_u = sorted(range(n), key=lambda i: u[i])
        by_v = sorted(range(n), key=lambda i: v[i])

        # candidates: the two smallest and two largest in each order
        # (two on each side so one survives after removing the other)
        cand = set(by_u[:2] + by_u[-2:] + by_v[:2] + by_v[-2:])

        def span(order, vals, skip):
            lo = order[0] if order[0] != skip else order[1]
            hi = order[-1] if order[-1] != skip else order[-2]
            return vals[hi] - vals[lo]

        best = float('inf')
        for c in cand:
            d = max(span(by_u, u, c), span(by_v, v, c))
            best = min(best, d)
        return best
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3426. Manhattan Distances of All Arrangements of Pieces](../../3001-3500/3426-manhattan-distances-of-all-arrangements-of-pieces/)
- [3443. Maximum Manhattan Distance After K Changes](../../3001-3500/3443-maximum-manhattan-distance-after-k-changes/)
- [3968. Maximum Manhattan Distance After All Moves](../../3501-4000/3968-maximum-manhattan-distance-after-all-moves/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-manhattan-distances/)
