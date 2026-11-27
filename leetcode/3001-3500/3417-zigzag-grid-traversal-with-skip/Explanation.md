# LeetCode 3417: Zigzag Grid Traversal With Skip

**LeetCode Problem #3417 — Zigzag Grid Traversal With Skip**
Solve LeetCode Zigzag Grid Traversal With Skip using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Zigzag Grid Traversal With Skip |
| LeetCode | #3417 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an `m x n` 2D array `grid` of **positive** integers.

Your task is to traverse `grid` in a **zigzag** pattern while skipping every **alternate** cell.

Zigzag pattern traversal is defined as following the below actions:

Start at the top-left cell `(0, 0)`. 
 Move *right* within a row until the end of the row is reached. 
 Drop down to the next row, then traverse *left* until the beginning of the row is reached. 
 Continue **alternating** between right and left traversal until every row has been traversed.

**Note **that you **must skip** every *alternate* cell during the traversal.

Return an array of integers `result` containing, **in order**, the value of the cells visited during the zigzag traversal with skips.

## Constraints
- `2 <= n == grid.length <= 50`
- `2 <= m == grid[i].length <= 50`
- `1 <= grid[i][j] <= 2500`

## Examples
### Example 1
- **Input:** `grid = [[1,2],[3,4]]`
- **Output:** `[1,4]`

### Example 2
- **Input:** `grid = [[2,1],[2,1],[2,1]]`
- **Output:** `[2,1,2]`

### Example 3
- **Input:** `grid = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `[1,3,5,7,9]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Zigzag Grid Traversal With Skip**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `grid = [[1,2],[3,4]]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,4]`.

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
var zigzagTraversal = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const result = [];
    let take = true;

    for (let r = 0; r < rows; r++) {
        if (r % 2 === 0) {
            for (let c = 0; c < cols; c++) {
                if (take) result.push(grid[r][c]);
                take = !take;
            }
        } else {
            for (let c = cols - 1; c >= 0; c--) {
                if (take) result.push(grid[r][c]);
                take = !take;
            }
        }
    }

    return result;
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
- [103. Binary Tree Zigzag Level Order Traversal](../../0001-0500/0103-binary-tree-zigzag-level-order-traversal/)
- [3552. Grid Teleportation Traversal](../../3501-4000/3552-grid-teleportation-traversal/)
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/zigzag-grid-traversal-with-skip/)
