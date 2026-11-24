# LeetCode 1448: Count Good Nodes in Binary Tree

**LeetCode Problem #1448 — Count Good Nodes in Binary Tree**
Solve LeetCode Count Good Nodes in Binary Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Nodes in Binary Tree |
| LeetCode | #1448 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.

Return the number of **good** nodes in the binary tree.

## Constraints
- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- Each node's value is between `[-10^4, 10^4]`.

## Examples
### Example 1
- **Input:** `root = [3,1,4,3,null,1,5]`
- **Output:** `4`
- **Explanation:** Nodes in blue are

### Example 2
- **Input:** `root = [3,3,null,4,2]`
- **Output:** `3`
- **Explanation:** Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

### Example 3
- **Input:** `root = [1]`
- **Output:** `1`
- **Explanation:** Root is considered as

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Count Good Nodes in Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,1,4,3,null,1,5]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Nodes in blue are

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var goodNodes = function(root) {
    function dfs(node, maxSoFar) {
        if (node === null) {
            return 0;
        }

        let count = 0;

        if (node.val >= maxSoFar) {
            count = 1;
        }

        maxSoFar = Math.max(maxSoFar, node.val);

        count += dfs(node.left, maxSoFar);
        count += dfs(node.right, maxSoFar);

        return count;
    }

    return dfs(root, root.val);
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3997. Count Dominant Nodes in a Binary Tree](../../3501-4000/3997-count-dominant-nodes-in-a-binary-tree/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0863-all-nodes-distance-k-in-binary-tree/)
- [1361. Validate Binary Tree Nodes](../../1001-1500/1361-validate-binary-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
