# LeetCode 1315: Sum of Nodes with Even-Valued Grandparent

**LeetCode Problem #1315 — Sum of Nodes with Even-Valued Grandparent**
Solve LeetCode Sum of Nodes with Even-Valued Grandparent using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Nodes with Even-Valued Grandparent |
| LeetCode | #1315 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return *the sum of values of nodes with an **even-valued grandparent***. If there are no nodes with an **even-valued grandparent**, return `0`.

A **grandparent** of a node is the parent of its parent if it exists.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 100`

## Examples
### Example 1
- **Input:** `root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]`
- **Output:** `18`
- **Explanation:** The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

### Example 2
- **Input:** `root = [1]`
- **Output:** `0`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Sum of Nodes with Even-Valued Grandparent**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import Optional

class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent, grand):
            if not node:
                return 0
            total = node.val if grand % 2 == 0 else 0
            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            return total

        return dfs(root, 1, 1)
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [985. Sum of Even Numbers After Queries](../../0501-1000/0985-sum-of-even-numbers-after-queries/)
- [2074. Reverse Nodes in Even Length Groups](../../2001-2500/2074-reverse-nodes-in-even-length-groups/)
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)
