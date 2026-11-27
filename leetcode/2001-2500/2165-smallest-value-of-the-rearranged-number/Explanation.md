# LeetCode 2165: Smallest Value of the Rearranged Number

**LeetCode Problem #2165 — Smallest Value of the Rearranged Number**
Solve LeetCode Smallest Value of the Rearranged Number using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Value of the Rearranged Number |
| LeetCode | #2165 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `num.` **Rearrange** the digits of `num` such that its value is **minimized** and it does not contain **any** leading zeros.

Return *the rearranged number with minimal value*.

Note that the sign of the number does not change after rearranging the digits.

## Constraints
- `-10^15 <= num <= 10^15`

## Examples
### Example 1
- **Input:** `num = 310`
- **Output:** `103`
- **Explanation:** The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.

### Example 2
- **Input:** `num = -7605`
- **Output:** `-7650`
- **Explanation:** Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Value of the Rearranged Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 310`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `103`.
4. **Verification:** The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.

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
var smallestNumber = function(num) {
    const digits = Math.abs(num).toString().split("");

    if (num >= 0) {
        digits.sort((a, b) => a - b);
        const firstNonZero = digits.findIndex(digit => digit !== "0");
        if (firstNonZero !== -1) {
            [digits[0], digits[firstNonZero]] =
                [digits[firstNonZero], digits[0]];
        }
        return Number(digits.join(""));
    } else {
        digits.sort((a, b) => b - a);
        return -Number(digits.join(""));
    }
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
- [2930. Number of Strings Which Can Be Rearranged to Contain Substring](../../2501-3000/2930-number-of-strings-which-can-be-rearranged-to-contain-substring/)
- [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](../../1501-2000/1509-minimum-difference-between-largest-and-smallest-value-in-three-moves/)
- [1663. Smallest String With A Given Numeric Value](../../1501-2000/1663-smallest-string-with-a-given-numeric-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/)
