# LeetCode 2673: Make Costs of Paths Equal in a Binary Tree

**LeetCode Problem #2673 — Make Costs of Paths Equal in a Binary Tree**
Solve LeetCode Make Costs of Paths Equal in a Binary Tree using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Costs of Paths Equal in a Binary Tree |
| LeetCode | #2673 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n` representing the number of nodes in a **perfect binary tree** consisting of nodes numbered from `1` to `n`. The root of the tree is node `1` and each node `i` in the tree has two children where the left child is the node `2 * i` and the right child is `2 * i + 1`.

Each node in the tree also has a **cost** represented by a given **0-indexed** integer array `cost` of size `n` where `cost[i]` is the cost of node `i + 1`. You are allowed to **increment** the cost of **any** node by `1` **any** number of times.

Return *the **minimum** number of increments you need to make the cost of paths from the root to each **leaf** node equal*.

**Note**:

A **perfect binary tree **is a tree where each node, except the leaf nodes, has exactly 2 children. 
 The **cost of a path** is the sum of costs of nodes in the path.

## Constraints
- `3 <= n <= 10^5`
- `n + 1` is a power of `2`
- `cost.length == n`
- `1 <= cost[i] <= 10^4`

## Examples
### Example 1
- **Input:** `n = 7, cost = [1,5,2,2,3,3,1]`
- **Output:** `6`
- **Explanation:** We can do the following increments:
- Increase the cost of node 4 one time.
- Increase the cost of node 3 three times.
- Increase the cost of node 7 two times.
Each path from the root to a leaf will have a total cost of 9.
The total increments we did is 1 + 3 + 2 = 6.
It can be shown that this is the minimum answer we can achieve.

### Example 2
- **Input:** `n = 3, cost = [5,3,3]`
- **Output:** `0`
- **Explanation:** The two paths already have equal total costs, so no increments are needed.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Make Costs of Paths Equal in a Binary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7, cost = [1,5,2,2,3,3,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** We can do the following increments:
- Increase the cost of node 4 one time.
- Increase the cost of node 3 three times.
- Increase the cost of node 7 two times.
Each path from the root to a leaf will have a total cost of 9.
The total increments we did is 1 + 3 + 2 = 6.
It can be shown that this is the minimum answer we can achieve.

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
var minIncrements = function(n, cost) {
    let increments = 0;
    
    // Traverse all non-leaf nodes bottom-up
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        const left = 2 * i + 1;
        const right = 2 * i + 2;
        
        // Equalize the left and right subtree path sums
        increments += Math.abs(cost[left] - cost[right]);
        
        // Propagate the max equalized subtree path sum upward
        cost[i] += Math.max(cost[left], cost[right]);
    }
    
    return increments;
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
- [3191. Minimum Operations to Make Binary Array Elements Equal to One I](../../3001-3500/3191-minimum-operations-to-make-binary-array-elements-equal-to-one-i/)
- [3192. Minimum Operations to Make Binary Array Elements Equal to One II](../../3001-3500/3192-minimum-operations-to-make-binary-array-elements-equal-to-one-ii/)
- [3800. Minimum Cost to Make Two Binary Strings Equal](../../3501-4000/3800-minimum-cost-to-make-two-binary-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/)
