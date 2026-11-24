# LeetCode 2730: Find the Longest Semi-Repetitive Substring

**LeetCode Problem #2730 — Find the Longest Semi-Repetitive Substring**
Solve LeetCode Find the Longest Semi-Repetitive Substring using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Longest Semi-Repetitive Substring |
| LeetCode | #2730 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a digit string `s` that consists of digits from 0 to 9.

A string is called **semi-repetitive** if there is **at most** one adjacent pair of the same digit. For example, `"0010"`, `"002020"`, `"0123"`, `"2002"`, and `"54944"` are semi-repetitive while the following are not: `"00101022"` (adjacent same digit pairs are 00 and 22), and `"1101234883"` (adjacent same digit pairs are 11 and 88).

Return the length of the **longest semi-repetitive substring ** of `s`.

## Constraints
- `1 <= s.length <= 50`
- `'0' <= s[i] <= '9'`

## Examples
### Example 1
- **Input:** `s = "52233"`
- **Output:** `4`
- **Explanation:** The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

### Example 2
- **Input:** `s = "5494"`
- **Output:** `4`
- **Explanation:** `s` is a semi-repetitive string.

### Example 3
- **Input:** `s = "1111111"`
- **Output:** `2`
- **Explanation:** The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Longest Semi-Repetitive Substring**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "52233"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.

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
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        last_pair_idx = 0
        max_len = 1
        
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                if last_pair_idx > 0:
                    left = last_pair_idx
                last_pair_idx = right
            if right - left + 1 > max_len:
                max_len = right - left + 1
                
        return max_len
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
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../../1001-1500/1371-find-the-longest-substring-containing-vowels-in-even-counts/)
- [1542. Find Longest Awesome Substring](../../1501-2000/1542-find-longest-awesome-substring/)
- [2981. Find Longest Special Substring That Occurs Thrice I](../../2501-3000/2981-find-longest-special-substring-that-occurs-thrice-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/)
