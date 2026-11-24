# LeetCode 1371: Find the Longest Substring Containing Vowels in Even Counts

**LeetCode Problem #1371 — Find the Longest Substring Containing Vowels in Even Counts**
Solve LeetCode Find the Longest Substring Containing Vowels in Even Counts using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Longest Substring Containing Vowels in Even Counts |
| LeetCode | #1371 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given the string `s`, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

## Constraints
- `1 <= s.length <= 5 x 10^5`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "eleetminicoworoep"`
- **Output:** `13`
- **Explanation:** The longest substring is "leetminicowor" which contains two each of the vowels:

### Example 2
- **Input:** `s = "leetcodeisgreat"`
- **Output:** `5`
- **Explanation:** The longest substring is "leetc" which contains two e's.

### Example 3
- **Input:** `s = "bcbcbc"`
- **Output:** `6`
- **Explanation:** In this case, the given string "bcbcbc" is the longest because all vowels:

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Longest Substring Containing Vowels in Even Counts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "eleetminicoworoep"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The longest substring is "leetminicowor" which contains two each of the vowels:

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        first = [-2] * 32
        first[0] = -1
        mask = 0
        ans = 0

        for j, ch in enumerate(s):
            if ch in bit:
                mask ^= bit[ch]
            if first[mask] != -2:
                ans = max(ans, j - first[mask])
            else:
                first[mask] = j

        return ans
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1542. Find Longest Awesome Substring](../../1501-2000/1668-find-longest-awesome-substring/)
- [1839. Longest Substring Of All Vowels in Order](../../1501-2000/1967-longest-substring-of-all-vowels-in-order/)
- [2730. Find the Longest Semi-Repetitive Substring](../../2501-3000/2786-find-the-longest-semi-repetitive-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/)
