# LeetCode 647: Palindromic Substrings

**LeetCode Problem #647 — Palindromic Substrings**
Solve LeetCode Palindromic Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindromic Substrings |
| LeetCode | #647 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc"`
- **Output:** `3`
- **Explanation:** Three palindromic strings: "a", "b", "c".

### Example 2
- **Input:** `s = "aaa"`
- **Output:** `6`
- **Explanation:** Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Palindromic Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Three palindromic strings: "a", "b", "c".

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
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(l: int, r: int) -> int:
            c = 0
            while l >= 0 and r < n and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c

        for center in range(n):
            count += expand(center, center)      # odd length
            count += expand(center, center + 1)  # even length

        return count
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
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1001-1500/1336-maximum-product-of-the-length-of-two-palindromic-substrings/)
- [467. Unique Substrings in Wraparound String](../../0001-0500/0467-unique-substrings-in-wraparound-string/)
- [696. Count Binary Substrings](../../0501-1000/0696-count-binary-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindromic-substrings/)
