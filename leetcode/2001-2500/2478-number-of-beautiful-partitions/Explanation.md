# LeetCode 2478: Number of Beautiful Partitions

**LeetCode Problem #2478 — Number of Beautiful Partitions**
Solve LeetCode Number of Beautiful Partitions using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Beautiful Partitions |
| LeetCode | #2478 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` that consists of the digits `'1'` to `'9'` and two integers `k` and `minLength`.

A partition of `s` is called **beautiful** if:

`s` is partitioned into `k` non-intersecting substrings. 
 Each substring has a length of **at least** `minLength`. 
 Each substring starts with a **prime** digit and ends with a **non-prime** digit. Prime digits are `'2'`, `'3'`, `'5'`, and `'7'`, and the rest of the digits are non-prime.

Return* the number of **beautiful** partitions of *`s`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **substring** is a contiguous sequence of characters within a string.

## Constraints
- `1 <= k, minLength <= s.length <= 1000`
- `s` consists of the digits `'1'` to `'9'`.

## Examples
### Example 1
- **Input:** `s = "23542185131", k = 3, minLength = 2`
- **Output:** `3`
- **Explanation:** There exists three ways to create a beautiful partition:
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"

### Example 2
- **Input:** `s = "23542185131", k = 3, minLength = 3`
- **Output:** `1`
- **Explanation:** There exists one way to create a beautiful partition: "2354 | 218 | 5131".

### Example 3
- **Input:** `s = "3312958", k = 3, minLength = 1`
- **Output:** `1`
- **Explanation:** There exists one way to create a beautiful partition: "331 | 29 | 58".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Beautiful Partitions**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "23542185131", k = 3, minLength = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There exists three ways to create a beautiful partition:
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"

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
var beautifulPartitions = function(s, k, minLength) {
    const MOD = 1000000007;
    const n = s.length;
    const isPrime = (digit) => {
        return digit === '2' ||
               digit === '3' ||
               digit === '5' ||
               digit === '7';
    };
    if (!isPrime(s[0]) || isPrime(s[n - 1])) {
        return 0;
    }
    if (k * minLength > n) {
        return 0;
    }
    let prev = new Array(n + 1).fill(0);
    prev[0] = 1;
    for (let part = 1; part <= k; part++) {
        let curr = new Array(n + 1).fill(0);
        let ways = 0;
        for (let i = 1; i <= n; i++) {
            let t = i - minLength;
            if (
                t >= 0 &&
                isPrime(s[t]) &&
                (t === 0 || !isPrime(s[t - 1]))
            ) {
                ways = (ways + prev[t]) % MOD;
            }
            if (!isPrime(s[i - 1])) {
                curr[i] = ways;
            }
        }
        prev = curr;
    }
    return prev[n];
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
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2588-count-the-number-of-beautiful-subarrays/)
- [2597. The Number of Beautiful Subsets](../../2501-3000/2597-the-number-of-beautiful-subsets/)
- [2748. Number of Beautiful Pairs](../../2501-3000/2748-number-of-beautiful-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-beautiful-partitions/)
