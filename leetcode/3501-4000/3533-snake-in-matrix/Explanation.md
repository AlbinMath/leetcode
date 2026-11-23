# LeetCode 3248: Snake in Matrix

**LeetCode Problem #3248 — Snake in Matrix**
Solve LeetCode Snake in Matrix using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Snake in Matrix |
| LeetCode | #3248 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a snake in an `n x n` matrix `grid` and can move in **four possible directions**. Each cell in the `grid` is identified by the position: `grid[i][j] = (i * n) + j`.

The snake starts at cell 0 and follows a sequence of commands.

You are given an integer `n` representing the size of the `grid` and an array of strings `commands` where each `command[i]` is either `"UP"`, `"RIGHT"`, `"DOWN"`, and `"LEFT"`. It's guaranteed that the snake will remain within the `grid` boundaries throughout its movement.

Return the position of the final cell where the snake ends up after executing `commands`.

## Constraints
- `2 <= n <= 10`
- `1 <= commands.length <= 100`
- `commands` consists only of `"UP"`, `"RIGHT"`, `"DOWN"`, and `"LEFT"`.
- The input is generated such the snake will not move outside of the boundaries.

## Examples
### Example 1
- **Input:** `n = 2, commands = ["RIGHT","DOWN"]`
- **Output:** `3`
- **Explanation:** 0 
 1 
 
 
 2 
 3 
 
 
 

 
 
 
 0 
 1 
 
 
 2 
 3 
 
 
 

 
 
 
 0 
 1 
 
 
 2 
 3

### Example 2
- **Input:** `n = 3, commands = ["DOWN","RIGHT","UP"]`
- **Output:** `1`
- **Explanation:** 0 
 1 
 2 
 
 
 3 
 4 
 5 
 
 
 6 
 7 
 8 
 
 
 

 
 
 
 0 
 1 
 2 
 
 
 3 
 4 
 5 
 
 
 6 
 7 
 8 
 
 
 

 
 
 
 0 
 1 
 2 
 
 
 3 
 4 
 5 
 
 
 6 
 7 
 8 
 
 
 

 
 
 
 0 
 1 
 2 
 
 
 3 
 4 
 5 
 
 
 6 
 7 
 8

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Snake in Matrix**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, commands = ["RIGHT","DOWN"]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** 0 
 1 
 
 
 2 
 3 
 
 
 

 
 
 
 0 
 1 
 
 
 2 
 3 
 
 
 

 
 
 
 0 
 1 
 
 
 2 
 3

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
var finalPositionOfSnake = function(n, commands) {
    let pos = 0;

    for (const cmd of commands) {
        if (cmd === "UP") pos -= n;
        else if (cmd === "DOWN") pos += n;
        else if (cmd === "LEFT") pos -= 1;
        else pos += 1;
    }

    return pos;
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
- [54. Spiral Matrix](../../0001-0500/0054-spiral-matrix/)
- [59. Spiral Matrix II](../../0001-0500/0059-spiral-matrix-ii/)
- [73. Set Matrix Zeroes](../../0001-0500/0073-set-matrix-zeroes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/snake-in-matrix/)
