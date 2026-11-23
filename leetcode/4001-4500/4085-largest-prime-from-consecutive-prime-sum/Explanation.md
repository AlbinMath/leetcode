# LeetCode 3770: Largest Prime from Consecutive Prime Sum

**LeetCode Problem #3770 — Largest Prime from Consecutive Prime Sum**
Solve LeetCode Largest Prime from Consecutive Prime Sum using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Prime from Consecutive Prime Sum |
| LeetCode | #3770 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

Return the **largest prime number ** less than or equal to `n` that can be expressed as the **sum** of one or more **consecutive prime numbers** starting from 2. If no such number exists, return 0.

## Constraints
- `1 <= n <= 5 * 10^5`

## Examples
### Example 1
- **Input:** `n = 20`
- **Output:** `17`
- **Explanation:** The prime numbers less than or equal to `n = 20` which are consecutive prime sums are: 

 
 
 `2 = 2` 
 
 
 `5 = 2 + 3` 
 
 
 `17 = 2 + 3 + 5 + 7` 
 
 

 The largest is 17, so it is the answer.

### Example 2
- **Input:** `n = 2`
- **Output:** `2`
- **Explanation:** The only consecutive prime sum less than or equal to 2 is 2 itself.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Largest Prime from Consecutive Prime Sum**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 20`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `17`.
4. **Verification:** The prime numbers less than or equal to `n = 20` which are consecutive prime sums are: 

 
 
 `2 = 2` 
 
 
 `5 = 2 + 3` 
 
 
 `17 = 2 + 3 + 5 + 7` 
 
 

 The largest is 17, so it is the answer.

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
var largestPrime = function(n) {
    if (n < 2) return 0;

    // 1. Sieve of Eratosthenes to find all primes up to n
    const isPrime = new Uint8Array(n + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Sum consecutive primes starting from 2 while sum <= n
    let sum = 0;
    let ans = 0;

    for (let p = 2; p <= n; p++) {
        if (isPrime[p]) {
            sum += p;
            if (sum > n) break;
            if (isPrime[sum]) {
                ans = sum;
            }
        }
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
- [3556. Sum of Largest Prime Substrings](../../3501-4000/3815-sum-of-largest-prime-substrings/)
- [1171. Remove Zero Sum Consecutive Nodes from Linked List](../../1001-1500/1267-remove-zero-sum-consecutive-nodes-from-linked-list/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/)
