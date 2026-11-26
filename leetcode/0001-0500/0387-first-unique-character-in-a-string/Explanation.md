# LeetCode 387: First Unique Character in a String

**LeetCode Problem #387 — First Unique Character in a String**
Solve LeetCode First Unique Character in a String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Unique Character in a String |
| LeetCode | #387 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "leetcode"`
- **Output:** `0`
- **Explanation:** The character `'l'` at index 0 is the first character that does not occur at any other index.

### Example 2
- **Input:** `s = "loveleetcode"`
- **Output:** `2`

### Example 3
- **Input:** `s = "aabb"`
- **Output:** `-1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **First Unique Character in a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcode"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** The character `'l'` at index 0 is the first character that does not occur at any other index.

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
    def firstUniqChar(self, s):
        count = [0] * 26

        # Count each character
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Find the first character that appears once
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i

        return -1
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
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [2108. Find First Palindromic String in the Array](../../2001-2500/2108-find-first-palindromic-string-in-the-array/)
- [3843. First Element with Unique Frequency](../../3501-4000/3843-first-element-with-unique-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)
