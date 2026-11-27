# LeetCode 337: House Robber III

**LeetCode Problem #337 — House Robber III**
Solve LeetCode House Robber III using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | House Robber III |
| LeetCode | #337 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called `root`.

Besides the `root`, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if **two directly-linked houses were broken into on the same night**.

Given the `root` of the binary tree, return *the maximum amount of money the thief can rob **without alerting the police***.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `0 <= Node.val <= 10^4`

## Examples
### Example 1
- **Input:** `root = [3,2,3,null,3,null,1]`
- **Output:** `7`
- **Explanation:** Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

### Example 2
- **Input:** `root = [3,4,5,1,3,null,1]`
- **Output:** `9`
- **Explanation:** Maximum amount of money the thief can rob = 4 + 5 = 9.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **House Robber III**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,2,3,null,3,null,1]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var rob = function(root) {
    function dfs(node) {
        if (!node) return [0, 0];
        
        const [leftRob, leftSkip] = dfs(node.left);
        const [rightRob, rightSkip] = dfs(node.right);
        
        const robCurr = node.val + leftSkip + rightSkip;
        const skipCurr = Math.max(leftRob, leftSkip) + Math.max(rightRob, rightSkip);
        
        return [robCurr, skipCurr];
    }
    
    return Math.max(...dfs(root));
};
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
- [198. House Robber](../../0001-0500/0198-house-robber/)
- [213. House Robber II](../../0001-0500/0213-house-robber-ii/)
- [2560. House Robber IV](../../2501-3000/2560-house-robber-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/house-robber-iii/)
