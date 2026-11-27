# LeetCode 3261: Count Substrings That Satisfy K-Constraint II

**LeetCode Problem #3261 — Count Substrings That Satisfy K-Constraint II**
Solve LeetCode Count Substrings That Satisfy K-Constraint II using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Substrings That Satisfy K-Constraint II |
| LeetCode | #3261 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **binary** string `s` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

The number of `0`'s in the string is at most `k`. 
 The number of `1`'s in the string is at most `k`.

Return an integer array `answer`, where `answer[i]` is the number of substrings of `s[l_i..r_i]` that satisfy the **k-constraint**.

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= k <= s.length`
- `1 <= queries.length <= 10^5`
- `queries[i] == [l_i, r_i]`
- `0 <= l_i <= r_i < s.length`
- All queries are distinct.

## Examples
### Example 1
- **Input:** `s = "0001111", k = 2, queries = [[0,6]]`
- **Output:** `[26]`
- **Explanation:** For the query `[0, 6]`, all substrings of `s[0..6] = "0001111"` satisfy the k-constraint except for the substrings `s[0..5] = "000111"` and `s[0..6] = "0001111"`.

### Example 2
- **Input:** `s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]`
- **Output:** `[15,9,3]`
- **Explanation:** The substrings of `s` with a length greater than 3 do not satisfy the k-constraint.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Count Substrings That Satisfy K-Constraint II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0001111", k = 2, queries = [[0,6]]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[26]`.
4. **Verification:** For the query `[0, 6]`, all substrings of `s[0..6] = "0001111"` satisfy the k-constraint except for the substrings `s[0..5] = "000111"` and `s[0..6] = "0001111"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from bisect import bisect_left

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        R = [0] * n
        zeros = ones = 0
        j = 0  # window is [i, j), j exclusive
        for i in range(n):
            while j < n:
                z = zeros + (s[j] == '0')
                o = ones + (s[j] == '1')
                if z <= k or o <= k:
                    zeros, ones = z, o
                    j += 1
                else:
                    break
            R[i] = j - 1
            if s[i] == '0':
                zeros -= 1
            else:
                ones -= 1

        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + (R[i] - i + 1)

        ans = []
        for l, r in queries:
            p = bisect_left(R, r, l, r + 1)   # first i in [l, r] with R[i] >= r
            m = r - p + 1
            ans.append(pre[p] - pre[l] + m * (m + 1) // 2)
        return ans
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [3258. Count Substrings That Satisfy K-Constraint I](../../3001-3500/3258-count-substrings-that-satisfy-k-constraint-i/)
- [3305. Count of Substrings Containing Every Vowel and K Consonants I](../../3001-3500/3305-count-of-substrings-containing-every-vowel-and-k-consonants-i/)
- [3306. Count of Substrings Containing Every Vowel and K Consonants II](../../3001-3500/3306-count-of-substrings-containing-every-vowel-and-k-consonants-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/)
