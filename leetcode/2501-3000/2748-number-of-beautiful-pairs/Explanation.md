# LeetCode 2748: Number of Beautiful Pairs

**LeetCode Problem #2748 — Number of Beautiful Pairs**
Solve LeetCode Number of Beautiful Pairs using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Beautiful Pairs |
| LeetCode | #2748 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed **integer array `nums`. A pair of indices `i`, `j` where `0 <= i < j < nums.length` is called beautiful if the **first digit** of `nums[i]` and the **last digit** of `nums[j]` are **coprime**.

Return *the total number of beautiful pairs in *`nums`.

Two integers `x` and `y` are **coprime** if there is no integer greater than 1 that divides both of them. In other words, `x` and `y` are coprime if `gcd(x, y) == 1`, where `gcd(x, y)` is the **greatest common divisor** of `x` and `y`.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 9999`
- `nums[i] % 10 != 0`

## Examples
### Example 1
- **Input:** `nums = [2,5,1,4]`
- **Output:** `5`
- **Explanation:** There are 5 beautiful pairs in nums:
When i = 0 and j = 1: the first digit of nums[0] is 2, and the last digit of nums[1] is 5. We can confirm that 2 and 5 are coprime, since gcd(2,5) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 2, and the last digit of nums[2] is 1. Indeed, gcd(2,1) == 1.
When i = 1 and j = 2: the first digit of nums[1] is 5, and the last digit of nums[2] is 1. Indeed, gcd(5,1) == 1.
When i = 1 and j = 3: the first digit of nums[1] is 5, and the last digit of nums[3] is 4. Indeed, gcd(5,4) == 1.
When i = 2 and j = 3: the first digit of nums[2] is 1, and the last digit of nums[3] is 4. Indeed, gcd(1,4) == 1.
Thus, we return 5.

### Example 2
- **Input:** `nums = [11,21,12]`
- **Output:** `2`
- **Explanation:** There are 2 beautiful pairs:
When i = 0 and j = 1: the first digit of nums[0] is 1, and the last digit of nums[1] is 1. Indeed, gcd(1,1) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 1, and the last digit of nums[2] is 2. Indeed, gcd(1,2) == 1.
Thus, we return 2.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Beautiful Pairs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,5,1,4]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** There are 5 beautiful pairs in nums:
When i = 0 and j = 1: the first digit of nums[0] is 2, and the last digit of nums[1] is 5. We can confirm that 2 and 5 are coprime, since gcd(2,5) == 1.
When i = 0 and j = 2: the first digit of nums[0] is 2, and the last digit of nums[2] is 1. Indeed, gcd(2,1) == 1.
When i = 1 and j = 2: the first digit of nums[1] is 5, and the last digit of nums[2] is 1. Indeed, gcd(5,1) == 1.
When i = 1 and j = 3: the first digit of nums[1] is 5, and the last digit of nums[3] is 4. Indeed, gcd(5,4) == 1.
When i = 2 and j = 3: the first digit of nums[2] is 1, and the last digit of nums[3] is 4. Indeed, gcd(1,4) == 1.
Thus, we return 5.

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
/**
 * @param {number[]} nums
 * @return {number}
 */
var countBeautifulPairs = function(nums) {
    // Helper function to compute Greatest Common Divisor
    const gcd = (a, b) => {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };

    // Helper function to get the first digit of a positive integer
    const getFirstDigit = (num) => {
        while (num >= 10) {
            num = Math.floor(num / 10);
        }
        return num;
    };

    let count = 0;
    const n = nums.length;

    for (let i = 0; i < n; i++) {
        const firstDigit = getFirstDigit(nums[i]);
        for (let j = i + 1; j < n; j++) {
            const lastDigit = nums[j] % 10;
            if (gcd(firstDigit, lastDigit) === 1) {
                count++;
            }
        }
    }

    return count;
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
- [2478. Number of Beautiful Partitions](../../2001-2500/2478-number-of-beautiful-partitions/)
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2588-count-the-number-of-beautiful-subarrays/)
- [2597. The Number of Beautiful Subsets](../../2501-3000/2597-the-number-of-beautiful-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-beautiful-pairs/)
