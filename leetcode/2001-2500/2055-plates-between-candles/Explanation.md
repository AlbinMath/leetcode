# LeetCode 2055: Plates Between Candles

**LeetCode Problem #2055 — Plates Between Candles**
Solve LeetCode Plates Between Candles using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Plates Between Candles |
| LeetCode | #2055 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is a long table with a line of plates and candles arranged on top of it. You are given a **0-indexed** string `s` consisting of characters `'*'` and `'|'` only, where a `'*'` represents a **plate** and a `'|'` represents a **candle**.

You are also given a **0-indexed** 2D integer array `queries` where `queries[i] = [left_i, right_i]` denotes the **substring** `s[left_i...right_i]` (**inclusive**). For each query, you need to find the **number** of plates **between candles** that are **in the substring**. A plate is considered **between candles** if there is at least one candle to its left **and** at least one candle to its right **in the substring**.

For example, `s = "||**||**|*"`, and a query `[3, 8]` denotes the substring `"*||** ** **|"`. The number of plates between candles in this substring is `2`, as each of the two plates has at least one candle **in the substring** to its left **and** right.

Return *an integer array* `answer` *where* `answer[i]` *is the answer to the* `i^th` *query*.

## Constraints
- `3 <= s.length <= 10^5`
- `s` consists of `'*'` and `'|'` characters.
- `1 <= queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= left_i <= right_i < s.length`

## Examples
### Example 1
- **Input:** `s = "**|**|***|", queries = [[2,5],[5,9]]`
- **Output:** `[2,3]`
- **Explanation:** - queries[0] has two plates between candles.
- queries[1] has three plates between candles.

### Example 2
- **Input:** `s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]`
- **Output:** `[9,0,0,0,0]`
- **Explanation:** - queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Plates Between Candles**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "**|**|***|", queries = [[2,5],[5,9]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.
4. **Verification:** - queries[0] has two plates between candles.
- queries[1] has three plates between candles.

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
from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s, queries):
        c = [i for i, ch in enumerate(s) if ch == '|']
        ans = []
        for l, r in queries:
            i = bisect_left(c, l)
            j = bisect_right(c, r) - 1
            ans.append(c[j] - c[i] - (j - i) if i < j else 0)
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
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1190. Reverse Substrings Between Each Pair of Parentheses](../../1001-1500/1190-reverse-substrings-between-each-pair-of-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/plates-between-candles/)
