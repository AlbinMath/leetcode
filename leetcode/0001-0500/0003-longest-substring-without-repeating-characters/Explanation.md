# LeetCode 3: Longest Substring Without Repeating Characters

**LeetCode Problem #3 — Longest Substring Without Repeating Characters**
Solve LeetCode Longest Substring Without Repeating Characters using JavaScript, Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Substring Without Repeating Characters |
| LeetCode | #3 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

## Constraints
- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols and spaces.

## Examples
### Example 1
- **Input:** `s = "abcabcbb"`
- **Output:** `3`
- **Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

### Example 2
- **Input:** `s = "bbbbb"`
- **Output:** `1`
- **Explanation:** The answer is "b", with the length of 1.

### Example 3
- **Input:** `s = "pwwkew"`
- **Output:** `3`
- **Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
The code uses a **Sliding Window** technique with two pointers (`left` and `right`) and a `set` to keep track of unique characters.
1. It initializes an empty set `seen` to store characters currently in the window, a `left` pointer to represent the start of the window, and a `max_length` to track the longest valid substring found.
2. A `for` loop moves the `right` pointer across the string from left to right, expanding the window.
3. If the character at `s[right]` is already in the `seen` set, it means we found a repeating character. A `while` loop then removes characters from the left side of the window (moving the `left` pointer forward) until the duplicate character is removed from the set.
4. After ensuring the character `s[right]` is not a duplicate in the current window, it adds `s[right]` to the `seen` set.
5. It then updates `max_length` by comparing the current maximum with the size of the current window (`right - left + 1`).
6. Finally, once the `right` pointer finishes scanning the string, `max_length` will contain the length of the longest valid substring.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcabcbb"`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var lengthOfLongestSubstring = function(s) {
    const lastSeen = new Map();

    let left = 0;
    let maxLength = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        // If the character repeats inside the current window,
        // move left past its previous occurrence
        if (lastSeen.has(char) && lastSeen.get(char) >= left) {
            left = lastSeen.get(char) + 1;
        }

        lastSeen.set(char, right);

        maxLength = Math.max(maxLength, right - left + 1);
    }

    return maxLength;
};
```

### Python
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)
- [2213. Longest Substring of One Repeating Character](../../2001-2500/2213-longest-substring-of-one-repeating-character/)
- [1576. Replace All ?'s to Avoid Consecutive Repeating Characters](../../1501-2000/1576-replace-all-s-to-avoid-consecutive-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
