# LeetCode 2472: Maximum Number of Non-overlapping Palindrome Substrings

**LeetCode Problem #2472 — Maximum Number of Non-overlapping Palindrome Substrings**
Solve LeetCode Maximum Number of Non-overlapping Palindrome Substrings using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Non-overlapping Palindrome Substrings |
| LeetCode | #2472 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and a **positive** integer `k`.

Select a set of **non-overlapping** substrings from the string `s` that satisfy the following conditions:

The **length** of each substring is **at least** `k`. 
 Each substring is a **palindrome**.

Return *the **maximum** number of substrings in an optimal selection*.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= k <= s.length <= 2000`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abaccdbbd", k = 3`
- **Output:** `2`
- **Explanation:** We can select the substrings underlined in s = "

### Example 2
- **Input:** `s = "adbcda", k = 2`
- **Output:** `0`
- **Explanation:** There is no palindrome substring of length at least 2 in the string.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Uses **DP** combined with palindrome detection (expand-around-center or Manacher's). For each position, compute `dp[i]` = max non-overlapping palindromes in `s[0..i-1]`. When a palindrome of length ≥ k ending at position i is found, update dp accordingly.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abaccdbbd", k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can select the substrings underlined in s = "

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
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxPalindromes = function(s, k) {
    const n = s.length;

    // dp[i] = maximum number of valid palindromes
    // using the first i characters.
    const dp = new Array(n + 1).fill(0);

    // palindrome[l][r] = true if s[l...r] is a palindrome
    const palindrome = Array.from(
        { length: n },
        () => new Array(n).fill(false)
    );

    // Build palindrome table
    for (let len = 1; len <= n; len++) {
        for (let l = 0; l + len <= n; l++) {
            const r = l + len - 1;

            if (
                s[l] === s[r] &&
                (len <= 2 || palindrome[l + 1][r - 1])
            ) {
                palindrome[l][r] = true;
            }
        }
    }

    // Find the maximum number of non-overlapping palindromes
    for (let i = 1; i <= n; i++) {
        // Don't take a palindrome ending at i
        dp[i] = dp[i - 1];

        for (let len = k; len <= i; len++) {
            const l = i - len;
            const r = i - 1;

            if (palindrome[l][r]) {
                dp[i] = Math.max(dp[i], dp[l] + 1);
            }
        }
    }

    return dp[n];
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
- [1520. Maximum Number of Non-Overlapping Substrings](../../1501-2000/1644-maximum-number-of-non-overlapping-substrings/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)
