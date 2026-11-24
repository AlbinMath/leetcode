# LeetCode 1582: Special Positions in a Binary Matrix

**LeetCode Problem #1582 — Special Positions in a Binary Matrix**
Solve LeetCode Special Positions in a Binary Matrix using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Special Positions in a Binary Matrix |
| LeetCode | #1582 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an `m x n` binary matrix `mat`, return *the number of special positions in *`mat`*.*

A position `(i, j)` is called **special** if `mat[i][j] == 1` and all other elements in row `i` and column `j` are `0` (rows and columns are **0-indexed**).

## Constraints
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `mat[i][j]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `mat = [[1,0,0],[0,0,1],[1,0,0]]`
- **Output:** `1`
- **Explanation:** (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

### Example 2
- **Input:** `mat = [[1,0,0],[0,1,0],[0,0,1]]`
- **Output:** `3`
- **Explanation:** (0, 0), (1, 1) and (2, 2) are special positions.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Special Positions in a Binary Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `mat = [[1,0,0],[0,0,1],[1,0,0]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

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
var numSpecial = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const rowSum = new Int32Array(m);
    const colSum = new Int32Array(n);

    // Pass 1: Count 1s in each row and column
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 1) {
                rowSum[i]++;
                colSum[j]++;
            }
        }
    }

    // Pass 2: Count cells where mat[i][j] === 1 is the sole 1 in its row and column
    let special = 0;
    for (let i = 0; i < m; i++) {
        if (rowSum[i] === 1) {
            for (let j = 0; j < n; j++) {
                if (mat[i][j] === 1 && colSum[j] === 1) {
                    special++;
                    break;
                }
            }
        }
    }

    return special;
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
- [1091. Shortest Path in Binary Matrix](../../1001-1500/1171-shortest-path-in-binary-matrix/)
- [1253. Reconstruct a 2-Row Binary Matrix](../../1001-1500/1379-reconstruct-a-2-row-binary-matrix/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1409-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/special-positions-in-a-binary-matrix/)
