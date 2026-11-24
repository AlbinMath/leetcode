# LeetCode 3438: Find Valid Pair of Adjacent Digits in String

**LeetCode Problem #3438 — Find Valid Pair of Adjacent Digits in String**
Solve LeetCode Find Valid Pair of Adjacent Digits in String using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Valid Pair of Adjacent Digits in String |
| LeetCode | #3438 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting only of digits. A **valid pair** is defined as two **adjacent** digits in `s` such that:

The first digit is **not equal** to the second. 
 Each digit in the pair appears in `s` **exactly** as many times as its numeric value.

Return the first **valid pair** found in the string `s` when traversing from left to right. If no valid pair exists, return an empty string.

## Constraints
- `2 <= s.length <= 100`
- `s` only consists of digits from `'1'` to `'9'`.

## Examples
### Example 1
- **Input:** `s = "2523533"`
- **Output:** `"23"`
- **Explanation:** Digit `'2'` appears 2 times and digit `'3'` appears 3 times. Each digit in the pair `"23"` appears in `s` exactly as many times as its numeric value. Hence, the output is `"23"`.

### Example 2
- **Input:** `s = "221"`
- **Output:** `"21"`
- **Explanation:** Digit `'2'` appears 2 times and digit `'1'` appears 1 time. Hence, the output is `"21"`.

### Example 3
- **Input:** `s = "22"`
- **Output:** `""`
- **Explanation:** There are no valid adjacent pairs.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Valid Pair of Adjacent Digits in String**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "2523533"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"23"`.
4. **Verification:** Digit `'2'` appears 2 times and digit `'3'` appears 3 times. Each digit in the pair `"23"` appears in `s` exactly as many times as its numeric value. Hence, the output is `"23"`.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var findValidPair = function(s) {
    let freq = Array(10).fill(0);

    // Count frequency of each digit
    for (const ch of s) {
        freq[Number(ch)]++;
    }

    // Traverse adjacent pairs from left to right
    for (let i = 0; i < s.length - 1; i++) {
        let a = Number(s[i]);
        let b = Number(s[i + 1]);

        if (a !== b && freq[a] === a && freq[b] === b) {
            return s[i] + s[i + 1];
        }
    }

    return "";
};
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
- [678. Valid Parenthesis String](../../0501-1000/0678-valid-parenthesis-string/)
- [1517. Find Users With Valid E-Mails](../../1501-2000/1517-find-users-with-valid-e-mails/)
- [1964. Find the Longest Valid Obstacle Course at Each Position](../../1501-2000/1964-find-the-longest-valid-obstacle-course-at-each-position/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/)
