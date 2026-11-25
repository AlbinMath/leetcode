# LeetCode 1779: Find Nearest Point That Has the Same X or Y Coordinate

**LeetCode Problem #1779 — Find Nearest Point That Has the Same X or Y Coordinate**
Solve LeetCode Find Nearest Point That Has the Same X or Y Coordinate using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Nearest Point That Has the Same X or Y Coordinate |
| LeetCode | #1779 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers, `x` and `y`, which represent your current location on a Cartesian grid: `(x, y)`. You are also given an array `points` where each `points[i] = [a_i, b_i]` represents that a point exists at `(a_i, b_i)`. A point is **valid** if it shares the same x-coordinate or the same y-coordinate as your location.

Return *the index **(0-indexed)** of the **valid** point with the smallest **Manhattan distance** from your current location*. If there are multiple, return *the valid point with the **smallest** index*. If there are no valid points, return `-1`.

The **Manhattan distance** between two points `(x_1, y_1)` and `(x_2, y_2)` is `abs(x_1 - x_2) + abs(y_1 - y_2)`.

## Constraints
- `1 <= points.length <= 10^4`
- `points[i].length == 2`
- `1 <= x, y, a_i, b_i <= 10^4`

## Examples
### Example 1
- **Input:** `x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]`
- **Output:** `2`
- **Explanation:** Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

### Example 2
- **Input:** `x = 3, y = 4, points = [[3,4]]`
- **Output:** `0`
- **Explanation:** The answer is allowed to be on the same location as your current location.

### Example 3
- **Input:** `x = 3, y = 4, points = [[2,3]]`
- **Output:** `-1`
- **Explanation:** There are no valid points.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Nearest Point That Has the Same X or Y Coordinate**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int minDistance = INT_MAX;
        int result = -1;

        for (int i = 0; i < points.size(); i++) {
            int a = points[i][0];
            int b = points[i][1];

            // Check whether the point is valid
            if (a == x || b == y) {
                int distance = abs(x - a) + abs(y - b);

                if (distance < minDistance) {
                    minDistance = distance;
                    result = i;
                }
            }
        }

        return result;
    }
};
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
- [2998. Minimum Number of Operations to Make X and Y Equal](../../2501-3000/2998-minimum-number-of-operations-to-make-x-and-y-equal/)
- [3212. Count Submatrices With Equal Frequency of X and Y](../../3001-3500/3212-count-submatrices-with-equal-frequency-of-x-and-y/)
- [3178. Find the Child Who Has the Ball After K Seconds](../../3001-3500/3178-find-the-child-who-has-the-ball-after-k-seconds/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/)
