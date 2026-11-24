# LeetCode 3260: Find the Largest Palindrome Divisible by K

**LeetCode Problem #3260 — Find the Largest Palindrome Divisible by K**
Solve LeetCode Find the Largest Palindrome Divisible by K using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Largest Palindrome Divisible by K |
| LeetCode | #3260 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **positive** integers `n` and `k`.

An integer `x` is called **k-palindromic** if:

`x` is a palindrome . 
 `x` is divisible by `k`.

Return the** largest** integer having `n` digits (as a string) that is **k-palindromic**.

**Note** that the integer must **not** have leading zeros.

## Constraints
- `1 <= n <= 10^5`
- `1 <= k <= 9`

## Examples
### Example 1
- **Input:** `n = 3, k = 5`
- **Output:** `"595"`
- **Explanation:** 595 is the largest k-palindromic integer with 3 digits.

### Example 2
- **Input:** `n = 1, k = 4`
- **Output:** `"8"`
- **Explanation:** 4 and 8 are the only k-palindromic integers with 1 digit.

### Example 3
- **Input:** `n = 5, k = 6`
- **Output:** `"89898"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Largest Palindrome Divisible by K**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, k = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"595"`.
4. **Verification:** 595 is the largest k-palindromic integer with 3 digits.

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
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var largestPalindrome = function(n, k) {
    // Fast path for k = 1, 3, 9: all 9s is always divisible by 1, 3, and 9
    if (k === 1 || k === 3 || k === 9) {
        return '9'.repeat(n);
    }

    const half = Math.ceil(n / 2);

    // Precompute powers of 10 modulo k
    const pow10 = new Int32Array(n);
    pow10[0] = 1 % k;
    for (let i = 1; i < n; i++) {
        pow10[i] = (pow10[i - 1] * 10) % k;
    }

    // Precompute the modular weight of placing digit 1 at symmetric positions (i, n - 1 - i)
    const weight = new Int32Array(half);
    for (let i = 0; i < half; i++) {
        const j = n - 1 - i;
        weight[i] = (i === j) ? pow10[n - 1 - i] : (pow10[n - 1 - i] + pow10[i]) % k;
    }

    // visited[i * k + rem] = 1 if (i, rem) cannot form a valid palindrome
    const visited = new Uint8Array(half * k);
    const chosen = new Int32Array(half);

    const dfs = (i, rem) => {
        if (i === half) {
            return rem === 0;
        }

        const state = i * k + rem;
        if (visited[state]) {
            return false;
        }

        const minDigit = (i === 0) ? 1 : 0;
        const w = weight[i];

        // Try digits greedily from 9 down to minDigit
        for (let d = 9; d >= minDigit; d--) {
            const nextRem = (rem + d * w) % k;
            if (dfs(i + 1, nextRem)) {
                chosen[i] = d;
                return true;
            }
        }

        visited[state] = 1;
        return false;
    };

    dfs(0, 0);

    // Reconstruct the full n-digit palindrome string
    const res = new Array(n);
    for (let i = 0; i < half; i++) {
        const ch = String(chosen[i]);
        res[i] = ch;
        res[n - 1 - i] = ch;
    }

    return res.join('');
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
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2204-find-subsequence-of-length-k-with-the-largest-sum/)
- [479. Largest Palindrome Product](../../0001-0500/0479-largest-palindrome-product/)
- [515. Find Largest Value in Each Tree Row](../../0501-1000/0515-find-largest-value-in-each-tree-row/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/)
