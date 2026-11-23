# LeetCode 1898: Maximum Number of Removable Characters

**LeetCode Problem #1898 — Maximum Number of Removable Characters**
Solve LeetCode Maximum Number of Removable Characters using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Removable Characters |
| LeetCode | #1898 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `p` where `p` is a **subsequence **of `s`. You are also given a **distinct 0-indexed **integer array `removable` containing a subset of indices of `s` (`s` is also **0-indexed**).

You want to choose an integer `k` (`0 <= k <= removable.length`) such that, after removing `k` characters from `s` using the **first** `k` indices in `removable`, `p` is still a **subsequence** of `s`. More formally, you will mark the character at `s[removable[i]]` for each `0 <= i < k`, then remove all marked characters and check if `p` is still a subsequence.

Return *the **maximum** *`k`* you can choose such that *`p`* is still a **subsequence** of *`s`* after the removals*.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Constraints
- `1 <= p.length <= s.length <= 10^5`
- `0 <= removable.length < s.length`
- `0 <= removable[i] < s.length`
- `p` is a **subsequence** of `s`.
- `s` and `p` both consist of lowercase English letters.
- The elements in `removable` are **distinct**.

## Examples
### Example 1
- **Input:** `s = "abcacb", p = "ab", removable = [3,1,0]`
- **Output:** `2`
- **Explanation:** : After removing the characters at indices 3 and 1, "a

### Example 2
- **Input:** `s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]`
- **Output:** `1`
- **Explanation:** : After removing the character at index 3, "abc

### Example 3
- **Input:** `s = "abcab", p = "abc", removable = [0,1,2,3,4]`
- **Output:** `0`
- **Explanation:** : If you remove the first index in the array removable, "abc" is no longer a subsequence.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Removable Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcacb", p = "ab", removable = [3,1,0]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** : After removing the characters at indices 3 and 1, "a

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        n = len(s)
        INF = len(removable) + 1
        removed_at = [INF] * n
        for step, idx in enumerate(removable):
            removed_at[idx] = step

        def ok(k: int) -> bool:
            j = 0
            m = len(p)
            for i in range(n):
                if removed_at[i] < k:
                    continue
                if s[i] == p[j]:
                    j += 1
                    if j == m:
                        return True
            return False

        lo, hi = 0, len(removable)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [414. Third Maximum Number](../../0001-0500/0414-third-maximum-number/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1147-flip-columns-for-maximum-number-of-equal-rows/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-removable-characters/)
