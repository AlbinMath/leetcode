# LeetCode 3714: Longest Balanced Substring II

**LeetCode Problem #3714 — Longest Balanced Substring II**
Solve LeetCode Longest Balanced Substring II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Balanced Substring II |
| LeetCode | #3714 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of the characters `'a'`, `'b'`, and `'c'`.

A ** substring ** of `s` is called **balanced** if all **distinct** characters in the **substring** appear the **same** number of times.

Return the **length of the longest balanced substring** of `s`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains only the characters `'a'`, `'b'`, and `'c'`.

## Examples
### Example 1
- **Input:** `s = "abbac"`
- **Output:** `4`
- **Explanation:** The longest balanced substring is `"abba"` because both distinct characters `'a'` and `'b'` each appear exactly 2 times.

### Example 2
- **Input:** `s = "aabcc"`
- **Output:** `3`
- **Explanation:** The longest balanced substring is `"abc"` because all distinct characters `'a'`, `'b'` and `'c'` each appear exactly 1 time.

### Example 3
- **Input:** `s = "aba"`
- **Output:** `2`
- **Explanation:** One of the longest balanced substrings is `"ab"` because both distinct characters `'a'` and `'b'` each appear exactly 1 time. Another longest balanced substring is `"ba"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Balanced Substring II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abbac"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest balanced substring is `"abba"` because both distinct characters `'a'` and `'b'` each appear exactly 2 times.

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
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        # Case 1: single repeated letter
        run = 0
        for i in range(n):
            run = run + 1 if i and s[i] == s[i - 1] else 1
            res = max(res, run)

        # Case 2: exactly two letters, third letter excluded
        for x, y, z in (('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'c', 'a')):
            first = {0: -1}
            diff = 0
            for i, ch in enumerate(s):
                if ch == z:
                    first = {0: i}
                    diff = 0
                    continue
                diff += 1 if ch == x else -1
                if diff in first:
                    res = max(res, i - first[diff])
                else:
                    first[diff] = i

        # Case 3: all three letters equal
        first = {(0, 0): -1}
        a = b = c = 0
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            key = (a - b, b - c)
            if key in first:
                res = max(res, i - first[key])
            else:
                first[key] = i

        return res
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
- [3713. Longest Balanced Substring I](../../3501-4000/3713-longest-balanced-substring-i/)
- [3900. Longest Balanced Substring After One Swap](../../3501-4000/3900-longest-balanced-substring-after-one-swap/)
- [1234. Replace the Substring for Balanced String](../../1001-1500/1234-replace-the-substring-for-balanced-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-balanced-substring-ii/)
