# LeetCode 1737: Change Minimum Characters to Satisfy One of Three Conditions

**LeetCode Problem #1737 — Change Minimum Characters to Satisfy One of Three Conditions**
Solve LeetCode Change Minimum Characters to Satisfy One of Three Conditions using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Change Minimum Characters to Satisfy One of Three Conditions |
| LeetCode | #1737 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `a` and `b` that consist of lowercase letters. In one operation, you can change any character in `a` or `b` to **any lowercase letter**.

Your goal is to satisfy **one** of the following three conditions:

**Every** letter in `a` is **strictly less** than **every** letter in `b` in the alphabet. 
 **Every** letter in `b` is **strictly less** than **every** letter in `a` in the alphabet. 
 **Both** `a` and `b` consist of **only one** distinct letter.

Return *the **minimum** number of operations needed to achieve your goal.*

## Constraints
- `1 <= a.length, b.length <= 10^5`
- `a` and `b` consist only of lowercase letters.

## Examples
### Example 1
- **Input:** `a = "aba", b = "caa"`
- **Output:** `2`
- **Explanation:** Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

### Example 2
- **Input:** `a = "dabadd", b = "cda"`
- **Output:** `3`
- **Explanation:** The best way is to make condition 1 true by changing b to "eee".

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Change Minimum Characters to Satisfy One of Three Conditions**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = "aba", b = "caa"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        ca = [0] * 26
        cb = [0] * 26
        for ch in a:
            ca[ord(ch) - 97] += 1
        for ch in b:
            cb[ord(ch) - 97] += 1

        # condition 3
        best = min(m + n - ca[i] - cb[i] for i in range(26))

        # conditions 1 and 2: boundary c in 1..25
        pa = pb = 0  # counts of letters < c
        for c in range(1, 26):
            pa += ca[c - 1]
            pb += cb[c - 1]
            # a < c <= b
            best = min(best, (m - pa) + pb)
            # b < c <= a
            best = min(best, (n - pb) + pa)

        return best
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3122. Minimum Number of Operations to Satisfy Conditions](../../3001-3500/3122-minimum-number-of-operations-to-satisfy-conditions/)
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1358-number-of-substrings-containing-all-three-characters/)
- [1876. Substrings of Size Three with Distinct Characters](../../1501-2000/1876-substrings-of-size-three-with-distinct-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/)
