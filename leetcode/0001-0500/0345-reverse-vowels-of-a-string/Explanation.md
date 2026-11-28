# LeetCode 345: Reverse Vowels of a String

**LeetCode Problem #345 — Reverse Vowels of a String**
Solve LeetCode Reverse Vowels of a String using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Vowels of a String |
| LeetCode | #345 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consist of **printable ASCII** characters.

## Examples
### Example 1
- **Input:** `s = "IceCreAm"`
- **Output:** `"AceCreIm"`
- **Explanation:** The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

### Example 2
- **Input:** `s = "leetcode"`
- **Output:** `"leotcede"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reverse Vowels of a String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "IceCreAm"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"AceCreIm"`.
4. **Verification:** The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

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
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    const chars = s.split("");
    const vowels = new Set("aeiouAEIOU");

    let left = 0;
    let right = chars.length - 1;

    while (left < right) {
        while (left < right && !vowels.has(chars[left])) {
            left++;
        }

        while (left < right && !vowels.has(chars[right])) {
            right--;
        }

        [chars[left], chars[right]] = [chars[right], chars[left]];

        left++;
        right--;
    }

    return chars.join("");
};
```

### Python
```python
class Solution:
    def reverseVowels(self, s):
        vowels = "aeiouAEIOU"
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            # Move left until it finds a vowel
            while left < right and s[left] not in vowels:
                left += 1

            # Move right until it finds a vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return ''.join(s)
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
- [2785. Sort Vowels in a String](../../2501-3000/2785-sort-vowels-in-a-string/)
- [3227. Vowels Game in a String](../../3001-3500/3227-vowels-game-in-a-string/)
- [151. Reverse Words in a String](../../0001-0500/0151-reverse-words-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)
