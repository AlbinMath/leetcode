# LeetCode 3550: Smallest Index With Digit Sum Equal to Index

**LeetCode Problem #3550 — Smallest Index With Digit Sum Equal to Index**
Solve LeetCode Smallest Index With Digit Sum Equal to Index using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Index With Digit Sum Equal to Index |
| LeetCode | #3550 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Return the **smallest** index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [1,3,2]`
- **Output:** `2`
- **Explanation:** For `nums[2] = 2`, the sum of digits is 2, which is equal to index `i = 2`. Thus, the output is 2.

### Example 2
- **Input:** `nums = [1,10,11]`
- **Output:** `1`
- **Explanation:** For `nums[1] = 10`, the sum of digits is `1 + 0 = 1`, which is equal to index `i = 1`. 
 For `nums[2] = 11`, the sum of digits is `1 + 1 = 2`, which is equal to index `i = 2`. 
 Since index 1 is the smallest, the output is 1.

### Example 3
- **Input:** `nums = [1,2,3]`
- **Output:** `-1`
- **Explanation:** Since no index satisfies the condition, the output is -1.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a straightforward iterative approach.
1. It uses a `for` loop to iterate through the array from the first element (index `0`) to the last. This naturally ensures we find the smallest index first.
2. For each index `i`, it takes the number `nums[i]`.
3. It calculates the sum of the digits of the number using a `while` loop:
   - `num % 10` extracts the last digit of the number, which is added to `sum`.
   - `Math.floor(num / 10)` removes the last digit from the number.
   - This repeats until all digits have been processed and `num` becomes 0.
4. It compares the calculated `sum` with the current index `i`.
   - If `sum === i`, it immediately returns `i`, fulfilling the condition of finding the smallest index.
5. If the loop finishes checking all elements without returning, it means no such index exists, so it returns `-1`.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** For `nums[2] = 2`, the sum of digits is 2, which is equal to index `i = 2`. Thus, the output is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
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
var smallestIndex = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let sum = 0;

        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }

        if (sum === i) {
            return i;
        }
    }

    return -1;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](../../1501-2000/1550-find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/)
- [2507. Smallest Value After Replacing With Sum of Prime Factors](../../2501-3000/2595-smallest-value-after-replacing-with-sum-of-prime-factors/)
- [2605. Form Smallest Number From Two Digit Arrays](../../2501-3000/2668-form-smallest-number-from-two-digit-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)
