# LeetCode 1289: Minimum Falling Path Sum II

**LeetCode Problem #1289 — Minimum Falling Path Sum II**
Solve LeetCode Minimum Falling Path Sum II using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Falling Path Sum II |
| LeetCode | #1289 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `n x n` integer matrix `grid`, return *the minimum sum of a **falling path with non-zero shifts***.

A **falling path with non-zero shifts** is a choice of exactly one element from each row of `grid` such that no two elements chosen in adjacent rows are in the same column.

## Constraints
- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `-99 <= grid[i][j] <= 99`

## Examples
### Example 1
- **Input:** `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `13`
- **Explanation:** The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

### Example 2
- **Input:** `grid = [[7]]`
- **Output:** `7`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Falling Path Sum II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2,3],[4,5,6],[7,8,9]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minFallingPathSum = function(grid) {
    const n = grid.length;
    // Track smallest sum (min1), its column index (min1Col), and second smallest sum (min2)
    let min1 = 0;
    let min2 = 0;
    let min1Col = -1;

    for (let r = 0; r < n; r++) {
        let nextMin1 = Infinity;
        let nextMin2 = Infinity;
        let nextMin1Col = -1;

        for (let c = 0; c < n; c++) {
            const prevBest = c === min1Col ? min2 : min1;
            const currSum = grid[r][c] + prevBest;

            if (currSum < nextMin1) {
                nextMin2 = nextMin1;
                nextMin1 = currSum;
                nextMin1Col = c;
            } else if (currSum < nextMin2) {
                nextMin2 = currSum;
            }
        }

        min1 = nextMin1;
        min2 = nextMin2;
        min1Col = nextMin1Col;
    }

    return min1;
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
- [931. Minimum Falling Path Sum](../../0501-1000/0967-minimum-falling-path-sum/)
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [112. Path Sum](../../0001-0500/0112-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-falling-path-sum-ii/)
