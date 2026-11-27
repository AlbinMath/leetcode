# LeetCode 3557: Find Maximum Number of Non Intersecting Substrings

**LeetCode Problem #3557 — Find Maximum Number of Non Intersecting Substrings**
Solve LeetCode Find Maximum Number of Non Intersecting Substrings using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Maximum Number of Non Intersecting Substrings |
| LeetCode | #3557 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `word`.

Return the **maximum** number of non-intersecting ** substrings ** of word that are at **least** four characters long and start and end with the same letter.

## Constraints
- `1 <= word.length <= 2 * 10^5`
- `word` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "abcdeafdef"`
- **Output:** `2`
- **Explanation:** The two substrings are `"abcdea"` and `"fdef"`.

### Example 2
- **Input:** `word = "bcdaaaab"`
- **Output:** `1`
- **Explanation:** The only substring is `"aaaa"`. Note that we cannot

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Maximum Number of Non Intersecting Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "abcdeafdef"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The two substrings are `"abcdea"` and `"fdef"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxSubstrings = function(word) {
    const n = word.length;

    const nextEnd = new Int32Array(n).fill(-1);
    const nearest = new Int32Array(26).fill(-1);
    for (let i = n - 1; i >= 0; i--) {
        if (i + 3 < n) {
            const c = word.charCodeAt(i + 3) - 97;
            nearest[c] = i + 3;
        }

        const c = word.charCodeAt(i) - 97;
        nextEnd[i] = nearest[c];
    }
    let count = 0;
    let earliestEnd = n;

    for (let i = 0; i < n; i++) {
        const end = nextEnd[i];

        if (end !== -1) {
            earliestEnd = Math.min(earliestEnd, end);
        }
        if (i === earliestEnd) {
            count++;
            earliestEnd = n;
        }
    }

    return count;
};
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
- [1520. Maximum Number of Non-Overlapping Substrings](../../1501-2000/1520-maximum-number-of-non-overlapping-substrings/)
- [2472. Maximum Number of Non-overlapping Palindrome Substrings](../../2001-2500/2472-maximum-number-of-non-overlapping-palindrome-substrings/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/)
