# LeetCode 2003: Smallest Missing Genetic Value in Each Subtree

**LeetCode Problem #2003 — Smallest Missing Genetic Value in Each Subtree**
Solve LeetCode Smallest Missing Genetic Value in Each Subtree using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Genetic Value in Each Subtree |
| LeetCode | #2003 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a **family tree** rooted at `0` consisting of `n` nodes numbered `0` to `n - 1`. You are given a **0-indexed** integer array `parents`, where `parents[i]` is the parent for node `i`. Since node `0` is the **root**, `parents[0] == -1`.

There are `10^5` genetic values, each represented by an integer in the **inclusive** range `[1, 10^5]`. You are given a **0-indexed** integer array `nums`, where `nums[i]` is a **distinct **genetic value for node `i`.

Return *an array *`ans`* of length *`n`* where *`ans[i]`* is* *the **smallest** genetic value that is **missing** from the subtree rooted at node* `i`.

The **subtree** rooted at a node `x` contains node `x` and all of its **descendant** nodes.

## Constraints
- `n == parents.length == nums.length`
- `2 <= n <= 10^5`
- `0 <= parents[i] <= n - 1` for `i != 0`
- `parents[0] == -1`
- `parents` represents a valid tree.
- `1 <= nums[i] <= 10^5`
- Each `nums[i]` is distinct.

## Examples
### Example 1
- **Input:** `parents = [-1,0,0,2], nums = [1,2,3,4]`
- **Output:** `[5,1,1,1]`
- **Explanation:** The answer for each subtree is calculated as follows:
- 0: The subtree contains nodes [0,1,2,3] with values [1,2,3,4]. 5 is the smallest missing value.
- 1: The subtree contains only node 1 with value 2. 1 is the smallest missing value.
- 2: The subtree contains nodes [2,3] with values [3,4]. 1 is the smallest missing value.
- 3: The subtree contains only node 3 with value 4. 1 is the smallest missing value.

### Example 2
- **Input:** `parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]`
- **Output:** `[7,1,1,4,2,1]`
- **Explanation:** The answer for each subtree is calculated as follows:
- 0: The subtree contains nodes [0,1,2,3,4,5] with values [5,4,6,2,1,3]. 7 is the smallest missing value.
- 1: The subtree contains nodes [1,2] with values [4,6]. 1 is the smallest missing value.
- 2: The subtree contains only node 2 with value 6. 1 is the smallest missing value.
- 3: The subtree contains nodes [3,4,5] with values [2,1,3]. 4 is the smallest missing value.
- 4: The subtree contains only node 4 with value 1. 2 is the smallest missing value.
- 5: The subtree contains only node 5 with value 3. 1 is the smallest missing value.

### Example 3
- **Input:** `parents = [-1,2,3,0,2,4,1], nums = [2,3,4,5,6,7,8]`
- **Output:** `[1,1,1,1,1,1,1]`
- **Explanation:** The value 1 is missing from all the subtrees.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Missing Genetic Value in Each Subtree**, we observe the problem requirements and utilize the **Prefix Sum** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parents = [-1,0,0,2], nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,1,1,1]`.
4. **Verification:** The answer for each subtree is calculated as follows:
- 0: The subtree contains nodes [0,1,2,3] with values [1,2,3,4]. 5 is the smallest missing value.
- 1: The subtree contains only node 1 with value 2. 1 is the smallest missing value.
- 2: The subtree contains nodes [2,3] with values [3,4]. 1 is the smallest missing value.
- 3: The subtree contains only node 3 with value 4. 1 is the smallest missing value.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import sys
from typing import List

# Extend recursion limit for deep chain trees
sys.setrecursionlimit(200000)

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n

        # If 1 is not present, all subtrees are missing 1
        if 1 not in nums:
            return ans

        # Build adjacency list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        # Track observed genetic values and visited nodes
        seen_vals = [False] * 100005
        visited_nodes = [False] * n

        def dfs(u: int):
            visited_nodes[u] = True
            if nums[u] <= 100002:
                seen_vals[nums[u]] = True
            for child in children[u]:
                if not visited_nodes[child]:
                    dfs(child)

        curr = nums.index(1)
        missing = 1

        # Walk up from node with 1 to the root
        while curr != -1:
            dfs(curr)
            while seen_vals[missing]:
                missing += 1
            ans[curr] = missing
            curr = parents[curr]

        return ans
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)
- [2500. Delete Greatest Value in Each Row](../../2001-2500/2500-delete-greatest-value-in-each-row/)
- [2598. Smallest Missing Non-negative Integer After Operations](../../2501-3000/2598-smallest-missing-non-negative-integer-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/)
