# LeetCode 2982: Find Longest Special Substring That Occurs Thrice II

**LeetCode Problem #2982 — Find Longest Special Substring That Occurs Thrice II**
Solve LeetCode Find Longest Special Substring That Occurs Thrice II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Longest Special Substring That Occurs Thrice II |
| LeetCode | #2982 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` that consists of lowercase English letters.

A string is called **special** if it is made up of only a single character. For example, the string `"abc"` is not special, whereas the strings `"ddd"`, `"zz"`, and `"f"` are special.

Return *the length of the **longest special substring** of *`s` *which occurs **at least thrice***, *or *`-1`* if no special substring occurs at least thrice*.

A **substring** is a contiguous **non-empty** sequence of characters within a string.

## Constraints
- `3 <= s.length <= 5 * 10^5`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aaaa"`
- **Output:** `2`
- **Explanation:** The longest special substring which occurs thrice is "aa": substrings "

### Example 2
- **Input:** `s = "abcdef"`
- **Output:** `-1`
- **Explanation:** There exists no special substring which occurs at least thrice. Hence return -1.

### Example 3
- **Input:** `s = "abcaba"`
- **Output:** `1`
- **Explanation:** The longest special substring which occurs thrice is "a": substrings "

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Longest Special Substring That Occurs Thrice II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaaa"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The longest special substring which occurs thrice is "aa": substrings "

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
    def maximumLength(self, s: str) -> int:
        top = [[0, 0, 0] for _ in range(26)]  # three longest runs per letter
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            L = j - i
            t = top[ord(s[i]) - 97]
            if L > t[0]:
                t[0], t[1], t[2] = L, t[0], t[1]
            elif L > t[1]:
                t[1], t[2] = L, t[1]
            elif L > t[2]:
                t[2] = L
            i = j

        ans = 0
        for a, b, c in top:
            ans = max(ans, a - 2, min(a - 1, b), c)
        return ans if ans >= 1 else -1
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
- [2981. Find Longest Special Substring That Occurs Thrice I](../../3001-3500/3267-find-longest-special-substring-that-occurs-thrice-i/)
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../../1001-1500/1473-find-the-longest-substring-containing-vowels-in-even-counts/)
- [1542. Find Longest Awesome Substring](../../1501-2000/1668-find-longest-awesome-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/)
