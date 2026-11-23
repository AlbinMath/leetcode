# LeetCode 1361: Validate Binary Tree Nodes

**LeetCode Problem #1361 — Validate Binary Tree Nodes**
Solve LeetCode Validate Binary Tree Nodes using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Validate Binary Tree Nodes |
| LeetCode | #1361 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `n` binary tree nodes numbered from `0` to `n - 1` where node `i` has two children `leftChild[i]` and `rightChild[i]`, return `true` if and only if **all** the given nodes form **exactly one** valid binary tree.

If node `i` has no left child then `leftChild[i]` will equal `-1`, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

## Constraints
- `n == leftChild.length == rightChild.length`
- `1 <= n <= 10^4`
- `-1 <= leftChild[i], rightChild[i] <= n - 1`

## Examples
### Example 1
- **Input:** `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]`
- **Output:** `true`

### Example 2
- **Input:** `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]`
- **Output:** `false`

### Example 3
- **Input:** `n = 2, leftChild = [1,0], rightChild = [-1,-1]`
- **Output:** `false`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Validate Binary Tree Nodes**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import deque
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degree = [0] * n

        # 1. Compute in-degree for each node
        for child in leftChild + rightChild:
            if child != -1:
                in_degree[child] += 1
                if in_degree[child] > 1:
                    return False  # A node cannot have more than one parent

        # 2. Identify the single root candidate (in-degree == 0)
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                if root != -1:
                    return False  # Multiple roots -> multiple disconnected trees
                root = i

        if root == -1:
            return False  # Cycle among all nodes (no root)

        # 3. BFS traversal to verify connectivity and absence of cycles
        visited = [False] * n
        queue = deque([root])
        visited[root] = True
        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    if visited[child]:
                        return False  # Cycle detected
                    visited[child] = True
                    queue.append(child)

        # All n nodes must be reachable from the root
        return count == n
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
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [863. All Nodes Distance K in Binary Tree](../../0501-1000/0893-all-nodes-distance-k-in-binary-tree/)
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/validate-binary-tree-nodes/)
