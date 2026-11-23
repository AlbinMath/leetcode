# LeetCode 437: Path Sum III

**LeetCode Problem #437 — Path Sum III**
Solve LeetCode Path Sum III using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Path Sum III |
| LeetCode | #437 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree and an integer `targetSum`, return *the number of paths where the sum of the values along the path equals* `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

## Constraints
- The number of nodes in the tree is in the range `[0, 1000]`.
- `-10^9 <= Node.val <= 10^9`
- `-1000 <= targetSum <= 1000`

## Examples
### Example 1
- **Input:** `root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8`
- **Output:** `3`
- **Explanation:** The paths that sum to 8 are shown.

### Example 2
- **Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22`
- **Output:** `3`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Path Sum III**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The paths that sum to 8 are shown.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var pathSum = function(root, targetSum) {
    const prefixCount = new Map();
    prefixCount.set(0, 1);

    let count = 0;

    function dfs(node, currentSum) {
        if (node === null) {
            return;
        }

        currentSum += node.val;

        // Find paths ending at this node with the target sum.
        const needed = currentSum - targetSum;
        count += prefixCount.get(needed) || 0;

        // Add the current prefix sum before visiting children.
        prefixCount.set(
            currentSum,
            (prefixCount.get(currentSum) || 0) + 1
        );

        dfs(node.left, currentSum);
        dfs(node.right, currentSum);

        // Backtrack: remove this prefix sum for other branches.
        prefixCount.set(
            currentSum,
            prefixCount.get(currentSum) - 1
        );
    }

    dfs(root, 0);

    return count;
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [112. Path Sum](../../0001-0500/0112-path-sum/)
- [113. Path Sum II](../../0001-0500/0113-path-sum-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/path-sum-iii/)
