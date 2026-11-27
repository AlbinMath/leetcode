# LeetCode 2663: Lexicographically Smallest Beautiful String

**LeetCode Problem #2663 — Lexicographically Smallest Beautiful String**
Solve LeetCode Lexicographically Smallest Beautiful String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest Beautiful String |
| LeetCode | #2663 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string is **beautiful** if:

It consists of the first `k` letters of the English lowercase alphabet. 
 It does not contain any substring of length `2` or more which is a palindrome.

You are given a beautiful string `s` of length `n` and a positive integer `k`.

Return *the lexicographically smallest string of length *`n`*, which is larger than *`s`* and is **beautiful***. If there is no such string, return an empty string.

A string `a` is lexicographically larger than a string `b` (of the same length) if in the first position where `a` and `b` differ, `a` has a character strictly larger than the corresponding character in `b`.

For example, `"abcd"` is lexicographically larger than `"abcc"` because the first position they differ is at the fourth character, and `d` is greater than `c`.

## Constraints
- `1 <= n == s.length <= 10^5`
- `4 <= k <= 26`
- `s` is a beautiful string.

## Examples
### Example 1
- **Input:** `s = "abcz", k = 26`
- **Output:** `"abda"`
- **Explanation:** The string "abda" is beautiful and lexicographically larger than the string "abcz".
It can be proven that there is no string that is lexicographically larger than the string "abcz", beautiful, and lexicographically smaller than the string "abda".

### Example 2
- **Input:** `s = "dc", k = 4`
- **Output:** `""`
- **Explanation:** It can be proven that there is no string that is lexicographically larger than the string "dc" and is beautiful.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest Beautiful String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcz", k = 26`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abda"`.
4. **Verification:** The string "abda" is beautiful and lexicographically larger than the string "abcz".
It can be proven that there is no string that is lexicographically larger than the string "abcz", beautiful, and lexicographically smaller than the string "abda".

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
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        a = [ord(c) - 97 for c in s]

        def ok(i: int, c: int) -> bool:
            if i >= 1 and a[i - 1] == c:
                return False
            if i >= 2 and a[i - 2] == c:
                return False
            return True

        for i in range(n - 1, -1, -1):
            for c in range(a[i] + 1, k):
                if ok(i, c):
                    a[i] = c
                    # fill the suffix greedily with the smallest valid letters
                    for j in range(i + 1, n):
                        for d in range(3):
                            if ok(j, d):
                                a[j] = d
                                break
                    return ''.join(chr(x + 97) for x in a)
        return ""
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
- [2904. Shortest and Lexicographically Smallest Beautiful String](../../2501-3000/2904-shortest-and-lexicographically-smallest-beautiful-string/)
- [1061. Lexicographically Smallest Equivalent String](../../1001-1500/1061-lexicographically-smallest-equivalent-string/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/)
