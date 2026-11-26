# LeetCode 3407: Substring Matching Pattern

**LeetCode Problem #3407 — Substring Matching Pattern**
Solve LeetCode Substring Matching Pattern using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Substring Matching Pattern |
| LeetCode | #3407 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and a pattern string `p`, where `p` contains **exactly one** `'*'` character.

The `'*'` in `p` can be replaced with any sequence of zero or more characters.

Return `true` if `p` can be made a substring of `s`, and `false` otherwise.

## Constraints
- `1 <= s.length <= 50`
- `1 <= p.length <= 50 `
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters and exactly one `'*'`

## Examples
### Example 1
- **Input:** `s = "leetcode", p = "ee*e"`
- **Output:** `true`
- **Explanation:** By replacing the `'*'` with `"tcod"`, the substring `"eetcode"` matches the pattern.

### Example 2
- **Input:** `s = "car", p = "c*v"`
- **Output:** `false`
- **Explanation:** There is no substring matching the pattern.

### Example 3
- **Input:** `s = "luck", p = "u*"`
- **Output:** `true`
- **Explanation:** The substrings `"u"`, `"uc"`, and `"uck"` match the pattern.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Substring Matching Pattern**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcode", p = "ee*e"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** By replacing the `'*'` with `"tcod"`, the substring `"eetcode"` matches the pattern.

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
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split('*')

        i = s.find(left)
        if i == -1:
            return False

        return s.find(right, i + len(left)) != -1
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
- [3455. Shortest Matching Substring](../../3001-3500/3455-shortest-matching-substring/)
- [459. Repeated Substring Pattern](../../0001-0500/0459-repeated-substring-pattern/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/substring-matching-pattern/)
