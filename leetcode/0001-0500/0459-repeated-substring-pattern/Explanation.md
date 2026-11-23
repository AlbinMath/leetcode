# LeetCode 459: Repeated Substring Pattern

**LeetCode Problem #459 — Repeated Substring Pattern**
Solve LeetCode Repeated Substring Pattern using JavaScript, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Repeated Substring Pattern |
| LeetCode | #459 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abab"`
- **Output:** `true`
- **Explanation:** It is the substring "ab" twice.

### Example 2
- **Input:** `s = "aba"`
- **Output:** `false`

### Example 3
- **Input:** `s = "abcabcabcabc"`
- **Output:** `true`
- **Explanation:** It is the substring "abc" four times or the substring "abcabc" twice.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Repeated Substring Pattern**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abab"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** It is the substring "ab" twice.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var repeatedSubstringPattern = function(s) {
    return (s + s).slice(1, -1).includes(s);
};
```

### Python
```python
class Solution:
    def repeatedSubstringPattern(self, s):
        return s in (s + s)[1:-1]
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
- [1156. Swap For Longest Repeated Character Substring](../../1001-1500/1261-swap-for-longest-repeated-character-substring/)
- [1566. Detect Pattern of Length M Repeated K or More Times](../../1501-2000/1689-detect-pattern-of-length-m-repeated-k-or-more-times/)
- [3407. Substring Matching Pattern](../../3501-4000/3684-substring-matching-pattern/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/repeated-substring-pattern/)
