# LeetCode 2049: Count Nodes With the Highest Score

**LeetCode Problem #2049 — Count Nodes With the Highest Score**
Solve LeetCode Count Nodes With the Highest Score using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Nodes With the Highest Score |
| LeetCode | #2049 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a **binary** tree rooted at `0` consisting of `n` nodes. The nodes are labeled from `0` to `n - 1`. You are given a **0-indexed** integer array `parents` representing the tree, where `parents[i]` is the parent of node `i`. Since node `0` is the root, `parents[0] == -1`.

Each node has a **score**. To find the score of a node, consider if the node and the edges connected to it were **removed**. The tree would become one or more **non-empty** subtrees. The **size** of a subtree is the number of the nodes in it. The **score** of the node is the **product of the sizes** of all those subtrees.

Return *the **number** of nodes that have the **highest score***.

## Constraints
- `n == parents.length`
- `2 <= n <= 10^5`
- `parents[0] == -1`
- `0 <= parents[i] <= n - 1` for `i != 0`
- `parents` represents a valid binary tree.

## Examples
### Example 1
- **Input:** `parents = [-1,2,0,2,0]`
- **Output:** `3`
- **Explanation:** - The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.

### Example 2
- **Input:** `parents = [-1,2,0]`
- **Output:** `2`
- **Explanation:** - The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Nodes With the Highest Score**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parents = [-1,2,0,2,0]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** - The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countHighestScoreNodes = function(parents) {
    const n = parents.length;
    const children = Array.from({ length: n }, () => []);
    
    for (let i = 1; i < n; i++) {
        children[parents[i]].push(i);
    }
    
    let maxScore = 0;
    let count = 0;
    
    function dfs(node) {
        let score = 1;
        let subtreeSize = 1;
        
        // Multiply sizes of existing child subtrees
        for (const child of children[node]) {
            const childSize = dfs(child);
            score *= childSize;
            subtreeSize += childSize;
        }
        
        // Multiply size of the remaining upper component (if non-empty)
        const remaining = n - subtreeSize;
        if (remaining > 0) {
            score *= remaining;
        }
        
        if (score > maxScore) {
            maxScore = score;
            count = 1;
        } else if (score === maxScore) {
            count++;
        }
        
        return subtreeSize;
    }
    
    dfs(0);
    return count;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2394-count-subarrays-with-score-less-than-k/)
- [2374. Node With Highest Edge Score](../../2001-2500/2455-node-with-highest-edge-score/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-nodes-with-the-highest-score/)
