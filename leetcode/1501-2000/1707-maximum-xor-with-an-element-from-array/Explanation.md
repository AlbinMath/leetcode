# LeetCode 1707: Maximum XOR With an Element From Array

**LeetCode Problem #1707 — Maximum XOR With an Element From Array**
Solve LeetCode Maximum XOR With an Element From Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum XOR With an Element From Array |
| LeetCode | #1707 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of non-negative integers. You are also given a `queries` array, where `queries[i] = [x_i, m_i]`.

The answer to the `i^th` query is the maximum bitwise `XOR` value of `x_i` and any element of `nums` that does not exceed `m_i`. In other words, the answer is `max(nums[j] XOR x_i)` for all `j` such that `nums[j] <= m_i`. If all elements in `nums` are larger than `m_i`, then the answer is `-1`.

Return *an integer array *`answer`* where *`answer.length == queries.length`* and *`answer[i]`* is the answer to the *`i^th`* query.*

## Constraints
- `1 <= nums.length, queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= nums[j], x_i, m_i <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]`
- **Output:** `[3,3,7]`
- **Explanation:** 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

### Example 2
- **Input:** `nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]`
- **Output:** `[15,-1,5]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum XOR With an Element From Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,3,7]`.
4. **Verification:** 1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

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
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        order = sorted(range(len(queries)), key=lambda i: queries[i][1])

        # trie stored as two child arrays
        left = [0]   # child for bit 0 (0 means none; root is node 0)
        right = [0]  # child for bit 1

        def insert(v):
            node = 0
            for b in range(29, -1, -1):
                if (v >> b) & 1:
                    if not right[node]:
                        left.append(0); right.append(0)
                        right[node] = len(left) - 1
                    node = right[node]
                else:
                    if not left[node]:
                        left.append(0); right.append(0)
                        left[node] = len(left) - 1
                    node = left[node]

        ans = [-1] * len(queries)
        p = 0
        n = len(nums)
        for qi in order:
            x, m = queries[qi]
            while p < n and nums[p] <= m:
                insert(nums[p])
                p += 1
            if p == 0:
                continue  # no element <= m
            node = 0
            res = 0
            for b in range(29, -1, -1):
                bit = (x >> b) & 1
                if bit:  # want a 0 child
                    if left[node]:
                        res |= 1 << b
                        node = left[node]
                    else:
                        node = right[node]
                else:    # want a 1 child
                    if right[node]:
                        res |= 1 << b
                        node = right[node]
                    else:
                        node = left[node]
            ans[qi] = res
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2091-removing-minimum-and-maximum-from-array/)
- [3630. Partition Array for Maximum XOR and AND](../../3501-4000/3630-partition-array-for-maximum-xor-and-and/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)
