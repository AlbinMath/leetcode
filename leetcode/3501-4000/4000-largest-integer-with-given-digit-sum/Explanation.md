# LeetCode 4000: Largest Integer With Given Digit Sum

**LeetCode Problem #4000 — Largest Integer With Given Digit Sum**
Solve LeetCode Largest Integer With Given Digit Sum using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Integer With Given Digit Sum |
| LeetCode | #4000 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two non-negative integers `n` and `s`.

Return the **largest** integer that has **at most** `n` digits and whose sum of digits is `s`. If no such integer exists, return -1.

## Constraints
- `1 <= n <= 5`
- `0 <= s <= 100`

## Examples
### Example 1
- **Input:** `n = 2, s = 9`
- **Output:** `90`
- **Explanation:** The largest integer with at most 2 digits that has a sum of digits of 9 is 90.

### Example 2
- **Input:** `n = 2, s = 19`
- **Output:** `-1`
- **Explanation:** There is no integer with at most 2 digits that has a sum of digits of 19, so the answer is -1.

### Example 3
- **Input:** `n = 5, s = 0`
- **Output:** `0`
- **Explanation:** The only non-negative integer whose digits sum to 0 is 0.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Largest Integer With Given Digit Sum**, we observe the problem requirements and utilize the **Math & Logic** technique. We iterate through the inputs using **Mathematical Simulation & Modular Arithmetic**, leveraging a **Primitive Types** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Primitive Types**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, s = 9`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `90`.
4. **Verification:** The largest integer with at most 2 digits that has a sum of digits of 9 is 90.

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
var largestInteger = function(n, s) {
    if (s > 9 * n) {
        return -1;
    }

    if (s === 0) {
        return 0;
    }

    let result = "";

    while (s >= 9) {
        result += "9";
        s -= 9;
    }

    if (s > 0) {
        result += String(s);
    }

    while (result.length < n) {
        result += "0";
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
- [902. Numbers At Most N Given Digit Set](../../0501-1000/0902-numbers-at-most-n-given-digit-set/)
- [949. Largest Time for Given Digits](../../0501-1000/0949-largest-time-for-given-digits/)
- [1237. Find Positive Integer Solution for a Given Equation](../../1001-1500/1237-find-positive-integer-solution-for-a-given-equation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-integer-with-given-digit-sum/)
