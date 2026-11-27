# LeetCode 2521: Distinct Prime Factors of Product of Array

**LeetCode Problem #2521 — Distinct Prime Factors of Product of Array**
Solve LeetCode Distinct Prime Factors of Product of Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distinct Prime Factors of Product of Array |
| LeetCode | #2521 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of positive integers `nums`, return *the number of **distinct prime factors** in the product of the elements of* `nums`.

**Note** that:

A number greater than `1` is called **prime** if it is divisible by only `1` and itself. 
 An integer `val1` is a factor of another integer `val2` if `val2 / val1` is an integer.

## Constraints
- `1 <= nums.length <= 10^4`
- `2 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [2,4,3,7,10,6]`
- **Output:** `4`
- **Explanation:** The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 2^5 * 3^2 * 5 * 7.
There are 4 distinct prime factors so we return 4.

### Example 2
- **Input:** `nums = [2,4,8,16]`
- **Output:** `1`
- **Explanation:** The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 2^10.
There is 1 distinct prime factor so we return 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Distinct Prime Factors of Product of Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,3,7,10,6]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 2^5 * 3^2 * 5 * 7.
There are 4 distinct prime factors so we return 4.

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
var distinctPrimeFactors = function(nums) {
    const primeFactors = new Set();

    for (let num of nums) {
        for (let i = 2; i * i <= num; i++) {
            if (num % i === 0) {
                primeFactors.add(i);

                while (num % i === 0) {
                    num /= i;
                }
            }
        }

        if (num > 1) {
            primeFactors.add(num);
        }
    }

    return primeFactors.size;
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
- [4032. Longest Subarray With at Most K Distinct Prime Factors](../../4001-4500/4032-longest-subarray-with-at-most-k-distinct-prime-factors/)
- [2507. Smallest Value After Replacing With Sum of Prime Factors](../../2501-3000/2507-smallest-value-after-replacing-with-sum-of-prime-factors/)
- [3618. Split Array by Prime Indices](../../3501-4000/3618-split-array-by-prime-indices/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/)
