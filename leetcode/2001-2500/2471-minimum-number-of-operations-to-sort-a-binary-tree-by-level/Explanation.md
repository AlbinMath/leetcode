# LeetCode 2471: Minimum Number of Operations to Sort a Binary Tree by Level

**LeetCode Problem #2471 — Minimum Number of Operations to Sort a Binary Tree by Level**
Solve LeetCode Minimum Number of Operations to Sort a Binary Tree by Level using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Sort a Binary Tree by Level |
| LeetCode | #2471 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given the `root` of a binary tree with **unique values**.

In one operation, you can choose any two nodes **at the same level** and swap their values.

Return *the minimum number of operations needed to make the values at each level sorted in a **strictly increasing order***.

The **level** of a node is the number of edges along the path between it and the root node*.*

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
- All the values of the tree are **unique**.

## Examples
### Example 1
- **Input:** `root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]`
- **Output:** `3`
- **Explanation:** - Swap 4 and 3. The 2^nd level becomes [3,4].
- Swap 7 and 5. The 3^rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3^rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

### Example 2
- **Input:** `root = [1,3,2,7,6,5,4]`
- **Output:** `3`
- **Explanation:** - Swap 3 and 2. The 2^nd level becomes [2,3].
- Swap 7 and 4. The 3^rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3^rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

### Example 3
- **Input:** `root = [1,2,3,4,5,6]`
- **Output:** `0`
- **Explanation:** Each level is already sorted in increasing order so return 0.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Operations to Sort a Binary Tree by Level**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** - Swap 4 and 3. The 2^nd level becomes [3,4].
- Swap 7 and 5. The 3^rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3^rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

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
from collections import deque
from typing import Optional

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps(vals):
            k = len(vals)
            order = sorted(range(k), key=lambda i: vals[i])
            # order[j] = index of the element that belongs at position j
            seen = [False] * k
            swaps = 0
            for i in range(k):
                if seen[i] or order[i] == i:
                    continue
                length = 0
                j = i
                while not seen[j]:
                    seen[j] = True
                    j = order[j]
                    length += 1
                swaps += length - 1
            return swaps

        ans = 0
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += min_swaps(vals)
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
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](../../1501-2000/1689-partitioning-into-minimum-number-of-deci-binary-numbers/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1769-minimum-number-of-operations-to-move-all-balls-to-each-box/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/)
