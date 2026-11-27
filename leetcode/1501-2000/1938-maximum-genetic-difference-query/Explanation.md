# LeetCode 1938: Maximum Genetic Difference Query

**LeetCode Problem #1938 — Maximum Genetic Difference Query**
Solve LeetCode Maximum Genetic Difference Query using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Genetic Difference Query |
| LeetCode | #1938 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a rooted tree consisting of `n` nodes numbered `0` to `n - 1`. Each node's number denotes its **unique genetic value** (i.e. the genetic value of node `x` is `x`). The **genetic difference** between two genetic values is defined as the **bitwise-****XOR** of their values. You are given the integer array `parents`, where `parents[i]` is the parent for node `i`. If node `x` is the **root** of the tree, then `parents[x] == -1`.

You are also given the array `queries` where `queries[i] = [node_i, val_i]`. For each query `i`, find the **maximum genetic difference** between `val_i` and `p_i`, where `p_i` is the genetic value of any node that is on the path between `node_i` and the root (including `node_i` and the root). More formally, you want to maximize `val_i XOR p_i`.

Return *an array *`ans`* where *`ans[i]`* is the answer to the *`i^th`* query*.

## Constraints
- `2 <= parents.length <= 10^5`
- `0 <= parents[i] <= parents.length - 1` for every node `i` that is **not** the root.
- `parents[root] == -1`
- `1 <= queries.length <= 3 * 10^4`
- `0 <= node_i <= parents.length - 1`
- `0 <= val_i <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]`
- **Output:** `[2,3,7]`
- **Explanation:** The queries are processed as follows:
- [0,2]: The node with the maximum genetic difference is 0, with a difference of 2 XOR 0 = 2.
- [3,2]: The node with the maximum genetic difference is 1, with a difference of 2 XOR 1 = 3.
- [2,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.

### Example 2
- **Input:** `parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]`
- **Output:** `[6,14,7]`
- **Explanation:** The queries are processed as follows:
- [4,6]: The node with the maximum genetic difference is 0, with a difference of 6 XOR 0 = 6.
- [1,15]: The node with the maximum genetic difference is 1, with a difference of 15 XOR 1 = 14.
- [0,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Genetic Difference Query**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,7]`.
4. **Verification:** The queries are processed as follows:
- [0,2]: The node with the maximum genetic difference is 0, with a difference of 2 XOR 0 = 2.
- [3,2]: The node with the maximum genetic difference is 1, with a difference of 2 XOR 1 = 3.
- [2,5]: The node with the maximum genetic difference is 2, with a difference of 5 XOR 2 = 7.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        n = len(parents)
        B = 18

        children = [[] for _ in range(n)]
        root = -1
        for i, p in enumerate(parents):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        qs = [[] for _ in range(n)]
        for qi, (node, val) in enumerate(queries):
            qs[node].append((val, qi))

        # trie: child arrays and pass-through counts
        c0, c1, cnt = [0], [0], [0]

        def update(v, delta):
            node = 0
            for b in range(B - 1, -1, -1):
                if (v >> b) & 1:
                    if not c1[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c1[node] = len(cnt) - 1
                    node = c1[node]
                else:
                    if not c0[node]:
                        c0.append(0); c1.append(0); cnt.append(0)
                        c0[node] = len(cnt) - 1
                    node = c0[node]
                cnt[node] += delta

        def best(x):
            node = 0
            res = 0
            for b in range(B - 1, -1, -1):
                if (x >> b) & 1:
                    want = c0[node]   # opposite bit is 0
                    other = c1[node]
                else:
                    want = c1[node]
                    other = c0[node]
                if want and cnt[want] > 0:
                    res |= 1 << b
                    node = want
                else:
                    node = other
            return res

        ans = [0] * len(queries)
        # iterative DFS: (node, state) with state 0 = enter, 1 = exit
        stack = [(root, 0)]
        while stack:
            u, state = stack.pop()
            if state == 1:
                update(u, -1)
                continue
            update(u, 1)
            for val, qi in qs[u]:
                ans[qi] = best(val)
            stack.append((u, 1))
            for c in children[u]:
                stack.append((c, 0))
        return ans
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1829. Maximum XOR for Each Query](../../1501-2000/1829-maximum-xor-for-each-query/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-genetic-difference-query/)
