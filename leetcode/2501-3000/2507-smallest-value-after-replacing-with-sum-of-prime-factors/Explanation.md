# LeetCode 2507: Smallest Value After Replacing With Sum of Prime Factors

**LeetCode Problem #2507 — Smallest Value After Replacing With Sum of Prime Factors**
Solve LeetCode Smallest Value After Replacing With Sum of Prime Factors using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Value After Replacing With Sum of Prime Factors |
| LeetCode | #2507 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `n`.

Continuously replace `n` with the sum of its **prime factors**.

Note that if a prime factor divides `n` multiple times, it should be included in the sum as many times as it divides `n`.

Return *the smallest value *`n`* will take on.*

## Constraints
- `2 <= n <= 10^5`

## Examples
### Example 1
- **Input:** `n = 15`
- **Output:** `5`
- **Explanation:** Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.

### Example 2
- **Input:** `n = 3`
- **Output:** `3`
- **Explanation:** Initially, n = 3.
3 is the smallest value n will take on.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Value After Replacing With Sum of Prime Factors**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 15`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.

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
var smallestValue = function(n) {
    function sumPrimeFactors(num) {
        let sum = 0;

        for (let i = 2; i * i <= num; i++) {
            while (num % i === 0) {
                sum += i;
                num /= i;
            }
        }

        if (num > 1) {
            sum += num;
        }

        return sum;
    }

    while (true) {
        const sum = sumPrimeFactors(n);

        if (sum === n) {
            return n;
        }

        n = sum;
    }
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
- [2918. Minimum Equal Sum of Two Arrays After Replacing Zeros](../../2501-3000/2918-minimum-equal-sum-of-two-arrays-after-replacing-zeros/)
- [3114. Latest Time You Can Obtain After Replacing Characters](../../3001-3500/3114-latest-time-you-can-obtain-after-replacing-characters/)
- [2521. Distinct Prime Factors of Product of Array](../../2501-3000/2521-distinct-prime-factors-of-product-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/)
