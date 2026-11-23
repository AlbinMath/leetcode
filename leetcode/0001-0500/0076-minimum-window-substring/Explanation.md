# LeetCode 76: Minimum Window Substring

**LeetCode Problem #76 — Minimum Window Substring**
Solve LeetCode Minimum Window Substring using JavaScript, PHP and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Window Substring |
| LeetCode | #76 |
| Difficulty | Hard |
| Language | JavaScript, PHP |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring*** * of *`s`* such that every character in *`t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string *`""`.

The testcases will be generated such that the answer is **unique**.

## Constraints
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "ADOBECODEBANC", t = "ABC"`
- **Output:** `"BANC"`
- **Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

### Example 2
- **Input:** `s = "a", t = "a"`
- **Output:** `"a"`
- **Explanation:** The entire string s is the minimum window.

### Example 3
- **Input:** `s = "a", t = "aa"`
- **Output:** `""`
- **Explanation:** Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Window Substring**, we observe the problem requirements and utilize the **Sliding Window** technique. By maintaining a **Array / Hash Set**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array / Hash Set** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ADOBECODEBANC", t = "ABC"`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"BANC"`.
4. **Verification:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

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
JavaScript, PHP

## Source Code
- [solution.js](./solution.js)
- [solution.php](./solution.php)


### JavaScript
```javascript
var minWindow = function(s, t) {
    if (s.length < t.length) return "";

    const need = new Map();

    for (const char of t) {
        need.set(char, (need.get(char) || 0) + 1);
    }

    let left = 0;
    let required = t.length;
    let minLength = Infinity;
    let start = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];

        if (need.has(char)) {
            if (need.get(char) > 0) {
                required--;
            }

            need.set(char, need.get(char) - 1);
        }

        // When all required characters are included
        while (required === 0) {
            const windowLength = right - left + 1;

            if (windowLength < minLength) {
                minLength = windowLength;
                start = left;
            }

            const leftChar = s[left];

            if (need.has(leftChar)) {
                need.set(leftChar, need.get(leftChar) + 1);

                if (need.get(leftChar) > 0) {
                    required++;
                }
            }

            left++;
        }
    }

    return minLength === Infinity
        ? ""
        : s.substring(start, start + minLength);
};
```

### PHP
```php
class Solution {
    function minWindow($s, $t) {
        // Count required characters from t
        $need = [];

        for ($i = 0; $i < strlen($t); $i++) {
            $char = $t[$i];

            if (isset($need[$char])) {
                $need[$char]++;
            } else {
                $need[$char] = 1;
            }
        }

        $left = 0;
        $right = 0;

        $required = count($need);
        $formed = 0;

        $window = [];

        $minLength = PHP_INT_MAX;
        $minLeft = 0;

        $sLength = strlen($s);

        while ($right < $sLength) {
            $char = $s[$right];

            // Add current character to window
            if (isset($window[$char])) {
                $window[$char]++;
            } else {
                $window[$char] = 1;
            }

            // Character requirement is now satisfied
            if (isset($need[$char]) &&
                $window[$char] == $need[$char]) {
                $formed++;
            }

            // Try shrinking the window
            while ($left <= $right && $formed == $required) {

                $currentLength = $right - $left + 1;

                if ($currentLength < $minLength) {
                    $minLength = $currentLength;
                    $minLeft = $left;
                }

                $leftChar = $s[$left];

                $window[$leftChar]--;

                // Removing this character breaks a requirement
                if (isset($need[$leftChar]) &&
                    $window[$leftChar] < $need[$leftChar]) {
                    $formed--;
                }

                $left++;
            }

            $right++;
        }

        if ($minLength == PHP_INT_MAX) {
            return "";
        }

        return substr($s, $minLeft, $minLength);
    }
}
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-window-substring/)
