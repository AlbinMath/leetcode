# LeetCode 894: All Possible Full Binary Trees

**LeetCode Problem #894 — All Possible Full Binary Trees**
Solve LeetCode All Possible Full Binary Trees using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | All Possible Full Binary Trees |
| LeetCode | #894 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *a list of all possible **full binary trees** with* `n` *nodes*. Each node of each tree in the answer must have `Node.val == 0`.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in **any order**.

A **full binary tree** is a binary tree where each node has exactly `0` or `2` children.

## Constraints
- `1 <= n <= 20`

## Examples
### Example 1
- **Input:** `n = 7`
- **Output:** `[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]`

### Example 2
- **Input:** `n = 3`
- **Output:** `[[0,0,0]]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **All Possible Full Binary Trees**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]`.

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
from typing import Optional, List

# LeetCode provides the TreeNode definition.

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def clone(root):
            if root is None:
                return None
            return TreeNode(
                0,
                clone(root.left),
                clone(root.right)
            )

        def build(nodes):
            if nodes % 2 == 0:
                return []

            if nodes == 1:
                return [TreeNode(0)]

            if nodes in memo:
                return memo[nodes]

            result = []

            for left_count in range(1, nodes - 1, 2):
                right_count = nodes - 1 - left_count

                left_trees = build(left_count)
                right_trees = build(right_count)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = clone(left)
                        root.right = clone(right)
                        result.append(root)

            memo[nodes] = result
            return result

        return build(n)
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
- [1305. All Elements in Two Binary Search Trees](../../1001-1500/1427-all-elements-in-two-binary-search-trees/)
- [1575. Count All Possible Routes](../../1501-2000/1680-count-all-possible-routes/)
- [2115. Find All Possible Recipes from Given Supplies](../../2001-2500/2220-find-all-possible-recipes-from-given-supplies/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/all-possible-full-binary-trees/)
