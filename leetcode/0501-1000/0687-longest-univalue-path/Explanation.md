# LeetCode 687: Longest Univalue Path

**LeetCode Problem #687 — Longest Univalue Path**
Solve LeetCode Longest Univalue Path using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Univalue Path |
| LeetCode | #687 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return *the length of the longest path, where each node in the path has the same value*. This path may or may not pass through the root.

**The length of the path** between two nodes is represented by the number of edges between them.

## Constraints
- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-1000 <= Node.val <= 1000`
- The depth of the tree will not exceed `1000`.

## Examples
### Example 1
- **Input:** `root = [5,4,5,1,1,null,5]`
- **Output:** `2`
- **Explanation:** The shown image shows that the longest path of the same value (i.e. 5).

### Example 2
- **Input:** `root = [1,4,5,4,4,null,5]`
- **Output:** `2`
- **Explanation:** The shown image shows that the longest path of the same value (i.e. 4).

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Univalue Path**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,4,5,1,1,null,5]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The shown image shows that the longest path of the same value (i.e. 5).

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
    def longestUnivaluePath(self, root) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            a = l + 1 if node.left and node.left.val == node.val else 0
            b = r + 1 if node.right and node.right.val == node.val else 0
            ans = max(ans, a + b)
            return max(a, b)

        dfs(root)
        return ans
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
- [329. Longest Increasing Path in a Matrix](../../0001-0500/0329-longest-increasing-path-in-a-matrix/)
- [388. Longest Absolute File Path](../../0001-0500/0388-longest-absolute-file-path/)
- [1372. Longest ZigZag Path in a Binary Tree](../../1001-1500/1372-longest-zigzag-path-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-univalue-path/)
