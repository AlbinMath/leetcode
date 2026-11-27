# LeetCode 2385: Amount of Time for Binary Tree to Be Infected

**LeetCode Problem #2385 — Amount of Time for Binary Tree to Be Infected**
Solve LeetCode Amount of Time for Binary Tree to Be Infected using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Amount of Time for Binary Tree to Be Infected |
| LeetCode | #2385 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the `root` of a binary tree with **unique** values, and an integer `start`. At minute `0`, an **infection** starts from the node with value `start`.

Each minute, a node becomes infected if:

The node is currently uninfected. 
 The node is adjacent to an infected node.

Return *the number of minutes needed for the entire tree to be infected.*

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
- Each node has a **unique** value.
- A node with a value of `start` exists in the tree.

## Examples
### Example 1
- **Input:** `root = [1,5,3,null,4,10,6,9,2], start = 3`
- **Output:** `4`
- **Explanation:** The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

### Example 2
- **Input:** `root = [1], start = 1`
- **Output:** `0`
- **Explanation:** At minute 0, the only node in the tree is infected so we return 0.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Amount of Time for Binary Tree to Be Infected**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [1,5,3,null,4,10,6,9,2], start = 3`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

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
from collections import deque, defaultdict
from typing import Optional

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    adj[node.val].append(child.val)
                    adj[child.val].append(node.val)
                    stack.append(child)

        seen = {start}
        q = deque([start])
        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                u = q.popleft()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
        return minutes
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
- [94. Binary Tree Inorder Traversal](../../0001-0500/0094-binary-tree-inorder-traversal/)
- [98. Validate Binary Search Tree](../../0001-0500/0098-validate-binary-search-tree/)
- [99. Recover Binary Search Tree](../../0001-0500/0099-recover-binary-search-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/)
