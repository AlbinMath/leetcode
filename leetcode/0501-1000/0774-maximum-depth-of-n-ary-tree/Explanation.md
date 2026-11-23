# LeetCode 559: Maximum Depth of N-ary Tree

**LeetCode Problem #559 — Maximum Depth of N-ary Tree**
Solve LeetCode Maximum Depth of N-ary Tree using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Depth of N-ary Tree |
| LeetCode | #559 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

## Constraints
- The total number of nodes is in the range `[0, 10^4]`.
- The depth of the n-ary tree is less than or equal to `1000`.

## Examples
### Example 1
- **Input:** `root = [1,null,3,2,4,null,5,6]`
- **Output:** `3`

### Example 2
- **Input:** `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
- **Output:** `5`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Depth of N-ary Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,null,3,2,4,null,5,6]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        max_child_depth = 0

        for child in root.children:
            max_child_depth = max(max_child_depth, self.maxDepth(child))

        return 1 + max_child_depth
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
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [429. N-ary Tree Level Order Traversal](../../0501-1000/0764-n-ary-tree-level-order-traversal/)
- [589. N-ary Tree Preorder Traversal](../../0501-1000/0775-n-ary-tree-preorder-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)
