# LeetCode 1071: Greatest Common Divisor of Strings

**LeetCode Problem #1071 — Greatest Common Divisor of Strings**
Solve LeetCode Greatest Common Divisor of Strings using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest Common Divisor of Strings |
| LeetCode | #1071 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return *the largest string *`x`* such that *`x`* divides both *`str1`* and *`str2`.

## Constraints
- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of English uppercase letters.

## Examples
### Example 1
- **Input:** `str1 = "ABCABC", str2 = "ABC"`
- **Output:** `"ABC"`

### Example 2
- **Input:** `str1 = "ABABAB", str2 = "ABAB"`
- **Output:** `"AB"`

### Example 3
- **Input:** `str1 = "LEET", str2 = "CODE"`
- **Output:** `""`

### Example 4
- **Input:** `str1 = "AAAAAB", str2 = "AAA"`
- **Output:** `"" ​​​​​​​`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Greatest Common Divisor of Strings**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `str1 = "ABCABC", str2 = "ABC"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ABC"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    if (str1 + str2 !== str2 + str1) {
        return "";
    }

    function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }

    const len = gcd(str1.length, str2.length);

    return str1.substring(0, len);
};
```

### Python
```python
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1979. Find Greatest Common Divisor of Array](../../1501-2000/1979-find-greatest-common-divisor-of-array/)
- [2709. Greatest Common Divisor Traversal](../../2501-3000/2709-greatest-common-divisor-traversal/)
- [3485. Longest Common Prefix of K Strings After Removal](../../3001-3500/3485-longest-common-prefix-of-k-strings-after-removal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
