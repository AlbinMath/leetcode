# LeetCode 2734: Lexicographically Smallest String After Substring Operation

**LeetCode Problem #2734 — Lexicographically Smallest String After Substring Operation**
Solve LeetCode Lexicographically Smallest String After Substring Operation using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest String After Substring Operation |
| LeetCode | #2734 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` consisting of lowercase English letters. Perform the following operation:

Select any non-empty substring then replace every letter of the substring with the preceding letter of the English alphabet. For example, 'b' is converted to 'a', and 'a' is converted to 'z'.

Return the **lexicographically smallest** string **after performing the operation**.

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consists of lowercase English letters

## Examples
### Example 1
- **Input:** `s = "cbabc"`
- **Output:** `"baabc"`
- **Explanation:** Perform the operation on the substring starting at index 0, and ending at index 1 inclusive.

### Example 2
- **Input:** `s = "aa"`
- **Output:** `"az"`
- **Explanation:** Perform the operation on the last letter.

### Example 3
- **Input:** `s = "acbbc"`
- **Output:** `"abaab"`
- **Explanation:** Perform the operation on the substring starting at index 1, and ending at index 4 inclusive.

### Example 4
- **Input:** `s = "leetcode"`
- **Output:** `"kddsbncd"`
- **Explanation:** Perform the operation on the entire string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest String After Substring Operation**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "cbabc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"baabc"`.
4. **Verification:** Perform the operation on the substring starting at index 0, and ending at index 1 inclusive.

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
    def smallestString(self, s: str) -> str:
        a = list(s)
        n = len(a)
        i = 0
        while i < n and a[i] == 'a':
            i += 1
        if i == n:
            a[-1] = 'z'
            return ''.join(a)
        while i < n and a[i] != 'a':
            a[i] = chr(ord(a[i]) - 1)
            i += 1
        return ''.join(a)
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
- [3106. Lexicographically Smallest String After Operations With Constraint](../../3001-3500/3106-lexicographically-smallest-string-after-operations-with-constraint/)
- [3216. Lexicographically Smallest String After a Swap](../../3001-3500/3216-lexicographically-smallest-string-after-a-swap/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/)
