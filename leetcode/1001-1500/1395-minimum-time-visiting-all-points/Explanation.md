# LeetCode 1266: Minimum Time Visiting All Points

**LeetCode Problem #1266 — Minimum Time Visiting All Points**
Solve LeetCode Minimum Time Visiting All Points using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time Visiting All Points |
| LeetCode | #1266 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
On a 2D plane, there are `n` points with integer coordinates `points[i] = [x_i, y_i]`. Return *the **minimum time** in seconds to visit all the points in the order given by *`points`.

You can move according to these rules:

In `1` second, you can either:

move vertically by one unit, 
 move horizontally by one unit, or 
 move diagonally `sqrt(2)` units (in other words, move one unit vertically then one unit horizontally in `1` second). 
 
 
 You have to visit the points in the same order as they appear in the array. 
 You are allowed to pass through points that appear later in the order, but these do not count as visits.

## Constraints
- `points.length == n`
- `1 <= n <= 100`
- `points[i].length == 2`
- `-1000 <= points[i][0], points[i][1] <= 1000`

## Examples
### Example 1
- **Input:** `points = [[1,1],[3,4],[-1,0]]`
- **Output:** `7`
- **Explanation:** One optimal path is

### Example 2
- **Input:** `points = [[3,2],[-2,2]]`
- **Output:** `5`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time Visiting All Points**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `points = [[1,1],[3,4],[-1,0]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** One optimal path is

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            total += max(abs(x2 - x1), abs(y2 - y1))

        return total
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1443. Minimum Time to Collect All Apples in a Tree](../../1501-2000/1554-minimum-time-to-collect-all-apples-in-a-tree/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1825-find-minimum-time-to-finish-all-jobs/)
- [2589. Minimum Time to Complete All Tasks](../../2501-3000/2657-minimum-time-to-complete-all-tasks/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-visiting-all-points/)
