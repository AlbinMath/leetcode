# LeetCode 3003: Maximize the Number of Partitions After Operations

**LeetCode Problem #3003 — Maximize the Number of Partitions After Operations**
Solve LeetCode Maximize the Number of Partitions After Operations using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximize the Number of Partitions After Operations |
| LeetCode | #3003 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and an integer `k`.

First, you are allowed to change **at most** **one** index in `s` to another lowercase English letter.

After that, do the following partitioning operation until `s` is **empty**:

Choose the **longest** **prefix** of `s` containing at most `k` **distinct** characters. 
 **Delete** the prefix from `s` and increase the number of partitions by one. The remaining characters (if any) in `s` maintain their initial order.

Return an integer denoting the **maximum** number of resulting partitions after the operations by optimally choosing at most one index to change.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists only of lowercase English letters.
- `1 <= k <= 26`

## Examples
### Example 1
- **Input:** `s = "accca", k = 2`
- **Output:** `3`
- **Explanation:** The optimal way is to change `s[2]` to something other than a and c, for example, b. then it becomes `"acbca"`. 

 Then we perform the operations: 

 
 The longest prefix containing at most 2 distinct characters is `"ac"`, we remove it and `s` becomes `"bca"`. 
 Now The longest prefix containing at most 2 distinct characters is `"bc"`, so we remove it and `s` becomes `"a"`. 
 Finally, we remove `"a"` and `s` becomes empty, so the procedure ends. 
 

 Doing the operations, the string is divided into 3 partitions, so the answer is 3.

### Example 2
- **Input:** `s = "aabaab", k = 3`
- **Output:** `1`
- **Explanation:** Initially `s` contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

### Example 3
- **Input:** `s = "xxyz", k = 1`
- **Output:** `4`
- **Explanation:** The optimal way is to change `s[0]` or `s[1]` to something other than characters in `s`, for example, to change `s[0]` to `w`. 

 Then `s` becomes `"wxyz"`, which consists of 4 distinct characters, so as `k` is 1, it will divide into 4 partitions.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximize the Number of Partitions After Operations**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "accca", k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The optimal way is to change `s[2]` to something other than a and c, for example, b. then it becomes `"acbca"`. 

 Then we perform the operations: 

 
 The longest prefix containing at most 2 distinct characters is `"ac"`, we remove it and `s` becomes `"bca"`. 
 Now The longest prefix containing at most 2 distinct characters is `"bc"`, so we remove it and `s` becomes `"a"`. 
 Finally, we remove `"a"` and `s` becomes empty, so the procedure ends. 
 

 Doing the operations, the string is divided into 3 partitions, so the answer is 3.

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
import sys
from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        sys.setrecursionlimit(30000)
        n = len(s)

        @lru_cache(maxsize=None)
        def dfs(i: int, mask: int, can_change: bool) -> int:
            if i == n:
                return 1

            bit = 1 << (ord(s[i]) - 97)
            nm = mask | bit
            if nm.bit_count() > k:
                res = dfs(i + 1, bit, can_change) + 1
            else:
                res = dfs(i + 1, nm, can_change)

            if can_change:
                for j in range(26):
                    b = 1 << j
                    nm = mask | b
                    if nm.bit_count() > k:
                        res = max(res, dfs(i + 1, b, False) + 1)
                    else:
                        res = max(res, dfs(i + 1, nm, False))
            return res

        return dfs(0, 0, True)
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
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [3372. Maximize the Number of Target Nodes After Connecting Trees I](../../3001-3500/3372-maximize-the-number-of-target-nodes-after-connecting-trees-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/)
