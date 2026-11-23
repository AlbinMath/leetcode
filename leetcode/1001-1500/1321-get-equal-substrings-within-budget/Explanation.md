# LeetCode 1208: Get Equal Substrings Within Budget

**LeetCode Problem #1208 — Get Equal Substrings Within Budget**
Solve LeetCode Get Equal Substrings Within Budget using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get Equal Substrings Within Budget |
| LeetCode | #1208 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s` and `t` of the same length and an integer `maxCost`.

You want to change `s` to `t`. Changing the `i^th` character of `s` to `i^th` character of `t` costs `|s[i] - t[i]|` (i.e., the absolute difference between the ASCII values of the characters).

Return *the maximum length of a substring of *`s`* that can be changed to be the same as the corresponding substring of *`t`* with a cost less than or equal to *`maxCost`. If there is no substring from `s` that can be changed to its corresponding substring from `t`, return `0`.

## Constraints
- `1 <= s.length <= 10^5`
- `t.length == s.length`
- `0 <= maxCost <= 10^6`
- `s` and `t` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcd", t = "bcdf", maxCost = 3`
- **Output:** `3`
- **Explanation:** "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

### Example 2
- **Input:** `s = "abcd", t = "cdef", maxCost = 3`
- **Output:** `1`
- **Explanation:** Each character in s costs 2 to change to character in t, so the maximum length is 1.

### Example 3
- **Input:** `s = "abcd", t = "acde", maxCost = 0`
- **Output:** `1`
- **Explanation:** You cannot make any change, so the maximum length is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Get Equal Substrings Within Budget**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcd", t = "bcdf", maxCost = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

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
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        curr_cost = 0
        
        for right in range(len(s)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            if curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
                
        return len(s) - left
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
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3717-minimum-operations-to-make-elements-within-k-subarrays-equal/)
- [2398. Maximum Number of Robots Within Budget](../../2001-2500/2449-maximum-number-of-robots-within-budget/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/get-equal-substrings-within-budget/)
