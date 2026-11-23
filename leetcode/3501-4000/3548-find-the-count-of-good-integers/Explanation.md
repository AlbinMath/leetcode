# LeetCode 3272: Find the Count of Good Integers

**LeetCode Problem #3272 — Find the Count of Good Integers**
Solve LeetCode Find the Count of Good Integers using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Count of Good Integers |
| LeetCode | #3272 |
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

An integer is called **good** if its digits can be *rearranged* to form a **k-palindromic** integer. For example, for `k = 2`, 2020 can be rearranged to form the *k-palindromic* integer 2002, whereas 1010 cannot be rearranged to form a *k-palindromic* integer.

Return the count of **good** integers containing `n` digits.

**Note** that *any* integer must **not** have leading zeros, **neither** before **nor** after rearrangement. For example, 1010 *cannot* be rearranged to form 101.

## Constraints
- `1 <= n <= 10`
- `1 <= k <= 9`

## Examples
### Example 1
- **Input:** `n = 3, k = 5`
- **Output:** `27`
- **Explanation:** *Some* of the good integers are: 

 
 551 because it can be rearranged to form 515. 
 525 because it is already k-palindromic.

### Example 2
- **Input:** `n = 1, k = 4`
- **Output:** `2`
- **Explanation:** The two good integers are 4 and 8.

### Example 3
- **Input:** `n = 5, k = 6`
- **Output:** `2468`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find the Count of Good Integers**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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
3. **Result:** Arrive at the expected output `27`.
4. **Verification:** *Some* of the good integers are: 

 
 551 because it can be rearranged to form 515. 
 525 because it is already k-palindromic.

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
var countGoodIntegers = function(n, k) {
    const fact = Array(n + 1).fill(1);
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i;
    }

    const seen = new Set();
    const half = Math.ceil(n / 2);
    const start = 10 ** (half - 1);
    const end = 10 ** half;
    let ans = 0;

    for (let first = start; first < end; first++) {
        const left = String(first);
        const palindrome = left +
            left.slice(0, n % 2 ? -1 : undefined).split("").reverse().join("");

        if (BigInt(palindrome) % BigInt(k) !== 0n) continue;

        const freq = Array(10).fill(0);
        for (const digit of palindrome) {
            freq[Number(digit)]++;
        }

        const key = freq.join(",");
        if (seen.has(key)) continue;
        seen.add(key);

        let ways = fact[n];
        for (const count of freq) {
            ways /= fact[count];
        }

        if (freq[0] > 0) {
            let leadingZeroWays = fact[n - 1];
            for (let d = 0; d < 10; d++) {
                const count = freq[d] - (d === 0 ? 1 : 0);
                leadingZeroWays /= fact[count];
            }
            ways -= leadingZeroWays;
        }

        ans += ways;
    }

    return ans;
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
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)
- [1534. Count Good Triplets](../../1501-2000/1656-count-good-triplets/)
- [1729. Find Followers Count](../../1501-2000/1877-find-followers-count/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-count-of-good-integers/)
