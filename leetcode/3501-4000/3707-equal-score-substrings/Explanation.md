# LeetCode 3707: Equal Score Substrings

**LeetCode Problem #3707 — Equal Score Substrings**
Solve LeetCode Equal Score Substrings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Equal Score Substrings |
| LeetCode | #3707 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

The **score** of a string is the sum of the positions of its characters in the alphabet, where `'a' = 1`, `'b' = 2`, ..., `'z' = 26`.

Determine whether there exists an index `i` such that the string can be split into two **non-empty** ** substrings ** `s[0..i]` and `s[(i + 1)..(n - 1)]` that have **equal** scores.

Return `true` if such a split exists, otherwise return `false`.

## Constraints
- `2 <= s.length <= 100`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "adcb"`
- **Output:** `true`
- **Explanation:** Split at index `i = 1`: 

 
 Left substring = `s[0..1] = "ad"` with `score = 1 + 4 = 5` 
 Right substring = `s[2..3] = "cb"` with `score = 3 + 2 = 5` 
 

 Both substrings have equal scores, so the output is `true`.

### Example 2
- **Input:** `s = "bace"`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Equal Score Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "adcb"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Split at index `i = 1`: 

 
 Left substring = `s[0..1] = "ad"` with `score = 1 + 4 = 5` 
 Right substring = `s[2..3] = "cb"` with `score = 3 + 2 = 5` 
 

 Both substrings have equal scores, so the output is `true`.

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
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(c) - 96 for c in s)
        left = 0
        for i in range(len(s) - 1):
            left += ord(s[i]) - 96
            if left * 2 == total:
                return True
        return False
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
- [1208. Get Equal Substrings Within Budget](../../1001-1500/1208-get-equal-substrings-within-budget/)
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1717-maximum-score-from-removing-substrings/)
- [467. Unique Substrings in Wraparound String](../../0001-0500/0467-unique-substrings-in-wraparound-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/equal-score-substrings/)
