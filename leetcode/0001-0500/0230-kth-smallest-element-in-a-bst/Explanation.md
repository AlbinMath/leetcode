# LeetCode 230: Kth Smallest Element in a BST

**LeetCode Problem #230 — Kth Smallest Element in a BST**
Solve LeetCode Kth Smallest Element in a BST using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Element in a BST |
| LeetCode | #230 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the `root` of a binary search tree, and an integer `k`, return *the* `k^th` *smallest value (**1-indexed**) of all the values of the nodes in the tree*.

## Constraints
- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

## Examples
### Example 1
- **Input:** `root = [3,1,4,null,2], k = 1`
- **Output:** `1`

### Example 2
- **Input:** `root = [5,3,6,2,4,null,null,1], k = 3`
- **Output:** `3`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Kth Smallest Element in a BST**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,1,4,null,2], k = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
var kthSmallest = function(root, k) {
    const stack = [];
    let current = root;
    let count = 0;

    while (current !== null || stack.length > 0) {
        // Traverse as far left as possible
        while (current !== null) {
            stack.push(current);
            current = current.left;
        }

        // Visit the next smallest node
        current = stack.pop();
        count++;

        if (count === k) {
            return current.val;
        }

        // Explore the right subtree
        current = current.right;
    }
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
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)
- [215. Kth Largest Element in an Array](../../0001-0500/0215-kth-largest-element-in-an-array/)
- [703. Kth Largest Element in a Stream](../../0501-1000/0789-kth-largest-element-in-a-stream/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
