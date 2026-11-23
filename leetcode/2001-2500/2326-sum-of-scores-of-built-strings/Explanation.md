# LeetCode 2223: Sum of Scores of Built Strings

**LeetCode Problem #2223 — Sum of Scores of Built Strings**
Solve LeetCode Sum of Scores of Built Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Scores of Built Strings |
| LeetCode | #2223 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are **building** a string `s` of length `n` **one** character at a time, **prepending** each new character to the **front** of the string. The strings are labeled from `1` to `n`, where the string with length `i` is labeled `s_i`.

For example, for `s = "abaca"`, `s_1 == "a"`, `s_2 == "ca"`, `s_3 == "aca"`, etc.

The **score** of `s_i` is the length of the **longest common prefix** between `s_i` and `s_n` (Note that `s == s_n`).

Given the final string `s`, return* the **sum** of the **score** of every *`s_i`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "babab"`
- **Output:** `9`
- **Explanation:** For s_1 == "b", the longest common prefix is "b" which has a score of 1.
For s_2 == "ab", there is no common prefix so the score is 0.
For s_3 == "bab", the longest common prefix is "bab" which has a score of 3.
For s_4 == "abab", there is no common prefix so the score is 0.
For s_5 == "babab", the longest common prefix is "babab" which has a score of 5.
The sum of the scores is 1 + 0 + 3 + 0 + 5 = 9, so we return 9.

### Example 2
- **Input:** `s = "azbazbzaz"`
- **Output:** `14`
- **Explanation:** For s_2 == "az", the longest common prefix is "az" which has a score of 2.
For s_6 == "azbzaz", the longest common prefix is "azb" which has a score of 3.
For s_9 == "azbazbzaz", the longest common prefix is "azbazbzaz" which has a score of 9.
For all other s_i, the score is 0.
The sum of the scores is 2 + 3 + 9 = 14, so we return 14.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Scores of Built Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "babab"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** For s_1 == "b", the longest common prefix is "b" which has a score of 1.
For s_2 == "ab", there is no common prefix so the score is 0.
For s_3 == "bab", the longest common prefix is "bab" which has a score of 3.
For s_4 == "abab", there is no common prefix so the score is 0.
For s_5 == "babab", the longest common prefix is "babab" which has a score of 5.
The sum of the scores is 1 + 0 + 3 + 0 + 5 = 9, so we return 9.

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
    def sumScores(self, s: str) -> int:
        n = len(s)
        z = [0] * n
        l = r = 0

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])

            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1

            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        return n + sum(z)
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
- [2416. Sum of Prefix Scores of Strings](../../2001-2500/2494-sum-of-prefix-scores-of-strings/)
- [712. Minimum ASCII Delete Sum for Two Strings](../../0501-1000/0712-minimum-ascii-delete-sum-for-two-strings/)
- [178. Rank Scores](../../0001-0500/0178-rank-scores/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-scores-of-built-strings/)
