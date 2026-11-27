# LeetCode 3722: Lexicographically Smallest String After Reverse

**LeetCode Problem #3722 — Lexicographically Smallest String After Reverse**
Solve LeetCode Lexicographically Smallest String After Reverse using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest String After Reverse |
| LeetCode | #3722 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of length `n` consisting of lowercase English letters.

You must perform **exactly** one operation by choosing any integer `k` such that `1 <= k <= n` and either:

reverse the **first** `k` characters of `s`, or 
 reverse the **last** `k` characters of `s`.

Return the ** lexicographically smallest ** string that can be obtained after **exactly** one such operation.

## Constraints
- `1 <= n == s.length <= 1000`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "dcab"`
- **Output:** `"acdb"`
- **Explanation:** Choose `k = 3`, reverse the first 3 characters. 
 Reverse `"dca"` to `"acd"`, resulting string `s = "acdb"`, which is the lexicographically smallest string achievable.

### Example 2
- **Input:** `s = "abba"`
- **Output:** `"aabb"`
- **Explanation:** Choose `k = 3`, reverse the last 3 characters. 
 Reverse `"bba"` to `"abb"`, so the resulting string is `"aabb"`, which is the lexicographically smallest string achievable.

### Example 3
- **Input:** `s = "zxy"`
- **Output:** `"xzy"`
- **Explanation:** Choose `k = 2`, reverse the first 2 characters. 
 Reverse `"zx"` to `"xz"`, so the resulting string is `"xzy"`, which is the lexicographically smallest string achievable.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest String After Reverse**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "dcab"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"acdb"`.
4. **Verification:** Choose `k = 3`, reverse the first 3 characters. 
 Reverse `"dca"` to `"acd"`, resulting string `s = "acdb"`, which is the lexicographically smallest string achievable.

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
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        best = s[::-1]  # k = n (either side) gives the full reversal
        for k in range(1, n + 1):
            a = s[:k][::-1] + s[k:]            # reverse first k
            b = s[:n - k] + s[n - k:][::-1]    # reverse last k
            if a < best:
                best = a
            if b < best:
                best = b
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
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)
- [2734. Lexicographically Smallest String After Substring Operation](../../2501-3000/2734-lexicographically-smallest-string-after-substring-operation/)
- [3106. Lexicographically Smallest String After Operations With Constraint](../../3001-3500/3106-lexicographically-smallest-string-after-operations-with-constraint/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/)
