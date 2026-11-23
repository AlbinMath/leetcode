# LeetCode 1750: Minimum Length of String After Deleting Similar Ends

**LeetCode Problem #1750 — Minimum Length of String After Deleting Similar Ends**
Solve LeetCode Minimum Length of String After Deleting Similar Ends using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Length of String After Deleting Similar Ends |
| LeetCode | #1750 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` consisting only of characters `'a'`, `'b'`, and `'c'`. You are asked to apply the following algorithm on the string any number of times:

Pick a **non-empty** prefix from the string `s` where all the characters in the prefix are equal. 
 Pick a **non-empty** suffix from the string `s` where all the characters in this suffix are equal. 
 The prefix and the suffix should not intersect at any index. 
 The characters from the prefix and suffix must be the same. 
 Delete both the prefix and the suffix.

Return *the **minimum length** of *`s` *after performing the above operation any number of times (possibly zero times)*.

## Constraints
- `1 <= s.length <= 10^5`
- `s` only consists of characters `'a'`, `'b'`, and `'c'`.

## Examples
### Example 1
- **Input:** `s = "ca"`
- **Output:** `2`
- **Explanation:** You can't remove any characters, so the string stays as is.

### Example 2
- **Input:** `s = "cabaabac"`
- **Output:** `0`
- **Explanation:** An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

### Example 3
- **Input:** `s = "aabccabba"`
- **Output:** `3`
- **Explanation:** An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Length of String After Deleting Similar Ends**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ca"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** You can't remove any characters, so the string stays as is.

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
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r and s[l] == s[r]:
            ch = s[l]
            while l <= r and s[l] == ch:
                l += 1
            while r >= l and s[r] == ch:
                r -= 1

        return r - l + 1
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
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2800-minimum-string-length-after-removing-substrings/)
- [3223. Minimum Length of String After Operations](../../3001-3500/3455-minimum-length-of-string-after-operations/)
- [3746. Minimum String Length After Balanced Removals](../../4001-4500/4090-minimum-string-length-after-balanced-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/)
