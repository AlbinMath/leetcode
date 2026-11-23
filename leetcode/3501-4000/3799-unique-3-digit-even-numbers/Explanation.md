# LeetCode 3483: Unique 3-Digit Even Numbers

**LeetCode Problem #3483 — Unique 3-Digit Even Numbers**
Solve LeetCode Unique 3-Digit Even Numbers using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique 3-Digit Even Numbers |
| LeetCode | #3483 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of digits called `digits`. Your task is to determine the number of **distinct** three-digit even numbers that can be formed using these digits.

**Note**: Each *copy* of a digit can only be used **once per number**, and there may **not** be leading zeros.

## Constraints
- `3 <= digits.length <= 10`
- `0 <= digits[i] <= 9`

## Examples
### Example 1
- **Input:** `digits = [1,2,3,4]`
- **Output:** `12`
- **Explanation:** The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

### Example 2
- **Input:** `digits = [0,2,2]`
- **Output:** `2`
- **Explanation:** The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

### Example 3
- **Input:** `digits = [6,6,6]`
- **Output:** `1`
- **Explanation:** Only 666 can be formed.

### Example 4
- **Input:** `digits = [1,3,5]`
- **Output:** `0`
- **Explanation:** No even 3-digit numbers can be formed.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Unique 3-Digit Even Numbers**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `digits = [1,2,3,4]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

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
 * @param {number[]} digits
 * @return {number}
 */
var totalNumbers = function(digits) {
    let set = new Set();

    for (let i = 0; i < digits.length; i++) {
        // Hundreds digit cannot be 0
        if (digits[i] === 0) continue;

        for (let j = 0; j < digits.length; j++) {
            if (j === i) continue;

            for (let k = 0; k < digits.length; k++) {
                if (k === i || k === j) continue;

                // Last digit must be even
                if (digits[k] % 2 !== 0) continue;

                let num = digits[i] * 100 + digits[j] * 10 + digits[k];
                set.add(num);
            }
        }
    }

    return set.size;
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
- [2094. Finding 3-Digit Even Numbers](../../2001-2500/2215-finding-3-digit-even-numbers/)
- [357. Count Numbers with Unique Digits](../../0001-0500/0357-count-numbers-with-unique-digits/)
- [1930. Unique Length-3 Palindromic Subsequences](../../2001-2500/2059-unique-length-3-palindromic-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/)
