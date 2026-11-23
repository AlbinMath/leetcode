# LeetCode 44: Wildcard Matching

**LeetCode Problem #44 — Wildcard Matching**
Solve LeetCode Wildcard Matching using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Wildcard Matching |
| LeetCode | #44 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'` where:

`'?'` Matches any single character. 
 `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

## Constraints
- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'` or `'*'`.

## Examples
### Example 1
- **Input:** `s = "aa", p = "a"`
- **Output:** `false`
- **Explanation:** "a" does not match the entire string "aa".

### Example 2
- **Input:** `s = "aa", p = "*"`
- **Output:** `true`
- **Explanation:** '*' matches any sequence.

### Example 3
- **Input:** `s = "cb", p = "?a"`
- **Output:** `false`
- **Explanation:** '?' matches 'c', but the second letter is 'a', which does not match 'b'.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Wildcard Matching**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aa", p = "a"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** "a" does not match the entire string "aa".

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
    def isMatch(self, s, p):
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Case 1: Characters match or pattern has '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # Case 2: We found '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1

            # Case 3: Mismatch, but we have seen a '*'
            elif star != -1:
                j = star + 1
                match += 1
                i = match

            # Case 4: Mismatch and no '*'
            else:
                return False

        # Remaining pattern must contain only '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
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
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [792. Number of Matching Subsequences](../../0501-1000/0808-number-of-matching-subsequences/)
- [1023. Camelcase Matching](../../1001-1500/1080-camelcase-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/wildcard-matching/)
