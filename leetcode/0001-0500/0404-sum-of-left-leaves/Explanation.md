# LeetCode 404: Sum of Left Leaves

**LeetCode Problem #404 — Sum of Left Leaves**
Solve LeetCode Sum of Left Leaves using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Left Leaves |
| LeetCode | #404 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return *the sum of all left leaves.*

A **leaf** is a node with no children. A **left leaf** is a leaf that is the left child of another node.

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-1000 <= Node.val <= 1000`

## Examples
### Example 1
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `24`
- **Explanation:** There are two left leaves in the binary tree, with values 9 and 15 respectively.

### Example 2
- **Input:** `root = [1]`
- **Output:** `0`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Left Leaves**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [3,9,20,null,null,15,7]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `24`.
4. **Verification:** There are two left leaves in the binary tree, with values 9 and 15 respectively.

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
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0

        total = 0

        # Check if the left child is a leaf
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                total += root.left.val
            else:
                total += self.sumOfLeftLeaves(root.left)

        # Check the right subtree
        total += self.sumOfLeftLeaves(root.right)

        return total
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
- [2574. Left and Right Sum Differences](../../2501-3000/2574-left-and-right-sum-differences/)
- [3070. Count Submatrices with Top-Left Element and Sum Less Than k](../../3001-3500/3070-count-submatrices-with-top-left-element-and-sum-less-than-k/)
- [1302. Deepest Leaves Sum](../../1001-1500/1302-deepest-leaves-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-left-leaves/)
