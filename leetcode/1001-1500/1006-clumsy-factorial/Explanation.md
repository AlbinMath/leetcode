# LeetCode 1006: Clumsy Factorial

**LeetCode Problem #1006 — Clumsy Factorial**
Solve LeetCode Clumsy Factorial using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Clumsy Factorial |
| LeetCode | #1006 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **factorial** of a positive integer `n` is the product of all positive integers less than or equal to `n`.

For example, `factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`.

We make a **clumsy factorial** using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply `'*'`, divide `'/'`, add `'+'`, and subtract `'-'` in this order.

For example, `clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`.

However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that `10 * 9 / 8 = 90 / 8 = 11`.

Given an integer `n`, return *the clumsy factorial of *`n`.

## Constraints
- `1 <= n <= 10^4`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `7`
- **Explanation:** 7 = 4 * 3 / 2 + 1

### Example 2
- **Input:** `n = 10`
- **Output:** `12`
- **Explanation:** 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Clumsy Factorial**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** 7 = 4 * 3 / 2 + 1

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
var clumsy = function(n) {
    let total = 0;
    let current = n;
    let sign = 1;

    for (let i = n - 1; i > 0; i--) {
        const op = (n - i - 1) % 4;

        if (op === 0) {
            // Multiplication
            current *= i;
        }
        else if (op === 1) {
            // Floor division
            current = Math.floor(current / i);
        }
        else if (op === 2) {
            // Addition: finish previous group
            total += sign * current;
            sign = 1;
            current = i;
        }
        else {
            // Subtraction: finish previous group
            total += sign * current;
            sign = -1;
            current = i;
        }
    }

    return total + sign * current;
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
- [172. Factorial Trailing Zeroes](../../0001-0500/0172-factorial-trailing-zeroes/)
- [793. Preimage Size of Factorial Zeroes Function](../../0501-1000/0793-preimage-size-of-factorial-zeroes-function/)
- [48. Rotate Image](../../0001-0500/0048-rotate-image/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/clumsy-factorial/)
