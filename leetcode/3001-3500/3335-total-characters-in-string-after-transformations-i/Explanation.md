# LeetCode 3335: Total Characters in String After Transformations I

**LeetCode Problem #3335 — Total Characters in String After Transformations I**
Solve LeetCode Total Characters in String After Transformations I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Characters in String After Transformations I |
| LeetCode | #3335 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and an integer `t`, representing the number of **transformations** to perform. In one **transformation**, every character in `s` is replaced according to the following rules:

If the character is `'z'`, replace it with the string `"ab"`. 
 Otherwise, replace it with the **next** character in the alphabet. For example, `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.

Return the **length** of the resulting string after **exactly** `t` transformations.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.
- `1 <= t <= 10^5`

## Examples
### Example 1
- **Input:** `s = "abcyy", t = 2`
- **Output:** `7`

### Example 2
- **Input:** `s = "azbk", t = 1`
- **Output:** `5`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Total Characters in String After Transformations I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcyy", t = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.

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
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26
        
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
            
        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[0] + cnt[25]) % MOD
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
            
        return sum(cnt) % MOD
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
- [3337. Total Characters in String After Transformations II](../../3001-3500/3337-total-characters-in-string-after-transformations-ii/)
- [4036. Lexicographically Largest String After Pair Transformations](../../4001-4500/4036-lexicographically-largest-string-after-pair-transformations/)
- [3816. Lexicographically Smallest String After Deleting Duplicate Characters](../../3501-4000/3816-lexicographically-smallest-string-after-deleting-duplicate-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-characters-in-string-after-transformations-i/)
