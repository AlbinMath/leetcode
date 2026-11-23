# LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length

**LeetCode Problem #1456 — Maximum Number of Vowels in a Substring of Given Length**
Solve LeetCode Maximum Number of Vowels in a Substring of Given Length using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Vowels in a Substring of Given Length |
| LeetCode | #1456 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` and an integer `k`, return *the maximum number of vowel letters in any substring of *`s`* with length *`k`.

**Vowel letters** in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `1 <= k <= s.length`

## Examples
### Example 1
- **Input:** `s = "abciiidef", k = 3`
- **Output:** `3`
- **Explanation:** The substring "iii" contains 3 vowel letters.

### Example 2
- **Input:** `s = "aeiou", k = 2`
- **Output:** `2`
- **Explanation:** Any substring of length 2 contains 2 vowels.

### Example 3
- **Input:** `s = "leetcode", k = 3`
- **Output:** `2`
- **Explanation:** "lee", "eet" and "ode" contain 2 vowels.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Maximum Number of Vowels in a Substring of Given Length**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abciiidef", k = 3`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The substring "iii" contains 3 vowel letters.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxVowels = function(s, k) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let count = 0;

    // Count vowels in the first window
    for (let i = 0; i < k; i++) {
        if (vowels.has(s[i])) {
            count++;
        }
    }

    let maxCount = count;

    // Slide the window
    for (let i = k; i < s.length; i++) {
        if (vowels.has(s[i - k])) {
            count--;
        }

        if (vowels.has(s[i])) {
            count++;
        }

        maxCount = Math.max(maxCount, count);

        // Maximum possible number of vowels found
        if (maxCount === k) {
            return k;
        }
    }

    return maxCount;
};
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
- [3090. Maximum Length Substring With Two Occurrences](../../3001-3500/3349-maximum-length-substring-with-two-occurrences/)
- [1297. Maximum Number of Occurrences of a Substring](../../1001-1500/1423-maximum-number-of-occurrences-of-a-substring/)
- [718. Maximum Length of Repeated Subarray](../../0501-1000/0718-maximum-length-of-repeated-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)
