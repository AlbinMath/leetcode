# LeetCode 1542: Find Longest Awesome Substring

**LeetCode Problem #1542 — Find Longest Awesome Substring**
Solve LeetCode Find Longest Awesome Substring using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Longest Awesome Substring |
| LeetCode | #1542 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s`. An **awesome** substring is a non-empty substring of `s` such that we can make any number of swaps in order to make it a palindrome.

Return *the length of the maximum length **awesome substring** of* `s`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of digits.

## Examples
### Example 1
- **Input:** `s = "3242415"`
- **Output:** `5`
- **Explanation:** "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.

### Example 2
- **Input:** `s = "12345678"`
- **Output:** `1`

### Example 3
- **Input:** `s = "213123"`
- **Output:** `6`
- **Explanation:** "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Longest Awesome Substring**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "3242415"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.

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
    def longestAwesome(self, s: str) -> int:
        first = [None] * 1024
        first[0] = -1
        mask = 0
        ans = 0

        for j, ch in enumerate(s):
            mask ^= 1 << (ord(ch) - 48)

            if first[mask] is not None:
                ans = max(ans, j - first[mask])
            else:
                first[mask] = j

            for d in range(10):
                i = first[mask ^ (1 << d)]
                if i is not None:
                    ans = max(ans, j - i)

        return ans
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
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../../1001-1500/1473-find-the-longest-substring-containing-vowels-in-even-counts/)
- [2730. Find the Longest Semi-Repetitive Substring](../../2501-3000/2786-find-the-longest-semi-repetitive-substring/)
- [2981. Find Longest Special Substring That Occurs Thrice I](../../3001-3500/3267-find-longest-special-substring-that-occurs-thrice-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-longest-awesome-substring/)
