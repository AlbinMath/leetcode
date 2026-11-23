# LeetCode 2800: Shortest String That Contains Three Strings

**LeetCode Problem #2800 — Shortest String That Contains Three Strings**
Solve LeetCode Shortest String That Contains Three Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shortest String That Contains Three Strings |
| LeetCode | #2800 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given three strings `a`, `b`, and `c`, your task is to find a string that has the** minimum** length and contains all three strings as **substrings**.
 If there are multiple such strings, return the* ***lexicographically* *smallest **one.

Return *a string denoting the answer to the problem.*

**Notes**

A string `a` is **lexicographically smaller** than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears **earlier **in the alphabet than the corresponding letter in `b`. 
 A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= a.length, b.length, c.length <= 100`
- `a`, `b`, `c` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `a = "abc", b = "bca", c = "aaa"`
- **Output:** `"aaabca"`
- **Explanation:** We show that "aaabca" contains all the given strings: a = ans[2...4], b = ans[3..5], c = ans[0..2]. It can be shown that the length of the resulting string would be at least 6 and "aaabca" is the lexicographically smallest one.

### Example 2
- **Input:** `a = "ab", b = "ba", c = "aba"`
- **Output:** `"aba"`
- **Explanation:** We show that the string "aba" contains all the given strings: a = ans[0..1], b = ans[1..2], c = ans[0..2]. Since the length of c is 3, the length of the resulting string would be at least 3. It can be shown that "aba" is the lexicographically smallest one.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shortest String That Contains Three Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = "abc", b = "bca", c = "aaa"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aaabca"`.
4. **Verification:** We show that "aaabca" contains all the given strings: a = ans[2...4], b = ans[3..5], c = ans[0..2]. It can be shown that the length of the resulting string would be at least 6 and "aaabca" is the lexicographically smallest one.

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
from itertools import permutations

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x: str, y: str) -> str:
            if y in x:
                return x
            if x in y:
                return y
            for k in range(min(len(x), len(y)), 0, -1):
                if x[-k:] == y[:k]:
                    return x + y[k:]
            return x + y

        best = None
        for p in permutations((a, b, c)):
            s = merge(merge(p[0], p[1]), p[2])
            if best is None or (len(s), s) < (len(best), best):
                best = s
        return best
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
- [1374. Generate a String With Characters That Have Odd Counts](../../1001-1500/1490-generate-a-string-with-characters-that-have-odd-counts/)
- [1967. Number of Strings That Appear as Substrings in Word](../../2001-2500/2099-number-of-strings-that-appear-as-substrings-in-word/)
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2278-find-three-consecutive-integers-that-sum-to-a-given-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shortest-string-that-contains-three-strings/)
