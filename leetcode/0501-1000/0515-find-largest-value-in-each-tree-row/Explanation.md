# LeetCode 515: Find Largest Value in Each Tree Row

**LeetCode Problem #515 — Find Largest Value in Each Tree Row**
Solve LeetCode Find Largest Value in Each Tree Row using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Largest Value in Each Tree Row |
| LeetCode | #515 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return *an array of the largest value in each row* of the tree **(0-indexed)**.

## Constraints
- The number of nodes in the tree will be in the range `[0, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `root = [1,3,2,5,3,null,9]`
- **Output:** `[1,3,9]`

### Example 2
- **Input:** `root = [1,2,3]`
- **Output:** `[1,3]`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Largest Value in Each Tree Row**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,3,2,5,3,null,9]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,9]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List, Optional
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            row_max = float('-inf')
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.val > row_max:
                    row_max = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(row_max)
            
        return result
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [513. Find Bottom Left Tree Value](../../0501-1000/0513-find-bottom-left-tree-value/)
- [1738. Find Kth Largest XOR Coordinate Value](../../1501-2000/1738-find-kth-largest-xor-coordinate-value/)
- [2500. Delete Greatest Value in Each Row](../../2001-2500/2500-delete-greatest-value-in-each-row/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)
