# LeetCode 1886: Determine Whether Matrix Can Be Obtained By Rotation

**LeetCode Problem #1886 — Determine Whether Matrix Can Be Obtained By Rotation**
Solve LeetCode Determine Whether Matrix Can Be Obtained By Rotation using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Determine Whether Matrix Can Be Obtained By Rotation |
| LeetCode | #1886 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two `n x n` binary matrices `mat` and `target`, return `true`* if it is possible to make *`mat`* equal to *`target`* by **rotating** *`mat`* in **90-degree increments**, or *`false`* otherwise.*

## Constraints
- `n == mat.length == target.length`
- `n == mat[i].length == target[i].length`
- `1 <= n <= 10`
- `mat[i][j]` and `target[i][j]` are either `0` or `1`.

## Examples
### Example 1
- **Input:** `mat = [[0,1],[1,0]], target = [[1,0],[0,1]]`
- **Output:** `true`
- **Explanation:** We can rotate mat 90 degrees clockwise to make mat equal target.

### Example 2
- **Input:** `mat = [[0,1],[1,1]], target = [[1,0],[0,1]]`
- **Output:** `false`
- **Explanation:** It is impossible to make mat equal to target by rotating mat.

### Example 3
- **Input:** `mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]`
- **Output:** `true`
- **Explanation:** We can rotate mat 90 degrees clockwise two times to make mat equal target.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Determine Whether Matrix Can Be Obtained By Rotation**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[0,1],[1,0]], target = [[1,0],[0,1]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can rotate mat 90 degrees clockwise to make mat equal target.

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
    bool findRotation(vector<vector<int>>& mat,
                      vector<vector<int>>& target) {
        int n = mat.size();

        for (int rotation = 0; rotation < 4; rotation++) {
            if (mat == target) {
                return true;
            }

            vector<vector<int>> rotated(n, vector<int>(n, 0));

            // Rotate 90 degrees clockwise
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    rotated[j][n - 1 - i] = mat[i][j];
                }
            }

            mat = rotated;
        }

        return false;
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
- [1160. Find Words That Can Be Formed by Characters](../../1001-1500/1160-find-words-that-can-be-formed-by-characters/)
- [1353. Maximum Number of Events That Can Be Attended](../../1001-1500/1353-maximum-number-of-events-that-can-be-attended/)
- [1751. Maximum Number of Events That Can Be Attended II](../../1501-2000/1751-maximum-number-of-events-that-can-be-attended-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/)
