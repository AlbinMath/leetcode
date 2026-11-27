# LeetCode 2342: Max Sum of a Pair With Equal Sum of Digits

**LeetCode Problem #2342 — Max Sum of a Pair With Equal Sum of Digits**
Solve LeetCode Max Sum of a Pair With Equal Sum of Digits using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Sum of a Pair With Equal Sum of Digits |
| LeetCode | #2342 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of **positive** integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.

Return the **maximum** value of* *`nums[i] + nums[j]`* *that you can obtain over all possible indices `i` and `j` that satisfy the conditions. If no such pair of indices exists, return -1.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [18,43,36,13,7]`
- **Output:** `54`
- **Explanation:** The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

### Example 2
- **Input:** `nums = [10,12,19,14]`
- **Output:** `-1`
- **Explanation:** There are no two numbers that satisfy the conditions, so we return -1.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Max Sum of a Pair With Equal Sum of Digits**, we observe the problem requirements and utilize the **Math & Logic** technique. By maintaining a **Primitive Types**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Primitive Types** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [18,43,36,13,7]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `54`.
4. **Verification:** The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumSum = function(nums) {
    const map = new Map();
    let maxSum = -1;
    const digitSum = (num) => {
        let sum = 0;

        while (num > 0) {
            sum += num % 10;
            num = Math.floor(num / 10);
        }

        return sum;
    };

    for (const num of nums) {
        const sum = digitSum(num);

        if (map.has(sum)) {
            maxSum = Math.max(maxSum, num + map.get(sum));

            map.set(sum, Math.max(num, map.get(sum)));
        } else {
            map.set(sum, num);
        }
    }

    return maxSum;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1281. Subtract the Product and Sum of Digits of an Integer](../../1001-1500/1281-subtract-the-product-and-sum-of-digits-of-an-integer/)
- [1837. Sum of Digits in Base K](../../1501-2000/1837-sum-of-digits-in-base-k/)
- [1945. Sum of Digits of String After Convert](../../1501-2000/1945-sum-of-digits-of-string-after-convert/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/)
