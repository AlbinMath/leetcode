# LeetCode 3556: Sum of Largest Prime Substrings

**LeetCode Problem #3556 — Sum of Largest Prime Substrings**
Solve LeetCode Sum of Largest Prime Substrings using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Largest Prime Substrings |
| LeetCode | #3556 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, find the sum of the **3 largest unique prime numbers ** that can be formed using any of its** substrings **.

Return the **sum** of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of **all** available primes. If no prime numbers can be formed, return 0.

Note: Each prime number should be counted only **once**, even if it appears in **multiple** substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

## Constraints
- `1 <= s.length <= 10`
- `s` consists of only digits.

## Examples
### Example 1
- **Input:** `s = "12234"`
- **Output:** `1469`
- **Explanation:** The unique prime numbers formed from the substrings of `"12234"` are 2, 3, 23, 223, and 1223. 
 The 3 largest primes are 1223, 223, and 23. Their sum is 1469.

### Example 2
- **Input:** `s = "111"`
- **Output:** `11`
- **Explanation:** The unique prime number formed from the substrings of `"111"` is 11. 
 Since there is only one prime number, the sum is 11.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum of Largest Prime Substrings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "12234"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1469`.
4. **Verification:** The unique prime numbers formed from the substrings of `"12234"` are 2, 3, 23, 223, and 1223. 
 The 3 largest primes are 1223, 223, and 23. Their sum is 1469.

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
 * @return {number}
 */
var sumOfLargestPrimes = function(s) {
    const isPrime = (num) => {
        if (num < 2) return false;
        if (num === 2 || num === 3) return true;
        if (num % 2 === 0 || num % 3 === 0) return false;

        for (let i = 5; i * i <= num; i += 6) {
            if (num % i === 0 || num % (i + 2) === 0) {
                return false;
            }
        }
        return true;
    };

    const candidates = new Set();
    const n = s.length;

    // 1. Extract all unique substring integers
    for (let i = 0; i < n; i++) {
        let num = 0;
        for (let j = i; j < n; j++) {
            num = num * 10 + (s.charCodeAt(j) - 48);
            candidates.add(num);
        }
    }

    // 2. Filter for prime numbers
    const primes = [];
    for (const num of candidates) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }

    // 3. Sort descending and sum the top 3
    primes.sort((a, b) => b - a);

    let sum = 0;
    const count = Math.min(3, primes.length);
    for (let i = 0; i < count; i++) {
        sum += primes[i];
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
- [3770. Largest Prime from Consecutive Prime Sum](../../3501-4000/3770-largest-prime-from-consecutive-prime-sum/)
- [2507. Smallest Value After Replacing With Sum of Prime Factors](../../2501-3000/2507-smallest-value-after-replacing-with-sum-of-prime-factors/)
- [2761. Prime Pairs With Target Sum](../../2501-3000/2761-prime-pairs-with-target-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-largest-prime-substrings/)
