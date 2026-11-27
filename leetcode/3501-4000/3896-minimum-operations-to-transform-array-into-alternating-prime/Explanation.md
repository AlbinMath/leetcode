# LeetCode 3896: Minimum Operations to Transform Array into Alternating Prime

**LeetCode Problem #3896 — Minimum Operations to Transform Array into Alternating Prime**
Solve LeetCode Minimum Operations to Transform Array into Alternating Prime using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Transform Array into Alternating Prime |
| LeetCode | #3896 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

An array is considered **alternating prime** if:

Elements at **even** indices (0-based) are **prime** numbers. 
 Elements at **odd** indices are **non-prime** numbers.

In one operation, you may **increment** any element by 1.

Return the **minimum** number of operations required to transform `nums` into an **alternating prime** array.

A **prime** number is a natural number greater than 1 with only two factors, 1 and itself.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `3`
- **Explanation:** The element at index 0 must be prime. Increment `nums[0] = 1` to 2, using 1 operation. 
 The element at index 1 must be non-prime. Increment `nums[1] = 2` to 4, using 2 operations. 
 The element at index 2 is already prime. 
 The element at index 3 is already non-prime. 
 

 Total operations = `1 + 2 = 3`.

### Example 2
- **Input:** `nums = [5,6,7,8]`
- **Output:** `0`
- **Explanation:** The elements at indices 0 and 2 are already prime. 
 The elements at indices 1 and 3 are already non-prime. 
 

 No operations are needed.

### Example 3
- **Input:** `nums = [4,4]`
- **Output:** `1`
- **Explanation:** The element at index 0 must be prime. Increment `nums[0] = 4` to 5, using 1 operation. 
 The element at index 1 is already non-prime. 
 

 Total operations = 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Transform Array into Alternating Prime**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The element at index 0 must be prime. Increment `nums[0] = 1` to 2, using 1 operation. 
 The element at index 1 must be non-prime. Increment `nums[1] = 2` to 4, using 2 operations. 
 The element at index 2 is already prime. 
 The element at index 3 is already non-prime. 
 

 Total operations = `1 + 2 = 3`.

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
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    // Smallest prime > 100,000 is 100,003
    const LIMIT = 100005;

    // 1. Sieve of Eratosthenes up to LIMIT
    const isPrime = new Uint8Array(LIMIT + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= LIMIT; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= LIMIT; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Precompute the nearest prime >= x for every x in [1, 100000]
    const nextPrime = new Int32Array(LIMIT + 1);
    let lastPrime = LIMIT;
    for (let x = LIMIT; x >= 1; x--) {
        if (isPrime[x]) lastPrime = x;
        nextPrime[x] = lastPrime;
    }

    // 3. Sum minimum operations across all indices
    let totalOps = 0;

    for (let i = 0; i < nums.length; i++) {
        const val = nums[i];

        if (i % 2 === 0) {
            // Even index: must be prime
            totalOps += nextPrime[val] - val;
        } else {
            // Odd index: must be non-prime
            if (isPrime[val]) {
                totalOps += (val === 2) ? 2 : 1;
            }
        }
    }

    return totalOps;
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
- [2170. Minimum Operations to Make the Array Alternating](../../2001-2500/2170-minimum-operations-to-make-the-array-alternating/)
- [3854. Minimum Operations to Make Array Parity Alternating](../../3501-4000/3854-minimum-operations-to-make-array-parity-alternating/)
- [3937. Minimum Operations to Make Array Modulo Alternating I](../../3501-4000/3937-minimum-operations-to-make-array-modulo-alternating-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/)
