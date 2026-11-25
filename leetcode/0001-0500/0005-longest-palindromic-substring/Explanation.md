# LeetCode 5: Longest Palindromic Substring

**LeetCode Problem #5 — Longest Palindromic Substring**
Solve LeetCode Longest Palindromic Substring using JavaScript, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Palindromic Substring |
| LeetCode | #5 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return *the longest* *palindromic* *substring* in `s`.

## Constraints
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Examples
### Example 1
- **Input:** `s = "babad"`
- **Output:** `"bab"`
- **Explanation:** "aba" is also a valid answer.

### Example 2
- **Input:** `s = "cbbd"`
- **Output:** `"bb"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses the **Expand Around Center** approach. Since a palindrome mirrors around its center, we can iterate through the string and treat each character (or pair of characters) as a potential center, expanding outwards as long as the characters match.

1. It initializes `start` and `end` variables to keep track of the indices of the longest palindrome found so far.
2. It defines a helper function `expand(left, right)` which takes the starting center indices. It uses a `while` loop to expand outwards (`left -= 1` and `right += 1`) as long as the indices are within bounds and the characters at those indices are equal. It returns the boundaries of the identified palindrome.
3. It iterates through each character index `i` in the string:
   - **Odd-length Palindromes**: It calls `expand(i, i)` treating the single character at `i` as the center (e.g., "aba").
   - **Even-length Palindromes**: It calls `expand(i, i + 1)` treating the gap between `i` and `i+1` as the center (e.g., "abba").
4. After each expansion, it checks if the length of the newly found palindrome (`right - left`) is greater than the currently recorded maximum length (`end - start`). If it is, it updates `start` and `end`.
5. Finally, it returns the substring `s[start : end + 1]`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "babad"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"bab"`.
4. **Verification:** "aba" is also a valid answer.

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
var longestPalindrome = function(s) {
    let start = 0;
    let maxLength = 0;

    function expandAroundCenter(left, right) {
        while (
            left >= 0 &&
            right < s.length &&
            s[left] === s[right]
        ) {
            left--;
            right++;
        }

        // The pointers have moved one step beyond the palindrome.
        const length = right - left - 1;

        if (length > maxLength) {
            maxLength = length;
            start = left + 1;
        }
    }

    for (let i = 0; i < s.length; i++) {
        // Odd-length palindrome
        expandAroundCenter(i, i);

        // Even-length palindrome
        expandAroundCenter(i, i + 1);
    }

    return s.substring(start, start + maxLength);
};
```

### Python
```python
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome
            left1, right1 = expand(i, i)

            # Even-length palindrome
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]
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
- [516. Longest Palindromic Subsequence](../../0501-1000/0516-longest-palindromic-subsequence/)
- [3615. Longest Palindromic Path in Graph](../../3501-4000/3615-longest-palindromic-path-in-graph/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)
