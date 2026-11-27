# LeetCode 2231: Largest Number After Digit Swaps by Parity

**LeetCode Problem #2231 — Largest Number After Digit Swaps by Parity**
Solve LeetCode Largest Number After Digit Swaps by Parity using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Number After Digit Swaps by Parity |
| LeetCode | #2231 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a positive integer `num`. You may swap any two digits of `num` that have the same **parity** (i.e. both odd digits or both even digits).

Return* the **largest** possible value of *`num`* after **any** number of swaps.*

## Constraints
- `1 <= num <= 10^9`

## Examples
### Example 1
- **Input:** `num = 1234`
- **Output:** `3412`
- **Explanation:** Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

### Example 2
- **Input:** `num = 65875`
- **Output:** `87655`
- **Explanation:** Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Number After Digit Swaps by Parity**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 1234`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3412`.
4. **Verification:** Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

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
var largestInteger = function(num) {
    const digits = num.toString().split("").map(Number);

    const odd = [];
    const even = [];

    for (const digit of digits) {
        if (digit % 2 === 0) {
            even.push(digit);
        } else {
            odd.push(digit);
        }
    }

    odd.sort((a, b) => b - a);
    even.sort((a, b) => b - a);
    let result = "";

    for (const digit of digits) {
        if (digit % 2 === 0) {
            result += even.shift();
        } else {
            result += odd.shift();
        }
    }

    return Number(result);
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
- [1946. Largest Number After Mutating Substring](../../1501-2000/1946-largest-number-after-mutating-substring/)
- [2160. Minimum Sum of Four Digit Number After Splitting Digits](../../2001-2500/2160-minimum-sum-of-four-digit-number-after-splitting-digits/)
- [179. Largest Number](../../0001-0500/0179-largest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/)
