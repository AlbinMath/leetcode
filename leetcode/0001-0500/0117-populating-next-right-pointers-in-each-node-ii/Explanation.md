# LeetCode 117: Populating Next Right Pointers in Each Node II

**LeetCode Problem #117 — Populating Next Right Pointers in Each Node II**
Solve LeetCode Populating Next Right Pointers in Each Node II using JavaScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Populating Next Right Pointers in Each Node II |
| LeetCode | #117 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary tree

struct Node {
 int val;
 Node *left;
 Node *right;
 Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

## Constraints
- The number of nodes in the tree is in the range `[0, 6000]`.
- `-100 <= Node.val <= 100`
- You may only use constant extra space.
- The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

## Examples
### Example 1
- **Input:** `root = [1,2,3,4,5,null,7]`
- **Output:** `[1,#,2,3,#,4,5,7,#]`
- **Explanation:** Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

### Example 2
- **Input:** `root = []`
- **Output:** `[]`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Populating Next Right Pointers in Each Node II**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,2,3,4,5,null,7]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,#,2,3,#,4,5,7,#]`.
4. **Verification:** Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var connect = function(root) {
    if (root === null) return null;

    let current = root;

    while (current !== null) {
        // Dummy node for building the next level
        const dummy = new Node(0);
        let tail = dummy;

        // Traverse the current level
        while (current !== null) {
            if (current.left !== null) {
                tail.next = current.left;
                tail = tail.next;
            }

            if (current.right !== null) {
                tail.next = current.right;
                tail = tail.next;
            }

            current = current.next;
        }

        // Move to the first node of the next level
        current = dummy.next;
    }

    return root;
};
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [116. Populating Next Right Pointers in Each Node](../../0001-0500/0116-populating-next-right-pointers-in-each-node/)
- [1019. Next Greater Node In Linked List](../../1001-1500/1072-next-greater-node-in-linked-list/)
- [2516. Take K of Each Character From Left and Right](../../2501-3000/2599-take-k-of-each-character-from-left-and-right/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)
