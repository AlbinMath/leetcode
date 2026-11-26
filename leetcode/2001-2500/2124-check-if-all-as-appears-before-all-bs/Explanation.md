# LeetCode 2124: Check if All A's Appears Before All B's

**LeetCode Problem #2124 — Check if All A's Appears Before All B's**
Solve LeetCode Check if All A's Appears Before All B's using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if All A's Appears Before All B's |
| LeetCode | #2124 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` consisting of **only** the characters `'a'` and `'b'`, return `true` *if **every** *`'a'` *appears before **every** *`'b'`* in the string*. Otherwise, return `false`.

## Constraints
- `1 <= s.length <= 100`
- `s[i]` is either `'a'` or `'b'`.

## Examples
### Example 1
- **Input:** `s = "aaabbb"`
- **Output:** `true`
- **Explanation:** The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

### Example 2
- **Input:** `s = "abab"`
- **Output:** `false`
- **Explanation:** There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

### Example 3
- **Input:** `s = "bbb"`
- **Output:** `true`
- **Explanation:** There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if All A's Appears Before All B's**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaabbb"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

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
    def checkString(self, s: str) -> bool:
        return "ba" not in s
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
- [1437. Check If All 1's Are at Least Length K Places Away](../../1001-1500/1437-check-if-all-1s-are-at-least-length-k-places-away/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1001-1500/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [1461. Check If a String Contains All Binary Codes of Size K](../../1001-1500/1461-check-if-a-string-contains-all-binary-codes-of-size-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)
