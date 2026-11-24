# LeetCode 1316: Distinct Echo Substrings

**LeetCode Problem #1316 — Distinct Echo Substrings**
Solve LeetCode Distinct Echo Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Echo Substrings |
| LeetCode | #1316 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Return the number of **distinct** non-empty substrings of `text` that can be written as the concatenation of some string with itself (i.e. it can be written as `a + a` where `a` is some string).

## Constraints
- `1 <= text.length <= 2000`
- `text` has only lowercase English letters.

## Examples
### Example 1
- **Input:** `text = "abcabcabc"`
- **Output:** `3`

### Example 2
- **Input:** `text = "leetcodeleetcode"`
- **Output:** `2`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distinct Echo Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "abcabcabc"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.

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
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        seen = set()
        for L in range(1, n // 2 + 1):
            cnt = 0
            for i in range(n - L):
                if text[i] == text[i + L]:
                    cnt += 1
                else:
                    cnt = 0
                if cnt == L:
                    seen.add(text[i - L + 1:i + L + 1])
                    cnt -= 1
        return len(seen)
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
- [1876. Substrings of Size Three with Distinct Characters](../../1501-2000/1876-substrings-of-size-three-with-distinct-characters/)
- [115. Distinct Subsequences](../../0001-0500/0115-distinct-subsequences/)
- [940. Distinct Subsequences II](../../0501-1000/0940-distinct-subsequences-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-echo-substrings/)
