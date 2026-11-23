# LeetCode 1620: Coordinate With Maximum Network Quality

**LeetCode Problem #1620 — Coordinate With Maximum Network Quality**
Solve LeetCode Coordinate With Maximum Network Quality using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Coordinate With Maximum Network Quality |
| LeetCode | #1620 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of network towers `towers`, where `towers[i] = [x_i, y_i, q_i]` denotes the `i^th` network tower with location `(x_i, y_i)` and quality factor `q_i`. All the coordinates are **integral coordinates** on the X-Y plane, and the distance between the two coordinates is the **Euclidean distance**.

You are also given an integer `radius` where a tower is **reachable** if the distance is **less than or equal to** `radius`. Outside that distance, the signal becomes garbled, and the tower is **not reachable**.

The signal quality of the `i^th` tower at a coordinate `(x, y)` is calculated with the formula `&lfloor;q_i / (1 + d)&rfloor;`, where `d` is the distance between the tower and the coordinate. The **network quality** at a coordinate is the sum of the signal qualities from all the **reachable** towers.

Return *the array *`[c_x, c_y]`* representing the **integral** coordinate *`(c_x, c_y)`* where the **network quality** is maximum. If there are multiple coordinates with the same **network quality**, return the lexicographically minimum **non-negative** coordinate.*

**Note:**

A coordinate `(x1, y1)` is lexicographically smaller than `(x2, y2)` if either:

`x1 < x2`, or 
 `x1 == x2` and `y1 < y2`. 
 
 
 `&lfloor;val&rfloor;` is the greatest integer less than or equal to `val` (the floor function).

## Constraints
- `1 <= towers.length <= 50`
- `towers[i].length == 3`
- `0 <= x_i, y_i, q_i <= 50`
- `1 <= radius <= 50`

## Examples
### Example 1
- **Input:** `towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2`
- **Output:** `[2,1]`
- **Explanation:** At coordinate (2, 1) the total quality is 13.
- Quality of 7 from (2, 1) results in &lfloor;7 / (1 + sqrt(0)&rfloor; = &lfloor;7&rfloor; = 7
- Quality of 5 from (1, 2) results in &lfloor;5 / (1 + sqrt(2)&rfloor; = &lfloor;2.07&rfloor; = 2
- Quality of 9 from (3, 1) results in &lfloor;9 / (1 + sqrt(1)&rfloor; = &lfloor;4.5&rfloor; = 4
No other coordinate has a higher network quality.

### Example 2
- **Input:** `towers = [[23,11,21]], radius = 9`
- **Output:** `[23,11]`
- **Explanation:** Since there is only one tower, the network quality is highest right at the tower's location.

### Example 3
- **Input:** `towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2`
- **Output:** `[1,2]`
- **Explanation:** Coordinate (1, 2) has the highest network quality.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Coordinate With Maximum Network Quality**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1]`.
4. **Verification:** At coordinate (2, 1) the total quality is 13.
- Quality of 7 from (2, 1) results in &lfloor;7 / (1 + sqrt(0)&rfloor; = &lfloor;7&rfloor; = 7
- Quality of 5 from (1, 2) results in &lfloor;5 / (1 + sqrt(2)&rfloor; = &lfloor;2.07&rfloor; = 2
- Quality of 9 from (3, 1) results in &lfloor;9 / (1 + sqrt(1)&rfloor; = &lfloor;4.5&rfloor; = 4
No other coordinate has a higher network quality.

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
import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        max_x = max(t[0] for t in towers)
        max_y = max(t[1] for t in towers)
        r_sq = radius * radius
        
        best_quality = -1
        best_coord = [0, 0]
        
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                quality = 0
                for tx, ty, q in towers:
                    d_sq = (x - tx) ** 2 + (y - ty) ** 2
                    if d_sq <= r_sq:
                        quality += int(q / (1 + math.sqrt(d_sq)))
                
                if quality > best_quality:
                    best_quality = quality
                    best_coord = [x, y]
                    
        return best_coord
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
- [2065. Maximum Path Quality of a Graph](../../2001-2500/2189-maximum-path-quality-of-a-graph/)
- [1211. Queries Quality and Percentage](../../1001-1500/1338-queries-quality-and-percentage/)
- [743. Network Delay Time](../../0501-1000/0744-network-delay-time/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/coordinate-with-maximum-network-quality/)
