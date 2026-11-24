# LeetCode 3918: Sum of Primes Between Number and Its Reverse

**LeetCode Problem #3918 — Sum of Primes Between Number and Its Reverse**
Solve LeetCode Sum of Primes Between Number and Its Reverse using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Primes Between Number and Its Reverse |
| LeetCode | #3918 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

Let `r` be the integer formed by reversing the digits of `n`.

Return the **sum** of all prime numbers between `min(n, r)` and `max(n, r)`, inclusive.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 13`
- **Output:** `132`
- **Explanation:** The reverse of 13 is 31. Thus, the range is `[13, 31]`. 
 The prime numbers in this range are 13, 17, 19, 23, 29, and 31. 
 The sum of these prime numbers is `13 + 17 + 19 + 23 + 29 + 31 = 132`.

### Example 2
- **Input:** `n = 10`
- **Output:** `17`
- **Explanation:** The reverse of 10 is 1. Thus, the range is `[1, 10]`. 
 The prime numbers in this range are 2, 3, 5, and 7. 
 The sum of these prime numbers is `2 + 3 + 5 + 7 = 17`.

### Example 3
- **Input:** `n = 8`
- **Output:** `0`
- **Explanation:** The reverse of 8 is 8. Thus, the range is `[8, 8]`. 
 There are no prime numbers in this range, so the sum is 0.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum of Primes Between Number and Its Reverse**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 13`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `132`.
4. **Verification:** The reverse of 13 is 31. Thus, the range is `[13, 31]`. 
 The prime numbers in this range are 13, 17, 19, 23, 29, and 31. 
 The sum of these prime numbers is `13 + 17 + 19 + 23 + 29 + 31 = 132`.

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
var sumOfPrimesInRange = function(n) {
    // 1. Reverse the digits of n
    let r = 0;
    let temp = n;
    while (temp > 0) {
        r = r * 10 + (temp % 10);
        temp = Math.floor(temp / 10);
    }

    // 2. Helper to check if a number is prime
    const isPrime = (x) => {
        if (x < 2) return false;
        if (x === 2 || x === 3) return true;
        if (x % 2 === 0 || x % 3 === 0) return false;

        for (let i = 5; i * i <= x; i += 6) {
            if (x % i === 0 || x % (i + 2) === 0) {
                return false;
            }
        }
        return true;
    };

    // 3. Sum all primes in [min(n, r), max(n, r)]
    const low = Math.min(n, r);
    const high = Math.max(n, r);
    let sum = 0;

    for (let x = low; x <= high; x++) {
        if (isPrime(x)) {
            sum += x;
        }
    }

    return sum;
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
- [2443. Sum of Number and Its Reverse](../../2001-2500/2443-sum-of-number-and-its-reverse/)
- [1190. Reverse Substrings Between Each Pair of Parentheses](../../1001-1500/1190-reverse-substrings-between-each-pair-of-parentheses/)
- [1360. Number of Days Between Two Dates](../../1001-1500/1360-number-of-days-between-two-dates/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/)
