# LeetCode 1392: Longest Happy Prefix

**LeetCode Problem #1392 — Longest Happy Prefix**
Solve LeetCode Longest Happy Prefix using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Happy Prefix |
| LeetCode | #1392 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A string is called a **happy prefix** if it is a **non-empty** prefix which is also a suffix (excluding itself).

Given a string `s`, return *the **longest happy prefix** of* `s`. Return an empty string `""` if no such prefix exists.

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "level"`
- **Output:** `"l"`
- **Explanation:** s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

### Example 2
- **Input:** `s = "ababab"`
- **Output:** `"abab"`
- **Explanation:** "abab" is the largest prefix which is also suffix. They can overlap in the original string.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Happy Prefix**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "level"`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"l"`.
4. **Verification:** s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        j = 0

        for i in range(1, len(s)):
            while j and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j

        return s[:lps[-1]]
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1405. Longest Happy String](../../1001-1500/1304-longest-happy-string/)
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [2424. Longest Uploaded Prefix](../../2501-3000/2512-longest-uploaded-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-happy-prefix/)
