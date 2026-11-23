# LeetCode 1161: Maximum Level Sum of a Binary Tree

**LeetCode Problem #1161 — Maximum Level Sum of a Binary Tree**
Solve LeetCode Maximum Level Sum of a Binary Tree using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Level Sum of a Binary Tree |
| LeetCode | #1161 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary tree, the level of its root is `1`, the level of its children is `2`, and so on.

Return the **smallest** level `x` such that the sum of all the values of nodes at level `x` is **maximal**.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `root = [1,7,0,7,-8,null,null]`
- **Output:** `2`
- **Explanation:** Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

### Example 2
- **Input:** `root = [989,null,10250,98693,-89388,null,null,null,-32127]`
- **Output:** `2`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Maximum Level Sum of a Binary Tree**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,7,0,7,-8,null,null]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

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
var maxLevelSum = function(root) {
    const queue = [root];
    let level = 1;
    let maxSum = -Infinity;
    let result = 1;

    while (queue.length > 0) {
        const levelSize = queue.length;
        let sum = 0;

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();
            sum += node.val;

            if (node.left !== null) {
                queue.push(node.left);
            }

            if (node.right !== null) {
                queue.push(node.right);
            }
        }

        if (sum > maxSum) {
            maxSum = sum;
            result = level;
        }

        level++;
    }

    return result;
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1373. Maximum Sum BST in Binary Tree](../../1001-1500/1475-maximum-sum-bst-in-binary-tree/)
- [1038. Binary Search Tree to Greater Sum Tree](../../1001-1500/1114-binary-search-tree-to-greater-sum-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)
